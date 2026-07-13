---
id: qa-recent-attacks
title: "最近一小時有哪些攻擊？"
doc_type: qa
category: qa
intent: timeline
summary: "回報指定時間窗（預設近一小時）內的攻擊活動，依時間排序並標戰術階段。"
required_fields: ["timestamp", "rule.mitre.tactic", "agent.name", "rule.level", "data.win.eventdata.ipAddress"]
related_entities: [ent-alert]
dashboard_widgets: [dsh-attack-timeline]
tags: [cat:qa, type:qa]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "MITRE ATT&CK 官方網站"]
keywords: ["最近攻擊", "近一小時", "recent attacks", "timeline"]
last_updated: 2026-07-09
---

# 最近一小時有哪些攻擊？

## 1. 使用者可能問法
「這一小時發生什麼？」「剛剛有攻擊嗎？」「最近的告警？」

## 2. 使用者意圖
timeline：掌握近期時間窗內的攻擊活動與序列。

## 3. 需要查詢的資料來源
指定時間窗的 Wazuh 告警（即時源）。

## 4. 需要使用的 Wazuh 欄位
`timestamp`、`rule.mitre.tactic`、`agent.name`、`rule.level`、`ipAddress`。

## 5. 需要關聯的實體
Alert（含涉及的 Host/IP/Account）。

## 6. 回答邏輯
取時間窗告警 → 依 timestamp 排序 → 依戰術標階段 → 摘要「何時、哪台、什麼類型」，凸顯關聯鏈。

## 7. AI 回答範例
「近一小時 <N> 起：<時間> 外部 <IP> 對 <主機> 大量 RDP 失敗（Credential Access）；<時間> 出現一次成功登入。疑似暴力破解進行中。」（值為佔位。）

## 8. 若資料不足時的回答方式
無即時源 → 說明需連 Wazuh；時間窗內無事件則明說「近一小時未見告警」。

## 9. 儀表板建議呈現方式
[[dsh-attack-timeline]]（刷選近一小時）。

## 10. 注意事項
時區依 `timestamp`（env-specific）；時間窗可由使用者調整。
