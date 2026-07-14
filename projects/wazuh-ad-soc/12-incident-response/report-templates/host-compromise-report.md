---
id: rpt-host-compromise
title: "主機遭攻擊事件報告"
doc_type: report
category: report
summary: "以主機為單位的完整事件報告：該主機在事件期間的所有告警、攻擊鏈、受影響帳號、網路行為、持久化與處置，供主機層級的整體交代。"
audience: analyst
required_inputs: ["agent.name", "timestamp", "rule.level", "data.win.system.eventID", "rule.mitre.id"]
optional_inputs: ["data.win.eventdata.targetUserName", "data.win.eventdata.ipAddress"]
related_docs: [rpt-multi-alert-aggregate, rpt-attack-timeline, doc-host-roles]
tags: [cat:report, type:report]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "MITRE ATT&CK 官方網站"]
keywords: ["主機遭攻擊報告", "host compromise report", "主機事件"]
last_updated: 2026-07-09
---

# 主機遭攻擊事件報告

## 1. 報告目的
以主機為主體，整體交代一台主機在事件中的遭遇與處置。

## 2. 適用情境
單一主機（如靶機或 DC）成為攻擊焦點時。主機角色見 [[doc-host-roles]]。

## 3. 必要輸入欄位
`agent.name`、`timestamp`、`rule.level`、`eventID`、`rule.mitre.id`。

## 4. 可選輸入欄位
`targetUserName`、`ipAddress`。

## 5. 報告產出格式
```markdown
### 主機遭攻擊事件報告：<host>
- 主機/角色：<host> / <role>
- 事件期間：<起>–<迄>
- 攻擊鏈摘要：<時間軸重點>
- 受影響帳號：<...>
- 網路行為：<可疑外連/來源，若有>
- 持久化/提權：<新建帳號/群組/自啟，若有>
- 對應技術：<T-id 清單>
- 整體風險：<severity>
- 處置與復原：<步驟>
- 主機完整性：<可信/需重灌>
```

## 6. 嚴重性判斷方式
以主機整體遭遇分級；關鍵資產（DC）或確認淪陷 → 升級。

## 7. MITRE ATT&CK 對應方式
彙整該主機所有告警的技術，標出攻擊經過的戰術鏈。

## 8. 建議處置格式
依 [[doc-ir-sop]] 六階段；含主機完整性判斷（是否需重灌/還原快照）。

## 9. 範例輸入
該主機事件期間的告警集（佔位）。

## 10. 範例輸出
```markdown
### 主機遭攻擊事件報告：<host>
- 主機/角色：<host> / 靶機
- 事件期間：<ts>–<ts>
- 攻擊鏈摘要：RDP 暴力→成功→建帳號→提權
- 受影響帳號：<account>
- 網路行為：對 <ip> 週期連線（疑 C2）
- 持久化/提權：新建 <account> 並加入 Administrators
- 技術：T1110/T1078/T1136/T1098/T1071
- 整體風險：critical
- 處置與復原：隔離、重設憑證、移除持久化、重灌
- 主機完整性：需重灌
```
（值為佔位。）

## 相關文件
[[rpt-multi-alert-aggregate]]、[[rpt-attack-timeline]]、[[doc-host-roles]]、[[doc-ir-sop]]
