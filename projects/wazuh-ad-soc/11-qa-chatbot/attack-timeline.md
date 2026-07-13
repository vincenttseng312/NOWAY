---
id: qa-attack-timeline
title: "請產出攻擊時間軸。"
doc_type: qa
category: qa
intent: timeline
summary: "把指定範圍（時間/主機/帳號/事件）的告警依 timestamp 排序，標戰術階段與關聯鏈，輸出可讀時間軸。"
required_fields: ["timestamp", "rule.mitre.tactic", "agent.name", "data.win.system.eventID", "data.win.eventdata.targetUserName"]
related_entities: [ent-incident]
dashboard_widgets: [dsh-attack-timeline]
tags: [cat:qa, type:qa]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "MITRE ATT&CK 官方網站"]
keywords: ["攻擊時間軸", "attack timeline", "時序", "kill chain"]
last_updated: 2026-07-09
---

# 請產出攻擊時間軸。

## 1. 使用者可能問法
「幫我整理時間軸」「這起事件的來龍去脈」「按時間列出來」

## 2. 使用者意圖
timeline：產出可讀的攻擊時序敘事。

## 3. 需要查詢的資料來源
指定範圍的 Wazuh 告警。流程依 [[doc-data-and-event-flow]]。

## 4. 需要使用的 Wazuh 欄位
`timestamp`、`rule.mitre.tactic`、`agent.name`、`eventID`、`targetUserName`。

## 5. 需要關聯的實體
Incident（聚合的告警集）。

## 6. 回答邏輯
取範圍告警 → 依 timestamp 排序 → 標戰術階段 → 標關聯鏈（[[doc-correlation-rules]]）→ 輸出「時間｜主機｜動作｜階段」。

## 7. AI 回答範例
「T+00 外部 <IP> 對 <主機> 大量 RDP 失敗（Credential Access）→ T+05 一次成功（Valid Accounts）→ T+08 建立帳號（Persistence）→ T+09 加入 Administrators（Priv-Esc）。」（值為佔位。）

## 8. 若資料不足時的回答方式
無即時源 → 說明需連 Wazuh；範圍內事件稀疏則明說並只列現有。

## 9. 儀表板建議呈現方式
[[dsh-attack-timeline]]。

## 10. 注意事項
時區依 `timestamp`；時間軸呈現關聯，「同一性」仍以實體欄位驗證，不硬把不相關事件串一起。
