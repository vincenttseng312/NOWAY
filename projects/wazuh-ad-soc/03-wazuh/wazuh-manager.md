---
id: doc-wazuh-manager
title: "Wazuh Manager 說明"
doc_type: wazuh
category: wazuh
summary: "Wazuh Manager 接收 Agent 資料，經 decoder 解析、rule 比對後產生 alert，並附帶嚴重度（rule.level）與 MITRE 對應（rule.mitre.*）。是告警與 ATT&CK 對應的產生點。"
tags: [cat:wazuh, type:wazuh, source:wazuh-rule]
related_entities: [ent-host-wazuh-manager, ent-rule, ent-alert]
related_docs: [doc-wazuh-agent, doc-wazuh-rules-and-levels, doc-wazuh-alert-structure, doc-wazuh-mitre-linkage]
keywords: ["Wazuh Manager", "decoder", "rule", "alert", "analysisd", "告警產生", "manager"]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
last_updated: 2026-07-09
---

# Wazuh Manager 說明

## 1. 這是什麼
Wazuh 的核心處理端。接收 Agent 送來的原始事件，兩步處理：
1. **Decoder**：把原始日誌解析成結構化欄位（如 `data.win.eventdata.*`）。
2. **Rule**：對結構化欄位比對規則，符合就產生 **alert**，賦予 `rule.id`、`rule.level`、`rule.description`、`rule.groups`，並可附 `rule.mitre.*`。

## 2. 在本專題中的角色
是「原始事件 → 可分析告警」的轉換點，也是 MITRE 對應的來源。下游 AI 消費它產出的 alert JSON。

## 3. 關鍵產物
alert JSON（結構見 [[doc-wazuh-alert-structure]]）。規則與嚴重度見 [[doc-wazuh-rules-and-levels]]；MITRE 對應見 [[doc-wazuh-mitre-linkage]]。

> **具體 `rule.id` 數字、規則集內容、decoder 名稱皆為部署/ruleset 相關**，一律標「需依實際環境確認」，不臆造。

## 4. AI 如何使用
AI 把 alert 的欄位對映成實體（`agent.name`→Host、`targetUserName`→Account…，見 `_meta/entity-model.md`），並用 `rule.description`/`rule.mitre.*` 作為摘要與 ATT&CK 對應的種子。

## 5. 需依實際環境確認
Manager 版本、啟用的規則集、自訂規則、`rule.id` 對應關係。

## 相關文件
[[doc-wazuh-agent]]、[[doc-wazuh-rules-and-levels]]、[[doc-wazuh-alert-structure]]、[[doc-wazuh-mitre-linkage]]

## 建議查證來源
Wazuh 官方文件。

## 可被檢索的關鍵字（中英）
Wazuh Manager、decoder、規則比對、告警、alert level、analysisd、alert generation。
