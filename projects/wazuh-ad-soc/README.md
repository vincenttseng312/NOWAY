# Wazuh × 生成式 AI × Active Directory 資安監控知識庫

> 專題：**基於 Wazuh 與生成式 AI 之 Active Directory 環境資安事件監控與智慧分析系統**
> 定位：一份供 **RAG／儀表板／聊天機器人／事件報告生成** 查詢、引用、摘要與推理的結構化知識庫。
> 邊界：僅限授權實驗室、防禦、偵測、資安教育與事件分析用途。

## 這份知識庫做什麼

把「Wazuh 蒐集到的 Windows／AD／網路安全事件」與「LLM 分析能力」之間的知識固化下來，讓後端 AI 能穩定產出：攻擊摘要、攻擊時間軸、風險分級、MITRE ATT&CK 對應、受影響主機/帳號/來源 IP、處置建議、儀表板資料、自然語言問答。

## 怎麼讀（給人與給 AI）

1. **先讀 [SCHEMA.md](SCHEMA.md)** — 本 KB 的權威慣例（frontmatter、taxonomy、反幻覺規則）。
2. **`_meta/`** — 給機器讀的規格層：metadata schema、實體關係模型、問答 routing、引用/防幻覺規則。
3. **[index.md](index.md)** — 全頁一行摘要目錄，是 RAG router 的第一站。
4. 內容依編號資料夾展開（00 總覽 → 13 Demo），詳見 SCHEMA 第 3 節。

## 三條不可違反的原則

1. **不編造** Wazuh `rule.id`、Windows Event ID、MITRE technique ID 或產品功能；不確定就標「（需依實際環境確認）」或「（需依官方文件確認）」。
2. **防禦優先**：攻擊情境只描述偵測重點、可觀測日誌、Wazuh 告警、MITRE 對應與處置建議，**不提供可武器化的攻擊指令**。
3. **可追溯**：每頁帶 `verification_status` 與 `source_refs`；官方查證來源固定指向 **Wazuh 官方文件 / Microsoft Windows Security Auditing 文件 / MITRE ATT&CK 官方網站**。

## 專題環境（摘要，詳見 02-environment）

內部網段：Windows 11 靶機（加入 AD 網域、裝 Wazuh Agent）、AD Domain Controller、Wazuh Server/Manager、路由器；外部網段：授權實驗用攻擊者主機。Wazuh 蒐集事件 → 後端串接 LLM 分析。

## 狀態

本 KB 為 `LLM_Wiki` 的子專案，**批 0–7 全數完成（8 批，共 132 檔）**：骨架/規格層/模板、總覽/架構、Wazuh、Windows/AD 事件、攻擊情境+偵測、MITRE/嚴重性/AI/儀表板/問答、事件回應 SOP/報告模板/Demo、RAG 整合規格+system prompt。

**要上線 AI 助手**：複製 [09-ai-analysis/system-prompt.md](09-ai-analysis/system-prompt.md) 作系統提示詞，依 [09-ai-analysis/rag-integration-spec.md](09-ai-analysis/rag-integration-spec.md) 設定 RAG 與介接。

**可選後續**：填 `entities/` 的 host/account/ip 實體卡（各頁 frontmatter 已引用、實體卡本身待建）；技術卡可再擴充；接上即時 Wazuh 資料源後在 system prompt 補即時查詢工具。
