---
id: dsh-soc-home
title: "SOC 首頁設計"
doc_type: dashboard
category: dashboard
summary: "SOC 儀表板的著陸頁：頂部高風險卡片與嚴重性分布，中段攻擊時間軸與 Top 排行，側欄 AI 摘要。目標是 10 秒內掌握現況並可下鑽。"
tags: [cat:dashboard, type:dashboard]
data_fields: ["rule.level", "timestamp", "agent.name", "data.win.eventdata.ipAddress"]
ai_inputs: ["risk_level", "event_summary"]
viz_type: "layout"
filters: ["時間範圍", "嚴重性"]
related_docs: [dsh-overview, dsh-high-risk-events-card, dsh-attack-timeline, dsh-ai-summary-block]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
keywords: ["SOC 首頁", "soc home", "landing", "著陸頁", "layout"]
last_updated: 2026-07-09
---

# SOC 首頁設計

## 1. 元件目的
一頁掌握現況並快速下鑽的著陸頁。

## 2. 使用情境
分析人員上線第一眼；值班監看。

## 3. 建議版面
```
[高風險事件卡片]        [嚴重性分布]
[========== 攻擊時間軸 ==========]
[Top 來源IP] [Top 主機] [Top 帳號]
[側欄：AI 事件摘要 / 問答入口]
```

## 4. 需要的資料欄位 / 對應 Wazuh 欄位
`rule.level`、`timestamp`、`agent.name`、`ipAddress`（見 [[doc-wazuh-field-to-ai-mapping]]）。

## 5. 對應 AI 分析輸出
`risk_level`、`event_summary`（見 [[doc-ai-analysis-pipeline]]）。

## 6. 視覺化建議
上方卡片=即時警戒；中段時間軸=脈絡；下方排行=聚焦目標。

## 7. 使用者可互動功能
點卡片/排行下鑽至 [[doc-event-detail-view]]；時間軸刷選時間範圍。

## 8. 篩選條件
時間範圍、嚴重性。

## 9. 排序方式
卡片依風險/時間；排行依計數。

## 10. 範例資料格式
（見各子元件；此為版面頁，不含單一資料。）

## 11. 注意事項
版面依實際前端（Wazuh Dashboard 自訂 / 外部前端）調整，需確認。

## 相關文件
[[dsh-overview]]、[[dsh-high-risk-events-card]]、[[dsh-attack-timeline]]、[[dsh-ai-summary-block]]
