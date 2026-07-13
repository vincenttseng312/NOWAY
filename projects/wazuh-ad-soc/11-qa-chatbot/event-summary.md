---
id: qa-event-summary
title: "請產出事件摘要。"
doc_type: qa
category: qa
intent: report-gen
summary: "把一起事件濃縮成一段摘要：誰、何時、對哪台、做了什麼、風險、對應技術。可切換主管/技術版。對應單一告警摘要報告模板。"
required_fields: ["timestamp", "agent.name", "rule.description", "rule.level", "rule.mitre.id", "data.win.eventdata.targetUserName", "data.win.eventdata.ipAddress"]
related_entities: [ent-incident]
dashboard_widgets: [dsh-ai-summary-block]
tags: [cat:qa, type:qa, cat:report]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
keywords: ["事件摘要", "event summary", "摘要報告"]
last_updated: 2026-07-09
---

# 請產出事件摘要。

## 1. 使用者可能問法
「摘要一下這起事件」「簡單講發生什麼」「給我重點」

## 2. 使用者意圖
report-gen：取得事件的濃縮摘要。對應報告模板（⏳批 6）。

## 3. 需要查詢的資料來源
該事件的告警集。輸出承接 [[dsh-ai-summary-block]]。

## 4. 需要使用的 Wazuh 欄位
`timestamp`、`agent.name`、`rule.description`、`rule.level`、`rule.mitre.id`、`targetUserName`、`ipAddress`。

## 5. 需要關聯的實體
Incident（受影響 Host/Account/IP）。

## 6. 回答邏輯
聚合事件 → 抽「誰/何時/哪台/做什麼/風險/技術」→ 一段話輸出 → 依對象調整用語。

## 7. AI 回答範例
「<時間>，外部 <IP> 對 <主機> 的 <帳號> 進行 RDP 暴力破解並成功登入，隨後建立帳號並提權。風險 critical，對應 T1110/T1078/T1098。建議立即處置。」（值為佔位。）

## 8. 若資料不足時的回答方式
欄位缺失 → 摘要中標「未提供」；無即時源 → 說明需連 Wazuh。

## 9. 儀表板建議呈現方式
[[dsh-ai-summary-block]]。

## 10. 注意事項
摘要須可追溯到原始欄位（[[dsh-event-detail-view]]）；不臆造未發生的細節。
