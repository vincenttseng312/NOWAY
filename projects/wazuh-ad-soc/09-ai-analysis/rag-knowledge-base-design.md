---
id: doc-rag-knowledge-base-design
title: "RAG 知識庫設計"
doc_type: ai
category: ai
summary: "說明本 KB 如何被 RAG 檢索：以 ## 為 chunk 邊界、用 frontmatter metadata 過濾、依 intent routing、以 related_docs/related_entities 做鄰居擴充，並以引用與防幻覺規則約束回答。批 7 會出完整整合規格。"
tags: [cat:ai, type:ai]
related_entities: []
related_docs: [doc-ai-analysis-pipeline, doc-qa-role]
mitre_attack: []
wazuh_sources: []
windows_event_ids: []
risk_level: ""
confidence: medium
verification_status: needs-verification
source_refs: []
keywords: ["RAG 設計", "chunking", "metadata", "retrieval", "embedding", "knowledge base"]
last_updated: 2026-07-09
---

# RAG 知識庫設計

## 1. 檢索單位（chunking）
- **chunk 邊界對齊 `##`**：每個 H2 是一個可檢索片段；同型別頁用同一組 H2（見各 templates），讓檢索與 answer template 對齊。
- 每頁 `summary` + `keywords`（中英）進 embedding，提高召回。

## 2. Metadata 過濾
用 frontmatter 做結構化過濾：`doc_type`、`category`、`tags`、`risk_level`、`mitre_attack`、`verification_status`。權威定義見 `_meta/rag-metadata-schema.md`。

## 3. Routing（問題→分類）
依 `intent`（8 類）route 到候選 `doc_type/category`，見 `_meta/routing-rules.md`。先分類再檢索，減少雜訊。

## 4. 鄰居擴充
用 `related_docs`、`related_entities` 做一跳擴充（如從情境頁擴到其事件頁、technique 卡、entity 卡），補足單頁不足的脈絡。

## 5. 引用與防幻覺
- 回答附 `related_docs` 出處。
- `verification_status != verified` 的內容，回答時顯式加註不確定。
- env-specific 值不給死值。
- 權威規則見 `_meta/citation-hallucination-rules.md`。

## 6. 與 Wazuh 即時資料的分工
本 KB 提供**領域知識與模板**（穩定）；即時的告警數值由 Wazuh 資料源提供（動態）。AI 把兩者結合：KB 解釋「這代表什麼、怎麼處置」，即時資料提供「現在發生了什麼」。缺即時連線時只回 KB 能支持的一般性內容並說明界線。

## 7. 需依實際環境確認
embedding 模型、chunk 大小微調、檢索 top-k、與 Wazuh/Dashboard 的資料介接方式（批 7 整合規格詳述）。

## 相關文件
[[doc-ai-analysis-pipeline]]、[[doc-qa-role]]、`_meta/*`；批 7 RAG 整合規格（⏳）。

## 建議查證來源
（RAG 為系統設計，無單一官方來源；實作以所選框架文件為準。）

## 可被檢索的關鍵字（中英）
RAG 設計、chunking、metadata、retrieval、embedding、knowledge base。
