---
id: doc-wazuh-role
title: "Wazuh 在本專題中的角色"
doc_type: overview
category: overview
summary: "Wazuh 是本專題的資料蒐集與初步偵測引擎：Agent 於靶機採集 Windows／AD 事件，Manager 解碼比對規則產生告警，並提供 MITRE 對應與欄位化 JSON 供 AI 分析。"
tags: [cat:overview, type:overview, cat:wazuh, source:wazuh-rule]
related_entities: [ent-host-wazuh-manager, ent-host-win11-target]
related_docs: [doc-data-and-event-flow, doc-ai-role]
keywords: ["Wazuh 角色", "資料蒐集", "偵測引擎", "Agent", "Manager", "alert", "SIEM", "log collection", "detection"]
confidence: high
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
last_updated: 2026-07-09
---

# Wazuh 在本專題中的角色

## 1. 文件目的
用一頁說明 Wazuh 在整個系統的定位（資料蒐集 + 初步偵測），並指向 03-wazuh 的深入頁。

## 2. 背景說明
Wazuh 是開源資安監控平台。本專題中：
- **Wazuh Agent**（裝在 Windows 11 靶機）採集 Windows Security／System／PowerShell 等事件與主機狀態。
- **Wazuh Manager**（獨立主機）接收 Agent 資料，經 decoder 解析、rule 比對後產生 **alert**，並可附帶 MITRE ATT&CK 對應（`rule.mitre.*`）。
- 告警以結構化 JSON 呈現，欄位（`rule.id`、`rule.level`、`agent.name`、`data.win.*` 等）是後端 AI 分析的輸入。

> Wazuh 版本、規則集內容、具體 `rule.id` 皆為部署相關，使用時標「需依實際環境確認」。

## 3. 與本專題的關聯
Wazuh 是「日誌 → AI」流程的上游。下游 AI 如何使用這些欄位見 [[doc-ai-role]]；完整資料流見 [[doc-data-and-event-flow]]；欄位語意與 AI 對照見 03-wazuh（[[wazuh-alert-structure]]、[[wazuh-field-to-ai-mapping]]，⏳批 2）。

## 4. 主要實體
Host（Wazuh Manager、靶機 Agent）、Alert、Rule、Event、Technique。

## 5. 可被 LLM 檢索的關鍵字
Wazuh、Agent、Manager、decoder、rule、alert level、告警、資料蒐集、MITRE mapping、eventchannel。

## 6. 相關文件連結
- [[doc-data-and-event-flow]]、[[doc-ai-role]]
- 深入：03-wazuh/*（⏳批 2）

## 7. 後續可擴充內容
- Wazuh 部署拓樸與版本（需確認）、規則集來源、自訂規則策略（連 06-detection-logic）。
