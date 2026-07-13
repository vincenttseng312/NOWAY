---
id: scn-rdp-bruteforce
title: "RDP 暴力破解偵測"
doc_type: attack-scenario
category: attack-scenario
summary: "攻擊者對靶機 RDP 反覆嘗試登入，防禦面表現為大量 4625（LogonType 10）來自單一外部來源，可能伴隨帳號鎖定（4740）。核心是失敗頻率與來源，並警戒是否出現成功登入。"
tags: [cat:attack-scenario, mitre-tactic:credential-access, source:windows-security, risk:high]
related_entities: [ent-ip, ent-account, ent-host-win11-target]
related_docs: [evt-logon-failure, evt-rdp-logon, scn-failed-then-success-logon, evt-account-lockout]
mitre_attack: [t1110, t1021-001]
wazuh_sources: []
windows_event_ids: ["4625 (LogonType 10)", "4740"]
risk_level: high
confidence: high
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: ["RDP 暴力破解", "brute force", "4625", "LogonType 10", "T1110", "T1021.001"]
last_updated: 2026-07-09
---

# RDP 暴力破解偵測

## 1. 情境說明
攻擊者透過 RDP 對靶機反覆嘗試帳密。本頁只談偵測與處置，不含破解工具或字典操作。

## 2. 攻擊者可能目標
猜出有效 RDP 憑證，取得互動式存取以進一步橫向移動/提權。

## 3. 防禦方可觀測跡象
單一外部來源短時間大量 RDP 登入失敗；可能觸發帳號鎖定；失敗後若出現成功登入是最嚴重訊號。

## 4. 可能出現的 Windows / AD 事件
4625（LogonType 10）大量、可能 4740 鎖定、警戒 4624（LogonType 10）成功。詳見 [[evt-logon-failure]]、[[evt-rdp-logon]]、[[evt-account-lockout]]。

## 5. 可能出現的 Wazuh 告警欄位
`data.win.eventdata.ipAddress`（來源）、`logonType=10`、`targetUserName`、`rule.level`、`rule.groups`（authentication 類，值依規則集）；`rule.id` env-specific。

## 6. MITRE ATT&CK 對應
T1110 Brute Force（+ 可能 T1110.001 密碼猜測 / T1110.003 密碼噴灑，子技術以官方為準）；管道 T1021.001 RDP。

## 7. 風險等級判斷
持續失敗 high；一旦出現失敗後成功（[[scn-failed-then-success-logon]]）升為 critical。

## 8. AI 分析重點
單位時間失敗次數、來源是否外部/攻擊網段、目標帳號數（單帳號=暴力、多帳號=噴灑）、是否有對應成功。

## 9. 儀表板呈現方式
RDP 攻擊監控圖、Top RDP 失敗來源、失敗→成功關聯卡（高優先）。

## 10. 使用者可能詢問的問題
「RDP 有被暴力破解嗎？」「哪個 IP 在打 RDP？」

## 11. AI 回答範例
「外部 <IP> 於 <時間窗> 產生 <N> 次 RDP 失敗（4625, Type 10）針對 <帳號>，符合 T1110。尚未觀察到成功登入（需確認）。建議封鎖來源並限制 RDP 暴露面。」（值為佔位。）

## 12. 建議處置方式
封鎖來源、限制 RDP 僅內部/VPN、啟用帳號鎖定原則與 NLA（依環境）；若已成功則走事件回應 [[doc-ir-sop]]（⏳批 6）。

## 13. 誤判可能性
使用者忘記密碼多次重試、舊憑證的自動重連、滲透測試授權活動。

## 14. 需要進一步確認的資料
鎖定門檻、是否已有成功登入、RDP 是否應對外開放。

## 相關文件
[[evt-logon-failure]]、[[evt-rdp-logon]]、[[scn-failed-then-success-logon]]、[[evt-account-lockout]]

## 建議查證來源
Microsoft Windows Security Auditing 文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
RDP 暴力破解、brute force、4625、LogonType 10、T1110、T1021.001。
