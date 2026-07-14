---
id: rpt-manager-summary
title: "高風險事件主管摘要"
doc_type: report
category: report
summary: "給主管/決策者的非技術摘要：影響、風險、已採取與建議的行動，少術語、聚焦業務衝擊與需要的決策。對應 audience-adapt(manager) 問答。"
audience: manager
required_inputs: ["rule.level", "agent.name"]
optional_inputs: ["rule.mitre.technique", "受影響範圍"]
related_docs: [qa-explain-for-manager, dsh-ai-summary-block, rpt-analyst-report]
tags: [cat:report, type:report]
confidence: medium
verification_status: needs-verification
source_refs: []
keywords: ["主管摘要", "manager summary", "非技術報告", "決策"]
last_updated: 2026-07-09
---

# 高風險事件主管摘要

## 1. 報告目的
讓主管在不需技術背景下理解事件影響並做決策。

## 2. 適用情境
high/critical 事件需向上匯報時。對應問答 [[qa-explain-for-manager]]。

## 3. 必要輸入欄位
`rule.level`（→風險）、`agent.name`（→哪個系統）。

## 4. 可選輸入欄位
`rule.mitre.technique`（→白話手法）、受影響範圍。

## 5. 報告產出格式
```markdown
### 事件主管摘要
- 發生了什麼：<白話一句>
- 影響範圍：<哪些系統/資料>
- 風險程度：<高/極高> — <為什麼要在意>
- 已採取行動：<...>
- 需要的決策/資源：<...>
- 目前狀態：<控制中/已解決/調查中>
```

## 6. 嚴重性判斷方式
用「高/極高」等白話而非數字等級；聚焦業務衝擊。

## 7. MITRE ATT&CK 對應方式
不列 T-id；用白話描述手法（如「猜測密碼登入」）。

## 8. 建議處置格式
用「已做/建議做」兩欄,聚焦需主管核准的資源/決策。

## 9. 範例輸入
事件分析結果（佔位）。

## 10. 範例輸出
```markdown
### 事件主管摘要
- 發生了什麼：一台內部電腦遭外部猜測密碼並疑似登入成功。
- 影響範圍：該台電腦及其帳號，尚未擴散（調查中）。
- 風險程度：極高 — 攻擊者可能已能存取該機資料。
- 已採取行動：已隔離該機、重設相關密碼。
- 需要的決策/資源：核准後續深入調查。
- 目前狀態：控制中。
```
（值為佔位；風險陳述誠實、不確定處明說。）

## 相關文件
[[qa-explain-for-manager]]、[[dsh-ai-summary-block]]、[[rpt-analyst-report]]
