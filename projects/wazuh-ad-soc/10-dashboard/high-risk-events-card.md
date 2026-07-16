---
id: dsh-high-risk-events-card
title: "高風險事件卡片"
doc_type: dashboard
category: dashboard
summary: "首頁最醒目的即時卡片，列出目前 high/critical 事件（依 rule.level 與 AI 風險分級）。每筆含時間、主機、簡述與風險，可一鍵下鑽。"
tags: [cat:dashboard, type:dashboard, risk:high]
data_fields: ["rule.level", "rule.description", "timestamp", "agent.name"]
ai_inputs: ["risk_level", "event_summary"]
viz_type: "card"
filters: ["時間範圍", "嚴重性>=high"]
related_docs: [dsh-severity-distribution, dsh-event-detail-view, doc-severity-classification]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
keywords: ["高風險卡片", "high risk", "critical", "即時告警卡"]
last_updated: 2026-07-09
---

# 高風險事件卡片

## 1. 元件目的
即時凸顯需優先處置的高風險事件。

## 2. 使用情境
值班首要關注；triage-priority 類問答的視覺對應。

## 3. 需要的資料欄位
風險等級、時間、主機、事件簡述、對應技術。

## 4. 對應 Wazuh 欄位
`rule.level`、`rule.description`、`timestamp`、`agent.name`、（選）`rule.mitre.id`。

## 5. 對應 AI 分析輸出
`risk_level`（最終分級，見 [[doc-severity-classification]]）、`event_summary`（一句話摘要）。

## 6. 視覺化建議
紅/橙色卡片、依風險排序、critical 置頂並醒目。

## 7. 使用者可互動功能
點卡片→ [[dsh-event-detail-view]]；標記已讀/處理中。

## 8. 篩選條件
時間範圍、嚴重性 >= high。

## 9. 排序方式
風險等級 > 時間（新→舊）。

## 10. 範例資料格式
```json
{"time":"<ts>","host":"<agent.name>","risk":"critical","summary":"<AI 摘要>","technique":"T1110","alert_ref":"<id>"}
```
（值為佔位，實際來自 Wazuh 資料源。）

## 11. 注意事項
「high/critical」門檻為 env-specific（見 [[doc-severity-classification]]）；卡片是入口非結論，需下鑽佐證。

## 相關文件
[[dsh-severity-distribution]]、[[dsh-event-detail-view]]、[[doc-severity-classification]]
