---
id: scn-failed-then-success-logon
title: "失敗登入後成功登入偵測"
doc_type: attack-scenario
category: attack-scenario
summary: "大量失敗後緊接成功登入，是暴力破解/噴灑「猜中」的關鍵關聯訊號，風險遠高於單看失敗或成功。需以同帳號/同來源在時間窗內的 4625→4624 序列判定。"
tags: [cat:attack-scenario, mitre-tactic:credential-access, source:windows-security, risk:high]
related_entities: [ent-account, ent-ip]
related_docs: [evt-logon-failure, evt-logon-success, scn-rdp-bruteforce, doc-correlation-rules]
mitre_attack: [t1110, t1078]
wazuh_sources: []
windows_event_ids: ["4625", "4624"]
risk_level: high
confidence: high
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: ["失敗後成功", "brute force success", "關聯偵測", "4625 4624", "T1110", "T1078"]
last_updated: 2026-07-09
---

# 失敗登入後成功登入偵測

## 1. 情境說明
一個**關聯型**偵測：同帳號或同來源在短時間窗內先出現大量失敗（4625），隨後出現成功（4624）。這是暴力/噴灑「破解成功」的高信心訊號。

## 2. 攻擊者可能目標
確認已猜中有效憑證，取得存取。

## 3. 防禦方可觀測跡象
時間窗內 `4625×N → 4624` 的序列，且失敗與成功共享帳號或來源 IP。

## 4. 可能出現的 Windows / AD 事件
4625（多）緊接 4624（成功）。見 [[evt-logon-failure]]、[[evt-logon-success]]。此關聯邏輯見 [[doc-correlation-rules]]。

## 5. 可能出現的 Wazuh 告警欄位
`targetUserName`、`ipAddress`、`logonType`、`timestamp`（排序）、`rule.level`；關聯可能由 Wazuh 規則或後端 AI 完成（依環境）。

## 6. MITRE ATT&CK 對應
T1110 Brute Force（成功）+ T1078 Valid Accounts（隨後以有效帳號存取）。以官方為準。

## 7. 風險等級判斷
high–critical：代表憑證可能已淪陷，攻擊者已取得立足點。

## 8. AI 分析重點
確認失敗與成功的**同一性**（同帳號/同來源）、時間窗合理性、成功後的行為（是否隨即建立帳號/提權/連線）。

## 9. 儀表板呈現方式
失敗→成功關聯卡（最高優先）、受影響帳號時間線、來源 IP 標記。

## 10. 使用者可能詢問的問題
「有沒有登入失敗後又成功的？」「哪個帳號可能被破解了？」

## 11. AI 回答範例
「<帳號> 於 <時間> 從 <IP> 成功登入（4624），此前 <X 分鐘>內同來源有 <N> 次失敗（4625）。高度疑似暴力破解成功（T1110→T1078）。建議立即重設該帳號憑證並調查後續行為。」（值為佔位。）

## 12. 建議處置方式
立即重設憑證、凍結帳號、隔離主機、全面檢視成功登入後的所有活動；走事件回應 [[doc-ir-sop]]（⏳批 6）。

## 13. 誤判可能性
使用者多次打錯後終於打對（尤其人為互動、非自動化節奏、來源為慣用裝置）——需以來源與節奏區分。

## 14. 需要進一步確認的資料
關聯時間窗與次數門檻（env-specific）、失敗與成功是否確為同一主體、成功後行為。

## 相關文件
[[evt-logon-failure]]、[[evt-logon-success]]、[[scn-rdp-bruteforce]]、[[doc-correlation-rules]]

## 建議查證來源
Microsoft Windows Security Auditing 文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
失敗後成功、brute force success、關聯偵測、4625 4624、T1110、T1078。
