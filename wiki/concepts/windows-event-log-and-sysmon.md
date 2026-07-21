---
type: concept
title: "Windows Event Log 與 Sysmon 分析"
tags: [malware-analysis, dfir, windows, sysinternals]
sources: [malware-static-dynamic-analysis-notes, malware-dynamic-analysis, threat-hunting-course-midterm-report, range-main]
created: 2026-07-09
updated: 2026-07-20
---

# Windows Event Log 與 Sysmon 分析

動態分析的日誌層面：Windows 內建 Event Log 提供基礎程序/登入/服務事件，Sysmon（Sysinternals 工具）以 service+driver 常駐方式提供更細緻的遙測，是 malware analysis、threat hunting、DFIR 與 SIEM 的重要資料來源。

## Windows Event Log 常見來源

| Log | 用途 |
|---|---|
| Security | 登入、程序建立、權限使用、物件存取 |
| System | 服務、驅動、系統事件 |
| PowerShell | PowerShell engine / script block |
| TaskScheduler | Scheduled Task activity |
| WMI-Activity | WMI 操作 |
| Sysmon/Operational | Sysmon telemetry |

## Windows Security 重要 Event ID

| Event ID | 意義 |
|---:|---|
| 4624 / 4625 | 登入成功 / 失敗 |
| 4648 | 使用明確憑證登入 |
| 4672 | 高權限登入 |
| **4688** | **程序建立**（啟用相關稽核後可含 command line，是動態分析最常用的 Security log 事件） |
| 4689 | 程序結束 |
| 4697 | 服務安裝 |
| 4698 / 4702 | Scheduled task 建立 / 修改 |
| **1102** | **Security log 被清除**（高風險，常見於清痕跡行為） |

Event ID 4688 重要欄位：New Process Name、Process Command Line、Creator Process Name、Subject User Name、Token Elevation Type、Mandatory Label。注意：command line 欄位需額外啟用稽核設定，否則可能為空。

System Log 重要 Event ID：7036/7040（服務狀態/啟動類型改變）、**7045（新服務被安裝，Service persistence 分析時非常重要，見 [[persistence-mechanisms]]）**。

PowerShell Logs：400/403（engine 啟停）、4103（module logging）、4104（script block logging，若啟用可看到被執行的腳本內容），詳見 [[lolbin-and-powershell-abuse]]。

## Sysmon

Sysmon 是 Sysinternals 工具，以 service 與 driver 方式常駐，把更細緻的系統活動寫入 Windows Event Log。

> [!NOTE]
> Procmon 適合短時間、高細節的互動式觀察；Sysmon 適合跨重新啟動的持續遙測與 SIEM／Wazuh 關聯。兩者應互補使用，而不是二選一。

常見 Sysmon Event ID：

| ID | 名稱 | 分析用途 |
|---:|---|---|
| 1 | Process Create | 程序建立、命令列、父程序 |
| 2 | File creation time changed | timestomping 跡象 |
| 3 | Network Connection | 程序對外連線 |
| 6 | Driver Loaded | Driver 載入 |
| 7 | Image Loaded | DLL 載入；預設停用，需精準配置以控制事件量 |
| **8** | **CreateRemoteThread** | **remote thread，injection 跡象，見 [[process-hollowing]]** |
| **10** | **ProcessAccess** | **跨程序存取，例如 LSASS access / injection prep** |
| 11 | FileCreate | 檔案建立 |
| 12/13/14 | Registry 建立/刪除/寫入/更名 | 見 [[persistence-mechanisms]] |
| 22 | DNS Query | DNS 查詢 |
| 23/26 | File Delete (archived/detected) | 檔案刪除 |

Event ID 1 重要欄位：`ProcessGuid`、`Image`、`CommandLine`、`ParentProcessGuid`、`ParentImage`、`ParentCommandLine`、`IntegrityLevel`、`Hashes`。**關鍵：`ProcessGuid` 比 PID 更適合跨事件關聯，因為 PID 會被系統重複使用。**

