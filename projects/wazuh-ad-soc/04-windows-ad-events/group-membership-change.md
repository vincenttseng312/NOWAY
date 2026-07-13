---
id: evt-group-membership-change
title: "使用者加入群組事件"
doc_type: event
category: windows-ad-event
summary: "Event 4728/4732/4756 記錄帳號被加入安全群組（全域/本機/通用）。加入一般群組多為正常；加入特權群組（尤其 Administrators）是高風險，見管理者群組異動頁。"
tags: [cat:event, type:event, source:windows-security, mitre-technique:t1098]
event_source: security
windows_event_ids: ["4728", "4732", "4756"]
wazuh_sources: []
related_entities: [ent-account]
related_docs: [evt-admin-group-change, evt-user-creation, scn-add-to-administrators]
risk_level: medium
confidence: high
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件"]
keywords: ["加入群組", "4732", "4728", "4756", "群組異動", "account manipulation", "T1098"]
last_updated: 2026-07-09
---

# 使用者加入群組事件

## 1. 事件用途
記錄帳號被加入安全群組。核心 Event ID（以 Microsoft 官方為準）：
- **4732** 加入安全性本機群組
- **4728** 加入安全性全域群組
- **4756** 加入安全性通用群組

## 2. 可能代表的安全意義
- 加入一般群組多為正常權限管理。
- 對映 MITRE **T1098 Account Manipulation**：加入特權群組以提權/維持存取。
- **最高風險**是加入 Administrators/Domain Admins——獨立成頁 [[evt-admin-group-change]]。

## 3. 可能涉及的 Windows Event ID
| Event ID | 群組範圍 | 驗證 |
|---|---|---|
| 4732 | 本機安全群組 | 以 Microsoft 官方為準 |
| 4728 | 全域安全群組 | 以 Microsoft 官方為準 |
| 4756 | 通用安全群組 | 以 Microsoft 官方為準 |

## 4. 在 Wazuh Alert 中可能出現的欄位
`eventID`、`data.win.eventdata.targetUserName`（被加入者，或群組相關欄位）、`data.win.eventdata.subjectUserName`（操作者）；群組名稱欄位（若擷取）。

## 5. AI 分析時應注意的欄位
目標群組是否為特權群組、被加入帳號是否為剛建立的新帳號、操作者是否合理。

## 6. 儀表板可以如何視覺化
群組異動時間線、特權群組加入告警卡。

## 7. 使用者可能會問的問題
「有誰被加進特權群組？」「這次群組異動正常嗎？」

## 8. AI 回答範例
「<帳號> 於 <時間> 被 <subject> 加入 <群組>（Event 4732）。若 <群組> 屬特權群組且帳號為近期新建，風險升高。」（值為佔位。）

## 9. 誤判情境
IT 正常授權、角色調整、群組巢狀管理、自動化 RBAC 工具。

## 10. 處置建議
確認授權；未授權則移出群組、追操作者、檢查該帳號後續行為。

## 相關文件
[[evt-admin-group-change]]、[[evt-user-creation]]、[[scn-add-to-administrators]]；跨連父層 [[persistence-mechanisms]]。

## 建議查證來源
Microsoft Windows Security Auditing 文件。

## 可被檢索的關鍵字（中英）
加入群組、4732、4728、4756、群組異動、account manipulation、T1098。
