---
id: doc-wazuh-dashboard
title: "Wazuh Dashboard 在本專題中的用途"
doc_type: wazuh
category: wazuh
summary: "Wazuh 內建 Dashboard（以 OpenSearch Dashboards 為基礎）用於檢視原始告警、規則命中與 MITRE 視圖，是驗證與探索用；本專題另有由 AI 驅動的自訂 SOC 儀表板（10-dashboard），兩者分工不同。"
tags: [cat:wazuh, type:wazuh, cat:dashboard]
related_entities: [ent-alert]
related_docs: [doc-dashboard-role, doc-wazuh-alert-structure]
keywords: ["Wazuh Dashboard", "OpenSearch Dashboards", "原生儀表板", "告警檢視", "built-in dashboard"]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
last_updated: 2026-07-09
---

# Wazuh Dashboard 在本專題中的用途

## 1. 這是什麼
Wazuh 隨附的網頁介面（以 OpenSearch Dashboards 為基礎），用來檢視索引後的告警、規則命中、agent 狀態與 MITRE 相關視圖。

## 2. 與本專題自訂儀表板的分工

| | Wazuh 內建 Dashboard | 自訂 SOC 儀表板（10-dashboard） |
|---|---|---|
| 資料 | 原始 alert / 規則 / agent 狀態 | Wazuh 欄位 **+ AI 分析輸出** |
| 目的 | 驗證、探索、除錯規則 | 給人看的攻擊敘事、風險、處置 |
| 產生者 | Wazuh 原生 | 本專題自建，見 [[doc-dashboard-role]] |

> 內建 Dashboard 的可用視圖、模組、版本皆為部署相關（需依實際環境確認）。

## 3. 在本專題中的角色
- **驗證面**：核對 AI 分析所依據的原始告警是否存在、欄位是否如預期——這是防幻覺的人工對照點。
- **探索面**：分析人員手動 pivot 查詢，補 AI 未涵蓋的角度。

## 4. AI 如何使用
AI 一般不直接讀內建 Dashboard，而是讀底層 alert JSON。但「內建 Dashboard 能查到某告警」可作為 AI 結論的佐證來源。

## 5. 需依實際環境確認
可用模組/視圖、版本、權限、是否啟用 MITRE 模組。

## 相關文件
[[doc-dashboard-role]]、[[doc-wazuh-alert-structure]]、10-dashboard/*（⏳批 5）

## 建議查證來源
Wazuh 官方文件。

## 可被檢索的關鍵字（中英）
Wazuh Dashboard、OpenSearch Dashboards、原生儀表板、告警檢視、built-in dashboard、explore。
