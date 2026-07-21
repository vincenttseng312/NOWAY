---
id: doc-scope-and-limitations
title: "專題範圍與限制"
doc_type: overview
category: overview
summary: "界定本專題的授權、防禦、證據與資料治理邊界：不提供可武器化指令、不把截圖視為完整驗證、不公開 credential／原始敏感 artifact，高權限控制需最小化。"
tags: [cat:overview, type:overview, status:verified]
related_entities: []
related_docs: [doc-project-overview, doc-ai-role]
keywords: ["範圍", "限制", "授權實驗室", "防禦用途", "倫理邊界", "反幻覺", "scope", "limitations", "authorized lab", "defensive"]
confidence: high
verification_status: verified
source_refs: ["Wazuh 官方文件", "Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站", "range-main", "Threat Hunting Essential 期中／期末報告"]
last_updated: 2026-07-20
---

# 專題範圍與限制

## 1. 文件目的
明確界定本專題與知識庫「能做什麼、不能做什麼」，作為 AI 回答時的護欄，避免越界或產生誤導。

## 2. 背景說明
本專題涉及攻擊模擬與資安分析，因此必須有清楚的倫理與技術邊界。

**用途範圍**：授權實驗室環境、防禦、偵測、資安教育、事件分析。

**明確限制**：
1. 僅限授權實驗室。所有攻擊模擬都在隔離網段、對自有靶機進行。
2. **不提供**可直接用於真實攻擊的武器化指令；攻擊情境只談偵測重點、可觀測日誌、Wazuh 告警、MITRE 對應與處置建議。
3. 不確定資訊標「（需依實際環境確認）」或「（需依官方文件確認）」。
4. **不編造**不存在的 Wazuh `rule.id`、Windows Event ID、產品功能。
5. 引用官方資訊時標建議查證來源（Wazuh／Microsoft／MITRE）。
6. **不公開敏感設定**：帳密、token、private key、內部 listener、未去識別 IP／主機資料不得寫入公開 Git、prompt、截圖或範例 JSON。
7. **高權限功能採最小化**：remote command、Active Response、Suricata Drop、Indexer 對外監聽與 AI tool write access 必須有 allow-list、獨立身分、audit log、限時啟用與回復步驟。
8. **截圖不是完整驗證**：Agent Active 或 dashboard 告警只能證明局部管線；效能與回歸主張需有 raw artifact、ground truth、版本與重跑結果。
9. **AI／ML 不作證據來源**：LLM 摘要與模型分類必須回溯至原始事件；缺資料或缺指標時標為未驗證。

## 3. 與本專題的關聯
本頁的限制對**所有頁面**與 AI 回答生效，權威細則見 `_meta/citation-hallucination-rules.md`。

## 4. 主要實體
不適用（政策性文件）。

## 5. 可被 LLM 檢索的關鍵字
專題限制、使用邊界、授權範圍、防禦用途、不武器化、反幻覺規則、免責、authorized use、guardrails。

## 6. 相關文件連結
- `_meta/citation-hallucination-rules.md`、[[doc-project-overview]]、[[doc-ai-role]]

## 7. 後續可擴充內容
- 資料保存與隱私處理細則（PCAP／EVTX corpus、帳號去識別化、保留期限與存取權限，需依實際規範確認）。
- 法遵/校規對照（如適用，需確認）。
