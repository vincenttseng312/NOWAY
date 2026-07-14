---
id: rpt-rdp-bruteforce
title: "RDP 暴力破解事件報告"
doc_type: report
category: report
summary: "情境專用報告模板：彙整 RDP 暴力破解事件的失敗統計、來源、是否成功、對應技術與處置，供快速產出該類事件的標準報告。"
audience: analyst
required_inputs: ["data.win.system.eventID", "data.win.eventdata.ipAddress", "data.win.eventdata.targetUserName", "data.win.eventdata.logonType", "timestamp"]
optional_inputs: ["rule.level"]
related_docs: [scn-rdp-bruteforce, scn-failed-then-success-logon, rpt-multi-alert-aggregate]
tags: [cat:report, type:report, mitre-technique:t1110]
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: ["RDP 暴力破解報告", "rdp bruteforce report", "T1110"]
last_updated: 2026-07-09
---

# RDP 暴力破解事件報告

## 1. 報告目的
標準化產出 RDP 暴力破解事件的報告。

## 2. 適用情境
命中 [[scn-rdp-bruteforce]] 或 [[scn-failed-then-success-logon]] 的事件。

## 3. 必要輸入欄位
`eventID`（4625/4624）、`ipAddress`、`targetUserName`、`logonType`、`timestamp`。

## 4. 可選輸入欄位
`rule.level`。

## 5. 報告產出格式
```markdown
### RDP 暴力破解事件報告
- 時間窗：<起>–<迄>
- 來源 IP：<ip>（網段：內/外）
- 目標帳號：<account(s)>
- 失敗次數：<N>（4625, LogonType 10）
- 是否成功：<是/否>（若是：成功時間 <ts>）
- 對應技術：T1110（+ T1078 若成功）
- 風險：<severity>
- 處置：<步驟>
```

## 6. 嚴重性判斷方式
持續失敗 high；出現對應成功 → critical（見 [[doc-severity-classification]]）。

## 7. MITRE ATT&CK 對應方式
T1110 Brute Force；成功則加 T1078 Valid Accounts。

## 8. 建議處置格式
封鎖來源、限制 RDP 暴露、（若成功）重設憑證+隔離主機，連 [[doc-ir-sop]]。

## 9. 範例輸入
RDP 相關 4625/4624 事件集（佔位）。

## 10. 範例輸出
```markdown
### RDP 暴力破解事件報告
- 時間窗：<ts>–<ts>
- 來源 IP：<ip>（外部）
- 目標帳號：<account>
- 失敗次數：<N>（LogonType 10）
- 是否成功：是（成功時間 <ts>）
- 對應技術：T1110 + T1078
- 風險：critical
- 處置：隔離主機、重設 <account> 憑證、封鎖 <ip>、擴大調查。
```
（值為佔位。）

## 相關文件
[[scn-rdp-bruteforce]]、[[scn-failed-then-success-logon]]、[[rpt-multi-alert-aggregate]]