### Event ID 1 與 Event ID 7 的關聯判讀

EID 1 回答「誰啟動了誰、以什麼命令列和權限啟動」，EID 7 回答「該程序從哪裡載入了哪些 DLL／映像」。在 DLL Sideloading 調查中，應先由 EID 1 建立程序基線，再用 EID 7 比對 `ImageLoaded`、`Signed`、`SignatureStatus`、雜湊與完整路徑。

例如 `python.exe -> calc.exe` 或合法已簽章程式載入桌面中的 DLL，都是值得調查的偏差，不是惡意結論。至少再確認命令列、使用者操作、模組簽章／雜湊，以及後續 EID 3、11、13 或 EDR 記憶體事件。

> [!WARNING]
> Microsoft 官方 Sysmon 文件指出 Image Load（EID 7）預設停用，且全量啟用會產生大量日誌。應用 XML filter 限制到使用者可寫路徑、指定程序或其他有明確假設的條件，並先估算 Wazuh ingest 與保存容量。

官方欄位與預設行為參考：[Sysmon - Sysinternals](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)。

## 從「有事件」到「可驗證遙測」

[[threat-hunting-course-midterm-report]] 展示以窄化 Sysmon 設定驗證指定程序事件可以進入 Wazuh。這是 onboarding smoke test，不等於完整偵測基線。要把它升級成可回歸的 telemetry evidence，每次測試至少保存：

- Sysmon 版本與 XML config hash；
- Windows Audit／Event Channel 設定與 Wazuh Agent group config；
- 端點、DC、Wazuh Manager 的時間來源與 UTC 偏差；
- 原始 EVTX、對應 Wazuh alert JSON、產生事件的授權步驟與 run ID；
- 預期 Event ID／欄位與實際收集結果，而不是只記環境特定 `rule.id`。

若端點已產生事件但 Wazuh 查不到，應依序檢查 audit policy／Sysmon filter、Event Channel、Agent 採集、傳輸、decoder／parser 與規則。[[detection-validation-range]] 將這些結果分成 `None`、`Telemetry`、`Failed`、`Success`，可避免把 sensor 缺資料誤判成規則漏報。

2026-07-20 的第一批實作見 [[wazuh-windows-threat-detection-rules]]：以 18 條 custom rule 分開記錄下載／帳號／群組命令 attempt、Security 成功事件與 bind shell 高可信鏈，並附聚焦的 Sysmon Event ID 3／11／22 baseline。XML 已完成靜態驗證，但 Manager 載入與 live-event 命中仍待實機驗收。

## Sysmon 關聯分析範例

```text
Event ID 1: WINWORD.EXE starts powershell.exe        (同 ProcessGuid)
Event ID 22: powershell.exe queries suspicious domain (同 ProcessGuid)
Event ID 3: powershell.exe connects to remote IP:443  (同 ProcessGuid)
Event ID 11: powershell.exe writes payload.exe to AppData
Event ID 1: payload.exe starts
Event ID 13: payload.exe writes HKCU Run key
```

這就是一條完整的行為證據鏈——串接程序建立、DNS、網路連線、檔案寫入、Registry 寫入六個事件，呼應 [[malware-analysis-methodology]] 中「把證據串成故事線」的核心原則。日誌時間線模板欄位：`Time UTC | Source | Event ID | ProcessGuid | Process | Parent | Action | Target | Notes`。

## 與其他頁面的關聯

Injection/Hollowing 對應的 Sysmon EID 8/10 見 [[process-hollowing]]；Registry persistence 對應的 EID 12/13/14 見 [[persistence-mechanisms]]；PowerShell 專屬日誌見 [[lolbin-and-powershell-abuse]]；日誌證據最終如何組成 Timeline 章節見 [[malware-analysis-report-template]]；跨版本重放與四態驗證見 [[detection-validation-range]]。
