---
id: scn-add-to-administrators
title: "使用者加入 Administrators 群組偵測"
doc_type: attack-scenario
category: attack-scenario
summary: "偵測帳號被加入本機 Administrators 或網域特權群組（4732/4728），是提權與持久化的關鍵。與新帳號建立、可疑登入串成攻擊鏈時幾乎可定性為惡意。"
tags: [cat:attack-scenario, mitre-tactic:privilege-escalation, source:windows-security, risk:high]
related_entities: [ent-account]
related_docs: [evt-admin-group-change, scn-local-user-creation, scn-privilege-escalation-signs, doc-correlation-rules]
mitre_attack: [t1098]
wazuh_sources: []
windows_event_ids: ["4732", "4728"]
risk_level: high
confidence: high
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: ["加入 Administrators", "特權群組", "提權", "account manipulation", "T1098"]
last_updated: 2026-07-09
---

# 使用者加入 Administrators 群組偵測

## 1. 情境說明
偵測帳號被加入高權限群組。事件面見 [[evt-admin-group-change]]；本頁聚焦攻擊鏈與判定。

## 2. 攻擊者可能目標
把控制的帳號提升為管理員，取得對主機/網域的完整控制並維持存取。

## 3. 防禦方可觀測跡象
特權群組成員新增，尤其目標帳號為近期新建或非管理人員；操作者可能為被盜的特權帳號。

## 4. 可能出現的 Windows / AD 事件
4732（本機 Administrators）、4728（網域如 Domain Admins）。見 [[evt-admin-group-change]]。

## 5. 可能出現的 Wazuh 告警欄位
群組名稱、`targetUserName`（被加入者）、`subjectUserName`（操作者）、`rule.level`（通常高）；`rule.id` env-specific。

## 6. MITRE ATT&CK 對應
T1098 Account Manipulation（提權情境）。以官方為準。

## 7. 風險等級判斷
high；與 [[scn-local-user-creation]] 形成「建帳號→加管理員→登入」鏈時為 critical。

## 8. AI 分析重點
目標群組是否特權（依環境群組設計）、被加入帳號來歷、操作者合理性、時間鏈完整性。

## 9. 儀表板呈現方式
特權群組異動即時告警卡（最高優先）、攻擊鏈時間線。

## 10. 使用者可能詢問的問題
「有沒有人被加進 Administrators？」「這是提權嗎？」

## 11. AI 回答範例
「<帳號> 於 <時間> 被 <subject> 加入本機 Administrators（4732）。該帳號 <X 分鐘>前才由 4720 建立，構成典型持久化+提權鏈，建議列高優先、隔離主機。」（值為佔位。）

## 12. 建議處置方式
移出群組、停用相關帳號、隔離主機、回溯操作者與登入來源；走 [[doc-ir-sop]]（⏳批 6）。

## 13. 誤判可能性
IT 授權的管理員指派、PAM 工具、伺服器交接。

## 14. 需要進一步確認的資料
哪些群組屬特權、變更是否授權、操作者帳號是否被盜。

## 相關文件
[[evt-admin-group-change]]、[[scn-local-user-creation]]、[[scn-privilege-escalation-signs]]、[[doc-correlation-rules]]

## 建議查證來源
Microsoft Windows Security Auditing 文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
加入 Administrators、特權群組、提權、account manipulation、T1098。
