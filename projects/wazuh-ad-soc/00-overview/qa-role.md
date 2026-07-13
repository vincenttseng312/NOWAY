---
id: doc-qa-role
title: "使用者問答系統在本專題中的角色"
doc_type: overview
category: overview
summary: "問答系統是本專題的互動層：讓使用者用自然語言詢問 Wazuh 告警、Windows／AD 事件與攻擊情境，AI 依 intent 分類、檢索知識庫與關聯實體後作答，並在資料不足時說明限制。"
tags: [cat:overview, type:overview, cat:qa]
related_entities: []
related_docs: [doc-ai-role, doc-dashboard-role]
keywords: ["問答系統角色", "自然語言查詢", "chatbot", "intent", "RAG 檢索", "資安問答", "natural language Q&A"]
confidence: high
verification_status: verified
source_refs: ["Wazuh 官方文件", "MITRE ATT&CK 官方網站"]
last_updated: 2026-07-09
---

# 使用者問答系統在本專題中的角色

## 1. 文件目的
說明聊天問答的定位（自然語言互動入口），以及它如何把問題轉成對知識庫與告警的查詢。

## 2. 背景說明
使用者以自然語言提問（如「今天有哪些高風險事件？」「這筆 Alert 是什麼意思？」）。系統流程：
1. 分類 `intent`（8 類，見 `_meta/routing-rules.md`）。
2. 抽取實體（主機／帳號／IP／時間範圍）。
3. Route 到候選文件分類 → 讀 `index.md` 選頁 → 讀頁 → 一跳鄰居擴充。
4. 套對應 answer／report 模板作答，附引用與不確定性標註。
5. 資料不足時依 `_meta/citation-hallucination-rules.md` 第 5 節說明限制，不臆造。

## 3. 與本專題的關聯
問答系統由 AI（[[doc-ai-role]]）驅動，並可觸發儀表板（[[doc-dashboard-role]]）下鑽。問答條目逐一設計見 11-qa-chatbot/*（⏳批 5）。

## 4. 主要實體
問答涉及所有實體，尤其 Host／Account／IP（實體解析）與 Alert／Technique／Incident（內容）。

## 5. 可被 LLM 檢索的關鍵字
問答系統、chatbot、自然語言查詢、intent 分類、RAG routing、事件問答、誤判判斷、報告生成、Q&A。

## 6. 相關文件連結
- [[doc-ai-role]]、[[doc-dashboard-role]]、`_meta/routing-rules.md`
- 深入：11-qa-chatbot/*（⏳批 5）

## 7. 後續可擴充內容
- 多輪對話與上下文保留、追問澄清策略。
- 問答到儀表板/報告的交接（「幫我把這個做成報告」）。
