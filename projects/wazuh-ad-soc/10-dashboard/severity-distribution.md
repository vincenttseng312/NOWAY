---
id: dsh-severity-distribution
title: "事件嚴重性分布"
doc_type: dashboard
category: dashboard
summary: "以嚴重性等級聚合告警數，呈現 info→critical 的整體分布，快速看整體威脅水位。等級可用 rule.level 分桶或 AI 最終分級。"
tags: [cat:dashboard, type:dashboard]
data_fields: ["rule.level"]
ai_inputs: ["risk_level"]
viz_type: "pie"
filters: ["時間範圍", "主機"]
related_docs: [doc-severity-classification, dsh-high-risk-events-card]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
keywords: ["嚴重性分布", "severity distribution", "威脅水位", "分級占比"]
last_updated: 2026-07-09
---

# 事件嚴重性分布

## 1. 元件目的
呈現各嚴重性等級的占比，掌握整體威脅水位。

## 2. 使用情境
主管概覽、趨勢比較（今天 vs 昨天）。

## 3. 需要的資料欄位
嚴重性等級、計數。

## 4. 對應 Wazuh 欄位
`rule.level`（分桶）。

## 5. 對應 AI 分析輸出
`risk_level`（AI 最終分級，較貼近實際風險；見 [[doc-severity-classification]]）——建議以此為主、`rule.level` 為輔。

## 6. 視覺化建議
圓餅/堆疊長條；critical/high 用警示色。

## 7. 使用者可互動功能
點某等級→過濾該等級告警 → [[dsh-high-risk-events-card]]。

## 8. 篩選條件
時間範圍、主機。

## 9. 排序方式
依等級序（critical→info）。

## 10. 範例資料格式
```json
[{"severity":"critical","count":<n>},{"severity":"high","count":<n>}]
```
（值為佔位。）

## 11. 注意事項
`rule.level` 分桶門檻與 AI 分級門檻皆 env-specific（見 [[doc-severity-classification]]）；兩者可能不同，需標明用哪一個。

## 相關文件
[[doc-severity-classification]]、[[dsh-high-risk-events-card]]
