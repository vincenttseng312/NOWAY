---
id: qa-top-attacked-host
title: "哪一台主機被攻擊最多次？"
doc_type: qa
category: qa
intent: entity-ranking
summary: "以 agent.name 聚合告警數（建議風險加權）排出被攻擊最多的主機，並附主機角色脈絡。"
required_fields: ["agent.name", "agent.ip", "rule.level"]
related_entities: [ent-host-win11-target, ent-host-dc]
dashboard_widgets: [dsh-top-targeted-hosts]
tags: [cat:qa, type:qa, entity:host]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
keywords: ["被攻擊最多主機", "top attacked host", "主機排行"]
last_updated: 2026-07-09
---

# 哪一台主機被攻擊最多次？

## 1. 使用者可能問法
「哪台機器被打最兇？」「哪台主機告警最多？」

## 2. 使用者意圖
entity-ranking：以主機為維度排序威脅熱度。

## 3. 需要查詢的資料來源
時間窗內 Wazuh 告警，依主機聚合。

## 4. 需要使用的 Wazuh 欄位
`agent.name`、`agent.ip`、`rule.level`（加權）。

## 5. 需要關聯的實體
Host（含角色，見 [[doc-host-roles]]）。

## 6. 回答邏輯
依主機聚合告警數 → 建議以風險加權（避免雜訊）→ 排序 → 附主機角色（DC 風險權重高於一般端點）。

## 7. AI 回答範例
「時間窗內告警最多為 <主機>（<N> 筆，含 <M> 筆 high）。該主機為 <角色>。建議優先調查。」（值為佔位。）

## 8. 若資料不足時的回答方式
無即時源 → 說明需連 Wazuh；本專題主機少時，提醒「排行的相對意義大於絕對數」。

## 9. 儀表板建議呈現方式
[[dsh-top-targeted-hosts]]。

## 10. 注意事項
只看數量易誤導，建議風險加權；關鍵資產（DC）應加權。
