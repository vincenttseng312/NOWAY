---
id: qa-failed-then-success
title: "是否有登入失敗後成功？"
doc_type: qa
category: qa
intent: account-anomaly
summary: "偵測「大量失敗後緊接成功」的高風險關聯（可能暴力破解成功），需確認失敗與成功共享帳號/來源且在合理時間窗內。"
required_fields: ["data.win.system.eventID", "data.win.eventdata.targetUserName", "data.win.eventdata.ipAddress", "timestamp"]
related_entities: [ent-account, ent-ip]
dashboard_widgets: [dsh-logon-failure-trend]
tags: [cat:qa, type:qa, risk:high, mitre-technique:t1110]
confidence: high
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: ["失敗後成功", "brute force success", "關聯", "T1110", "T1078"]
last_updated: 2026-07-09
---

# 是否有登入失敗後成功？

## 1. 使用者可能問法
「有沒有破解成功的？」「失敗一堆之後有登入成功嗎？」

## 2. 使用者意圖
account-anomaly：偵測暴力破解「猜中」的高風險關聯。相關情境 [[scn-failed-then-success-logon]]。

## 3. 需要查詢的資料來源
Wazuh 4625 與 4624 告警，做時間關聯。關聯邏輯見 [[doc-correlation-rules]]（C1）。

## 4. 需要使用的 Wazuh 欄位
`eventID`（4625/4624）、`targetUserName`、`ipAddress`、`timestamp`。

## 5. 需要關聯的實體
Account、IP（須為同一主體）。

## 6. 回答邏輯
找時間窗內 `4625×N → 4624` 且失敗與成功共享帳號或來源 → 確認同一性與時間合理 → 若成立則高風險，檢查成功後行為。

## 7. AI 回答範例
「是。<帳號> 於 <時間> 從 <IP> 成功（4624），此前 <X 分鐘>同來源 <N> 次失敗。高度疑似暴力破解成功（T1110→T1078）。建議立即重設憑證並查後續行為。」（值為佔位。）

## 8. 若資料不足時的回答方式
無即時源 → 說明需連 Wazuh；只有失敗無成功則回「僅見失敗、未見對應成功」。

## 9. 儀表板建議呈現方式
[[dsh-logon-failure-trend]]（疊加成功點）、失敗→成功關聯卡。

## 10. 注意事項
使用者多次打錯後打對也會觸發；以來源與節奏（自動化 vs 人為）區分，避免誤報。
