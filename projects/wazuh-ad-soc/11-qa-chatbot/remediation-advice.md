---
id: qa-remediation-advice
title: "請給我處置建議。"
doc_type: qa
category: qa
intent: remediation
summary: "依事件類型給出處置步驟（隔離、封鎖、重設憑證、移除持久化、擴大調查），取自對應情境頁處置段與 SOP。屬防禦性一般指引。"
required_fields: ["rule.mitre.id", "data.win.system.eventID", "agent.name"]
related_entities: [ent-incident]
dashboard_widgets: [dsh-ai-remediation-block]
tags: [cat:qa, type:qa, cat:sop]
confidence: medium
verification_status: needs-verification
source_refs: ["MITRE ATT&CK 官方網站"]
keywords: ["處置建議", "remediation", "回應建議", "containment"]
last_updated: 2026-07-09
---

# 請給我處置建議。

## 1. 使用者可能問法
「該怎麼處理？」「下一步怎麼做？」「怎麼止血？」

## 2. 使用者意圖
remediation：取得可執行的處置步驟。

## 3. 需要查詢的資料來源
事件類型 → 對應情境頁「處置」段 + [[doc-ir-sop]]（⏳批 6）。

## 4. 需要使用的 Wazuh 欄位
`rule.mitre.id`/`eventID`（判事件類型）、`agent.name`（受影響主機）。

## 5. 需要關聯的實體
Incident（決定要對哪些 Host/Account/IP 處置）。

## 6. 回答邏輯
判事件類型 → 取對應情境頁處置步驟 → 依風險排急迫性 → 輸出勾選式步驟並附來源。

## 7. AI 回答範例
「針對此 RDP 暴力破解成功事件，建議：① 隔離 <主機>；② 重設 <帳號> 憑證；③ 移除任何新建帳號/持久化；④ 封鎖 <IP>；⑤ 擴大調查。（來源：[[scn-failed-then-success-logon]]、SOP）」（值為佔位。）

## 8. 若資料不足時的回答方式
事件類型不明 → 先給通用 triage 步驟並說明需更多脈絡。

## 9. 儀表板建議呈現方式
[[dsh-ai-remediation-block]]。

## 10. 注意事項
屬一般性防禦指引；實際執行依組織政策與授權（env-specific）。**不含攻擊性操作**。
