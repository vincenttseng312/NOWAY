---
id: qa-bruteforce-signs
title: "是否有暴力破解跡象？"
doc_type: qa
category: qa
intent: account-anomaly
summary: "判斷是否有暴力破解/密碼噴灑：短時間大量 4625，並以「單帳號多密碼 vs 多帳號同密碼」區分型態，警戒是否有對應成功。"
required_fields: ["data.win.system.eventID", "data.win.eventdata.targetUserName", "data.win.eventdata.ipAddress", "timestamp"]
related_entities: [ent-ip, ent-account]
dashboard_widgets: [dsh-logon-failure-trend, dsh-rdp-attack-monitor]
tags: [cat:qa, type:qa, mitre-technique:t1110]
confidence: high
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: ["暴力破解", "brute force", "密碼噴灑", "T1110"]
last_updated: 2026-07-09
---

# 是否有暴力破解跡象？

## 1. 使用者可能問法
「有人在猜密碼嗎？」「是不是被暴力破解？」「有密碼噴灑嗎？」

## 2. 使用者意圖
account-anomaly：判定暴力/噴灑攻擊（T1110）。

## 3. 需要查詢的資料來源
Wazuh 登入失敗告警（4625）。相關情境見 [[scn-rdp-bruteforce]]、[[scn-mass-logon-failure]]。

## 4. 需要使用的 Wazuh 欄位
`eventID`（4625）、`targetUserName`、`ipAddress`、`timestamp`（+ 失敗原因碼若有）。

## 5. 需要關聯的實體
IP（來源）、Account（目標）。

## 6. 回答邏輯
統計時間窗內失敗量與集中度 → 型態判斷（單帳號多次=暴力 / 多帳號=噴灑）→ 檢查是否有對應成功（升級為 [[qa-failed-then-success]]）。

## 7. AI 回答範例
「是。<時間窗>內來自 <IP> 對 <帳號> 有 <N> 次 4625，型態符合暴力破解（T1110）。尚未見成功登入（需確認）。」（值為佔位。）

## 8. 若資料不足時的回答方式
無即時源 → 說明需連 Wazuh；失敗量在正常範圍則明說「未見明顯暴力跡象」。

## 9. 儀表板建議呈現方式
[[dsh-logon-failure-trend]]、[[dsh-rdp-attack-monitor]]。

## 10. 注意事項
使用者忘密碼、服務錯誤重試會誤報；需看來源集中度與節奏。失敗原因碼代碼需 Microsoft 官方確認。
