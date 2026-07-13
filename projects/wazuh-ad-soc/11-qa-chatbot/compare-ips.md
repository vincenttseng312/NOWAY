---
id: qa-compare-ips
title: "請幫我比較兩個來源 IP 的風險。"
doc_type: qa
category: qa
intent: entity-ranking
summary: "並排比較兩個來源 IP 的告警量、風險加權、涉及主機/帳號、行為型態與網段，給出相對風險判斷。IP 信譽需外部查證。"
required_fields: ["data.win.eventdata.ipAddress", "rule.level", "rule.mitre.id", "agent.name", "data.win.eventdata.targetUserName"]
related_entities: [ent-ip]
dashboard_widgets: [dsh-top-source-ips]
tags: [cat:qa, type:qa, entity:ip]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
keywords: ["比較 IP", "compare ips", "來源風險比較"]
last_updated: 2026-07-09
---

# 請幫我比較兩個來源 IP 的風險。

## 1. 使用者可能問法
「這兩個 IP 誰比較危險？」「A 和 B 哪個要先處理？」

## 2. 使用者意圖
entity-ranking：兩實體風險並排比較。

## 3. 需要查詢的資料來源
兩 IP 各自的告警集。

## 4. 需要使用的 Wazuh 欄位
`ipAddress`、`rule.level`、`rule.mitre.id`、`agent.name`、`targetUserName`。

## 5. 需要關聯的實體
IP ×2（含 zone）。

## 6. 回答邏輯
對兩 IP 各算：告警量、風險加權、涉及主機/帳號數、行為型態（掃描/暴力/C2）、網段 → 並排 → 給相對判斷與理由。

## 7. AI 回答範例
「<IP-A>（外部，<Na> 筆，含暴力破解成功鏈）風險高於 <IP-B>（外部，<Nb> 筆，僅掃描）。建議先處理 A。兩者 IP 信譽均需外部查證。」（值為佔位。）

## 8. 若資料不足時的回答方式
某 IP 無足夠事件 → 說明「資料不足以評估」，不硬比。

## 9. 儀表板建議呈現方式
[[dsh-top-source-ips]]（並排/篩選兩 IP）。

## 10. 注意事項
以行為型態與風險而非單純告警量比較；IP 信譽需外部情資，不臆造。
