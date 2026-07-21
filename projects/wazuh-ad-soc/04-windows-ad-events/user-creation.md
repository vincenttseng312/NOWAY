---
id: evt-user-creation
title: "新增使用者事件"
doc_type: event
category: windows-ad-event
summary: "Event 4720 記錄新使用者帳號建立（本機或網域）。攻擊者常以新建帳號建立持久化或後門存取；本機端 net user 類操作也會反映。需區分授權的 IT 佈建與可疑建立。"
tags: [cat:event, type:event, source:windows-security, mitre-technique:t1136]
event_source: security
windows_event_ids: ["4720", "4722", "4738"]
wazuh_sources: ["custom:110120", "custom:110121"]
related_entities: [ent-account]
related_docs: [scn-local-user-creation, evt-group-membership-change, evt-admin-group-change]
risk_level: high
confidence: high
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件"]
keywords: ["新增使用者", "4720", "建立帳號", "持久化", "create account", "T1136"]
last_updated: 2026-07-20
---

# 新增使用者事件

## 1. 事件用途
記錄新使用者帳號被建立。核心 Event ID **4720**（4722 啟用、4738 帳號變更；以 Microsoft 官方為準）。本機帳號與網域帳號皆適用（網域端記於 DC）。

## 2. 可能代表的安全意義
- 對映 MITRE **T1136 Create Account**：攻擊者建立帳號作為持久化/後門。
- **高風險組合**：新帳號建立後立即被加入 Administrators（[[evt-admin-group-change]]），或帳號名偽裝成系統帳號。

## 3. 可能涉及的 Windows Event ID
| Event ID | 意義 | 驗證 |
|---|---|---|
| 4720 | 建立使用者帳號 | 以 Microsoft 官方為準 |
| 4722 | 啟用帳號 | 以 Microsoft 官方為準 |
| 4738 | 帳號被變更 | 以 Microsoft 官方為準 |

## 4. 在 Wazuh Alert 中可能出現的欄位
`eventID=4720`、`data.win.eventdata.targetUserName`（新帳號）、`data.win.eventdata.subjectUserName`（建立者）。

## 5. AI 分析時應注意的欄位
新帳號名、建立者、建立主機、以及**接下來是否有群組加入/登入**（關聯到持久化）。

### 可部署規則（待實機驗證）

- `110120`：Sysmon ProcessCreate 偵測帳號建立命令，僅代表 attempt。
- `110121`：Security 4720，代表帳號建立成功。
- Artifact：`code/2026-07-20/wazuh-windows-threat-detection-rules/windows-threat-detection-rules.xml`。

兩條規則尚需在 Wazuh 4.14.6 執行 `wazuh-analysisd -t` 並核對實際 `data.win.*` 欄位，故本頁仍維持 `needs-verification`。

## 6. 儀表板可以如何視覺化
新增帳號時間線、建立者分布、「新帳號→加入特權群組」關聯卡。

## 7. 使用者可能會問的問題
「有沒有新帳號被建立？」「這個新帳號是誰建的？」

## 8. AI 回答範例
「<主機> 於 <時間> 建立帳號 <名稱>（4720），建立者 <subject>。<X 分鐘>後該帳號被加入 Administrators（4732），符合持久化型樣，建議立即調查。」（值為佔位。）

## 9. 誤判情境
IT 正常佈建、自動化部署、加網域時的服務帳號建立。

## 10. 處置建議
確認是否授權；未授權則停用/刪除帳號、追建立者來源、檢查是否已被使用。連 [[doc-ir-sop]]（⏳批 6）。

## 相關文件
[[scn-local-user-creation]]、[[evt-group-membership-change]]、[[evt-admin-group-change]]；跨連父層 [[persistence-mechanisms]]。

## 建議查證來源
Microsoft Windows Security Auditing 文件。

## 可被檢索的關鍵字（中英）
新增使用者、4720、建立帳號、持久化、create account、T1136。
