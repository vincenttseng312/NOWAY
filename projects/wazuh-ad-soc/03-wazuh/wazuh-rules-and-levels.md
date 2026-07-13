---
id: doc-wazuh-rules-and-levels
title: "Wazuh Rule 與 Alert Level 說明"
doc_type: wazuh
category: wazuh
summary: "Wazuh 規則決定哪些事件成為告警並賦予嚴重度 rule.level（一般 0–15，數字越大越嚴重）。rule.groups 是分類標籤、rule.id 是規則編號（數字值 env-specific）。實際分級門檻與規則集需依環境確認。"
tags: [cat:wazuh, type:wazuh, source:wazuh-rule, status:env-specific]
related_entities: [ent-rule, ent-alert]
related_docs: [doc-wazuh-manager, doc-severity-classification, doc-wazuh-mitre-linkage]
keywords: ["Wazuh rule", "rule level", "alert level", "rule groups", "rule id", "嚴重度", "規則", "severity"]
confidence: medium
verification_status: env-specific
source_refs: ["Wazuh 官方文件"]
last_updated: 2026-07-09
---

# Wazuh Rule 與 Alert Level 說明

## 1. 這是什麼
規則（rule）是 Manager 判斷「事件是否成為告警、屬於什麼、多嚴重」的邏輯。

## 2. 關鍵欄位

| 欄位 | 意義 | 注意 |
|---|---|---|
| `rule.id` | 規則編號 | **數字值隨規則集版本/自訂而變 → env-specific，不臆造** |
| `rule.level` | 嚴重度，一般範圍 **0–15**（數字越大越嚴重；低值可能不產生告警） | 具體「幾級=高風險」的門檻依環境，需確認 |
| `rule.description` | 人類可讀描述 | 告警摘要種子 |
| `rule.groups` | 分類標籤（如 authentication、windows、sysmon 等） | 值依規則集；用於情境型樣對映 |

> Wazuh 規則集（內建 + 自訂）與各 `rule.id` 的意義是**部署相關**。本 KB 不記死特定 `rule.id`；需要時以實際 Manager 的規則為準。

## 3. 與嚴重性分級的關係
`rule.level` 是本專題風險分級的**輸入之一**，但最終 info/low/medium/high/critical 的判準另定於 [[doc-severity-classification]]（⏳批 5），且會結合關聯（如「失敗×N 後成功」會拉高等級）。

## 4. AI 如何使用
- 用 `rule.level` 做初步高風險過濾（門檻標「依環境」）。
- 用 `rule.groups` 對映到 05-attack-scenarios 的情境型樣。
- 用 `rule.description` 當摘要種子，但需與 `data.win.*` 交叉確認，不照抄。

## 5. 需依實際環境確認
啟用的規則集、自訂規則、`rule.id` 對應、`rule.level` 分級門檻。

## 相關文件
[[doc-wazuh-manager]]、[[doc-severity-classification]]、[[doc-wazuh-mitre-linkage]]；跨連父層 [[ioc-ttp-and-detection-engineering]]。

## 建議查證來源
Wazuh 官方文件。

## 可被檢索的關鍵字（中英）
Wazuh 規則、rule level、alert level、rule groups、rule id、嚴重度、severity、ruleset。
