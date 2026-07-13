---
id: doc-data-and-event-flow
title: "資料流與事件流"
doc_type: architecture
category: architecture
summary: "事件自 Windows 11 靶機/AD DC 產生 → Wazuh Agent 採集 → Manager 解碼比對規則產生 alert JSON → AI 以 RAG 分析 → 儀表板與問答呈現。本頁定義每一段的輸入輸出與關鍵欄位。"
tags: [cat:overview, type:architecture, source:wazuh-rule]
related_entities: [ent-alert, ent-event, ent-incident]
related_docs: [doc-system-architecture, doc-wazuh-role, doc-ai-role]
keywords: ["資料流", "事件流", "event pipeline", "alert JSON", "decoder", "rule", "RAG", "data flow", "event flow"]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
last_updated: 2026-07-09
---

# 資料流與事件流

## 1. 文件目的
定義一筆事件從產生到呈現的完整路徑與每段的輸入/輸出，是 AI 做時間軸與關聯分析的基礎。

## 2. 背景說明

```
① 事件產生    Windows 11 靶機 / AD DC 的 Security/System/PowerShell 日誌
      │        （欄位：Windows Event ID、providerName、eventdata.*）
      ▼
② 採集        Wazuh Agent（Windows eventchannel）
      ▼
③ 解碼+比對    Wazuh Manager：decoder 解析 → rule 比對 → 產生 alert
      │        （alert 欄位：rule.id/level/description/groups/mitre.*, agent.*, data.win.*）
      ▼
④ AI 分析      LLM + RAG（本知識庫）→ 摘要/時間軸/風險/MITRE/受影響實體/處置
      ▼
⑤ 呈現        儀表板（視覺化）＋ 問答（自然語言）
```

**每段關鍵**：
- ①→② 決定「哪些事件被採集」（Agent 設定，env-specific）。
- ③ 決定「哪些成為告警、對應哪個 MITRE」（ruleset，env-specific；`rule.id` 不臆造）。
- ④ AI 依 `_meta/entity-model.md` 把 alert 欄位對映成 Host/Account/IP/Technique，並串成 Incident。

## 3. 與本專題的關聯
本頁是 timeline 類問答（「整理最近一小時攻擊」）與 alert→報告流程的依據；深入見 03-wazuh/[[alert-to-report-pipeline]]（⏳批 2）。

## 4. 主要實體
Event → Alert → Incident 的轉換鏈；沿途關聯 Host/Account/IP/Technique。

## 5. 可被 LLM 檢索的關鍵字
資料流、事件流、pipeline、alert JSON、decoder、rule 比對、時間軸、event correlation、data flow。

## 6. 相關文件連結
- [[doc-system-architecture]]、[[doc-wazuh-role]]、[[doc-ai-role]]、`_meta/entity-model.md`

## 7. 後續可擴充內容
- 各段延遲/保存/取樣（需確認）。
- alert JSON 範例（去識別化、佔位值），連 03-wazuh。
