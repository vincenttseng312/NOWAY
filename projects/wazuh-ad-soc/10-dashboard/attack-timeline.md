---
id: dsh-attack-timeline
title: "攻擊時間軸"
doc_type: dashboard
category: dashboard
summary: "以時間為軸呈現告警序列，並可依 MITRE 戰術著色標記攻擊階段。是理解「攻擊如何展開」與 timeline 類問答的核心視覺。"
tags: [cat:dashboard, type:dashboard]
data_fields: ["timestamp", "rule.mitre.tactic", "agent.name", "rule.level"]
ai_inputs: ["timeline", "risk_level"]
viz_type: "timeline"
filters: ["時間範圍", "主機", "帳號", "來源 IP"]
related_docs: [doc-data-and-event-flow, doc-correlation-rules, dsh-event-detail-view]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "MITRE ATT&CK 官方網站"]
keywords: ["攻擊時間軸", "attack timeline", "kill chain", "時序"]
last_updated: 2026-07-09
---

# 攻擊時間軸

## 1. 元件目的
把離散告警串成時序，呈現攻擊展開過程。

## 2. 使用情境
「整理最近一小時攻擊」「這起事件怎麼發生的」；事件報告的 Timeline 章節視覺。

## 3. 需要的資料欄位
時間、戰術階段、主機/帳號/IP、風險。

## 4. 對應 Wazuh 欄位
`timestamp`、`rule.mitre.tactic`、`agent.name`、`rule.level`。

## 5. 對應 AI 分析輸出
`timeline`（AI 排序與關聯後的序列）、關聯型樣標記（見 [[doc-correlation-rules]]）。

## 6. 視覺化建議
水平時間軸；依戰術著色（Credential Access/Priv-Esc/…）；關聯鏈以連線標記。

## 7. 使用者可互動功能
刷選時間窗、點節點→ [[dsh-event-detail-view]]、依實體過濾。

## 8. 篩選條件
時間範圍、主機、帳號、來源 IP。

## 9. 排序方式
時間（舊→新）。

## 10. 範例資料格式
```json
[{"time":"<ts>","tactic":"Credential Access","event":"4625×N","host":"<agent>"},
 {"time":"<ts>","tactic":"Valid Accounts","event":"4624","host":"<agent>"}]
```
（值為佔位。）

## 11. 注意事項
時區依環境（`timestamp`）；時間軸呈現關聯，但「同一性」仍需以實體欄位驗證。

## 相關文件
[[doc-data-and-event-flow]]、[[doc-correlation-rules]]、[[dsh-event-detail-view]]
