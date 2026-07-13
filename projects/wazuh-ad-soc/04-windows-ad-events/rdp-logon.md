---
id: evt-rdp-logon
title: "遠端桌面登入事件"
doc_type: event
category: windows-ad-event
summary: "RDP 登入通常呈現為 Event 4624/4625 且 LogonType=10（RemoteInteractive）。TerminalServices 相關通道另有連線事件，具體 ID 需依 Microsoft 官方文件確認。RDP 是本專題外部攻擊面的重點。"
tags: [cat:event, type:event, source:windows-security, source:terminal-services, mitre-technique:t1021-001]
event_source: terminal-services
windows_event_ids: ["4624 (LogonType 10)", "4625 (LogonType 10)", "TerminalServices 通道事件 (需確認)"]
wazuh_sources: []
related_entities: [ent-ip, ent-account, ent-host-win11-target]
related_docs: [evt-logon-success, evt-logon-failure, scn-rdp-bruteforce]
risk_level: medium
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件"]
keywords: ["RDP", "遠端桌面", "LogonType 10", "RemoteInteractive", "TerminalServices", "T1021.001"]
last_updated: 2026-07-09
---

# 遠端桌面登入事件

## 1. 事件用途
偵測遠端桌面（RDP）登入。主要透過 **4624/4625 + LogonType=10（RemoteInteractive）**（以 Microsoft 官方為準）。此外 Windows TerminalServices 相關通道（如 RemoteConnectionManager、LocalSessionManager）另有連線/重連事件——**具體 Event ID（如常被引用的 1149 等）需依 Microsoft 官方文件確認**，本頁不記死。

## 2. 可能代表的安全意義
- 對映 MITRE **T1021.001 Remote Services: RDP**（橫向移動/遠端存取）。
- 本專題中，外部攻擊者主機經路由器對靶機的 RDP 嘗試是核心觀察面（見 [[scn-rdp-bruteforce]]）。
- 重點：來源 IP 是否為外部/非預期、是否緊接大量 4625 失敗。

## 3. 可能涉及的 Windows Event ID
| 來源 | Event ID | 意義 | 驗證 |
|---|---|---|---|
| Security | 4624 / 4625（LogonType 10） | RDP 登入成功/失敗 | 4624/4625 及 Type 10 以 Microsoft 官方為準 |
| TerminalServices 通道 | 連線/重連事件 | 連線管理層事件 | **需依 Microsoft 官方文件確認** |

## 4. 在 Wazuh Alert 中可能出現的欄位
`eventID`、`data.win.eventdata.logonType=10`、`data.win.eventdata.ipAddress`（來源）、`data.win.eventdata.targetUserName`、workstationName。

## 5. AI 分析時應注意的欄位
LogonType=10 的成功/失敗、來源 IP 的網段（內/外）、同來源失敗次數、登入時間是否異常。

## 6. 儀表板可以如何視覺化
RDP 攻擊監控圖、RDP 來源 IP 地圖/排行、RDP 失敗→成功關聯卡。

## 7. 使用者可能會問的問題
「有沒有外部 RDP 登入？」「RDP 有被暴力破解嗎？」

## 8. AI 回答範例
「偵測到來自外部 <IP> 的 RDP 登入活動（4624/4625, LogonType 10）。若該 IP 位於攻擊網段且伴隨大量失敗，符合 RDP 暴力破解型樣（T1021.001 + T1110）。」（值為佔位。）

## 9. 誤判情境
授權的遠端維運、跳板機、IT 支援連線、內部管理 RDP。

## 10. 處置建議
限制 RDP 來源（僅允許內部/VPN，依環境）；封鎖可疑外部來源；檢查成功登入後行為。

## 相關文件
[[evt-logon-success]]、[[evt-logon-failure]]、[[scn-rdp-bruteforce]]

## 建議查證來源
Microsoft Windows Security Auditing 文件。

## 可被檢索的關鍵字（中英）
RDP、遠端桌面、LogonType 10、RemoteInteractive、TerminalServices、T1021.001。
