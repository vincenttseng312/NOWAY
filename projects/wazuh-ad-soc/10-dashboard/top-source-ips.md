---
id: dsh-top-source-ips
title: "Top 攻擊來源 IP"
doc_type: dashboard
category: dashboard
summary: "以來源 IP 聚合告警數的排行，凸顯最活躍/可疑的來源，並標記內外網段。對應 entity-ranking 類問答。"
tags: [cat:dashboard, type:dashboard, entity:ip]
data_fields: ["data.win.eventdata.ipAddress", "rule.level", "agent.name"]
ai_inputs: ["risk_level"]
viz_type: "bar"
filters: ["時間範圍", "網段(內/外)", "嚴重性"]
related_docs: [dsh-top-targeted-hosts, dsh-top-affected-accounts, doc-network-topology]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
keywords: ["Top 來源 IP", "top source ip", "可疑來源", "排行"]
last_updated: 2026-07-09
---

# Top 攻擊來源 IP

## 1. 元件目的
排出告警最多/最可疑的來源 IP。

## 2. 使用情境
「哪個來源 IP 最可疑」「比較兩個 IP 的風險」。

## 3. 需要的資料欄位
來源 IP、告警數、風險加權、涉及主機。

## 4. 對應 Wazuh 欄位
`data.win.eventdata.ipAddress`（聚合計數）、`rule.level`（加權）、`agent.name`。

## 5. 對應 AI 分析輸出
`risk_level`（可用於加權而非只看數量）；IP 信譽需外部查證（AI 不臆造）。

## 6. 視覺化建議
橫向長條排行；內/外網段以顏色區分（見 [[doc-network-topology]]）。

## 7. 使用者可互動功能
點 IP→過濾其相關告警/時間軸；標記封鎖。

## 8. 篩選條件
時間範圍、網段、嚴重性。

## 9. 排序方式
告警數或風險加權（可切換）。

## 10. 範例資料格式
```json
[{"ip":"<ip>","zone":"external","count":<n>,"max_risk":"high"}]
```
（值為佔位；`-`/`::1` 代表本機，見 [[doc-wazuh-field-to-ai-mapping]]。）

## 11. 注意事項
只看數量易被雜訊誤導，建議風險加權；IP 信譽需外部來源，不在 KB 臆造。

## 相關文件
[[dsh-top-targeted-hosts]]、[[dsh-top-affected-accounts]]、[[doc-network-topology]]
