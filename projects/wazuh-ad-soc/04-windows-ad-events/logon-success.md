---
id: evt-logon-success
title: "登入成功事件"
doc_type: event
category: windows-ad-event
summary: "Event 4624 記錄登入成功，搭配 Logon Type、來源 IP、帳號可判斷登入場景。單一 4624 多為正常，價值在於與失敗事件、時間、來源的關聯。"
tags: [cat:event, type:event, source:windows-security, mitre-technique:t1078]
event_source: security
windows_event_ids: ["4624", "4672", "4648"]
wazuh_sources: []
related_entities: [ent-account, ent-ip, ent-host-win11-target]
related_docs: [evt-logon-failure, evt-rdp-logon, scn-failed-then-success-logon, evt-account-anomaly-detection]
risk_level: low
confidence: high
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件"]
keywords: ["登入成功", "4624", "Logon Type", "successful logon", "valid accounts", "T1078"]
last_updated: 2026-07-09
---

# 登入成功事件

## 1. 事件用途
記錄一次成功的登入。核心 Event ID **4624**（以 Microsoft 官方為準）。常伴隨 4672（若登入者具特殊權限）、4648（使用明確憑證）。

## 2. 可能代表的安全意義
- 多數為正常。
- **異常訊號**：非上班時間登入、罕見來源 IP、特權帳號登入一般端點、緊接大量失敗後的成功（見 [[scn-failed-then-success-logon]]）。
- 對映 MITRE **T1078 Valid Accounts**（濫用有效帳號）。

## 3. 可能涉及的 Windows Event ID
| Event ID | 意義 | 驗證 |
|---|---|---|
| 4624 | 登入成功 | 以 Microsoft 官方為準 |
| 4672 | 指派特殊權限給新登入 | 以 Microsoft 官方為準 |
| 4648 | 使用明確憑證登入 | 以 Microsoft 官方為準 |

Logon Type 判讀見 [[evt-windows-security-overview]]（2 本機、3 網路、10 RDP…）。

## 4. 在 Wazuh Alert 中可能出現的欄位
`eventID=4624`、`data.win.eventdata.targetUserName`、`data.win.eventdata.ipAddress`、`data.win.eventdata.logonType`、`data.win.eventdata.workstationName`。

## 5. AI 分析時應注意的欄位
targetUserName（誰）、ipAddress（哪來，`-`/`::1` 代表本機）、logonType（怎麼登）、timestamp（何時）；並回看同帳號/同來源的失敗事件。

## 6. 儀表板可以如何視覺化
登入成功趨勢、Top 登入帳號、依 Logon Type 分布、成功前失敗次數（關聯指標）。

## 7. 使用者可能會問的問題
「這個帳號今天從哪些 IP 登入成功？」「有沒有可疑的成功登入？」

## 8. AI 回答範例
「<帳號> 於 <時間> 從 <IP>（LogonType 10, RDP）登入成功。該來源在此前 <N> 分鐘內有 <M> 次失敗（4625），符合暴力破解後成功型樣，建議調查。」（值為佔位。）

## 9. 誤判情境
服務/排程帳號規律登入、VPN/跳板固定來源、多人共用工作站。

## 10. 處置建議
確認是否為本人/授權；可疑則重設憑證、檢查該登入後的行為（程序建立 4688、持久化）。

## 相關文件
[[evt-logon-failure]]、[[evt-rdp-logon]]、[[scn-failed-then-success-logon]]、[[evt-account-anomaly-detection]]

## 建議查證來源
Microsoft Windows Security Auditing 文件。

## 可被檢索的關鍵字（中英）
登入成功、4624、Logon Type、successful logon、valid accounts、T1078。
