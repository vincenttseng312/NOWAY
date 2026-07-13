---
id: scn-lateral-movement-signs
title: "橫向移動跡象偵測"
doc_type: attack-scenario
category: attack-scenario
summary: "橫向移動是攻擊者在內網從一台主機擴散到另一台。跡象包括跨主機的遠端登入、遠端服務使用、工具傳輸。以主機間的登入關係與遠端執行為核心。"
tags: [cat:attack-scenario, mitre-tactic:lateral-movement, source:windows-security, risk:high]
related_entities: [ent-account, ent-host-win11-target, ent-host-dc]
related_docs: [evt-rdp-logon, evt-logon-success, scn-ad-abnormal-logon, doc-correlation-rules]
mitre_attack: [t1021, t1021-001, t1570]
wazuh_sources: []
windows_event_ids: ["4624 (LogonType 3/10)", "4648"]
risk_level: high
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: ["橫向移動", "lateral movement", "遠端服務", "跨主機登入", "T1021", "T1570"]
last_updated: 2026-07-09
---

# 橫向移動跡象偵測

## 1. 情境說明
偵測攻擊者在內網主機間擴散的跡象。本專題主機較少，但靶機↔DC 或多端點間的遠端登入/執行仍是重點。不含橫向移動工具操作。

## 2. 攻擊者可能目標
從初始落腳點擴散到更有價值的主機（如 DC），擴大控制與存取。

## 3. 防禦方可觀測跡象
同帳號短時間登入多台主機、遠端互動/網路登入（LogonType 10/3）、使用明確憑證登入（4648）、遠端服務/工具傳輸、程序鏈跨主機呼應。

## 4. 可能出現的 Windows / AD 事件
4624（LogonType 3 網路 / 10 RDP）、4648（明確憑證登入）；遠端服務相關事件依手法而定。見 [[evt-rdp-logon]]、[[evt-logon-success]]。

## 5. 可能出現的 Wazuh 告警欄位
`targetUserName`、來源/目標主機（`agent.name`、`workstationName`、`ipAddress`）、`logonType`、`timestamp`；`rule.id` env-specific。

## 6. MITRE ATT&CK 對應
T1021 Remote Services（含 T1021.001 RDP、T1021.002 SMB 等子技術）、T1570 Lateral Tool Transfer。以官方為準。

## 7. 風險等級判斷
high；朝 DC/關鍵主機移動時 critical。

## 8. AI 分析重點
以帳號串起「來源主機→目標主機」的登入圖、時間先後、是否使用明確憑證、是否伴隨遠端執行。本專題主機少，重點在靶機與 DC 之間。

## 9. 儀表板呈現方式
主機間登入關係圖、帳號跨主機時間線、橫向移動路徑視圖。

## 10. 使用者可能詢問的問題
「有沒有橫向移動跡象？」「這個帳號在多台機器間跳嗎？」

## 11. AI 回答範例
「帳號 <user> 於 <時間> 自靶機以網路登入（4624, Type 3）連向 <另一主機>，並使用明確憑證（4648），符合橫向移動跡象（T1021）。建議確認該連線授權性並檢查目標主機。」（值為佔位。）

## 12. 建議處置方式
阻斷主機間不必要的橫向路徑、凍結帳號、隔離涉及主機、檢查目標主機是否已被存取。

## 13. 誤判可能性
IT 遠端維運、集中管理工具、備份/監控代理、正常網路檔案存取（Type 3）。

## 14. 需要進一步確認的資料
主機間正常存取基準、遠端服務事件是否採集、憑證使用是否授權。

## 相關文件
[[evt-rdp-logon]]、[[evt-logon-success]]、[[scn-ad-abnormal-logon]]、[[doc-correlation-rules]]

## 建議查證來源
Microsoft Windows Security Auditing 文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
橫向移動、lateral movement、遠端服務、跨主機登入、T1021、T1570。
