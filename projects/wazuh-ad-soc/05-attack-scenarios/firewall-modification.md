---
id: scn-firewall-modification
title: "防火牆設定遭修改偵測"
doc_type: attack-scenario
category: attack-scenario
summary: "偵測未授權的 Windows 防火牆規則/服務變更，常為攻擊者開後門埠或削弱防禦。防火牆相關 Event ID 需依 Microsoft 官方確認，重點放在變更授權性與時間關聯。"
tags: [cat:attack-scenario, mitre-tactic:defense-evasion, source:windows-security, risk:high]
related_entities: [ent-host-win11-target]
related_docs: [evt-security-config-change, scn-security-tool-disable]
mitre_attack: [t1562-004]
wazuh_sources: []
windows_event_ids: ["防火牆變更 ID (需確認)", "5025 (需確認)"]
risk_level: high
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: ["防火牆修改", "firewall", "defense evasion", "開後門埠", "T1562.004"]
last_updated: 2026-07-09
---

# 防火牆設定遭修改偵測

## 1. 情境說明
偵測防火牆規則新增/修改/刪除或服務停用。事件面見 [[evt-security-config-change]]；本頁聚焦攻擊意圖與判讀。不含修改防火牆的操作指令。

## 2. 攻擊者可能目標
開放特定埠以利 C2/遠端存取、關閉阻擋規則、或整體停用防火牆以降低偵測與阻擋。

## 3. 防禦方可觀測跡象
防火牆規則/設定變更、防火牆服務停止、變更緊接可疑登入或程序。

## 4. 可能出現的 Windows / AD 事件
Windows 防火牆變更相關事件（如 4946/4947/4948/4950 系列、5025）——**具體 ID 需依 Microsoft 官方文件確認**，見 [[evt-security-config-change]]。

## 5. 可能出現的 Wazuh 告警欄位
`data.win.system.providerName`、變更內容/操作者欄位（若擷取）、`full_log`（兜底）；`rule.id` env-specific。

## 6. MITRE ATT&CK 對應
T1562.004 Impair Defenses: Disable or Modify System Firewall。以官方為準。

## 7. 風險等級判斷
high；若與新開埠 + 對外連線關聯則升級。

## 8. AI 分析重點
變更是否授權、變更方向（開放 vs 收緊）、操作者、與其他削弱防禦動作是否同時發生（批次 Defense Evasion）。

## 9. 儀表板呈現方式
安全設定變更告警卡、防火牆狀態時間線。

## 10. 使用者可能詢問的問題
「有沒有人動過防火牆？」「防火牆是不是被關了？」

## 11. AI 回答範例
「<主機> 於 <時間> 出現防火牆設定變更（Event ID 需依環境確認），操作者 <subject>。若同時觀察到新開埠與對外連線，符合 T1562.004，建議調查授權性並還原設定。」（值為佔位。）

## 12. 建議處置方式
確認授權；未授權則還原規則、隔離主機、檢查變更期間的網路行為。

## 13. 誤判可能性
IT 正常規則調整、軟體安裝自動加規則、維運變更（應有紀錄）。

## 14. 需要進一步確認的資料
防火牆事件對應的實際 Event ID 與 Wazuh 規則、變更是否授權。

## 相關文件
[[evt-security-config-change]]、[[scn-security-tool-disable]]；跨連父層 [[ioc-ttp-and-detection-engineering]]。

## 建議查證來源
Microsoft Windows Security Auditing 文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
防火牆修改、firewall、defense evasion、開後門埠、T1562.004。
