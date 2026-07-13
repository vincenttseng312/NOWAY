---
id: dsh-top-affected-accounts
title: "Top 受影響帳號"
doc_type: dashboard
category: dashboard
summary: "以帳號（targetUserName）聚合告警數的排行，凸顯被鎖定、被嘗試或異常登入最多的帳號。對應帳號異常與 entity-ranking 問答。"
tags: [cat:dashboard, type:dashboard, entity:account]
data_fields: ["data.win.eventdata.targetUserName", "rule.level"]
ai_inputs: ["risk_level"]
viz_type: "bar"
filters: ["時間範圍", "嚴重性", "特權帳號"]
related_docs: [evt-account-anomaly-detection, dsh-top-source-ips]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
keywords: ["Top 受影響帳號", "top affected accounts", "帳號排行"]
last_updated: 2026-07-09
---

# Top 受影響帳號

## 1. 元件目的
排出涉及告警最多的帳號（被嘗試/鎖定/異常）。

## 2. 使用情境
「哪個帳號出現異常」「哪些帳號要優先調查」。

## 3. 需要的資料欄位
帳號名、告警數、風險、是否特權。

## 4. 對應 Wazuh 欄位
`data.win.eventdata.targetUserName`、`rule.level`。

## 5. 對應 AI 分析輸出
`risk_level`；帳號異常判斷見 [[evt-account-anomaly-detection]]。

## 6. 視覺化建議
長條排行；特權帳號醒目標記；機器帳號（`$` 結尾）可過濾。

## 7. 使用者可互動功能
點帳號→該帳號行為時間線；標記調查。

## 8. 篩選條件
時間範圍、嚴重性、特權帳號。

## 9. 排序方式
告警數或風險加權。

## 10. 範例資料格式
```json
[{"account":"<targetUserName>","count":<n>,"privileged":false}]
```
（值為佔位；機器帳號結尾為 `$`，見 [[doc-wazuh-field-to-ai-mapping]]。）

## 11. 注意事項
機器/服務帳號常大量出現但非惡意，需過濾；特權帳號應加權。

## 相關文件
[[evt-account-anomaly-detection]]、[[dsh-top-source-ips]]
