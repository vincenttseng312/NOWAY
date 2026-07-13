---
id: doc-ai-role
title: "AI 在本專題中的角色"
doc_type: overview
category: overview
summary: "生成式 AI 是本專題的分析與敘事層：以 Wazuh 告警與本知識庫（RAG）為輸入，產出攻擊摘要、時間軸、風險分級、MITRE 對應、處置建議與自然語言問答，並在資料不足時主動說明限制。"
tags: [cat:overview, type:overview, cat:ai]
related_entities: [ent-alert, ent-incident]
related_docs: [doc-wazuh-role, doc-dashboard-role, doc-qa-role, doc-scope-and-limitations]
keywords: ["AI 角色", "生成式 AI", "LLM", "RAG", "攻擊摘要", "時間軸", "風險分級", "處置建議", "event summarization", "analysis layer"]
confidence: high
verification_status: verified
source_refs: ["MITRE ATT&CK 官方網站", "Wazuh 官方文件"]
last_updated: 2026-07-09
---

# AI 在本專題中的角色

## 1. 文件目的
說明生成式 AI 在系統中的定位（分析與敘事層），以及它的輸入、輸出與行為準則。

## 2. 背景說明
AI 接收兩類輸入：**Wazuh 告警／日誌**（即時證據）與**本知識庫**（透過 RAG 提供的領域知識與模板）。據此產出：
- 攻擊摘要、攻擊時間軸
- 風險分級（依 08-severity 判準）
- MITRE ATT&CK 對應
- 受影響主機／帳號／來源 IP 的彙整
- 建議處置方式、儀表板資料、自然語言問答

**行為準則**（護欄）：資料不足時主動說明限制、不編造證據、不提供真實攻擊指令。權威規則見 `_meta/citation-hallucination-rules.md` 與 [[doc-scope-and-limitations]]。

## 3. 與本專題的關聯
AI 是 Wazuh（[[doc-wazuh-role]]）的下游，並驅動儀表板（[[doc-dashboard-role]]）與問答（[[doc-qa-role]]）。分析流程細節見 09-ai-analysis（⏳批 5）。

## 4. 主要實體
Alert、Event、Incident、Technique、Host、Account、IP——AI 的工作是把這些串成可解釋的事件敘事。

## 5. 可被 LLM 檢索的關鍵字
生成式 AI、LLM、RAG、事件摘要、時間軸、風險分級、MITRE 對應、處置建議、幻覺防治、event narrative、summarization。

## 6. 相關文件連結
- [[doc-wazuh-role]]、[[doc-dashboard-role]]、[[doc-qa-role]]、[[doc-scope-and-limitations]]
- 深入：09-ai-analysis/*（⏳批 5）、`_meta/routing-rules.md`

## 7. 後續可擴充內容
- 提示詞策略、RAG chunking 與召回設定（連批 7 的最終 system prompt 與 RAG 整合規格）。
- AI 輸出的驗證與人工複核流程。
