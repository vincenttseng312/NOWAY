---
id: rpt-single-alert-summary
title: "單一告警摘要報告"
doc_type: report
category: report
summary: "針對單一 Wazuh 告警的簡短摘要報告模板：一段話說清楚這筆告警代表什麼、涉及誰、風險與技術，供快速判讀與存檔。"
audience: analyst
required_inputs: ["timestamp", "rule.description", "rule.level", "data.win.system.eventID", "agent.name"]
optional_inputs: ["rule.mitre.id", "data.win.eventdata.targetUserName", "data.win.eventdata.ipAddress"]
related_docs: [qa-explain-alert, dsh-event-detail-view]
tags: [cat:report, type:report]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
keywords: ["單一告警摘要", "single alert report", "告警報告"]
last_updated: 2026-07-09
---

# 單一告警摘要報告

## 1. 報告目的
把一筆告警濃縮成可存檔、可傳遞的簡短摘要。

## 2. 適用情境
快速判讀、值班交班、附在事件記錄。對應問答 [[qa-explain-alert]]。

## 3. 必要輸入欄位
`timestamp`、`rule.description`、`rule.level`、`eventID`、`agent.name`。

## 4. 可選輸入欄位
`rule.mitre.id`、`targetUserName`、`ipAddress`。

## 5. 報告產出格式
```markdown
### 告警摘要
- 時間：<timestamp>
- 主機：<agent.name>
- 事件：<eventID> — <rule.description>
- 風險：<severity>（rule.level <n>）
- 對應技術：<T-id>（若有）
- 涉及：帳號 <targetUserName> / 來源 <ipAddress>
- 判讀：<一句話說明實際發生什麼與是否需關注>
```

## 6. 嚴重性判斷方式
依 [[doc-severity-classification]]（單筆以 rule.level 為基礎，關聯後可能升級）。

## 7. MITRE ATT&CK 對應方式
取 `rule.mitre.id` → technique 卡；無則標「需查官方確認」。

## 8. 建議處置格式
一行行動建議（詳細處置另用完整報告）。

## 9. 範例輸入
```json
{"timestamp":"<ts>","agent":{"name":"<host>"},"rule":{"description":"<desc>","level":<n>},"data":{"win":{"system":{"eventID":"4625"}}}}
```
（佔位。）

## 10. 範例輸出
```markdown
### 告警摘要
- 時間：<ts>
- 主機：<host>
- 事件：4625 — <desc>
- 風險：medium（rule.level <n>）
- 對應技術：T1110（若適用）
- 涉及：帳號 <user> / 來源 <ip>
- 判讀：一次 RDP 登入失敗；需觀察是否成串（暴力破解）。
```
（值為佔位；rule.id 等 env-specific 不虛構。）

## 相關文件
[[qa-explain-alert]]、[[dsh-event-detail-view]]、[[doc-severity-classification]]
