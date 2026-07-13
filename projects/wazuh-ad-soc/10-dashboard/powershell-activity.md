---
id: dsh-powershell-activity
title: "PowerShell 可疑活動圖"
doc_type: dashboard
category: dashboard
summary: "監控可疑 PowerShell 執行：可疑旗標命中、異常父程序（Office→PowerShell）、按主機/時間分布。對應可疑 PowerShell 情境。"
tags: [cat:dashboard, type:dashboard, mitre-technique:t1059-001]
data_fields: ["data.win.system.providerName", "timestamp", "agent.name"]
ai_inputs: ["event_summary"]
viz_type: "table"
filters: ["時間範圍", "主機", "父程序"]
related_docs: [evt-powershell-suspicious, scn-suspicious-powershell]
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "Wazuh 官方文件"]
keywords: ["PowerShell 活動", "powershell activity", "可疑旗標", "T1059.001"]
last_updated: 2026-07-09
---

# PowerShell 可疑活動圖

## 1. 元件目的
凸顯可疑 PowerShell 執行與其父程序鏈。

## 2. 使用情境
「有沒有可疑 PowerShell」；Office→PowerShell 鏈的即時警戒。

## 3. 需要的資料欄位
時間、主機、父程序、命令列/旗標（若擷取）。

## 4. 對應 Wazuh 欄位
`data.win.system.providerName`（PowerShell）、`timestamp`、`agent.name`、命令列欄位（若採集，見 [[evt-powershell-suspicious]]）。

## 5. 對應 AI 分析輸出
`event_summary`（AI 對命令列意圖的摘要）；可疑旗標清單見父層 [[lolbin-and-powershell-abuse]]。

## 6. 視覺化建議
表格（時間/主機/父程序/旗標）+ 可疑旗標命中排行；Office 父程序醒目。

## 7. 使用者可互動功能
點列→ [[doc-event-detail-view]]（看完整命令列/解碼）。

## 8. 篩選條件
時間範圍、主機、父程序。

## 9. 排序方式
時間序 / 風險。

## 10. 範例資料格式
```json
[{"time":"<ts>","host":"<agent>","parent":"WINWORD.EXE","flags":["-enc","-w hidden"]}]
```
（值為佔位。）

## 11. 注意事項
4104 未啟用時看不到解碼內容（見 [[evt-powershell-suspicious]]）；IT 管理腳本會誤報，需結合父程序與行為。

## 相關文件
[[evt-powershell-suspicious]]、[[scn-suspicious-powershell]]；跨連父層 [[lolbin-and-powershell-abuse]]。
