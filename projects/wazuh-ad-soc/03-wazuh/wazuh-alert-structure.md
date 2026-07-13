---
id: doc-wazuh-alert-structure
title: "Wazuh Alert 結構說明"
doc_type: wazuh
category: wazuh
summary: "Wazuh alert JSON 分為幾組欄位：時間（timestamp）、來源主機（agent.*）、處理者（manager.*）、規則（rule.*，含 mitre）、Windows 事件資料（data.win.*）、與定位（location、full_log）。逐欄的 AI 用途見對照表頁。"
tags: [cat:wazuh, type:wazuh, source:wazuh-rule]
related_entities: [ent-alert]
related_docs: [doc-wazuh-field-to-ai-mapping, doc-wazuh-rules-and-levels, doc-wazuh-mitre-linkage, doc-data-and-event-flow]
keywords: ["Wazuh alert", "alert 結構", "JSON 欄位", "rule", "data.win", "alert structure", "fields"]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
last_updated: 2026-07-09
---

# Wazuh Alert 結構說明

## 1. 這是什麼
一筆告警的結構化 JSON，是 AI 分析的主要輸入。以下依語意分組列出本專題關注的欄位；**逐欄「AI 如何使用」的完整對照表見 [[doc-wazuh-field-to-ai-mapping]]**。

## 2. 欄位分組（本專題關注的 18 欄）

| 群組 | 欄位 | 一句話 |
|---|---|---|
| 時間 | `timestamp` | 事件/告警時間 |
| 來源主機 | `agent.name`、`agent.ip` | 產生事件的受監控主機 |
| 處理者 | `manager.name` | 處理此告警的 Wazuh Manager |
| 規則 | `rule.id`、`rule.level`、`rule.description`、`rule.groups` | 觸發的規則與嚴重度（`rule.id` 數字 env-specific） |
| 規則-MITRE | `rule.mitre.id`、`rule.mitre.tactic`、`rule.mitre.technique` | ATT&CK 對應 |
| Windows 系統 | `data.win.system.eventID`、`data.win.system.providerName` | Windows Event ID 與來源提供者 |
| Windows 事件資料 | `data.win.eventdata.targetUserName`、`data.win.eventdata.ipAddress`、`data.win.eventdata.workstationName` | 帳號/來源 IP/工作站 |
| 定位 | `location`、`full_log` | 日誌來源通道與原始全文 |

> 欄位**路徑存在性**是 Wazuh 標準結構（可陳述）；欄位內的**值**（尤其 `rule.id`、`eventID` 語意）視情況標「需依實際環境／官方文件確認」。實際 alert 可能還有更多欄位，此處只列本專題核心。

## 3. AI 如何使用（摘要）
把欄位對映成實體（見 `_meta/entity-model.md`）、產生摘要（`rule.description` + `data.win.*`）、對應 ATT&CK（`rule.mitre.*`）、建時間軸（`timestamp`）。完整用途見對照表。

## 4. 需依實際環境確認
`rule.id` 數字、`eventID` 的具體規則觸發、額外欄位、時區。

## 相關文件
[[doc-wazuh-field-to-ai-mapping]]、[[doc-wazuh-rules-and-levels]]、[[doc-wazuh-mitre-linkage]]、[[doc-data-and-event-flow]]

## 建議查證來源
Wazuh 官方文件。

## 可被檢索的關鍵字（中英）
Wazuh alert 結構、JSON 欄位、rule、data.win、eventID、alert schema、fields。
