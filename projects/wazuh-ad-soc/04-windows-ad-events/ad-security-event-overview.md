---
id: evt-ad-security-overview
title: "Active Directory 安全事件總覽"
doc_type: event
category: windows-ad-event
summary: "AD 網域環境下，Domain Controller 記錄帳號管理、群組異動、Kerberos 認證等安全事件。本頁彙整這些事件家族與其在本專題（Windows 11 靶機已加入網域）中的意義。Kerberos/目錄變更 ID 需以 Microsoft 官方確認。"
tags: [cat:event, type:event, source:ad]
event_source: ad
windows_event_ids: ["4720", "4728/4732/4756", "4740", "4768/4769/4771 (需確認)", "5136 (需確認)"]
wazuh_sources: []
related_entities: [ent-host-dc, ent-account]
related_docs: [evt-windows-security-overview, evt-user-creation, evt-group-membership-change, scn-ad-abnormal-logon]
risk_level: ""
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件"]
keywords: ["Active Directory", "AD 安全事件", "Domain Controller", "Kerberos", "帳號管理", "群組異動", "ad security events"]
last_updated: 2026-07-09
---

# Active Directory 安全事件總覽

## 1. 事件用途
在 AD 網域中，Domain Controller 是帳號認證與目錄服務中心，記錄網域層級的帳號管理、群組異動與認證事件。本專題的 Windows 11 靶機已加入網域，故相關網域帳號活動會反映在 DC 日誌。

## 2. 可能代表的安全意義
攻擊者取得網域立足點後，常見動作會落在這些事件：建立帳號、加入特權群組、異常認證。

## 3. 常見 AD 事件家族

| 類別 | Event ID | 意義 | 驗證 |
|---|---|---|---|
| 帳號管理 | 4720/4722/4725/4726 | 建立/啟用/停用/刪除帳號 | 以 Microsoft 官方為準 |
| 群組異動 | 4728/4732/4756 | 加入安全群組 | 以 Microsoft 官方為準 |
| 帳號鎖定 | 4740 | 帳號鎖定（常記於 DC/PDC） | 以 Microsoft 官方為準 |
| Kerberos 認證 | 4768/4769/4771/4776 | TGT/服務票證/預驗證失敗/NTLM 驗證 | **需依 Microsoft 官方文件確認** |
| 目錄變更 | 5136 等 | 目錄物件被修改 | **需依 Microsoft 官方文件確認** |

## 4. 在 Wazuh Alert 中可能出現的欄位
`agent.name`（若 Agent 裝於 DC，需確認是否納入）、`data.win.system.eventID`、`data.win.eventdata.targetUserName`、`data.win.eventdata.subjectUserName`（操作者）。

> 本專題 DC 是否安裝 Wazuh Agent、採集哪些事件，屬部署相關（需依實際環境確認）。若 DC 未納管，部分 AD 事件可能收不到。

## 5. AI 分析時應注意的欄位
操作者（subject）vs 目標（target）帳號的區別；事件發生在 DC 還是成員主機；是否伴隨特權群組異動。

## 6. 儀表板可以如何視覺化
AD 帳號異動監控圖、特權群組變更時間線（見 10-dashboard，⏳批 5）。

## 7. 使用者可能會問的問題
「有沒有新帳號被建立？」「誰被加進 Administrators？」

## 8. AI 回答範例
「偵測到 <帳號> 於 <時間> 被建立（Event 4720，需依環境確認規則），操作者為 <subject>。建議確認是否為授權變更。」（值為佔位，不臆造。）

## 9. 誤判情境
IT 正常的帳號生命週期管理、批次佈建、目錄同步工具。

## 10. 處置建議
確認變更是否經授權；未授權則凍結帳號、回溯操作者來源，連 [[doc-ir-sop]]（⏳批 6）。

## 相關文件
[[evt-windows-security-overview]]、[[evt-user-creation]]、[[evt-group-membership-change]]、[[scn-ad-abnormal-logon]]；跨連父層 [[persistence-mechanisms]]。

## 建議查證來源
Microsoft Windows Security Auditing 文件。

## 可被檢索的關鍵字（中英）
Active Directory、AD 安全事件、Domain Controller、Kerberos、帳號管理、群組異動、ad security events。
