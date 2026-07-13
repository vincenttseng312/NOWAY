---
id: scn-suspicious-powershell
title: "可疑 PowerShell 執行偵測"
doc_type: attack-scenario
category: attack-scenario
summary: "偵測被濫用的 PowerShell：可疑命令列旗標（-EncodedCommand/-Hidden 等）、異常父程序（Office）、下載或記憶體執行。核心看命令列與父程序，而非程序名本身。"
tags: [cat:attack-scenario, mitre-tactic:execution, source:powershell, risk:high]
related_entities: [ent-host-win11-target]
related_docs: [evt-powershell-suspicious, scn-malicious-file-execution, doc-correlation-rules]
mitre_attack: [t1059-001]
wazuh_sources: []
windows_event_ids: ["4688", "4104 (需啟用)"]
risk_level: high
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "Wazuh 官方文件", "MITRE ATT&CK 官方網站"]
keywords: ["可疑 PowerShell", "EncodedCommand", "LOLBin", "T1059.001", "script block logging"]
last_updated: 2026-07-09
---

# 可疑 PowerShell 執行偵測

## 1. 情境說明
偵測 PowerShell 被當作攻擊工具使用。本頁談偵測跡象與判讀，不提供攻擊腳本。事件面細節見 [[evt-powershell-suspicious]]。

## 2. 攻擊者可能目標
下載/執行下一階段、記憶體內執行以規避落地、系統操作，同時濫用合法二進位降低偵測（LOLBin）。

## 3. 防禦方可觀測跡象
可疑命令列旗標、異常父程序（如 WINWORD→powershell）、隱藏視窗、對外連線或寫檔緊接其後。

## 4. 可能出現的 Windows / AD 事件
4688（命令列，需開稽核）、4104 Script Block Logging（需啟用）。見 [[evt-powershell-suspicious]]。

## 5. 可能出現的 Wazuh 告警欄位
`data.win.system.providerName`（PowerShell）、命令列/腳本欄位（若擷取）、父程序資訊、`rule.groups`；`rule.id` env-specific。

## 6. MITRE ATT&CK 對應
T1059.001 Command and Scripting Interpreter: PowerShell。以官方為準。

## 7. 風險等級判斷
high：尤其父程序為 Office/腳本宿主、含編碼命令、或緊接網路/寫檔行為。

## 8. AI 分析重點
命令列旗標（比程序名重要）、父程序鏈、是否下載/解碼/記憶體執行、後續是否持久化。完整旗標清單見父層 [[lolbin-and-powershell-abuse]]。

## 9. 儀表板呈現方式
PowerShell 可疑活動圖、Office→PowerShell 程序鏈卡、可疑旗標命中排行。

## 10. 使用者可能詢問的問題
「有沒有可疑 PowerShell？」「這段 PowerShell 想做什麼？」

## 11. AI 回答範例
「<主機> 上 WINWORD.EXE 生出 powershell.exe 且命令列含 `-enc`（4688），符合 T1059.001。若 4104 未啟用則無法還原解碼內容，建議確認記錄設定並隔離主機。」（值為佔位。）

## 12. 建議處置方式
還原命令列/解碼判斷意圖、隔離主機、檢查下載物與持久化、建議啟用 Script Block Logging。

## 13. 誤判可能性
IT 管理腳本、部署/CI 工具、軟體安裝程式正常使用 PowerShell。

## 14. 需要進一步確認的資料
是否啟用 4104、命令列稽核是否開、父程序鏈是否完整採集。

## 相關文件
[[evt-powershell-suspicious]]、[[scn-malicious-file-execution]]、[[doc-correlation-rules]]；跨連父層 [[lolbin-and-powershell-abuse]]、[[dynamic-behavior-analysis]]。

## 建議查證來源
Microsoft Windows Security Auditing 文件、Wazuh 官方文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
可疑 PowerShell、EncodedCommand、LOLBin、T1059.001、script block logging。
