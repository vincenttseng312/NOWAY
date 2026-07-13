---
id: scn-mass-logon-failure
title: "大量登入失敗偵測"
doc_type: attack-scenario
category: attack-scenario
summary: "短時間大量 4625 是暴力破解或密碼噴灑的通用訊號，不限 RDP。以「同來源多密碼 vs 多帳號同密碼」區分攻擊型態，並結合失敗原因碼判讀。"
tags: [cat:attack-scenario, mitre-tactic:credential-access, source:windows-security, risk:medium]
related_entities: [ent-ip, ent-account]
related_docs: [evt-logon-failure, scn-rdp-bruteforce, scn-failed-then-success-logon, evt-account-lockout]
mitre_attack: [t1110]
wazuh_sources: []
windows_event_ids: ["4625"]
risk_level: medium
confidence: high
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: ["大量登入失敗", "密碼噴灑", "password spray", "brute force", "4625", "T1110"]
last_updated: 2026-07-09
---

# 大量登入失敗偵測

## 1. 情境說明
偵測跨管道（RDP、SMB、網域認證等）的大量登入失敗。RDP 特化情境見 [[scn-rdp-bruteforce]]；本頁是通用型。

## 2. 攻擊者可能目標
以自動化嘗試猜測憑證（暴力）或以少量常見密碼試多帳號（噴灑）以避開單帳號鎖定。

## 3. 防禦方可觀測跡象
失敗量在短時間內飆升；失敗分布是「集中單帳號」還是「散在多帳號」；失敗原因碼分布。

## 4. 可能出現的 Windows / AD 事件
4625 大量（跨 logonType）；可能 4740 鎖定。失敗原因碼（Status/SubStatus）可區分密碼錯誤 vs 帳號不存在——具體代碼需依 Microsoft 官方確認，見 [[evt-logon-failure]]。

## 5. 可能出現的 Wazuh 告警欄位
`targetUserName`、`ipAddress`、`logonType`、失敗次數聚合、`rule.level`；`rule.id` env-specific。

## 6. MITRE ATT&CK 對應
T1110 Brute Force（噴灑對應 T1110.003、猜測 T1110.001，子技術以官方為準）。

## 7. 風險等級判斷
medium 起；集中單帳號或伴隨成功則升級；大範圍多帳號噴灑視涵蓋面升級。

## 8. AI 分析重點
失敗的「帳號數 vs 密碼數」型態、來源集中度、時間節奏（自動化常規律）、是否有成功。

## 9. 儀表板呈現方式
登入失敗趨勢圖、Top 被嘗試帳號、Top 失敗來源、噴灑 vs 暴力型態標記。

## 10. 使用者可能詢問的問題
「今天登入失敗異常多嗎？」「是暴力還是密碼噴灑？」

## 11. AI 回答範例
「<時間窗> 內出現 <N> 次 4625，散布於 <M> 個帳號、來自 <IP>，型態較接近密碼噴灑（T1110.003，需依失敗原因碼確認）。建議檢查是否有任一帳號成功。」（值為佔位。）

## 12. 建議處置方式
封鎖來源、檢視鎖定原則、強化弱密碼帳號、比對是否已有成功登入。

## 13. 誤判可能性
應用程式綁定過期密碼反覆重試、服務帳號設定錯誤、大型自動化任務。

## 14. 需要進一步確認的資料
失敗原因碼語意、鎖定門檻、失敗來源是否授權。

## 相關文件
[[evt-logon-failure]]、[[scn-rdp-bruteforce]]、[[scn-failed-then-success-logon]]、[[evt-account-lockout]]

## 建議查證來源
Microsoft Windows Security Auditing 文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
大量登入失敗、密碼噴灑、password spray、brute force、4625、T1110。
