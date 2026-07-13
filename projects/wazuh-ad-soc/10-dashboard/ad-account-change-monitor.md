---
id: dsh-ad-account-change-monitor
title: "AD 帳號異動監控圖"
doc_type: dashboard
category: dashboard
summary: "監控帳號生命週期與特權變更：建立(4720)、加入群組(4728/4732)、鎖定(4740)。特權群組異動醒目告警，並可串成「建帳號→加管理員」攻擊鏈。"
tags: [cat:dashboard, type:dashboard, entity:account, mitre-technique:t1098]
data_fields: ["data.win.system.eventID", "data.win.eventdata.targetUserName", "data.win.eventdata.subjectUserName", "timestamp"]
ai_inputs: ["risk_level"]
viz_type: "timeline"
filters: ["時間範圍", "事件類型", "特權群組"]
related_docs: [evt-user-creation, evt-admin-group-change, scn-add-to-administrators]
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件"]
keywords: ["AD 帳號異動", "account change monitor", "4720", "4732", "特權群組"]
last_updated: 2026-07-09
---

# AD 帳號異動監控圖

## 1. 元件目的
監控帳號建立/群組/鎖定等異動，凸顯持久化與提權跡象。

## 2. 使用情境
「有沒有新帳號被建立」「有誰被加進 Administrators」。

## 3. 需要的資料欄位
事件類型、目標帳號、操作者、時間。

## 4. 對應 Wazuh 欄位
`eventID`（4720/4728/4732/4740）、`targetUserName`、`subjectUserName`、`timestamp`。

## 5. 對應 AI 分析輸出
`risk_level`、攻擊鏈標記（見 [[scn-add-to-administrators]]）。

## 6. 視覺化建議
時間線 + 事件類型圖示；特權群組異動醒目；「建帳號→加管理員」以連線標記。

## 7. 使用者可互動功能
點事件→ [[doc-event-detail-view]]；依帳號過濾看其生命週期。

## 8. 篩選條件
時間範圍、事件類型、特權群組。

## 9. 排序方式
時間序。

## 10. 範例資料格式
```json
[{"time":"<ts>","event":"4720","target":"<user>","subject":"<admin>"},
 {"time":"<ts>","event":"4732","target":"<user>","group":"Administrators"}]
```
（值為佔位。）

## 11. 注意事項
IT 正常帳號管理會出現於此；重點在「未授權」與「特權/攻擊鏈」，需結合授權資訊。

## 相關文件
[[evt-user-creation]]、[[evt-admin-group-change]]、[[scn-add-to-administrators]]
