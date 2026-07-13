---
id: dsh-logon-failure-trend
title: "登入失敗趨勢圖"
doc_type: dashboard
category: dashboard
summary: "以時間為軸呈現登入失敗（4625）數量趨勢，凸顯暴力破解/噴灑的爆量時段，並可疊加成功登入以標記「失敗後成功」風險點。"
tags: [cat:dashboard, type:dashboard, mitre-technique:t1110]
data_fields: ["timestamp", "data.win.system.eventID", "data.win.eventdata.ipAddress"]
ai_inputs: []
viz_type: "trend"
filters: ["時間範圍", "帳號", "來源 IP"]
related_docs: [evt-logon-failure, scn-mass-logon-failure, scn-failed-then-success-logon]
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件"]
keywords: ["登入失敗趨勢", "logon failure trend", "4625", "暴力破解趨勢"]
last_updated: 2026-07-09
---

# 登入失敗趨勢圖

## 1. 元件目的
呈現失敗登入隨時間的量變，凸顯攻擊爆量時段。

## 2. 使用情境
「有沒有暴力破解跡象」的趨勢視覺；值班監看突增。

## 3. 需要的資料欄位
時間、4625 計數、來源/帳號（下鑽用）。

## 4. 對應 Wazuh 欄位
`timestamp`、`data.win.system.eventID`（4625）、`ipAddress`。

## 5. 對應 AI 分析輸出
（可選）AI 標記「失敗後成功」風險點（見 [[scn-failed-then-success-logon]]）。

## 6. 視覺化建議
折線/面積趨勢；疊加成功登入（4624）以標記交會的高風險點。

## 7. 使用者可互動功能
刷選時間窗、點峰值→下鑽該時段告警/來源。

## 8. 篩選條件
時間範圍、帳號、來源 IP。

## 9. 排序方式
時間序。

## 10. 範例資料格式
```json
[{"bucket":"<ts>","failures":<n>,"successes":<n>}]
```
（值為佔位。）

## 11. 注意事項
突增未必惡意（如服務錯誤重試）；需結合來源與帳號分布判讀，見 [[scn-mass-logon-failure]]。

## 相關文件
[[evt-logon-failure]]、[[scn-mass-logon-failure]]、[[scn-failed-then-success-logon]]
