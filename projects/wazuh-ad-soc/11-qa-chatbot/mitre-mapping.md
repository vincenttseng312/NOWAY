---
id: qa-mitre-mapping
title: "這個事件對應哪個 MITRE ATT&CK 技術？"
doc_type: qa
category: qa
intent: alert-explain
summary: "從 rule.mitre.* 給出對應技術並連 technique 卡；若告警未帶 mitre 欄位，依行為建議候選但標「需查 MITRE 官方確認」。"
required_fields: ["rule.mitre.id", "rule.mitre.tactic", "rule.mitre.technique", "data.win.system.eventID"]
related_entities: [ent-technique]
dashboard_widgets: [dsh-mitre-distribution]
tags: [cat:qa, type:qa, cat:mitre]
confidence: medium
verification_status: needs-verification
source_refs: ["MITRE ATT&CK 官方網站"]
keywords: ["MITRE 對應", "mitre mapping", "ATT&CK 技術", "technique"]
last_updated: 2026-07-09
---

# 這個事件對應哪個 MITRE ATT&CK 技術？

## 1. 使用者可能問法
「這是什麼攻擊手法？」「對應哪個 ATT&CK？」「這是 T 幾？」

## 2. 使用者意圖
alert-explain：取得事件的 ATT&CK 對應。

## 3. 需要查詢的資料來源
告警的 `rule.mitre.*`；對應樞紐 [[doc-mitre-mapping-overview]]。

## 4. 需要使用的 Wazuh 欄位
`rule.mitre.id`、`rule.mitre.tactic`、`rule.mitre.technique`、`eventID`（輔助判斷）。

## 5. 需要關聯的實體
Technique（連 technique 卡）。

## 6. 回答邏輯
若有 `rule.mitre.id` → 直接對應並連 technique 卡；若無 → 依行為（eventID/情境）建議候選技術，**標「需查 MITRE 官方確認」，不硬給 id**。

## 7. AI 回答範例
「此告警帶 `rule.mitre.id=T1110`，對應 Brute Force（Credential Access）。詳見 technique 卡 [[t1110]]。」／「此告警未帶 mitre 欄位；依行為（大量 4625）可能對應 T1110，建議查 MITRE 官方確認。」（值為佔位。）

## 8. 若資料不足時的回答方式
無 mitre 欄位且行為不明確 → 說明「無法確定對應，需更多脈絡」，不臆造 id。

## 9. 儀表板建議呈現方式
[[dsh-mitre-distribution]] + technique 卡。

## 10. 注意事項
對應完整度依規則集（見 [[doc-wazuh-mitre-linkage]]）；技術 id 以 MITRE 官方為準。
