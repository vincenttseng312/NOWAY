---
id: rpt-powershell-incident
title: "可疑 PowerShell 事件報告"
doc_type: report
category: report
summary: "情境專用報告：彙整可疑 PowerShell 執行的命令列/旗標、父程序鏈、後續行為與對應技術，供標準化產出該類事件報告。"
audience: analyst
required_inputs: ["data.win.system.providerName", "agent.name", "timestamp"]
optional_inputs: ["data.win.system.eventID", "命令列/腳本內容(若採集)", "父程序"]
related_docs: [scn-suspicious-powershell, evt-powershell-suspicious, rpt-multi-alert-aggregate]
tags: [cat:report, type:report, mitre-technique:t1059-001]
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: ["PowerShell 事件報告", "powershell incident report", "T1059.001"]
last_updated: 2026-07-09
---

# 可疑 PowerShell 事件報告

## 1. 報告目的
標準化產出可疑 PowerShell 執行事件報告。

## 2. 適用情境
命中 [[scn-suspicious-powershell]]。事件面見 [[evt-powershell-suspicious]]。

## 3. 必要輸入欄位
`providerName`（PowerShell）、`agent.name`、`timestamp`。

## 4. 可選輸入欄位
`eventID`（4688/4104）、命令列/腳本內容（若採集）、父程序。

## 5. 報告產出格式
```markdown
### 可疑 PowerShell 事件報告
- 時間：<ts> / 主機：<host>
- 父程序：<parent>（Office→PowerShell 尤其可疑）
- 命令列旗標：<-enc / -w hidden / IEX ...>
- 後續行為：<下載/寫檔/持久化/連線，若有>
- 對應技術：T1059.001
- 風險：<severity>
- 記錄狀態：<4104 是否啟用（影響能否還原解碼內容）>
- 處置：<步驟>
```

## 6. 嚴重性判斷方式
含編碼命令/異常父程序/後續惡意行為 → high 起（見 [[doc-severity-classification]]）。

## 7. MITRE ATT&CK 對應方式
T1059.001 PowerShell（+ 視後續行為加 T1105/T1204 等）。

## 8. 建議處置格式
還原命令列/解碼、隔離主機、檢查下載物與持久化、建議啟用 Script Block Logging。

## 9. 範例輸入
PowerShell 相關事件（佔位）。

## 10. 範例輸出
```markdown
### 可疑 PowerShell 事件報告
- 時間：<ts> / 主機：<host>
- 父程序：WINWORD.EXE
- 命令列旗標：-enc, -w hidden
- 後續行為：對外連線 <ip>
- 對應技術：T1059.001（+ T1071）
- 風險：high
- 記錄狀態：4104 未啟用（無法還原解碼內容）
- 處置：隔離主機、確認記錄設定、檢查連線目的。
```
（值為佔位。）

## 相關文件
[[scn-suspicious-powershell]]、[[evt-powershell-suspicious]]；跨連父層 [[lolbin-and-powershell-abuse]]。
