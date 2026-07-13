---
id: dsh-event-detail-view
title: "單一事件詳細頁"
doc_type: dashboard
category: dashboard
summary: "下鑽單一告警/事件的完整檢視：所有 Wazuh 欄位、full_log、關聯實體、MITRE 對應、AI 摘要與處置建議。是各排行/卡片/時間軸的下鑽終點與防幻覺對照點。"
tags: [cat:dashboard, type:dashboard]
data_fields: ["timestamp", "rule.id", "rule.level", "rule.description", "rule.mitre.id", "agent.name", "data.win.system.eventID", "data.win.eventdata.targetUserName", "data.win.eventdata.ipAddress", "full_log"]
ai_inputs: ["event_summary", "risk_level", "remediation"]
viz_type: "detail"
filters: []
related_docs: [doc-wazuh-alert-structure, doc-wazuh-field-to-ai-mapping, dsh-ai-summary-block, dsh-ai-remediation-block]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
keywords: ["單一事件詳細", "event detail", "下鑽", "full_log", "告警詳情"]
last_updated: 2026-07-09
---

# 單一事件詳細頁

## 1. 元件目的
呈現單一事件的全部證據，供深入判讀與驗證 AI 結論。

## 2. 使用情境
從卡片/排行/時間軸下鑽；「這筆 Alert 代表什麼」的完整解答。

## 3. 需要的資料欄位
該告警的全部欄位 + full_log + 關聯實體 + MITRE + AI 輸出。

## 4. 對應 Wazuh 欄位
完整 18 欄位（見 [[doc-wazuh-field-to-ai-mapping]]）＋ `full_log`（兜底原文）。

## 5. 對應 AI 分析輸出
`event_summary`（[[dsh-ai-summary-block]]）、`risk_level`、`remediation`（[[dsh-ai-remediation-block]]）。

## 6. 視覺化建議
分區：概要（風險/技術）→ 結構化欄位表 → 關聯實體/事件 → AI 摘要與處置 → full_log 原文。

## 7. 使用者可互動功能
展開 full_log、跳關聯實體卡、標記處理狀態、一鍵產報告。

## 8. 篩選條件
（單筆，不適用）

## 9. 排序方式
（單筆，不適用）

## 10. 範例資料格式
```json
{"time":"<ts>","rule":{"id":"<env-specific>","level":<n>,"description":"<desc>","mitre":{"id":"<Txxxx>"}},
 "agent":{"name":"<host>"},"data":{"win":{"system":{"eventID":"<id>"},"eventdata":{"targetUserName":"<user>","ipAddress":"<ip>"}}},
 "full_log":"<raw>","ai":{"summary":"<...>","risk":"high","remediation":"<...>"}}
```
（值為佔位；`rule.id` env-specific。）

## 11. 注意事項
**這是防幻覺的關鍵對照點**：AI 摘要/結論必須能在此頁的原始欄位/full_log 找到依據，否則應標不確定。

## 相關文件
[[doc-wazuh-alert-structure]]、[[doc-wazuh-field-to-ai-mapping]]、[[dsh-ai-summary-block]]、[[dsh-ai-remediation-block]]
