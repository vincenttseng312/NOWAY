---
id: qa-abnormal-account
title: "哪個帳號出現異常登入？"
doc_type: qa
category: qa
intent: account-anomaly
summary: "以帳號為主體，找出與基準偏離（罕見來源/時段、跨主機、特權異常）的登入，並說明偏離維度。"
required_fields: ["data.win.eventdata.targetUserName", "data.win.eventdata.ipAddress", "data.win.eventdata.logonType", "timestamp"]
related_entities: [ent-account, ent-ip]
dashboard_widgets: [dsh-top-affected-accounts]
tags: [cat:qa, type:qa, entity:account, mitre-technique:t1078]
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件"]
keywords: ["帳號異常登入", "abnormal account", "基準偏離", "T1078"]
last_updated: 2026-07-09
---

# 哪個帳號出現異常登入？

## 1. 使用者可能問法
「有帳號怪怪的嗎？」「誰的登入不正常？」

## 2. 使用者意圖
account-anomaly：找出行為偏離基準的帳號。

## 3. 需要查詢的資料來源
Wazuh 登入相關告警 + 帳號基準（需累積）。判斷法見 [[evt-account-anomaly-detection]]。

## 4. 需要使用的 Wazuh 欄位
`targetUserName`、`ipAddress`、`logonType`、`timestamp`。

## 5. 需要關聯的實體
Account、IP。

## 6. 回答邏輯
以帳號聚合其登入 → 對照基準（慣用來源/時段/主機）→ 標偏離維度（時間/來源/頻率/序列/權限/行為）→ 綜合判斷。

## 7. AI 回答範例
「<帳號> 於 <時間> 自罕見外部 <IP> 登入，且此前有失敗序列。多維偏離，疑似異常（T1078）。建議調查並考慮重設憑證。單一維度不足以定論。」（值為佔位。）

## 8. 若資料不足時的回答方式
無基準（冷啟動）→ 說明「基準不足、信心較低」；無即時源 → 說明需連 Wazuh。

## 9. 儀表板建議呈現方式
[[dsh-top-affected-accounts]] + 單一帳號行為時間線。

## 10. 注意事項
出差/在家/輪班會造成合理偏離；需結合情境，避免誤報。
