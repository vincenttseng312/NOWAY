---
id: qa-<slug>
title: ""
doc_type: qa
category: qa
intent:                     # 見 _meta/routing-rules（triage-priority / entity-ranking / timeline / alert-explain / account-anomaly / report-gen / remediation / audience-adapt）
summary: ""
required_fields: []         # 需查詢的 Wazuh 欄位
related_entities: []
related_docs: []
dashboard_widgets: []
risk_level: ""
tags: []                    # cat:qa, type:qa, ...
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: []
last_updated: YYYY-MM-DD
---

# <問題標題>

## 1. 使用者可能問法
（同義問法列舉，供 intent 分類與召回。）

## 2. 使用者意圖
（對應哪個 intent、真正想知道什麼。）

## 3. 需要查詢的資料來源
（Wazuh alert / Windows event / KB 頁 / entity 卡。）

## 4. 需要使用的 Wazuh 欄位
（如 `rule.level`、`agent.name`、`data.win.eventdata.ipAddress`。）

## 5. 需要關聯的實體
（Host / Account / IP / Technique / Incident，見 entity-model。）

## 6. 回答邏輯
（步驟：抽實體 → 查/聚合 → 判斷 → 組答。）

## 7. AI 回答範例
（示範回答；env-specific 值以佔位表示並標註。）

## 8. 若資料不足時的回答方式
（依 citation-hallucination-rules 第 5 節：明說缺什麼、不臆造。）

## 9. 儀表板建議呈現方式
（對應 10-dashboard 元件。）

## 10. 注意事項
（誤判、隱私、env-specific、需查證處。）
