# SCHEMA — wazuh-ad-soc 知識庫慣例（權威）

本檔是本子專案知識庫的權威設定，優先於父層 `LLM_Wiki/wiki/SCHEMA.md`（僅在本檔未規定時才回退到父層）。任何 AI 助手、RAG、儀表板、聊天機器人在讀寫本 KB 前，先讀本檔。

## 0. 這個 KB 是什麼、給誰用

- **專題**：基於 Wazuh 與生成式 AI 之 Active Directory 環境資安事件監控與智慧分析系統。
- **消費者**：RAG 檢索、儀表板、聊天機器人、事件報告生成——**機器讀優先**，故結構高度規格化。
- **邊界**：僅限授權實驗室、防禦、偵測、資安教育與事件分析。**不含**可武器化的攻擊指令；攻擊情境一律以「偵測重點、可觀測日誌、Wazuh 告警、MITRE 對應、處置建議」呈現。

## 1. 語言慣例（沿用父層）

- 對話與正文：繁體中文。
- 維持英文：frontmatter 欄位名、`tags` 值、slug／檔名、程式碼與欄位識別字（如 `rule.level`、`4625`、`T1110`）。
- 產品/事件專有名詞（Wazuh、Active Directory、Event ID、MITRE technique）維持原文。

## 2. 反幻覺與驗證規則（本 KB 的命脈）

權威定義見 `_meta/citation-hallucination-rules.md`。摘要：

- **絕不編造** Wazuh `rule.id` 數字、Windows Event ID、MITRE technique ID、產品功能。
- Wazuh 數字 `rule.id`、`rule.level` 門檻、decoder 名稱幾乎都是 **ruleset 版本／部署相關** → 一律 `verification_status: env-specific` 或句末標「（需依實際環境確認）」。
- 業界穩定的事實（常見 Windows Event ID、MITRE ID）可直接寫，但仍在 `source_refs` 標建議查證來源。
- 每頁 frontmatter 必帶 `verification_status` 與 `source_refs`。

## 3. 文件型別 doc_type ↔ 資料夾

| doc_type | 資料夾 | 說明 |
|---|---|---|
| overview | 00-overview | 專題總覽、範圍限制 |
| architecture | 01-architecture | 系統架構、拓樸、角色、資料流 |
| environment | 02-environment | AD、靶機、主機清單 |
| wazuh | 03-wazuh | Wazuh 架構/agent/manager/alert/rule/欄位對照 |
| event | 04-windows-ad-events | Windows/AD 安全事件 |
| attack-scenario | 05-attack-scenarios | 攻擊情境（固定 14 段模板） |
| detection | 06-detection-logic | 偵測邏輯、關聯規則 |
| mitre | 07-mitre-attack | MITRE 對應與 technique 卡 |
| severity | 08-severity-risk | 嚴重性分級 |
| ai | 09-ai-analysis | AI 分析流程、RAG 設計 |
| dashboard | 10-dashboard | 儀表板元件 |
| qa | 11-qa-chatbot | 使用者問答條目（固定 10 段模板） |
| report | 12-incident-response/report-templates | 事件報告模板 |
| sop | 12-incident-response | 事件回應 SOP |
| demo | 13-demo | Demo 劇本 |
| entity | entities | 實體卡（host/user/ip/rule/technique/incident） |

## 4. Frontmatter

Base 欄位與各型別擴充的權威定義見 `_meta/rag-metadata-schema.md`。每頁至少有 base 欄位；型別頁加對應擴充。

## 5. 標籤 taxonomy

命名空間化（`cat:`/`type:`/`entity:`/`source:`/`mitre-tactic:`/`mitre-technique:`/`risk:`/`status:`）。規則與已登記標籤見 `_meta/taxonomy.md`。每頁 tags ≤ 8。

## 6. 實體關係模型

見 `_meta/entity-model.md`。這是 RAG 關聯、儀表板聚合、問答實體解析的共用骨架，也是 Wazuh alert JSON → 文件的對映依據。

## 7. 頁面大小與 chunking

- 一頁一主題、可獨立理解；soft cap ~350 行。
- chunk 邊界對齊 `##`（每個 H2 是一個可檢索 chunk）；同型別頁用同一組 H2，讓 retrieval 與 answer template 對齊。

## 8. 連結慣例（跨工具相容）

- Obsidian：`[[slug]]`（同一 vault，可跨連到父層 `LLM_Wiki/wiki/concepts/*`）。
- RAG／Docusaurus／GitBook：不依賴 wikilink 語法，改用 frontmatter `related_docs: [slug]` 與相對路徑。
- **跨連結既有 DFIR 概念群**（父層 wiki）：如 `[[windows-event-log-and-sysmon]]`、`[[persistence-mechanisms]]`、`[[ioc-ttp-and-detection-engineering]]`、`[[process-hollowing]]`、`[[lolbin-and-powershell-abuse]]`——引用不複製，避免雙份漂移。

## 9. 分批生成順序

批0 骨架（本批）→ 批1 總覽/架構/環境+角色定位 → 批2 Wazuh → 批3 Windows/AD 事件 → 批4 攻擊情境+偵測 → 批5 MITRE/嚴重性/AI/儀表板/問答 → 批6 SOP/報告/Demo → 批7 RAG 整合規格 + 最終 system prompt。

## 10. 與父專案的關係

本 KB 是 `LLM_Wiki` 的子專案，**不套父層的 H-I-V-R-K-C 個人學習閉環**（那是學習日誌用；本 KB 是系統文件）。父層 `changelog.md` 記本 KB 的里程碑；本 KB 自己的逐頁進度記在本資料夾（未來可加 `log.md`）。
