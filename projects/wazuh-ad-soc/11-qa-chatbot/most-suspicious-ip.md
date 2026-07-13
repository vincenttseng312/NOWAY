---
id: qa-most-suspicious-ip
title: "哪個來源 IP 最可疑？"
doc_type: qa
category: qa
intent: entity-ranking
summary: "以來源 IP 聚合並風險加權，排出最可疑來源，標記內外網段；IP 信譽需外部查證，不臆造。"
required_fields: ["data.win.eventdata.ipAddress", "rule.level", "agent.name"]
related_entities: [ent-ip]
dashboard_widgets: [dsh-top-source-ips]
tags: [cat:qa, type:qa, entity:ip]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
keywords: ["最可疑 IP", "most suspicious ip", "來源 IP 排行"]
last_updated: 2026-07-09
---

# 哪個來源 IP 最可疑？

## 1. 使用者可能問法
「哪個 IP 最有問題？」「攻擊來源是誰？」

## 2. 使用者意圖
entity-ranking：找出最可疑的外部/內部來源。

## 3. 需要查詢的資料來源
時間窗內告警，依來源 IP 聚合。

## 4. 需要使用的 Wazuh 欄位
`data.win.eventdata.ipAddress`、`rule.level`、`agent.name`。

## 5. 需要關聯的實體
IP（zone：內/外/攻擊網段，見 [[doc-network-topology]]）。

## 6. 回答邏輯
依 IP 聚合 → 風險加權 + 網段（外部加權）→ 排序 → 附涉及主機/帳號與行為型態（如「大量 RDP 失敗」）。

## 7. AI 回答範例
「最可疑為外部 <IP>（<N> 筆告警，主要為 RDP 暴力）。位於攻擊網段。IP 信譽需外部查證。建議封鎖並調查。」（值為佔位。）

## 8. 若資料不足時的回答方式
無即時源 → 說明需連 Wazuh；`-`/`::1` 代表本機（見 [[doc-wazuh-field-to-ai-mapping]]），非外部威脅。

## 9. 儀表板建議呈現方式
[[dsh-top-source-ips]]。

## 10. 注意事項
IP 信譽**不在 KB 臆造**，需外部情資；只看量易被雜訊誤導，建議風險加權。
