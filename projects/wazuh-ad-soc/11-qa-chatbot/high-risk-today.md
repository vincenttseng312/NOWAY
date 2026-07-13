---
id: qa-high-risk-today
title: "今天有哪些高風險事件？"
doc_type: qa
category: qa
intent: triage-priority
summary: "回報當日 high/critical 事件清單，依風險與時間排序，每筆附主機、簡述與技術。"
required_fields: ["rule.level", "timestamp", "agent.name", "rule.description", "rule.mitre.id"]
related_entities: [ent-alert, ent-host-win11-target]
dashboard_widgets: [dsh-high-risk-events-card, dsh-severity-distribution]
tags: [cat:qa, type:qa, risk:high]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
keywords: ["高風險事件", "今天", "high risk today", "triage"]
last_updated: 2026-07-09
---

# 今天有哪些高風險事件？

## 1. 使用者可能問法
「今天有什麼要緊的？」「有沒有高風險告警？」「現在最嚴重的是什麼？」

## 2. 使用者意圖
triage-priority：掌握當日需優先處置的事件。

## 3. 需要查詢的資料來源
當日 Wazuh 告警（即時資料源）+ [[doc-severity-classification]] 判準。

## 4. 需要使用的 Wazuh 欄位
`rule.level`、`timestamp`、`agent.name`、`rule.description`、`rule.mitre.id`。

## 5. 需要關聯的實體
Alert、Host（受影響主機）。

## 6. 回答邏輯
篩當日 → 依 AI 風險分級（非只 rule.level）取 high/critical → 依風險/時間排序 → 每筆給主機/簡述/技術/時間。

## 7. AI 回答範例
「今日共 <N> 筆高風險：① <時間> <主機> 疑似 RDP 暴力破解成功（critical, T1110→T1078）；② …。建議優先處理 critical 項。」（值為佔位。）

## 8. 若資料不足時的回答方式
無即時告警連線 → 說明「需連 Wazuh 資料源」，只回「如何判定高風險」的一般說明；當日無高風險則明說「今日未見 high/critical」。

## 9. 儀表板建議呈現方式
[[dsh-high-risk-events-card]] + [[dsh-severity-distribution]]。

## 10. 注意事項
「高風險」門檻 env-specific；卡片是入口，結論需下鑽 [[dsh-event-detail-view]] 佐證。
