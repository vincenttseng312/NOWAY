---
id: qa-explain-alert
title: "這筆 Wazuh Alert 是什麼意思？"
doc_type: qa
category: qa
intent: alert-explain
summary: "解讀單一告警：用 rule.description + data.win.* 說明實際發生什麼、涉及哪些實體、對應技術與風險，並附下鑽。"
required_fields: ["rule.id", "rule.description", "rule.level", "rule.mitre.id", "data.win.system.eventID", "data.win.eventdata.targetUserName", "data.win.eventdata.ipAddress", "full_log"]
related_entities: [ent-alert, ent-technique]
dashboard_widgets: [dsh-event-detail-view]
tags: [cat:qa, type:qa]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "MITRE ATT&CK 官方網站"]
keywords: ["解讀告警", "explain alert", "這筆 alert", "告警意義"]
last_updated: 2026-07-09
---

# 這筆 Wazuh Alert 是什麼意思？

## 1. 使用者可能問法
「這個告警在說什麼？」「幫我看這筆 alert」「這代表被攻擊了嗎？」

## 2. 使用者意圖
alert-explain：理解單一告警的含義與嚴重性。

## 3. 需要查詢的資料來源
該筆告警 JSON（結構見 [[doc-wazuh-alert-structure]]）。

## 4. 需要使用的 Wazuh 欄位
`rule.description`（種子）、`eventID`、`data.win.eventdata.*`（驗證實際發生什麼）、`rule.level`、`rule.mitre.*`、`full_log`（兜底）。

## 5. 需要關聯的實體
Alert、Technique、涉及的 Host/Account/IP。

## 6. 回答邏輯
以 `rule.description` 為起點，用 `eventID`+`eventdata` 交叉確認實際行為 → 對映實體 → 說明風險與技術 → 附下鑽。**不照抄 description，要驗證。**

## 7. AI 回答範例
「這筆告警（Event <id>）代表 <主機> 上 <帳號> 的一次登入失敗，來源 <IP>。對應 <技術>。單筆風險 <級>，需看是否成串（暴力破解）。詳見事件詳細頁。」（值為佔位；`rule.id` env-specific。）

## 8. 若資料不足時的回答方式
`rule.id` 意義依規則集 → 標「需依實際環境確認」；欄位缺失則說明無法完整解讀。

## 9. 儀表板建議呈現方式
[[dsh-event-detail-view]]。

## 10. 注意事項
`rule.description` 是規則作者的話，須與實際欄位交叉確認；`rule.id` 不臆造。
