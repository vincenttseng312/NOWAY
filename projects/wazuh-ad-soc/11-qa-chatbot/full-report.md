---
id: qa-full-report
title: "請產出完整事件報告。"
doc_type: qa
category: qa
intent: report-gen
summary: "依 alert→報告流程產出完整事件報告：摘要、關鍵發現、樣本/環境、時間軸、Persistence、網路、MITRE、IOC、偵測機會、處置。套 12-report 模板。"
required_fields: ["timestamp", "rule.id", "rule.level", "rule.description", "rule.mitre.id", "agent.name", "data.win.system.eventID", "data.win.eventdata.targetUserName", "data.win.eventdata.ipAddress"]
related_entities: [ent-incident]
dashboard_widgets: [dsh-event-detail-view]
tags: [cat:qa, type:qa, cat:report]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "MITRE ATT&CK 官方網站"]
keywords: ["完整事件報告", "full report", "incident report"]
last_updated: 2026-07-09
---

# 請產出完整事件報告。

## 1. 使用者可能問法
「幫我寫完整報告」「產一份事件報告」「要交報告」

## 2. 使用者意圖
report-gen：取得結構化完整報告。流程見 [[doc-alert-to-report-pipeline]]，模板見 12-report（⏳批 6）。

## 3. 需要查詢的資料來源
該 Incident 的所有告警 + 關聯分析結果。

## 4. 需要使用的 Wazuh 欄位
完整欄位集（見 [[doc-wazuh-field-to-ai-mapping]]）。

## 5. 需要關聯的實體
Incident（聚合 Alert/Host/Account/IP/Technique）。

## 6. 回答邏輯
alert→報告 7 步（解析→實體→關聯→分級→MITRE→套模板）→ 依報告 15 節結構輸出 → 對象決定 manager/analyst 版。

## 7. AI 回答範例
「（依模板輸出）Executive Summary：… / Key Findings：… / Timeline：… / MITRE Mapping：T1110,T1078,T1098 / IOC：<來源 IP、帳號> / 處置建議：… 」（值為佔位，統計/IOC 僅反映實際告警。）

## 8. 若資料不足時的回答方式
缺欄位的章節標「資料不足，待補」；不虛構 IOC/統計/rule.id。

## 9. 儀表板建議呈現方式
從 [[dsh-event-detail-view]] 一鍵產報告。

## 10. 注意事項
報告中所有具體值（IP、帳號、rule.id、統計）只反映實際資料；env-specific 值標明。
