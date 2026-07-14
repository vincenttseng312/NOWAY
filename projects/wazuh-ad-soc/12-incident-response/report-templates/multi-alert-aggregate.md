---
id: rpt-multi-alert-aggregate
title: "多筆告警彙整報告"
doc_type: report
category: report
summary: "把一段時間/一主機/一帳號的多筆告警彙整成一份 Incident 報告：概況、關聯鏈、受影響實體、風險與建議，作為完整報告的中間層。"
audience: analyst
required_inputs: ["timestamp", "rule.level", "agent.name", "data.win.system.eventID"]
optional_inputs: ["rule.mitre.id", "data.win.eventdata.targetUserName", "data.win.eventdata.ipAddress"]
related_docs: [doc-alert-to-report-pipeline, rpt-full-report, doc-correlation-rules]
tags: [cat:report, type:report]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "MITRE ATT&CK 官方網站"]
keywords: ["多筆告警彙整", "aggregate report", "incident 彙整"]
last_updated: 2026-07-09
---

# 多筆告警彙整報告

## 1. 報告目的
把散落的多筆告警聚成一個 Incident 的整體圖像。

## 2. 適用情境
一段時間/一主機/一帳號的告警群；作為完整事件報告的骨幹。

## 3. 必要輸入欄位
`timestamp`、`rule.level`、`agent.name`、`eventID`（各筆）。

## 4. 可選輸入欄位
`rule.mitre.id`、`targetUserName`、`ipAddress`。

## 5. 報告產出格式
```markdown
### Incident 彙整
- 範圍：<時間窗> / <主機或帳號>
- 告警數：<N>（high <a> / critical <b>）
- 關聯鏈：<命中的 C1–C5 型樣，若有>
- 受影響實體：主機 <...> / 帳號 <...> / 來源 IP <...>
- 對應技術：<T-id 清單>
- 整體風險：<severity>
- 摘要：<一段話串起這批告警的故事>
- 建議：<處置方向>
```

## 6. 嚴重性判斷方式
以整體 Incident 為單位分級（見 [[doc-severity-classification]]）；關聯鏈通常升級。

## 7. MITRE ATT&CK 對應方式
彙整各筆 `rule.mitre.*` → 去重技術清單，並標出戰術涵蓋。

## 8. 建議處置格式
分階段（控制/根除/復原）條列，連 [[doc-ir-sop]]。

## 9. 範例輸入
一組告警的欄位陣列（佔位）。

## 10. 範例輸出
```markdown
### Incident 彙整
- 範圍：<時間窗> / <host>
- 告警數：<N>（critical 1）
- 關聯鏈：C1 暴力破解成功 + C2 持久化提權
- 受影響：<host> / <account> / 來源 <ip>
- 技術：T1110, T1078, T1136, T1098
- 整體風險：critical
- 摘要：外部來源暴力破解成功後建立帳號並提權。
- 建議：隔離主機、重設憑證、移除持久化。
```
（值為佔位。）

## 相關文件
[[doc-alert-to-report-pipeline]]、[[rpt-full-report]]、[[doc-correlation-rules]]
