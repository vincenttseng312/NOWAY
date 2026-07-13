---
id: scn-suspicious-external-connection
title: "可疑外部 IP 連線偵測"
doc_type: attack-scenario
category: attack-scenario
summary: "偵測靶機對外的可疑連線，尤其非瀏覽器程序對外、週期性 beacon、連往罕見/攻擊網段。可能是 C2 通訊或資料外洩，以程序-連線關聯與時間節奏為核心。"
tags: [cat:attack-scenario, mitre-tactic:command-and-control, source:wazuh-rule, risk:high]
related_entities: [ent-ip, ent-host-win11-target]
related_docs: [scn-malicious-file-execution, scn-port-scan, doc-network-topology, doc-correlation-rules]
mitre_attack: [t1071, t1571]
wazuh_sources: []
windows_event_ids: []
risk_level: high
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "MITRE ATT&CK 官方網站"]
keywords: ["可疑外部連線", "C2", "beacon", "資料外洩", "T1071", "external connection"]
last_updated: 2026-07-09
---

# 可疑外部 IP 連線偵測

## 1. 情境說明
偵測靶機對外的可疑連線（C2 回連或外洩）。本頁談偵測跡象與判讀，不含建立 C2/外洩通道的方法。

## 2. 攻擊者可能目標
與 C2 通訊接收指令、下載後續 payload、或將竊得資料外傳。

## 3. 防禦方可觀測跡象
非瀏覽器程序（如 rundll32/powershell/notepad）對外連線、固定間隔的小流量 beacon、連往罕見/新註冊網域或攻擊網段、跨路由器邊界的異常外連（見 [[doc-network-topology]]）。

## 4. 可能出現的 Windows / AD 事件
Windows Security 對純網路連線著墨有限；若有 Sysmon（EID 3 網路連線 / EID 22 DNS，見父層 [[windows-event-log-and-sysmon]]）證據更完整（依環境）。

## 5. 可能出現的 Wazuh 告警欄位
`data.win.eventdata.ipAddress`（若來自 Windows 事件）、程序-連線關聯欄位（若採集網路/ Sysmon）、`rule.groups`、`full_log`；`rule.id` env-specific。

## 6. MITRE ATT&CK 對應
T1071 Application Layer Protocol（C2）；非標準埠 T1571；資料外洩另關聯 exfiltration 技術（視情況，以官方為準）。

## 7. 風險等級判斷
high；確認為 C2 或伴隨資料外傳則 critical。

## 8. AI 分析重點
哪個程序發起連線（非瀏覽器對外很可疑）、目的 IP/網域信譽（需外部查證）、時間節奏（beacon 週期/jitter）、是否緊接惡意檔案執行。beacon 判讀見父層 [[dynamic-behavior-analysis]]。

## 9. 儀表板呈現方式
Top 可疑外部目的、beacon 週期偵測卡、程序-連線關係圖。

## 10. 使用者可能詢問的問題
「有沒有可疑對外連線？」「這個外部 IP 可信嗎？」「像不像 C2？」

## 11. AI 回答範例
「<主機> 上 <程序> 以固定間隔對外部 <IP> 連線（週期 ~<秒>），型樣類似 C2 beacon（T1071）。該 IP 位於攻擊網段。建議封鎖並檢查該程序來源與落地檔案。IP 信譽需外部查證。」（值為佔位。）

## 12. 建議處置方式
封鎖可疑目的、隔離主機、追發起程序與其來源檔案、檢查是否有資料外傳跡象。

## 13. 誤判可能性
軟體更新/遙測、雲端同步、合法應用的長連線、CDN 造成的 IP 多變。

## 14. 需要進一步確認的資料
是否採集網路/ Sysmon 事件、目的 IP/網域信譽、程序來源、是否為授權服務。

## 相關文件
[[scn-malicious-file-execution]]、[[scn-port-scan]]、[[doc-network-topology]]、[[doc-correlation-rules]]；跨連父層 [[dynamic-behavior-analysis]]、[[ioc-ttp-and-detection-engineering]]。

## 建議查證來源
Wazuh 官方文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
可疑外部連線、C2、beacon、資料外洩、T1071、external connection。
