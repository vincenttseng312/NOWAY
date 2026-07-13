---
id: dsh-ai-summary-block
title: "AI 事件摘要區塊"
doc_type: dashboard
category: dashboard
summary: "在儀表板/詳細頁嵌入的 AI 生成事件摘要：用一段話說清楚誰、何時、對哪台主機、做了什麼、風險與對應技術。可切換主管版/技術版。"
tags: [cat:dashboard, type:dashboard, cat:ai]
data_fields: []
ai_inputs: ["event_summary", "risk_level", "affected_entities"]
viz_type: "block"
filters: ["對象(主管/技術)"]
related_docs: [doc-ai-analysis-pipeline, dsh-ai-remediation-block, rpt-manager-summary]
confidence: medium
verification_status: needs-verification
source_refs: []
keywords: ["AI 摘要區塊", "ai summary", "事件摘要", "主管版/技術版"]
last_updated: 2026-07-09
---

# AI 事件摘要區塊

## 1. 元件目的
把一起事件/一段告警濃縮成人類可讀摘要，嵌在首頁側欄或詳細頁。

## 2. 使用情境
「用主管看得懂的方式說明」「這起事件的摘要」。

## 3. 需要的資料欄位
（消費 AI 輸出，不直接讀 Wazuh 原欄位）

## 4. 對應 Wazuh 欄位
間接：摘要背後的證據來自告警欄位（見 [[doc-ai-analysis-pipeline]]）。

## 5. 對應 AI 分析輸出
`event_summary`、`risk_level`、`affected_entities`（主機/帳號/IP）。

## 6. 視覺化建議
文字區塊 + 風險徽章 + 受影響實體標籤；可切換主管版（少術語）/技術版（含欄位、技術 id）。

## 7. 使用者可互動功能
切換對象、展開為完整報告（連 [[rpt-manager-summary]] / analyst 版）。

## 8. 篩選條件
對象（主管/技術）。

## 9. 排序方式
（單一區塊，不適用）

## 10. 範例資料格式
```json
{"summary":"<一段話>","risk":"high","technique":["T1110","T1078"],"affected":{"host":"<h>","account":"<a>","ip":"<ip>"},"audience":"manager"}
```
（值為佔位。）

## 11. 注意事項
摘要必須可追溯到 [[dsh-event-detail-view]] 的原始欄位；不足處標不確定，不臆造（見 `_meta/citation-hallucination-rules.md`）。

## 相關文件
[[doc-ai-analysis-pipeline]]、[[dsh-ai-remediation-block]]、[[rpt-manager-summary]]
