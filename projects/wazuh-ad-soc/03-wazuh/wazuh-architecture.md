---
id: doc-wazuh-architecture
title: "Wazuh 架構總覽"
doc_type: wazuh
category: wazuh
summary: "Wazuh 由 Agent（採集）、Server/Manager（解碼比對規則、產生告警）、Indexer（儲存索引）、Dashboard（檢視）四大元件組成；本專題用它蒐集 Windows/AD 事件並輸出結構化告警供 AI 分析。"
tags: [cat:wazuh, type:wazuh, source:wazuh-rule]
related_entities: [ent-host-wazuh-manager, ent-host-win11-target]
related_docs: [doc-wazuh-agent, doc-wazuh-manager, doc-wazuh-alert-structure, doc-data-and-event-flow]
keywords: ["Wazuh 架構", "Agent", "Manager", "Indexer", "Dashboard", "SIEM", "XDR", "wazuh architecture", "components"]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
last_updated: 2026-07-09
---

# Wazuh 架構總覽

## 1. 這是什麼
Wazuh 是開源資安監控平台（SIEM/XDR 類）。在本專題中扮演「資料蒐集 + 初步偵測」引擎，見 [[doc-wazuh-role]]。

## 2. 四大元件

| 元件 | 職責 | 本專題對應 |
|---|---|---|
| Wazuh Agent | 裝在受監控端點，採集日誌與主機狀態，回傳 Manager | 裝於 Windows 11 靶機，見 [[doc-wazuh-agent]] |
| Wazuh Server / Manager | 解碼（decoder）+ 規則比對（rule）→ 產生 alert；含 MITRE 對應 | 內部網段獨立主機，見 [[doc-wazuh-manager]] |
| Wazuh Indexer | 儲存與索引告警（以 OpenSearch 為基礎） | 供查詢；具體堆疊/版本需確認 |
| Wazuh Dashboard | 檢視告警與規則（以 OpenSearch Dashboards 為基礎） | 原生檢視，見 [[doc-wazuh-dashboard]] |

> 元件的部署方式（單機/分散式）、版本、堆疊名稱皆為部署相關（需依實際環境確認）。

## 3. 資料如何流動
Agent 採集 → Manager 解碼比對 → 產生 alert JSON → Indexer 儲存 → Dashboard/後端 AI 取用。完整五段流程見 [[doc-data-and-event-flow]]。

## 4. AI 如何使用
AI 不直接碰 Wazuh 內部，而是消費 Manager 產出的 **alert JSON 欄位**（見 [[doc-wazuh-alert-structure]] 與 [[doc-wazuh-field-to-ai-mapping]]）。

## 5. 需依實際環境確認
部署拓樸、各元件版本、Indexer/Dashboard 堆疊、是否單機。

## 相關文件
[[doc-wazuh-agent]]、[[doc-wazuh-manager]]、[[doc-wazuh-alert-structure]]、[[doc-data-and-event-flow]]

## 建議查證來源
Wazuh 官方文件。

## 可被檢索的關鍵字（中英）
Wazuh 架構、元件、Agent、Manager、Indexer、Dashboard、SIEM、XDR、architecture、components。
