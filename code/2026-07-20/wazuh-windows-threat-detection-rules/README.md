# Wazuh Windows／Sysmon 威脅偵測規則包

## 目的

為 VENTI-DC、SLIME、CELL 建立第一批可驗收的 Windows 偵測：可疑下載、payload staging、bind shell 跡象、帳號建立、Administrators／Domain Admins 異動、清除日誌、服務／排程持久化、編碼 PowerShell 與 Defender 削弱。

本規則包只用於自有或已授權的隔離實驗室。它不啟用 Active Response，也不自動封鎖或刪除帳號。

## 證據分層

| 類型 | Rule ID | 能證明什麼 |
|---|---|---|
| 可疑下載命令 | 110100–110101 | 有人執行下載相關程序／Script Block；不證明下載成功或檔案惡意 |
| Payload staging | 110102 | 指定副檔名寫入使用者可寫路徑；需再查 hash、來源與簽章 |
| Bind shell 嘗試 | 110110–110111 | listener／shell 程式碼出現 |
| Bind shell 入站連線 | 110112 | 可疑 listener 程序接受入站連線；不單獨宣稱 shell 已可用 |
| Bind shell 高可信鏈 | 110113–110114 | listener 程序建立 shell 子程序；仍應交叉核對 Event 3、使用者與時間 |
| 帳號建立命令 | 110120 | 命令嘗試，不等於成功 |
| 帳號建立成功 | 110121 | Security 4720 成功事件 |
| 群組修改命令 | 110130 | 成員新增命令嘗試，不等於成功 |
| Administrators 成功 | 110131 | 4732 且 group SID 為 `S-1-5-32-544` |
| Domain Admins 成功 | 110132 | 4728 且 group SID RID 為 `512` |
| 常見防禦／持久化 | 110140–110144 | 清 log、服務、排程、編碼 PowerShell、Defender 削弱 |

## 前置條件

1. Wazuh Agent 已 Active 且 group synchronized。
2. Sysmon Event ID 1 可在本機看到。
3. 套用 `sysmon-lab-baseline.xml` 後可看到 Event ID 3、11、22；Microsoft 官方指出預設安裝不啟用 Event ID 3。
4. Windows Audit Policy 啟用 `Audit User Account Management`、`Audit Security Group Management`、`Audit Other Object Access Events`（依 4698 需求）與必要的成功／失敗稽核。
5. PowerShell GPO 啟用 Script Block Logging，且 Wazuh 採集 `Microsoft-Windows-PowerShell/Operational`。
6. `Security`、Sysmon、PowerShell 通道只配置一次；先比較 endpoint `ossec.conf` 與 shared `agent.conf`，避免重複事件。

## 先檢查 Rule ID 衝突

在 Manager 執行：

```bash
sudo grep -R 'id="1101' /var/ossec/etc/rules /var/ossec/ruleset/rules
```

若已有 110100–110199，先重新分配整個 ID block，不要直接覆蓋。

## 部署 Wazuh Rules

先備份並複製為獨立檔，避免修改會在升級時被覆寫的 `/var/ossec/ruleset/rules/`：

```bash
sudo cp -a /var/ossec/etc/rules /var/ossec/etc/rules.backup-20260720
sudo cp windows-threat-detection-rules.xml \
  /var/ossec/etc/rules/110100-windows-threat-detection-rules.xml

sudo chown root:wazuh /var/ossec/etc/rules/110100-windows-threat-detection-rules.xml
sudo chmod 640 /var/ossec/etc/rules/110100-windows-threat-detection-rules.xml

sudo /var/ossec/bin/wazuh-analysisd -t
```

只有測試命令無錯誤時才套用：

```bash
sudo systemctl restart wazuh-manager
sudo systemctl status wazuh-manager --no-pager
sudo journalctl -u wazuh-manager -n 50 --no-pager
```

## 套用 Sysmon Baseline

先確認 Sysmon 路徑與目前設定：

```powershell
Get-CimInstance Win32_Service |
  Where-Object Name -Like "Sysmon*" |
  Select-Object Name,State,PathName

& "C:\Tools\Sysmon\Sysmon64.exe" -c |
  Out-File "C:\Tools\Sysmon\sysmon-config-before-20260720.txt" -Encoding utf8
```

確認實際執行檔路徑後套用：

```powershell
& "C:\Tools\Sysmon\Sysmon64.exe" -c "C:\Tools\Sysmon\sysmon-lab-baseline.xml"
```

若要回到 Sysmon 預設設定：

```powershell
& "C:\Tools\Sysmon\Sysmon64.exe" -c --
```

## 安全驗收

### V1：資料源

```powershell
Get-WinEvent -FilterHashtable @{
  LogName = "Microsoft-Windows-Sysmon/Operational"
  Id = 1,3,11,22
  StartTime = (Get-Date).AddMinutes(-15)
} -MaxEvents 20 | Select-Object TimeCreated,Id,ProviderName
```

### V2：不執行下載的規則 smoke test

這只把測試字串寫到 Script Block／ProcessCreate，不進行網路下載：

```powershell
Write-Output "Invoke-WebRequest http://example.invalid/lab-test.exe"
```

預期可能命中 110101；若只在既有 PowerShell 視窗執行而未產生新的 Sysmon ProcessCreate，110100 不一定命中。

### V3：成功事件

在隔離 VM 使用 Computer Management／AD Users and Computers GUI 建立名稱以 `WAZUH_TEST_` 開頭的臨時帳號，確認 110121；再由 GUI 加入本機 Administrators，確認 110131。完成後立即移出群組並刪除測試帳號，同時保存 4720、4732 與 Wazuh alert JSON。

### V4：Bind shell

不要為了測規則而在一般網段開 listener。110110–110114 應由攻擊者同學在已授權、受 OPNsense 限制的隔離情境測試；至少保存 Sysmon Event 1／3、來源 IP、ProcessGuid、父子程序與 PCAP。只有 110113／110114 再加相符入站 Event 3，才能標為高可信成功鏈。

## Dashboard 查詢

```text
rule.id: (110100 OR 110101 OR 110102 OR 110110 OR 110111 OR 110112 OR
          110113 OR 110114 OR 110120 OR 110121 OR 110130 OR 110131 OR
          110132 OR 110140 OR 110141 OR 110142 OR 110143 OR 110144)
```

也可查：

```text
rule.groups: bind_shell
rule.groups: suspicious_download
rule.groups: account_created_success
rule.groups: administrators_membership_success
```

## 回復

若 Manager 無法載入：

```bash
sudo rm /var/ossec/etc/rules/110100-windows-threat-detection-rules.xml
sudo /var/ossec/bin/wazuh-analysisd -t
sudo systemctl restart wazuh-manager
```

不要在尚未完成誤報基線前啟用 Active Response。先至少收集一週結果，再依合法軟體、管理帳號與維運時段建立 allow-list。

