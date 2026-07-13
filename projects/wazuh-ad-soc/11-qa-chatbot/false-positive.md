---
id: qa-false-positive
title: "這個事件可能是誤判嗎？"
doc_type: qa
category: qa
intent: remediation
summary: "評估告警是否為誤判：對照該事件類型的常見良性情境（IT 維運、服務重試、授權變更），並指出需要哪些資訊才能確認。"
required_fields: ["data.win.system.eventID", "data.win.eventdata.subjectUserName", "data.win.eventdata.ipAddress", "agent.name"]
related_entities: [ent-alert]
dashboard_widgets: [dsh-event-detail-view]
tags: [cat:qa, type:qa]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
keywords: ["誤判", "false positive", "是不是誤報", "良性情境"]
last_updated: 2026-07-09
---

# 這個事件可能是誤判嗎？

## 1. 使用者可能問法
「這會不會是誤報？」「這是正常的嗎？」「需要緊張嗎？」

## 2. 使用者意圖
remediation：判斷是否可降級/忽略。

## 3. 需要查詢的資料來源
該告警 + 對應情境/事件頁的「誤判可能性」段。

## 4. 需要使用的 Wazuh 欄位
`eventID`、`subjectUserName`（操作者）、`ipAddress`、`agent.name`。

## 5. 需要關聯的實體
Alert（及其脈絡）。

## 6. 回答邏輯
取事件類型 → 對照常見良性情境（IT 維運/服務重試/授權變更/慣用來源）→ 給「傾向誤判/傾向真實」的判斷 + 需補的資訊。

## 7. AI 回答範例
「此帳號建立（4720）由 IT 管理帳號於上班時間操作、來源為內部管理主機，較可能為授權作業（傾向誤判）。若能確認變更工單即可降級。反之若操作者/來源異常則需調查。」（值為佔位。）

## 8. 若資料不足時的回答方式
明說「需要 X 才能確認」（如變更紀錄、操作者身分），不武斷定論。

## 9. 儀表板建議呈現方式
[[dsh-event-detail-view]]（看操作者/來源脈絡）。

## 10. 注意事項
誤判判斷需情境（授權資訊為 env-specific）；寧可標「需確認」也不誤導使用者忽略真實威脅。
