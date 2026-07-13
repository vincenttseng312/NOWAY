---
id: doc-ai-analysis-pipeline
title: "AI 分析流程"
doc_type: ai
category: ai
summary: "AI 把 Wazuh 告警轉成事件敘事的流程：輸入(alert+RAG)→欄位/實體解析→關聯聚合→嚴重性分級→MITRE 對應→產出(摘要/時間軸/風險/受影響實體/處置)。資料不足時說明限制，不臆造。"
tags: [cat:ai, type:ai]
related_entities: [ent-alert, ent-incident]
related_docs: [doc-alert-to-report-pipeline, doc-severity-classification, doc-mitre-mapping-overview, doc-rag-knowledge-base-design]
mitre_attack: []
wazuh_sources: []
windows_event_ids: []
risk_level: ""
confidence: high
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "MITRE ATT&CK 官方網站"]
keywords: ["AI 分析流程", "analysis pipeline", "事件敘事", "摘要", "時間軸", "風險分級"]
last_updated: 2026-07-09
---

# AI 分析流程

## 1. 流程

```
輸入：Wazuh alert(s) + RAG 檢索本 KB
  ▼
① 欄位/實體解析   依 [[doc-wazuh-field-to-ai-mapping]] 取欄位；依 _meta/entity-model 對映 Host/Account/IP/Technique
  ▼
② 關聯聚合        同主機/帳號/IP/時間窗聚成 Incident；套 [[doc-correlation-rules]] 型樣
  ▼
③ 嚴重性分級      依 [[doc-severity-classification]]（基礎分 + 升降因子）
  ▼
④ MITRE 對應      rule.mitre.* → [[doc-mitre-mapping-overview]] → technique 卡
  ▼
⑤ 產出           攻擊摘要 / 時間軸 / 風險分級 / 受影響主機帳號IP / 建議處置 / 儀表板資料 / 問答
```

## 2. 每個產出對應的依據
| 產出 | 主要依據 |
|---|---|
| 攻擊摘要 | rule.description + data.win.* 交叉確認 |
| 攻擊時間軸 | timestamp 排序 + 事件序列 |
| 風險分級 | [[doc-severity-classification]] |
| MITRE 對應 | rule.mitre.* + [[doc-mitre-mapping-overview]] |
| 受影響實體 | 實體解析（agent/targetUserName/ipAddress） |
| 建議處置 | 對應情境頁「處置」段 + [[doc-ir-sop]]（⏳批 6） |

## 3. 行為準則（護欄）
- 資料不足 → 明說缺什麼、不臆造（見 `_meta/citation-hallucination-rules.md`）。
- env-specific 值（rule.id、門檻）→ 標「依實際環境」。
- 分級/結論要可解釋、可追溯到欄位與頁面。
- 不提供攻擊指令（見 [[doc-scope-and-limitations]]）。

## 4. 需依實際環境確認
關聯與分級是由 Wazuh 規則還是 AI 完成、RAG 檢索設定、即時資料連線方式。

## 相關文件
[[doc-alert-to-report-pipeline]]、[[doc-severity-classification]]、[[doc-mitre-mapping-overview]]、[[doc-rag-knowledge-base-design]]、[[doc-ai-role]]

## 建議查證來源
Wazuh 官方文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
AI 分析流程、analysis pipeline、事件敘事、摘要、時間軸、風險分級。
