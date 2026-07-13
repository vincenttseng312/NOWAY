---
id: scn-malicious-file-execution
title: "惡意檔案下載或執行偵測"
doc_type: attack-scenario
category: attack-scenario
summary: "偵測下載並執行惡意檔案：可疑路徑（Temp/AppData）落地、程序建立、緊接的網路/持久化行為。以程序鏈與落地路徑為核心，深入分析可跨連父層惡意程式分析概念群。"
tags: [cat:attack-scenario, mitre-tactic:execution, source:windows-security, risk:high]
related_entities: [ent-host-win11-target]
related_docs: [scn-suspicious-powershell, scn-suspicious-external-connection, doc-correlation-rules]
mitre_attack: [t1204, t1105, t1059]
wazuh_sources: []
windows_event_ids: ["4688"]
risk_level: high
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: ["惡意檔案", "下載執行", "dropper", "T1204", "T1105", "malicious execution"]
last_updated: 2026-07-09
---

# 惡意檔案下載或執行偵測

## 1. 情境說明
偵測惡意檔案被取得並執行。本頁談偵測跡象；惡意程式的深入靜/動態分析跨連父層概念群，不在此重述，也不含製作/散布惡意檔的內容。

## 2. 攻擊者可能目標
在靶機執行 payload（dropper/loader/RAT 等），建立控制、持久化或進一步行動。

## 3. 防禦方可觀測跡象
可疑路徑（`%TEMP%`、`%APPDATA%`、Downloads）出現新可執行檔並被執行、異常程序鏈、執行後對外連線或寫入自啟。

## 4. 可能出現的 Windows / AD 事件
4688（程序建立，命令列需開稽核）；若有 Sysmon，FileCreate/Image Loaded/Network 等更豐富（依環境）。父層 [[windows-event-log-and-sysmon]] 有 Sysmon EID 對照。

## 5. 可能出現的 Wazuh 告警欄位
程序路徑/父程序、`agent.name`、（若採集）檔案落地與 hash 相關欄位、`rule.groups`；`rule.id` env-specific。

## 6. MITRE ATT&CK 對應
T1204 User Execution、T1105 Ingress Tool Transfer、T1059 Command and Scripting Interpreter（視手法）。以官方為準。

## 7. 風險等級判斷
high；執行後出現 C2 連線（[[scn-suspicious-external-connection]]）或持久化則 critical。

## 8. AI 分析重點
落地路徑、父程序（誰啟動它）、執行後行為（網路/寫檔/持久化）、是否可取得 hash 供比對。行為判讀方法見父層 [[dynamic-behavior-analysis]]。

## 9. 儀表板呈現方式
可疑程序執行卡、落地路徑分布、「下載→執行→連線」關聯鏈。

## 10. 使用者可能詢問的問題
「有沒有惡意檔案被執行？」「這個程序是從哪來的？」

## 11. AI 回答範例
「<主機> 於 <時間> 從 %APPDATA% 執行 <檔名>（4688），父程序為 <parent>，隨後對外連線 <IP>。符合惡意檔案執行（T1204/T1105）。建議取得該檔 hash 比對並隔離主機。」（值為佔位。）

## 12. 建議處置方式
隔離主機、取得並比對檔案 hash、檢查持久化與網路行為、清除；深入分析參考父層惡意程式分析流程。

## 13. 誤判可能性
使用者正常下載安裝合法軟體、開發/測試產生的執行檔、可攜式工具。

## 14. 需要進一步確認的資料
是否採集檔案落地/hash、Sysmon 是否啟用、檔案來源與簽章。

## 相關文件
[[scn-suspicious-powershell]]、[[scn-suspicious-external-connection]]、[[doc-correlation-rules]]；跨連父層 [[dynamic-behavior-analysis]]、[[malware-behavior-patterns]]、[[pe-static-analysis]]。

## 建議查證來源
Microsoft Windows Security Auditing 文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
惡意檔案、下載執行、dropper、T1204、T1105、malicious execution。
