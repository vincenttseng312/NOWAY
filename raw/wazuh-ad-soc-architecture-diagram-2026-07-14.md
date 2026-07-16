# Wazuh × AD × AI SOC 專題架構圖（使用者提供）

- 提供日期：2026-07-14
- 來源：使用者在對話中提供的架構設計圖片
- 原始附件：`codex-clipboard-cd299967-87d5-4f19-a3ab-edc46c378016.png`
- 性質：設計基線，不代表實機已完成部署或已開放任何連接埠。

## 圖片轉錄

### 監控與 AD 區

| 元件 | 圖中角色與設定 | 資源規格 |
|---|---|---|
| Windows Server 2025 | AD basics：Domain Controller、ADCS；功能：RDP to Windows Server、SMB service、service、netbios | 2 CPU cores、4 GB RAM、64 GB SSD |
| Windows 11 A | 未標註額外權限的 Windows 端點 | 2 CPU cores、4 GB RAM、64 GB SSD |
| Windows 11 B | Local Group：Administrator、Remote Desktop Users（RDP）、Remote Management Users（WinRM） | 2 CPU cores、4 GB RAM、64 GB SSD |
| Wazuh Server | 偵測目標：network（IDS）、malicious command、malicious process | 4 CPU cores、8 GB RAM、200 GB SSD |

### 邊界與外部服務區

| 元件 | 圖中角色與設定 | 資源規格 |
|---|---|---|
| OPNsense | basic network settings、firewall、IDS、VPN（for AI server） | 2 CPU cores @ 1.5 GHz、8 GB RAM、120 GB SSD |
| AI Server | 由 Wazuh Server 以標示為 MCP 的連線介接 | 未標註 |
| attacker | 位於監控區外，圖以 RDP 標示其與 Windows 11 B 的測試路徑 | 未標註 |

## 圖形關係的保守解讀

- OPNsense 是監控區與外部服務／攻擊區的分段控制點。
- Wazuh 與 AI Server 的 MCP 線表示預計的應用整合，不足以推論傳輸協定、連接埠、認證、授權或資料最小化設定。
- RDP 箭頭表示預期測試路徑；它不是「應永久對攻擊端開放 RDP」的證據。
- 圖中沒有 IP、CIDR、VLAN、主機名、Wazuh Agent 安裝狀態或防火牆規則，因此這些值維持待驗證。

## 研究問題

1. 端點與 DC 是否都已安裝、註冊且回報 Wazuh Agent？
2. OPNsense 的分段、允許規則與 IDS 日誌是否已匯入 Wazuh？
3. MCP 介面是否採用只讀告警查詢、明確身分驗證與最小資料欄位？
4. RDP／WinRM 的授權範圍是否限於實驗所需來源、時段與帳號群組？
