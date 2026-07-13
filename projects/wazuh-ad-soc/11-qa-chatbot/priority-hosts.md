---
id: qa-priority-hosts
title: "哪些主機需要優先調查？"
doc_type: qa
category: qa
intent: triage-priority
summary: "以風險（非只告警量）+ 資產重要性 + 是否命中關聯鏈，排出需優先調查的主機清單。"
required_fields: ["agent.name", "rule.level", "rule.mitre.id"]
related_entities: [ent-host-win11-target, ent-host-dc]
dashboard_widgets: [dsh-top-targeted-hosts, dsh-high-risk-events-card]
tags: [cat:qa, type:qa, entity:host]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
keywords: ["優先調查主機", "priority hosts", "triage", "調查順序"]
last_updated: 2026-07-09
---

# 哪些主機需要優先調查？

## 1. 使用者可能問法
「先看哪台？」「哪些機器最急？」「調查順序？」

## 2. 使用者意圖
triage-priority：排出調查優先序。

## 3. 需要查詢的資料來源
時間窗告警（依主機聚合）+ 資產重要性（env-specific）。

## 4. 需要使用的 Wazuh 欄位
`agent.name`、`rule.level`、`rule.mitre.id`。

## 5. 需要關聯的實體
Host（角色見 [[doc-host-roles]]）。

## 6. 回答邏輯
綜合「最高風險等級 + 是否命中關聯鏈（如提權/成功登入）+ 資產重要性（DC>端點）」排序，非只看告警量。

## 7. AI 回答範例
「優先序：① <DC>（雖告警較少，但為關鍵資產且見帳號異動）；② <靶機>（命中暴力破解成功鏈）。建議先處理 critical 鏈涉及的主機。」（值為佔位。）

## 8. 若資料不足時的回答方式
無資產清單 → 說明「以風險排序，資產權重需依環境補」。

## 9. 儀表板建議呈現方式
[[dsh-top-targeted-hosts]] + [[dsh-high-risk-events-card]]。

## 10. 注意事項
告警量 ≠ 風險；關鍵資產與關聯鏈應優先，避免被雜訊主機洗版。
