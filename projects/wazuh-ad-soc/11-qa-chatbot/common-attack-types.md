---
id: qa-common-attack-types
title: "請列出目前最常見的攻擊類型。"
doc_type: qa
category: qa
intent: entity-ranking
summary: "以 rule.groups / rule.mitre.* 聚合，統計時間窗內最常見的攻擊類型/戰術，給出占比與代表事件。"
required_fields: ["rule.groups", "rule.mitre.tactic", "rule.mitre.id"]
related_entities: [ent-technique]
dashboard_widgets: [dsh-mitre-distribution]
tags: [cat:qa, type:qa, cat:mitre]
confidence: medium
verification_status: needs-verification
source_refs: ["MITRE ATT&CK 官方網站"]
keywords: ["常見攻擊類型", "common attack types", "攻擊分布", "戰術占比"]
last_updated: 2026-07-09
---

# 請列出目前最常見的攻擊類型。

## 1. 使用者可能問法
「最多的是哪種攻擊？」「主要威脅是什麼？」「攻擊類型排行」

## 2. 使用者意圖
entity-ranking（以攻擊類型為維度）：掌握威脅樣貌。

## 3. 需要查詢的資料來源
時間窗告警，依 groups/技術聚合。

## 4. 需要使用的 Wazuh 欄位
`rule.groups`、`rule.mitre.tactic`、`rule.mitre.id`。

## 5. 需要關聯的實體
Technique / Scenario 型樣。

## 6. 回答邏輯
依 groups 或戰術/技術聚合 → 排占比 → 附代表事件與對應情境頁。

## 7. AI 回答範例
「時間窗內最常見：① Brute Force（T1110，<N>%）；② 可疑 PowerShell（T1059.001，<M>%）；③ 連接埠掃描（T1046）。詳見對應情境頁。」（值為佔位。）

## 8. 若資料不足時的回答方式
無 mitre/groups 覆蓋 → 說明「僅能就有對應的告警統計」，不代表全貌（見 [[doc-wazuh-mitre-linkage]]）。

## 9. 儀表板建議呈現方式
[[dsh-mitre-distribution]]。

## 10. 注意事項
統計只反映「有觸發且有分類」的告警；覆蓋度依規則集，勿當成完整威脅面。
