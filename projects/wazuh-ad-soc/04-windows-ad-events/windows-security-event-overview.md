---
id: evt-windows-security-overview
title: "Windows Security Event Log 總覽"
doc_type: event
category: windows-ad-event
summary: "Windows Security 日誌記錄登入、帳號管理、權限、程序建立、稽核變更等安全事件；本頁彙整常見 Event ID 家族與 Logon Type，並說明它們如何進入 Wazuh 供 AI 分析。特定 ID 語意以 Microsoft 官方為準。"
tags: [cat:event, type:event, source:windows-security]
event_source: security
windows_event_ids: ["4624", "4625", "4634/4647", "4648", "4672", "4688", "4720", "4740", "1102"]
wazuh_sources: []
related_entities: [ent-host-win11-target, ent-account, ent-event]
related_docs: [evt-ad-security-overview, evt-logon-success, evt-logon-failure, doc-windows-events-into-wazuh]
risk_level: ""
confidence: high
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "Wazuh 官方文件"]
keywords: ["Windows Security Log", "Event ID", "Logon Type", "稽核", "安全事件", "security event overview"]
last_updated: 2026-07-09
---

# Windows Security Event Log 總覽

## 1. 事件用途
記錄與安全相關的系統活動：登入/登出、帳號與群組管理、權限使用、程序建立、稽核政策變更等。是本專題大多數偵測的原始資料。

## 2. 可能代表的安全意義
單一事件多為正常；價值在於**關聯與異常**（見 [[evt-account-anomaly-detection]]）。例如 4625 大量 + 4624 一次，可能是暴力破解後成功。

## 3. 常見 Event ID 家族（穩定值，仍以 Microsoft 官方為準）

| 家族 | Event ID | 意義 |
|---|---|---|
| 登入/登出 | 4624 / 4625 / 4634 / 4647 | 登入成功 / 失敗 / 登出 / 使用者登出 |
| 憑證/權限 | 4648 / 4672 | 明確憑證登入 / 指派特殊權限 |
| 程序 | 4688 | 程序建立（命令列需開稽核） |
| 帳號管理 | 4720 / 4722 / 4725 / 4726 / 4738 | 建立 / 啟用 / 停用 / 刪除 / 變更帳號 |
| 群組 | 4728 / 4732 / 4756 | 加入全域 / 本機 / 通用安全群組 |
| 鎖定 | 4740 / 4767 | 帳號鎖定 / 解鎖 |
| 稽核 | 4719 / 1102 | 稽核政策變更 / 稽核日誌被清除 |

## 4. Logon Type（判讀登入場景，以 Microsoft 官方為準）

| Type | 意義 |
|---|---|
| 2 | Interactive（本機互動） |
| 3 | Network（網路，如檔案共享） |
| 4 / 5 | Batch / Service |
| 7 | Unlock（解鎖） |
| 10 | RemoteInteractive（RDP） |
| 11 | CachedInteractive |

## 5. 在 Wazuh Alert 中可能出現的欄位
`data.win.system.eventID`、`data.win.system.providerName`（Microsoft-Windows-Security-Auditing）、`data.win.eventdata.targetUserName`、`data.win.eventdata.ipAddress`、`data.win.eventdata.logonType`（若有）。見 [[doc-wazuh-field-to-ai-mapping]]。

## 6. AI 分析時應注意的欄位
eventID + logonType + targetUserName + ipAddress 的組合；以及事件是否成串出現（時間關聯）。

## 7. 儀表板可以如何視覺化
事件類型分布、登入成功/失敗趨勢、Top 帳號/來源 IP（見 10-dashboard，⏳批 5）。

## 8. 使用者可能會問的問題
「今天有哪些登入失敗？」「這個 Event ID 是什麼？」→ 路由見 `_meta/routing-rules.md`。

## 9. 誤判情境
排程任務（Type 4/5）、服務帳號、正常網路存取（Type 3）常大量出現但非惡意。

## 10. 處置建議
以「單一事件」不下結論；建立主機/帳號基準，對照異常。詳見各專門事件頁。

## 相關文件
[[evt-ad-security-overview]]、[[evt-logon-success]]、[[evt-logon-failure]]、[[doc-windows-events-into-wazuh]]；跨連父層 [[windows-event-log-and-sysmon]]。

## 建議查證來源
Microsoft Windows Security Auditing 文件、Wazuh 官方文件。

## 可被檢索的關鍵字（中英）
Windows Security Log、Event ID、Logon Type、稽核、安全事件、security event、audit。
