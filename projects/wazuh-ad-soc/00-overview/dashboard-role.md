---
id: doc-dashboard-role
title: "儀表板在本專題中的角色"
doc_type: overview
category: overview
summary: "儀表板是本專題的呈現層：把 Wazuh 告警與 AI 分析結果視覺化成 SOC 首頁、高風險卡片、攻擊時間軸、Top 來源/主機/帳號、MITRE 分布等，支援下鑽與篩選。"
tags: [cat:overview, type:overview, cat:dashboard]
related_entities: [ent-alert, ent-host-win11-target]
related_docs: [doc-ai-role, doc-qa-role]
keywords: ["儀表板角色", "SOC 首頁", "視覺化", "攻擊時間軸", "Top IP", "MITRE 分布", "dashboard", "visualization", "SOC"]
confidence: high
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
last_updated: 2026-07-09
---

# 儀表板在本專題中的角色

## 1. 文件目的
說明儀表板的定位（把告警與 AI 分析變成可視、可互動的畫面），並指向 10-dashboard 的元件設計。

## 2. 背景說明
儀表板消費兩類資料：**Wazuh 告警欄位**與 **AI 分析輸出**。典型元件：SOC 首頁、高風險事件卡片、攻擊時間軸、Top 攻擊來源 IP、Top 被攻擊主機、Top 受影響帳號、MITRE 戰術分布、嚴重性分布、登入失敗趨勢、RDP／PowerShell／AD 帳號異動監控、單一事件詳細頁、AI 摘要與建議區塊、問答介面。

聚合維度以實體為準（Host／IP／Account），見 `_meta/entity-model.md`。門檻與具體欄位對應標「需依實際環境確認」。

## 3. 與本專題的關聯
儀表板是 AI（[[doc-ai-role]]）與問答（[[doc-qa-role]]）的視覺出口。元件逐一設計見 10-dashboard/*（⏳批 5）。

## 4. 主要實體
Alert、Host、IP、Account、Technique、Incident——多作為儀表板的聚合／篩選維度。

## 5. 可被 LLM 檢索的關鍵字
儀表板、SOC dashboard、視覺化、時間軸、Top 來源 IP、被攻擊主機、MITRE 分布、嚴重性分布、下鑽、drill-down。

## 6. 相關文件連結
- [[doc-ai-role]]、[[doc-qa-role]]
- 深入：10-dashboard/*（⏳批 5）、儀表板指標見專題總覽的指標段

## 7. 後續可擴充內容
- 儀表板資料 API 與 Wiki 文件的關聯（連批 7 RAG 整合規格）。
- 即時 vs 歷史檢視、時間範圍篩選設計。
