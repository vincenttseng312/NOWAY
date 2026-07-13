---
id: qa-explain-for-manager
title: "請用主管看得懂的方式說明。"
doc_type: qa
category: qa
intent: audience-adapt
summary: "把事件轉成非技術語言：影響、風險、已採取/建議的行動，少術語、聚焦業務衝擊與決策。"
required_fields: ["rule.level", "agent.name", "rule.mitre.technique"]
related_entities: [ent-incident]
dashboard_widgets: [dsh-ai-summary-block]
tags: [cat:qa, type:qa, cat:report]
confidence: medium
verification_status: needs-verification
source_refs: []
keywords: ["主管說明", "manager summary", "非技術", "業務衝擊"]
last_updated: 2026-07-09
---

# 請用主管看得懂的方式說明。

## 1. 使用者可能問法
「跟主管怎麼講？」「用白話說」「給老闆看的版本」

## 2. 使用者意圖
audience-adapt（manager）：非技術、聚焦影響與決策。

## 3. 需要查詢的資料來源
事件分析結果（同一資料，換表達）。對應 manager 版報告模板（⏳批 6）。

## 4. 需要使用的 Wazuh 欄位
間接：`rule.level`（→ 風險）、`agent.name`（→ 哪個系統）、`rule.mitre.technique`（→ 白話手法）。

## 5. 需要關聯的實體
Incident。

## 6. 回答邏輯
去術語 → 講「哪個系統受影響、可能的業務衝擊、風險高低、已做/建議做什麼」→ 一段話 + 明確建議。

## 7. AI 回答範例
「我們的一台內部電腦遭外部嘗試猜測密碼並疑似登入成功，風險高，可能影響該機資料。已隔離該機並重設相關帳號密碼，正擴大檢查。建議核准後續調查資源。」（值為佔位。）

## 8. 若資料不足時的回答方式
用「目前已知/尚待確認」分層陳述，不誇大也不隱瞞不確定。

## 9. 儀表板建議呈現方式
[[dsh-ai-summary-block]]（主管版）。

## 10. 注意事項
少術語但不失真；風險陳述要誠實，不確定處明說。
