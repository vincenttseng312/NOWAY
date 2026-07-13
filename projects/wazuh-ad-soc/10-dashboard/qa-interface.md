---
id: dsh-qa-interface
title: "使用者問答介面"
doc_type: dashboard
category: dashboard
summary: "嵌在儀表板的自然語言問答入口：使用者提問→intent 分類→檢索 KB/告警→回答並附引用與下鑽連結。是問答系統的前端呈現。"
tags: [cat:dashboard, type:dashboard, cat:qa]
data_fields: []
ai_inputs: ["qa_answer"]
viz_type: "chat"
filters: ["時間範圍(對話上下文)"]
related_docs: [doc-qa-role, doc-routing-rules, doc-ai-analysis-pipeline]
confidence: medium
verification_status: needs-verification
source_refs: []
keywords: ["問答介面", "qa interface", "chatbot", "自然語言查詢"]
last_updated: 2026-07-09
---

# 使用者問答介面

## 1. 元件目的
提供自然語言查詢入口，把問題轉成對 KB 與告警的檢索。

## 2. 使用情境
所有 11-qa-chatbot 問答類型的前端（見 [[doc-qa-role]]）。

## 3. 需要的資料欄位
（消費 AI 問答輸出；背後依 intent 決定查哪些欄位，見 `_meta/routing-rules.md`）

## 4. 對應 Wazuh 欄位
依問題 intent 動態決定（如 entity-ranking 用 ipAddress/agent.name）。

## 5. 對應 AI 分析輸出
`qa_answer`（含引用 related_docs 與下鑽連結）。

## 6. 視覺化建議
對話框 + 回答內嵌小圖/表 + 「下鑽」按鈕連到對應儀表板/詳細頁。

## 7. 使用者可互動功能
提問、追問、點引用來源、把回答轉報告、下鑽。

## 8. 篩選條件
對話上下文的時間範圍。

## 9. 排序方式
（對話時序）

## 10. 範例資料格式
```json
{"question":"<自然語言>","intent":"triage-priority","answer":"<...>","citations":["doc-severity-classification"],"drilldown":"dsh-high-risk-events-card"}
```
（值為佔位。）

## 11. 注意事項
回答須附引用、標不確定、資料不足時說明限制（見 `_meta/citation-hallucination-rules.md`）；不提供攻擊指令。

## 相關文件
[[doc-qa-role]]、`_meta/routing-rules.md`、[[doc-ai-analysis-pipeline]]
