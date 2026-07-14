---
id: rpt-demo-report
title: "Demo 展示用報告"
doc_type: report
category: report
summary: "為專題 Demo 設計的成果報告：把一次攻擊模擬的偵測→分析→處置閉環整理成可展示的敘事，凸顯系統價值（Wazuh 偵測 + AI 分析）。"
audience: manager
required_inputs: ["timestamp", "rule.mitre.id", "agent.name", "data.win.system.eventID"]
optional_inputs: ["rule.level"]
related_docs: [doc-demo-script, dsh-demo-dashboard, qa-demo-summary]
tags: [cat:report, type:report, cat:demo]
confidence: medium
verification_status: needs-verification
source_refs: ["MITRE ATT&CK 官方網站"]
keywords: ["Demo 報告", "demo report", "成果展示", "專題"]
last_updated: 2026-07-09
---

# Demo 展示用報告

## 1. 報告目的
把 Demo 攻擊模擬的成果整理成可展示、易懂的報告，凸顯系統能力。

## 2. 適用情境
專題成果展示、口頭報告佐證。對應 [[doc-demo-script]] 與問答 [[qa-demo-summary]]。

## 3. 必要輸入欄位
`timestamp`、`rule.mitre.id`、`agent.name`、`eventID`（Demo 時間窗）。

## 4. 可選輸入欄位
`rule.level`。

## 5. 報告產出格式
```markdown
### Demo 成果報告
- Demo 情境：<模擬的攻擊，如 RDP 暴力破解鏈>
- 攻擊步驟 vs 偵測結果：<每步：攻擊動作 → 系統偵測到的告警/技術>
- AI 分析輸出：<摘要 / 風險分級 / MITRE 對應>
- AI 處置建議：<步驟>
- 展示重點：<系統展現的閉環價值：偵測→分析→處置>
- 限制與未來：<未涵蓋/可改進處>
```

## 6. 嚴重性判斷方式
展示 AI 如何即時分級（如 critical），並說明依據。

## 7. MITRE ATT&CK 對應方式
展示攻擊鏈的完整戰術覆蓋（如 T1110→T1078→T1098）。

## 8. 建議處置格式
展示 AI 產出的處置建議，強調從偵測到回應的自動化。

## 9. 範例輸入
Demo 執行的實際告警（佔位）。

## 10. 範例輸出
```markdown
### Demo 成果報告
- Demo 情境：RDP 暴力破解 → 成功 → 提權
- 攻擊步驟 vs 偵測：暴力破解→4625×N(T1110)；成功→4624(T1078)；提權→4732(T1098)
- AI 分析：摘要「外部破解成功並提權」/ 風險 critical / MITRE T1110,T1078,T1098
- AI 處置建議：隔離、重設憑證、移除持久化
- 展示重點：偵測→分析→處置的完整閉環
- 限制與未來：主機/攻擊樣本有限；可擴充更多情境
```
（值為佔位；用實際 Demo 產生的告警，不誇大偵測涵蓋。）

## 相關文件
[[doc-demo-script]]、[[dsh-demo-dashboard]]、[[qa-demo-summary]]
