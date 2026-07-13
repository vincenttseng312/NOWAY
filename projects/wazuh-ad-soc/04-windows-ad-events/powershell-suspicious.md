---
id: evt-powershell-suspicious
title: "PowerShell 可疑執行事件"
doc_type: event
category: windows-ad-event
summary: "PowerShell 濫用是常見攻擊手法。Script Block Logging（Event 4104）啟用時可看到腳本內容；程序建立（4688）可看命令列。可疑旗標如 -EncodedCommand/-WindowStyle Hidden 是重點。PowerShell operational 事件需啟用相關記錄。"
tags: [cat:event, type:event, source:powershell, mitre-technique:t1059-001]
event_source: powershell
windows_event_ids: ["4104 (需啟用 Script Block Logging)", "4103", "4688"]
wazuh_sources: []
related_entities: [ent-host-win11-target]
related_docs: [scn-suspicious-powershell, evt-windows-security-overview]
risk_level: high
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "Wazuh 官方文件"]
keywords: ["PowerShell", "4104", "Script Block Logging", "EncodedCommand", "LOLBin", "T1059.001"]
last_updated: 2026-07-09
---

# PowerShell 可疑執行事件

## 1. 事件用途
偵測可疑的 PowerShell 執行。資料來源有二：**程序建立**（4688，含命令列，需開命令列稽核）與 **PowerShell Operational 通道**（Script Block Logging 4104、Module Logging 4103——**需啟用對應記錄，且具體 ID 建議依 Microsoft 官方文件確認**）。

## 2. 可能代表的安全意義
對映 MITRE **T1059.001 PowerShell**。可疑旗標（父層 [[lolbin-and-powershell-abuse]] 有完整清單）：`-EncodedCommand`/`-enc`、`-ExecutionPolicy Bypass`、`-WindowStyle Hidden`/`-w hidden`、`IEX`/`Invoke-Expression`、`DownloadString`/`FromBase64String`。父程序若為 Office（WINWORD/EXCEL）更可疑。

## 3. 可能涉及的 Windows Event ID
| Event ID | 意義 | 驗證 |
|---|---|---|
| 4688 | 程序建立（可含 PowerShell 命令列） | 命令列需開稽核 |
| 4104 | Script Block Logging（腳本內容） | **需啟用 Script Block Logging；ID 以 Microsoft 官方為準** |
| 4103 | Module Logging | **需啟用；以 Microsoft 官方為準** |

> PowerShell 引擎另有 400/403/600 等事件；語意見父層 [[windows-event-log-and-sysmon]] 並以官方為準。

## 4. 在 Wazuh Alert 中可能出現的欄位
`eventID`、`data.win.system.providerName`（Microsoft-Windows-PowerShell）、命令列/腳本內容欄位（若 decoder 擷取）、父程序資訊（若來自 4688/Sysmon）。

## 5. AI 分析時應注意的欄位
命令列旗標（比程序名重要，見父層 [[dynamic-behavior-analysis]]）、父程序、是否下載/解碼、是否隱藏視窗、執行後是否寫檔/持久化。

## 6. 儀表板可以如何視覺化
PowerShell 可疑活動圖、可疑旗標命中排行、Office→PowerShell 程序鏈告警卡。

## 7. 使用者可能會問的問題
「有沒有可疑的 PowerShell 執行？」「這段 PowerShell 在做什麼？」

## 8. AI 回答範例
「<主機> 上 <父程序> 啟動 powershell.exe，命令列含 `-EncodedCommand`（4688/4104）。符合 T1059.001 可疑執行。若 4104 未啟用則僅能看到命令列、看不到解碼後內容，建議確認記錄設定。」（值為佔位。）

## 9. 誤判情境
IT 管理腳本、軟體安裝程式、CI/部署工具正常使用 PowerShell、系統管理自動化。

## 10. 處置建議
還原命令列/解碼內容判斷意圖；惡意則隔離主機、檢查下載物與持久化；建議啟用 Script Block Logging 以利日後分析。

## 相關文件
[[scn-suspicious-powershell]]、[[evt-windows-security-overview]]；跨連父層 [[lolbin-and-powershell-abuse]]、[[dynamic-behavior-analysis]]。

## 建議查證來源
Microsoft Windows Security Auditing 文件、Wazuh 官方文件。

## 可被檢索的關鍵字（中英）
PowerShell、4104、Script Block Logging、EncodedCommand、LOLBin、T1059.001。
