---
id: doc-wazuh-field-to-ai-mapping
title: "Wazuh Alert 欄位與 AI 分析欄位對照表"
doc_type: wazuh
category: wazuh
summary: "本頁逐一說明 18 個核心 Wazuh alert 欄位的意義、AI 如何使用、以及驗證注意事項。是 AI 把 alert JSON 轉成實體、摘要、時間軸、風險與 MITRE 對應的權威對照。"
tags: [cat:wazuh, type:wazuh, source:wazuh-rule]
related_entities: [ent-alert, ent-host-win11-target, ent-rule, ent-technique]
related_docs: [doc-wazuh-alert-structure, doc-ai-role, doc-wazuh-mitre-linkage, doc-alert-to-report-pipeline]
keywords: ["欄位對照", "field mapping", "AI 分析欄位", "rule.mitre", "data.win.eventdata", "targetUserName", "ipAddress", "field to AI"]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
last_updated: 2026-07-09
---

# Wazuh Alert 欄位與 AI 分析欄位對照表

AI 分析的權威對照。**欄位路徑存在性**為 Wazuh 標準結構（可陳述）；欄位內**值**的語意視情況標驗證。實體對映依 `_meta/entity-model.md`。

## 18 核心欄位

| # | Wazuh 欄位 | 意義 | AI 如何使用 | 對映實體 | 驗證注意 |
|---|---|---|---|---|---|
| 1 | `timestamp` | 事件/告警時間 | 建攻擊時間軸、時間範圍過濾、beacon 週期判斷 | — | 時區/格式 env-specific |
| 2 | `agent.name` | 產生事件的受監控主機名 | 「Top 被攻擊主機」聚合、主機解析 | Host | 值 env-specific |
| 3 | `agent.ip` | 該主機 IP | 主機定位、內外網判斷 | Host / IP | 值 env-specific |
| 4 | `manager.name` | 處理此告警的 Manager | 多 Manager 環境溯源 | — | 值 env-specific |
| 5 | `rule.id` | 觸發的規則編號 | 連規則說明；**不臆造數字值** | Rule | **env-specific** |
| 6 | `rule.level` | 嚴重度（一般 0–15） | 風險分級輸入、高風險過濾 | — | 分級門檻需確認 |
| 7 | `rule.description` | 規則人類可讀描述 | 告警摘要種子（需與 data.win 交叉確認，不照抄） | — | 隨規則集 |
| 8 | `rule.groups` | 規則分類標籤 | 對映攻擊情境型樣（→05） | Scenario | 值隨規則集 |
| 9 | `rule.mitre.id` | 對應 MITRE technique id | 連 technique 卡、ATT&CK 對應 | Technique | 以 MITRE 官方為準 |
| 10 | `rule.mitre.tactic` | 對應戰術 | 戰術分布圖、時間軸階段標記 | Tactic | 同上 |
| 11 | `rule.mitre.technique` | 技術名稱 | 報告可讀化 | Technique | 同上 |
| 12 | `data.win.system.eventID` | Windows Event ID | 連事件頁（04）、判讀事件語意 | Event | 語意見白名單，其餘需確認 |
| 13 | `data.win.system.providerName` | 事件來源提供者 | 判斷來源類別（Security/PowerShell/…） | — | 欄位穩定 |
| 14 | `data.win.eventdata.targetUserName` | 目標帳號名 | 帳號解析、暴力破解/異常登入主體 | Account | 可能為機器帳號（結尾 `$`）或 SYSTEM |
| 15 | `data.win.eventdata.ipAddress` | 來源 IP | 「可疑來源 IP」排行、內外判斷、實體解析 | IP | 本機登入可能為 `-`／`::1`／`127.0.0.1` |
| 16 | `data.win.eventdata.workstationName` | 來源工作站名 | 橫向移動/來源溯源 | Host | 可能為空或偽造 |
| 17 | `location` | 日誌來源位置/通道 | 判斷來自哪個 log channel | — | 欄位穩定 |
| 18 | `full_log` | 原始日誌全文 | 兜底解析、佐證、擷取未結構化細節 | — | 內容依事件 |

## 使用原則
1. **先結構化欄位、後 full_log**：能用 `data.win.eventdata.*` 就別只靠 `full_log` 抽字。
2. **交叉確認**：`rule.description` 是「規則作者的話」，仍要用 `eventID` + `eventdata` 驗證實際發生什麼。
3. **實體優先**：把 2/3/14/15/16 解析成 Host/Account/IP，是聚合、排行、關聯的基礎。
4. **不臆造值**：`rule.id`（#5）與未列入白名單的 `eventID` 語意（#12），標「需依實際環境／官方文件確認」。
5. **空值有意義**：`ipAddress` 為 `-`／`workstationName` 為空，本身就是判讀線索（本機 vs 遠端）。

## 相關文件
[[doc-wazuh-alert-structure]]、[[doc-ai-role]]、[[doc-wazuh-mitre-linkage]]、[[doc-alert-to-report-pipeline]]、`_meta/entity-model.md`

## 建議查證來源
Wazuh 官方文件、Microsoft Windows Security Auditing 文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
欄位對照、field mapping、AI 分析欄位、rule.mitre、eventID、targetUserName、ipAddress、workstationName、full_log、field to AI usage。
