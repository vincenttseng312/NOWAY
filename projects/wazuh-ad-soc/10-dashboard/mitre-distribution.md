---
id: dsh-mitre-distribution
title: "MITRE ATT&CK 分布圖"
doc_type: dashboard
category: dashboard
summary: "以 rule.mitre.tactic/technique 聚合，呈現觀察到的攻擊戰術/技術分布，幫助掌握攻擊集中在哪些階段。對應 technique-mapping 問答。"
tags: [cat:dashboard, type:dashboard, cat:mitre]
data_fields: ["rule.mitre.tactic", "rule.mitre.id", "rule.mitre.technique"]
ai_inputs: []
viz_type: "bar"
filters: ["時間範圍", "戰術"]
related_docs: [doc-mitre-mapping-overview, doc-wazuh-mitre-linkage]
confidence: medium
verification_status: needs-verification
source_refs: ["MITRE ATT&CK 官方網站"]
keywords: ["MITRE 分布", "mitre distribution", "戰術分布", "ATT&CK 熱度"]
last_updated: 2026-07-09
---

# MITRE ATT&CK 分布圖

## 1. 元件目的
呈現告警對應的戰術/技術分布，看攻擊集中在哪些階段。

## 2. 使用情境
「目前最常見的攻擊類型」「攻擊走到哪個階段」；ATT&CK 矩陣式概覽。

## 3. 需要的資料欄位
戰術、技術 id/名稱、計數。

## 4. 對應 Wazuh 欄位
`rule.mitre.tactic`、`rule.mitre.id`、`rule.mitre.technique`（見 [[doc-wazuh-mitre-linkage]]）。

## 5. 對應 AI 分析輸出
（可選）AI 對無 mitre 欄位告警的建議對應，須標「需查官方確認」。

## 6. 視覺化建議
戰術長條 / ATT&CK 矩陣熱度；點技術連 technique 卡。

## 7. 使用者可互動功能
點戰術/技術→過濾相關告警、開 [[doc-mitre-mapping-overview]] 或 technique 卡。

## 8. 篩選條件
時間範圍、戰術。

## 9. 排序方式
計數（多→少）或依 kill chain 階段排列。

## 10. 範例資料格式
```json
[{"tactic":"Credential Access","technique_id":"T1110","count":<n>}]
```
（值為佔位。）

## 11. 注意事項
分布只反映「有 mitre 對應且被觸發」的告警；覆蓋度依規則集，不代表全部攻擊（見 [[doc-wazuh-mitre-linkage]]）。

## 相關文件
[[doc-mitre-mapping-overview]]、[[doc-wazuh-mitre-linkage]]
