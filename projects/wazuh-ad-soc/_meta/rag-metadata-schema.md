# RAG Metadata Schema（frontmatter 權威定義）

本檔定義每頁 YAML frontmatter 的欄位、型別、允許值，以及 RAG／儀表板／問答如何使用各欄位。SCHEMA.md 第 4 節指向本檔。

## Base 欄位（每頁必備）

| 欄位 | 型別 | 必填 | 允許值 / 格式 | RAG/系統用途 |
|---|---|---|---|---|
| `id` | string | ✅ | 唯一 slug，型別前綴：`scn-`(情境) `evt-`(事件) `ent-`(實體) `qa-`(問答) `dsh-`(儀表板) `rpt-`(報告) `doc-`(其他) | 主鍵、去重、關聯 |
| `title` | string | ✅ | | 標題、引用顯示 |
| `doc_type` | enum | ✅ | 見 SCHEMA 第 3 節 | routing 分類 |
| `category` | string | ✅ | 對應資料夾主題 | 分區檢索 |
| `summary` | string | ✅ | 1–2 句 | embedding、卡片摘要 |
| `tags` | list | ✅ | 命名空間化，≤8，見 taxonomy | 過濾、facet |
| `related_entities` | list | ▲ | entity id | 實體解析、儀表板下鑽 |
| `related_docs` | list | ▲ | 其他頁 slug | 跨工具連結（取代 wikilink） |
| `keywords` | list | ▲ | 中英關鍵字 | 關鍵字召回、同義詞 |
| `confidence` | enum | ✅ | `low` / `medium` / `high` | 本頁內容把握度 |
| `verification_status` | enum | ✅ | `verified` / `needs-verification` / `env-specific` | 防幻覺，見 citation 規則 |
| `source_refs` | list | ✅ | 建議查證來源字串 | 引用出處 |
| `last_updated` | date | ✅ | `YYYY-MM-DD` | 時效 |

▲ = 適用時填。

## 型別擴充

**attack-scenario**（`doc_type: attack-scenario`）
| 欄位 | 型別 | 說明 |
|---|---|---|
| `mitre_attack` | list | technique id，如 `t1110`、`t1059-001` |
| `wazuh_sources` | list | `rule.groups` / decoder 名；數字 `rule.id` 一律標 env-specific |
| `windows_event_ids` | list | 涉及的 Event ID，逐項可帶驗證標記 |
| `risk_level` | enum | `info`/`low`/`medium`/`high`/`critical` |

**event**（`doc_type: event`）：`windows_event_ids`、`event_source`（`security`/`sysmon`/`powershell`/`terminal-services`/`ad`）、`wazuh_sources`。

**qa**（`doc_type: qa`）：`intent`（見 routing-rules）、`required_fields`（需查詢的 Wazuh 欄位）、`related_entities`、`dashboard_widgets`、`risk_level`。

**entity**（`doc_type: entity`）：`entity_type`（`host`/`account`/`ip`/`rule`/`alert`/`technique`/`incident`）、`attributes`（物件）、`relationships`（list，見 entity-model）。

**dashboard**（`doc_type: dashboard`）：`data_fields`（來源 Wazuh 欄位）、`ai_inputs`、`viz_type`、`filters`。

**report**（`doc_type: report`）：`required_inputs`、`optional_inputs`、`audience`（`manager`/`analyst`）。

## RAG 用法備註

- `summary` + `keywords` 進 embedding；`tags` + `doc_type` + `category` 做 metadata 過濾。
- `verification_status != verified` 的內容，回答時 AI 必須顯式加註不確定性（見 citation-hallucination-rules）。
- `related_entities` / `related_docs` 支援 graph-style 擴充檢索（一跳鄰居）。
