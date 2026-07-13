---
id: qa-explain-for-analyst
title: "請用資安人員看得懂的方式分析。"
doc_type: qa
category: qa
intent: audience-adapt
summary: "技術版分析：含 Event ID、Wazuh 欄位、MITRE 技術 id、程序鏈與關聯邏輯、偵測與 IOC，供資安人員深入處理。"
required_fields: ["rule.id", "rule.mitre.id", "data.win.system.eventID", "data.win.eventdata.targetUserName", "data.win.eventdata.ipAddress", "full_log"]
related_entities: [ent-incident, ent-technique]
dashboard_widgets: [dsh-event-detail-view, dsh-ai-summary-block]
tags: [cat:qa, type:qa, cat:report]
confidence: medium
verification_status: needs-verification
source_refs: ["MITRE ATT&CK 官方網站", "Microsoft Windows Security Auditing 文件"]
keywords: ["資安人員分析", "analyst analysis", "技術版", "Event ID", "IOC"]
last_updated: 2026-07-09
---

# 請用資安人員看得懂的方式分析。

## 1. 使用者可能問法
「給技術細節」「完整分析」「SOC 分析師版」

## 2. 使用者意圖
audience-adapt（analyst）：含技術細節、可據以行動。

## 3. 需要查詢的資料來源
完整告警集 + full_log + 關聯分析。對應 analyst 版報告模板（⏳批 6）。

## 4. 需要使用的 Wazuh 欄位
`rule.id`（標 env-specific）、`rule.mitre.id`、`eventID`、`eventdata.*`、`full_log`。

## 5. 需要關聯的實體
Incident、Technique。

## 6. 回答邏輯
給「Event ID + 欄位證據 + 程序/登入鏈 + MITRE 技術 id + 關聯邏輯 + IOC + 偵測機會」，可追溯、可驗證。

## 7. AI 回答範例
「4625×N（LogonType 10, src <IP>）→ 4624（同源）→ 4720 → 4732(Administrators)。對應 T1110→T1078→T1136→T1098。IOC：src IP、新建帳號名。偵測：C1+C2 關聯規則。rule.id 依環境確認。」（值為佔位。）

## 8. 若資料不足時的回答方式
明列缺哪些欄位/事件、對結論的影響，不臆造補齊。

## 9. 儀表板建議呈現方式
[[dsh-event-detail-view]] + [[dsh-ai-summary-block]]（技術版）。

## 10. 注意事項
技術 id 以 MITRE 官方、Event ID 以 Microsoft 官方、rule.id 以實際環境為準。
