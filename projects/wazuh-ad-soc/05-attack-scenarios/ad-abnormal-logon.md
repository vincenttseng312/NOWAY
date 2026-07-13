---
id: scn-ad-abnormal-logon
title: "AD 帳號異常登入偵測"
doc_type: attack-scenario
category: attack-scenario
summary: "偵測網域帳號的異常登入：罕見來源/時段、地理或主機跳躍、特權帳號登入非預期主機。以帳號基準偏離為核心，對應濫用有效網域帳號。"
tags: [cat:attack-scenario, mitre-tactic:initial-access, source:ad, risk:high]
related_entities: [ent-account, ent-ip, ent-host-dc]
related_docs: [evt-account-anomaly-detection, evt-logon-success, evt-ad-security-overview]
mitre_attack: [t1078-002]
wazuh_sources: []
windows_event_ids: ["4624", "4768/4769 (需確認)"]
risk_level: high
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: ["AD 異常登入", "網域帳號", "valid accounts", "基準偏離", "T1078.002"]
last_updated: 2026-07-09
---

# AD 帳號異常登入偵測

## 1. 情境說明
偵測網域帳號被濫用的異常登入。判斷方法論見 [[evt-account-anomaly-detection]]；本頁聚焦 AD 情境。

## 2. 攻擊者可能目標
以竊得或濫用的網域帳號在環境中存取資源，因其為「有效帳號」而較不易被察覺。

## 3. 防禦方可觀測跡象
帳號自罕見來源/時段登入、短時間跨多主機、特權帳號登入一般端點、與慣用基準明顯偏離。

## 4. 可能出現的 Windows / AD 事件
4624（成功登入，看 logonType/來源）；Kerberos 認證事件 4768/4769（**需依 Microsoft 官方確認**）可佐證網域認證軌跡。見 [[evt-ad-security-overview]]。

## 5. 可能出現的 Wazuh 告警欄位
`targetUserName`、`ipAddress`、`logonType`、`timestamp`、`agent.name`（登入的主機）；`rule.id` env-specific。

## 6. MITRE ATT&CK 對應
T1078.002 Valid Accounts: Domain Accounts。以官方為準。

## 7. 風險等級判斷
high；特權網域帳號異常或跨多主機時升級。

## 8. AI 分析重點
以帳號為主體聚合、對照基準（慣用來源/時段/主機）、是否跨主機、是否特權帳號；冷啟動無基準時信心較低要說明。

## 9. 儀表板呈現方式
單一帳號行為時間線、帳號風險評分、跨主機登入關係圖。

## 10. 使用者可能詢問的問題
「這個網域帳號登入正常嗎？」「有沒有帳號在多台機器異常登入？」

## 11. AI 回答範例
「網域帳號 <user> 於 <時間> 自 <罕見 IP> 登入 <主機>（4624），與其近 <期間>基準（慣用來源/時段）明顯偏離，且為特權帳號。對應 T1078.002，建議優先調查並考慮重設憑證。」（值為佔位。）

## 12. 建議處置方式
確認是否本人（出差/在家）；異常則凍結帳號、重設憑證、檢查該帳號跨主機的所有活動。

## 13. 誤判可能性
出差/遠端辦公改變來源、輪班改變時段、新進人員無基準、共用帳號。

## 14. 需要進一步確認的資料
帳號基準是否足夠、Kerberos 事件是否採集、來源變更是否有正當理由。

## 相關文件
[[evt-account-anomaly-detection]]、[[evt-logon-success]]、[[evt-ad-security-overview]]

## 建議查證來源
Microsoft Windows Security Auditing 文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
AD 異常登入、網域帳號、valid accounts、基準偏離、T1078.002。
