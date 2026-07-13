---
id: evt-admin-group-change
title: "管理者群組異動事件"
doc_type: event
category: windows-ad-event
summary: "帳號被加入 Administrators / Domain Admins 等高權限群組是提權與持久化的關鍵訊號，透過 4732（本機）/4728（全域）等事件觀察。特權群組異動應視為高風險並優先調查。"
tags: [cat:event, type:event, source:windows-security, mitre-technique:t1098, risk:high]
event_source: security
windows_event_ids: ["4732", "4728", "4756"]
wazuh_sources: []
related_entities: [ent-account]
related_docs: [evt-group-membership-change, evt-user-creation, scn-add-to-administrators, scn-privilege-escalation-signs]
risk_level: high
confidence: high
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件"]
keywords: ["管理者群組", "Administrators", "Domain Admins", "提權", "特權群組", "privilege escalation", "T1098"]
last_updated: 2026-07-09
---

# 管理者群組異動事件

## 1. 事件用途
專門追蹤帳號被加入**高權限群組**（本機 Administrators、網域 Domain Admins/Enterprise Admins 等）。事件機制與 [[evt-group-membership-change]] 相同（4732/4728/4756），但因群組敏感度而獨立為高風險類別。

## 2. 可能代表的安全意義
- 對映 MITRE **T1098 Account Manipulation** 與提權跡象（[[scn-privilege-escalation-signs]]）。
- **最典型的攻擊鏈**：建立新帳號（4720）→ 加入 Administrators（4732）→ 用該帳號登入操作。三者時間相近時，幾乎可判定為持久化/提權。

## 3. 可能涉及的 Windows Event ID
| Event ID | 意義 | 驗證 |
|---|---|---|
| 4732 | 加入本機安全群組（如 Administrators） | 以 Microsoft 官方為準 |
| 4728 | 加入全域安全群組（如 Domain Admins） | 以 Microsoft 官方為準 |
| 4756 | 加入通用安全群組 | 以 Microsoft 官方為準 |

> 「哪些群組算特權」需依實際環境的群組設計確認（不只名稱為 Administrators 的群組）。

## 4. 在 Wazuh Alert 中可能出現的欄位
`eventID`、目標群組名稱、被加入帳號（targetUserName）、操作者（subjectUserName）。

## 5. AI 分析時應注意的欄位
目標群組是否特權、被加入帳號的來歷（是否剛建立）、操作者是否為特權帳號本身（可能被盜用）、時間鏈。

## 6. 儀表板可以如何視覺化
特權群組異動即時告警卡（高優先）、「建帳號→加特權群組」關聯時間線。

## 7. 使用者可能會問的問題
「有沒有人被加進 Administrators？」「這是不是提權？」

## 8. AI 回答範例
「<帳號>（<X>分鐘前由 4720 建立）於 <時間> 被加入本機 Administrators（4732），操作者 <subject>。此為典型持久化+提權鏈，建議列為高優先事件並隔離主機調查。」（值為佔位。）

## 9. 誤判情境
IT 授權的管理員指派、伺服器交接、自動化特權管理（PAM）工具的合法變更。

## 10. 處置建議
立即確認授權；未授權則移出群組、停用相關帳號、隔離主機、回溯操作者與登入來源。連 [[doc-ir-sop]]（⏳批 6）。

## 相關文件
[[evt-group-membership-change]]、[[evt-user-creation]]、[[scn-add-to-administrators]]、[[scn-privilege-escalation-signs]]

## 建議查證來源
Microsoft Windows Security Auditing 文件。

## 可被檢索的關鍵字（中英）
管理者群組、Administrators、Domain Admins、提權、特權群組、privilege escalation、T1098。
