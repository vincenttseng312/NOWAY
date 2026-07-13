---
id: scn-local-user-creation
title: "新增本機使用者偵測"
doc_type: attack-scenario
category: attack-scenario
summary: "偵測未授權的本機/網域帳號建立（4720），常為持久化後門。高風險組合是新帳號建立後立即被加入特權群組或用於登入。"
tags: [cat:attack-scenario, mitre-tactic:persistence, source:windows-security, risk:high]
related_entities: [ent-account, ent-host-win11-target]
related_docs: [evt-user-creation, scn-add-to-administrators, doc-correlation-rules]
mitre_attack: [t1136-001]
wazuh_sources: []
windows_event_ids: ["4720", "4722"]
risk_level: high
confidence: high
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: ["新增使用者", "本機帳號", "持久化", "後門帳號", "create account", "T1136"]
last_updated: 2026-07-09
---

# 新增本機使用者偵測

## 1. 情境說明
偵測未授權的帳號建立。事件面見 [[evt-user-creation]]；本頁聚焦攻擊情境與關聯。不含建立帳號的操作指令。

## 2. 攻擊者可能目標
建立長期後門帳號以維持存取，避免依賴可能被重設的既有帳號。

## 3. 防禦方可觀測跡象
非 IT 流程外的帳號建立、可疑建立者、帳號名偽裝、建立後立即的群組加入或登入。

## 4. 可能出現的 Windows / AD 事件
4720（建立）、4722（啟用）；高風險後續 4732/4728（加入特權群組）。

## 5. 可能出現的 Wazuh 告警欄位
`targetUserName`（新帳號）、`subjectUserName`（建立者）、`agent.name`、`rule.groups`；`rule.id` env-specific。

## 6. MITRE ATT&CK 對應
T1136.001 Create Account: Local Account（網域帳號為 T1136.002，以官方為準）。

## 7. 風險等級判斷
high；若建立後立即加入 Administrators（[[scn-add-to-administrators]]）升為 critical。

## 8. AI 分析重點
建立者是否合理、帳號名是否偽裝、與群組加入/登入的時間關聯（見 [[doc-correlation-rules]]）。

## 9. 儀表板呈現方式
新增帳號時間線、「建帳號→加特權群組」關聯卡、建立者分布。

## 10. 使用者可能詢問的問題
「有沒有新帳號被建立？」「這個帳號誰建的、拿來做什麼？」

## 11. AI 回答範例
「<主機> 於 <時間> 由 <subject> 建立帳號 <名稱>（4720），非既知 IT 流程。<X 分鐘>後該帳號登入，建議確認授權並調查其行為。」（值為佔位。）

## 12. 建議處置方式
確認授權；未授權則停用/刪除、追建立者來源、檢查帳號已進行的活動。

## 13. 誤判可能性
IT 佈建、自動化部署、加網域產生的服務帳號。

## 14. 需要進一步確認的資料
既知的合法帳號建立流程、建立者身分、後續使用情形。

## 相關文件
[[evt-user-creation]]、[[scn-add-to-administrators]]、[[doc-correlation-rules]]；跨連父層 [[persistence-mechanisms]]。

## 建議查證來源
Microsoft Windows Security Auditing 文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
新增使用者、本機帳號、持久化、後門帳號、create account、T1136。
