---
id: scn-privilege-escalation-signs
title: "權限提升跡象偵測"
doc_type: attack-scenario
category: attack-scenario
summary: "權限提升是一類跡象而非單一事件：加入特權群組、特殊權限指派、以高完整性層級執行、可疑提權工具。以多訊號綜合判斷，並回連相關事件與情境頁。"
tags: [cat:attack-scenario, mitre-tactic:privilege-escalation, source:windows-security, risk:high]
related_entities: [ent-account, ent-host-win11-target]
related_docs: [scn-add-to-administrators, evt-admin-group-change, evt-windows-security-overview, doc-correlation-rules]
mitre_attack: [t1078, t1098, t1548]
wazuh_sources: []
windows_event_ids: ["4672", "4732", "4728"]
risk_level: high
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: ["權限提升", "提權", "privilege escalation", "特殊權限", "4672", "T1548"]
last_updated: 2026-07-09
---

# 權限提升跡象偵測

## 1. 情境說明
偵測帳號/程序取得超出原有的權限。這是**一類跡象的集合**，需綜合多訊號，而非依賴單一 Event ID。不含提權漏洞利用步驟。

## 2. 攻擊者可能目標
從一般權限提升到管理員/系統層級，以控制主機、存取敏感資料、建立持久化。

## 3. 防禦方可觀測跡象
帳號被加入特權群組、登入時被指派特殊權限（4672）、以高完整性層級執行的可疑程序、UAC/服務/排程相關的可疑提權路徑。

## 4. 可能出現的 Windows / AD 事件
4672（特殊權限指派）、4732/4728（加入特權群組，見 [[evt-admin-group-change]]）、4688（高完整性程序，命令列需開稽核）。

## 5. 可能出現的 Wazuh 告警欄位
`targetUserName`、`subjectUserName`、群組/權限欄位、程序完整性層級（若擷取）、`rule.level`；`rule.id` env-specific。

## 6. MITRE ATT&CK 對應
提權戰術下多技術：T1098 Account Manipulation、T1078 Valid Accounts、T1548 Abuse Elevation Control Mechanism 等——**具體技術依實際手法，以 MITRE 官方為準，不臆造單一 id**。

## 7. 風險等級判斷
high；與新帳號建立或可疑登入串鏈時 critical。

## 8. AI 分析重點
多訊號關聯（群組+權限+程序）、時間鏈、帳號來歷；避免只憑 4672（正常管理登入也會產生）就判提權。

## 9. 儀表板呈現方式
提權跡象綜合卡、特權活動時間線、攻擊鏈視圖。

## 10. 使用者可能詢問的問題
「有沒有權限提升跡象？」「這個帳號是不是提權了？」

## 11. AI 回答範例
「<帳號> 於短時間內被加入 Administrators（4732）並以高完整性執行 <程序>，且此前為一般帳號。多訊號綜合符合權限提升跡象（提權戰術）。單看 4672 不足以定論，但合併群組異動後風險升高，建議調查。」（值為佔位。）

## 12. 建議處置方式
撤銷不當權限、停用相關帳號、隔離主機、回溯提權路徑；走 [[doc-ir-sop]]（⏳批 6）。

## 13. 誤判可能性
管理員正常登入（4672 常見）、IT 授權提權、PAM 工具、安裝程式以高權限執行。

## 14. 需要進一步確認的資料
哪些群組/權限屬敏感、程序完整性是否採集、提權是否授權。

## 相關文件
[[scn-add-to-administrators]]、[[evt-admin-group-change]]、[[evt-windows-security-overview]]、[[doc-correlation-rules]]

## 建議查證來源
Microsoft Windows Security Auditing 文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
權限提升、提權、privilege escalation、特殊權限、4672、T1548。
