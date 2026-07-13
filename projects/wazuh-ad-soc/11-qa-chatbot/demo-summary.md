---
id: qa-demo-summary
title: "請幫我整理 Demo 結果。"
doc_type: qa
category: qa
intent: report-gen
summary: "把一次 Demo 攻擊模擬的偵測成果整理成展示摘要：攻擊鏈時間軸、各階段偵測到的告警、MITRE 對應、AI 摘要與處置，對應 Demo 報告與展示儀表板。"
required_fields: ["timestamp", "rule.mitre.id", "agent.name", "data.win.system.eventID"]
related_entities: [ent-incident]
dashboard_widgets: [dsh-demo-dashboard]
tags: [cat:qa, type:qa, cat:demo, cat:report]
confidence: medium
verification_status: needs-verification
source_refs: ["MITRE ATT&CK 官方網站"]
keywords: ["Demo 整理", "demo summary", "展示結果", "成果摘要"]
last_updated: 2026-07-09
---

# 請幫我整理 Demo 結果。

## 1. 使用者可能問法
「Demo 做完幫我總結」「展示結果整理一下」「Demo 抓到什麼」

## 2. 使用者意圖
report-gen（Demo 導向）：把模擬成果整理成可展示摘要。對應 [[doc-demo-script]]（⏳批 6）。

## 3. 需要查詢的資料來源
Demo 時間窗的告警集。

## 4. 需要使用的 Wazuh 欄位
`timestamp`、`rule.mitre.id`、`agent.name`、`eventID`。

## 5. 需要關聯的實體
Incident（Demo 攻擊鏈）。

## 6. 回答邏輯
取 Demo 時間窗 → 串攻擊鏈時間軸 → 標各階段偵測到的告警與 MITRE → 附 AI 摘要與處置 → 輸出展示用摘要。

## 7. AI 回答範例
「本次 Demo 模擬 RDP 暴力破解鏈：偵測到 4625×N（T1110）→ 4624 成功（T1078）→ 4720/4732 提權（T1136/T1098）。系統即時分級 critical 並產出處置建議。展示了偵測→分析→處置的完整閉環。」（值為佔位，數據取自實際 Demo。）

## 8. 若資料不足時的回答方式
Demo 未涵蓋某階段 → 據實只列偵測到的，不補未發生的階段。

## 9. 儀表板建議呈現方式
[[dsh-demo-dashboard]]。

## 10. 注意事項
Demo 摘要用實際模擬產生的告警；不誇大偵測涵蓋、不虛構未觸發的告警。
