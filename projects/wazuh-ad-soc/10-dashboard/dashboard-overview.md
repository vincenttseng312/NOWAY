---
id: dsh-overview
title: "儀表板總覽"
doc_type: dashboard
category: dashboard
summary: "本專題自訂 SOC 儀表板的總覽：把 Wazuh 告警與 AI 分析結果組成 SOC 首頁、排行、趨勢、MITRE、單一事件與 AI 區塊。本頁列出所有元件與其資料來源分工。"
tags: [cat:dashboard, type:dashboard]
data_fields: []
ai_inputs: []
viz_type: ""
filters: ["時間範圍", "嚴重性", "主機", "來源 IP"]
related_docs: [doc-dashboard-role, dsh-soc-home, doc-ai-analysis-pipeline]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
keywords: ["儀表板總覽", "dashboard overview", "SOC", "元件清單"]
last_updated: 2026-07-09
---

# 儀表板總覽

## 1. 元件目的
提供自訂 SOC 儀表板的地圖：有哪些元件、各自吃什麼資料。與 Wazuh 內建 Dashboard 的分工見 [[doc-wazuh-dashboard]]。

## 2. 使用情境
分析人員/主管一眼掌握現況；作為其他儀表板頁的索引。

## 3. 元件清單
- 入口：[[dsh-soc-home]]
- 卡片：[[dsh-high-risk-events-card]]、[[dsh-severity-distribution]]
- 排行：[[dsh-top-source-ips]]、[[dsh-top-targeted-hosts]]、[[dsh-top-affected-accounts]]
- 時序：[[dsh-attack-timeline]]、[[dsh-logon-failure-trend]]
- 專項監控：[[dsh-rdp-attack-monitor]]、[[dsh-powershell-activity]]、[[dsh-ad-account-change-monitor]]
- 分析：[[dsh-mitre-distribution]]、[[dsh-event-detail-view]]
- AI 區塊：[[dsh-ai-summary-block]]、[[dsh-ai-remediation-block]]、[[dsh-qa-interface]]
- 展示：[[dsh-demo-dashboard]]

## 4. 資料來源分工
Wazuh 欄位（即時數值，見 [[doc-wazuh-field-to-ai-mapping]]）+ AI 分析輸出（摘要/風險/MITRE，見 [[doc-ai-analysis-pipeline]]）。

## 5. 全域篩選
時間範圍、嚴重性、主機、來源 IP（實作依所選前端，需確認）。

## 6. 注意事項
所有數值來自實際 Wazuh 資料源；本 KB 只定義「元件要什麼、怎麼呈現」，不含真實數據。

## 相關文件
[[doc-dashboard-role]]、[[dsh-soc-home]]、[[doc-ai-analysis-pipeline]]
