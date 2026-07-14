---
id: rpt-ad-account-anomaly
title: "AD 帳號異常事件報告"
doc_type: report
category: report
summary: "情境專用報告：彙整帳號異常（異常登入、建立、群組異動、鎖定）的偏離維度、涉及帳號/來源、對應技術與處置。"
audience: analyst
required_inputs: ["data.win.eventdata.targetUserName", "data.win.system.eventID", "timestamp"]
optional_inputs: ["data.win.eventdata.ipAddress", "data.win.eventdata.subjectUserName", "data.win.eventdata.logonType"]
related_docs: [scn-ad-abnormal-logon, evt-account-anomaly-detection, evt-admin-group-change]
tags: [cat:report, type:report, mitre-technique:t1078]
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: ["AD 帳號異常報告", "account anomaly report", "T1078", "T1098"]
last_updated: 2026-07-09
---

# AD 帳號異常事件報告

## 1. 報告目的
標準化產出帳號異常事件報告（登入/建立/群組/鎖定）。

## 2. 適用情境
命中 [[scn-ad-abnormal-logon]] 或帳號生命週期異動。判斷法見 [[evt-account-anomaly-detection]]。

## 3. 必要輸入欄位
`targetUserName`、`eventID`、`timestamp`。

## 4. 可選輸入欄位
`ipAddress`、`subjectUserName`（操作者）、`logonType`。

## 5. 報告產出格式
```markdown
### AD 帳號異常事件報告
- 帳號：<account>（是否特權：<y/n>）
- 異常類型：<異常登入/建立/群組異動/鎖定>
- 偏離維度：<時間/來源/頻率/序列/權限>
- 涉及來源/操作者：<ip / subject>
- 對應技術：<T1078 / T1098 / T1136>
- 風險：<severity>
- 處置：<步驟>
```

## 6. 嚴重性判斷方式
特權帳號/多維偏離/伴隨提權 → 升級（見 [[doc-severity-classification]]）。

## 7. MITRE ATT&CK 對應方式
異常登入 T1078；群組異動 T1098；建立帳號 T1136（以官方為準）。

## 8. 建議處置格式
凍結帳號、重設憑證、（若群組異動）移出群組、檢查該帳號活動，連 [[doc-ir-sop]]。

## 9. 範例輸入
帳號相關事件集（佔位）。

## 10. 範例輸出
```markdown
### AD 帳號異常事件報告
- 帳號：<account>（特權：是）
- 異常類型：異常登入 + 群組異動
- 偏離維度：來源(外部) + 權限(獲特權群組)
- 涉及來源/操作者：<ip> / <subject>
- 對應技術：T1078 + T1098
- 風險：high
- 處置：凍結帳號、重設憑證、移出特權群組、調查後續。
```
（值為佔位。）

## 相關文件
[[scn-ad-abnormal-logon]]、[[evt-account-anomaly-detection]]、[[evt-admin-group-change]]
