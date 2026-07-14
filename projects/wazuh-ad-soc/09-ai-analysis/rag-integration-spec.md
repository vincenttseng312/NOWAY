---
id: doc-rag-integration-spec
title: "RAG 整合規格（KB → RAG/儀表板/聊天機器人）"
doc_type: ai
category: ai
summary: "把整個 wazuh-ad-soc 知識庫整理成可被 RAG 系統、儀表板 API、聊天機器人使用的整合規格：資料夾/命名/frontmatter/標籤/chunking/metadata/retrieval/routing/引用/防幻覺/資料不足規則，以及 Wazuh alert JSON、Dashboard、Chatbot 三者與文件的關聯方式。"
tags: [cat:ai, type:ai]
related_entities: []
related_docs: [doc-rag-knowledge-base-design, doc-ai-analysis-pipeline, doc-system-prompt]
mitre_attack: []
wazuh_sources: []
windows_event_ids: []
risk_level: ""
confidence: medium
verification_status: needs-verification
source_refs: []
keywords: ["RAG 整合", "rag integration", "系統規格", "chunking", "routing", "整合方式"]
last_updated: 2026-07-09
---

# RAG 整合規格

本頁是把本 KB 接上 RAG／儀表板／聊天機器人的權威整合規格。多數細節已定義於 `_meta/`，此處統整並補上三大介接方式（第 12–14 項）。

## 1. 建議資料夾結構
見 [SCHEMA 第 3 節](../SCHEMA.md) 的 doc_type↔資料夾對映。編號資料夾（00–13）同時滿足 GitBook/Docusaurus 排序與 RAG 分區；`_meta/` 為規格層、`templates/` 為模板、`entities/` 為實體卡。

## 2. Markdown 檔案命名規則
全小寫、連字號、`.md`；slug 穩定不可翻譯（wikilink/related_docs 依賴）。id 前綴：`doc-`/`evt-`/`scn-`/`ent-`/`qa-`/`dsh-`/`rpt-`/`ent-tech-`。

## 3. YAML frontmatter 統一格式
權威定義見 `_meta/rag-metadata-schema.md`。base 欄位每頁必備；型別擴充依 doc_type。

## 4. 標籤命名規則
命名空間化（`cat:`/`type:`/`entity:`/`source:`/`mitre-tactic:`/`mitre-technique:`/`risk:`/`status:`），見 `_meta/taxonomy.md`。

## 5. 文件 chunking 策略
**chunk 邊界對齊 `##`（H2）**；同型別頁共用同一組 H2，使 retrieval 與 answer/report template 對齊。每頁 `summary`+`keywords`（中英）進 embedding。見 `_meta` 與 [[doc-rag-knowledge-base-design]]。

## 6. metadata 設計
用 frontmatter 做結構化過濾：`doc_type`/`category`/`tags`/`risk_level`/`mitre_attack`/`verification_status`。`related_docs`/`related_entities` 支援 graph 式鄰居擴充。

## 7. retrieval query 設計
`embedding(summary+keywords) + metadata 過濾 + 一跳鄰居擴充`。fuzzy 查詢先過 `index.md` 一行摘要做語意比對，再進頁。

## 8. 問題→文件分類 routing
先分類 `intent`（8 類）再檢索，見 `_meta/routing-rules.md`。每個 qa 頁帶 `intent` 作為 routing 種子語料。

## 9. LLM 引用規則
回答附 `related_docs` 出處（頁 title/slug）；陳述事件/技術事實附「（來源：Microsoft/MITRE 官方，建議查證）」；env-specific 值附「（需依實際環境確認）」。見 `_meta/citation-hallucination-rules.md`。

## 10. 避免幻覺規則
絕不編造 Wazuh 數字 `rule.id`、未確認 Event ID、未確認 technique id、產品功能。有把握者見白名單（citation-hallucination-rules 第 3 節），其餘標驗證狀態。

## 11. 資料不足規則
明說缺什麼（缺即時源/缺頁/需環境確認）→ 只回 KB 能支持的一般性內容 → 提出補齊需要的資料 → 不用假值填補。見 citation-hallucination-rules 第 5 節。

## 12. Wazuh alert JSON ↔ Wiki 文件的關聯方式
一筆 alert 進來時：
```
rule.mitre.id            → 07-mitre-attack/technique-cards/<tid>
data.win.system.eventID  → 04-windows-ad-events/<event>
rule.groups              → 05-attack-scenarios/<scenario 型樣>
agent.name               → entities/ent-host-*
data.win.eventdata.targetUserName → entities/ent-acct-*
data.win.eventdata.ipAddress      → entities/ent-ip-*
```
對映表見 `_meta/entity-model.md`；欄位語意見 [[doc-wazuh-field-to-ai-mapping]]。**具體 rule.id/eventID 語意標驗證狀態。**

## 13. Dashboard API ↔ Wiki 文件的關聯方式
每個 `dsh-*` 頁的 frontmatter `data_fields`（Wazuh 欄位）與 `ai_inputs`（AI 輸出）就是該元件的資料契約：儀表板 API 依 `data_fields` 取即時值、依 `ai_inputs` 取 AI 分析、依 `viz_type`/`filters` 呈現。元件與問題的對應見各 qa 頁的 `dashboard_widgets`。

## 14. AI Chatbot ↔ Wiki 文件的關聯方式
```
使用者問題 → 分類 intent（routing-rules） → 檢索候選頁（index + metadata）
          → 讀頁 + 一跳鄰居擴充（entity-model） → 套 answer/report 模板
          → 附引用、標不確定 → （可選）觸發儀表板下鑽
```
即時告警數值由 Wazuh 資料源提供；KB 提供「這代表什麼、怎麼處置」的知識與模板。系統提示詞見 [[doc-system-prompt]]。

## 需依實際環境確認
embedding 模型、chunk 大小微調、top-k、與 Wazuh/Dashboard 的實際 API 介接、即時資料連線方式。

## 相關文件
[[doc-rag-knowledge-base-design]]、[[doc-ai-analysis-pipeline]]、[[doc-system-prompt]]、`_meta/*`

## 可被檢索的關鍵字（中英）
RAG 整合、rag integration、系統規格、chunking、routing、metadata、alert 關聯、dashboard 關聯、chatbot 關聯。
