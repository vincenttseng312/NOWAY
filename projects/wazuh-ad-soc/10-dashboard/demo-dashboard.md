---
id: dsh-demo-dashboard
title: "Demo 展示儀表板"
doc_type: dashboard
category: dashboard
summary: "為專題 Demo 精選的展示版面：把一次完整攻擊模擬（如 RDP 暴力→成功→提權）的偵測、時間軸、AI 摘要與處置串成一頁故事，方便現場演示。"
tags: [cat:dashboard, type:dashboard, cat:demo]
data_fields: ["timestamp", "rule.level", "agent.name", "data.win.eventdata.ipAddress"]
ai_inputs: ["event_summary", "timeline", "risk_level", "remediation"]
viz_type: "layout"
filters: ["Demo 時間窗"]
related_docs: [doc-demo-script, dsh-attack-timeline, dsh-ai-summary-block]
confidence: medium
verification_status: needs-verification
source_refs: []
keywords: ["Demo 儀表板", "demo dashboard", "展示版面", "專題演示"]
last_updated: 2026-07-09
---

# Demo 展示儀表板

## 1. 元件目的
把一次完整攻擊模擬串成一頁可演示的故事線。

## 2. 使用情境
專題 Demo 現場、成果展示（見 [[doc-demo-script]]，⏳批 6）。

## 3. 建議版面（以 RDP 暴力破解鏈為例）
```
[攻擊時間軸：4625×N → 4624 → 4732]
[AI 事件摘要]        [風險徽章 critical]
[Top 來源IP: 攻擊機]  [受影響帳號/主機]
[AI 建議處置]        [MITRE: T1110→T1078→T1098]
```

## 4. 需要的資料欄位 / 對應 Wazuh 欄位
`timestamp`、`rule.level`、`agent.name`、`ipAddress`（聚焦 Demo 時間窗）。

## 5. 對應 AI 分析輸出
`event_summary`、`timeline`、`risk_level`、`remediation` 一次展示。

## 6. 視覺化建議
單頁故事線、由左至右/上至下呈現攻擊展開與 AI 回應。

## 7. 使用者可互動功能
播放 Demo 時間窗、逐步高亮攻擊階段。

## 8. 篩選條件
Demo 時間窗。

## 9. 排序方式
攻擊階段時序。

## 10. 範例資料格式
（複用各元件；聚焦單一 Demo 案例的時間窗。）

## 11. 注意事項
Demo 使用實驗室產生的真實告警；示範資料仍不臆造（用實際 Demo 執行的結果或明確標示的佔位）。

## 相關文件
[[doc-demo-script]]（⏳批 6）、[[dsh-attack-timeline]]、[[dsh-ai-summary-block]]
