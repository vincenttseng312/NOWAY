---
id: dsh-top-targeted-hosts
title: "Top 被攻擊主機"
doc_type: dashboard
category: dashboard
summary: "以主機（agent.name）聚合告警數的排行，凸顯被攻擊最多的端點。本專題主機少，重點在靶機與 DC 的相對熱度與風險。"
tags: [cat:dashboard, type:dashboard, entity:host]
data_fields: ["agent.name", "agent.ip", "rule.level"]
ai_inputs: ["risk_level"]
viz_type: "bar"
filters: ["時間範圍", "嚴重性"]
related_docs: [dsh-top-source-ips, doc-host-roles]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
keywords: ["Top 被攻擊主機", "top targeted host", "主機排行"]
last_updated: 2026-07-09
---

# Top 被攻擊主機

## 1. 元件目的
排出告警最多的受監控主機。

## 2. 使用情境
「哪一台主機被攻擊最多次」「哪些主機需要優先調查」。

## 3. 需要的資料欄位
主機名/IP、告警數、風險加權。

## 4. 對應 Wazuh 欄位
`agent.name`、`agent.ip`、`rule.level`。

## 5. 對應 AI 分析輸出
`risk_level`；主機角色脈絡見 [[doc-host-roles]]（DC 被攻擊風險高於一般端點）。

## 6. 視覺化建議
長條排行；DC 等關鍵資產醒目標記。

## 7. 使用者可互動功能
點主機→過濾其告警/時間軸；下鑽該主機的 entity 卡。

## 8. 篩選條件
時間範圍、嚴重性。

## 9. 排序方式
告警數或風險加權。

## 10. 範例資料格式
```json
[{"host":"<agent.name>","ip":"<agent.ip>","count":<n>,"role":"target"}]
```
（值為佔位。）

## 11. 注意事項
本專題主機少，排行的相對意義大於絕對數；關鍵資產應加權而非只看量。

## 相關文件
[[dsh-top-source-ips]]、[[doc-host-roles]]
