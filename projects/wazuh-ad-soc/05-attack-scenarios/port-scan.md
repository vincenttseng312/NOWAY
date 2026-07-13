---
id: scn-port-scan
title: "連接埠掃描偵測"
doc_type: attack-scenario
category: attack-scenario
summary: "攻擊者主機對靶機做連接埠/服務探測，防禦面表現為短時間大量連線嘗試、多埠、來自外部網段。以偵測與可觀測跡象為主，不含掃描工具指令。"
tags: [cat:attack-scenario, mitre-tactic:discovery, source:wazuh-rule, risk:low]
related_entities: [ent-ip, ent-host-win11-target]
related_docs: [scn-suspicious-external-connection, doc-network-topology, doc-detection-logic-overview]
mitre_attack: [t1046, t1595]
wazuh_sources: []
windows_event_ids: []
risk_level: low
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "MITRE ATT&CK 官方網站"]
keywords: ["連接埠掃描", "port scan", "service discovery", "偵察", "T1046", "T1595"]
last_updated: 2026-07-09
---

# 連接埠掃描偵測

## 1. 情境說明
攻擊者主機（外部網段）對 Windows 11 靶機探測開放埠與服務，作為後續攻擊的偵察。本頁僅談如何**偵測**，不描述掃描操作。

## 2. 攻擊者可能目標
辨識靶機開放的服務（如 RDP、SMB）與版本，規劃下一步。

## 3. 防禦方可觀測跡象
短時間內來自單一外部來源、對多個埠或多主機的連線嘗試；大量半開/被拒連線；跨越路由器邊界的異常流量（見 [[doc-network-topology]]）。

## 4. 可能出現的 Windows / AD 事件
Windows Security 日誌對純掃描通常著墨有限；若掃描觸及需認證的服務，可能間接產生登入失敗（4625）。主要證據多在網路層（防火牆/連線紀錄），需依實際採集確認。

## 5. 可能出現的 Wazuh 告警欄位
`rule.groups`（如 recon/網路類，值依規則集）、`data.win.eventdata.ipAddress`（來源）、`rule.description`；具體規則與 `rule.id` env-specific。

## 6. MITRE ATT&CK 對應
T1046 Network Service Discovery（探測服務）；若視為外部主動偵察亦可對應 T1595 Active Scanning。以 MITRE 官方為準。

## 7. 風險等級判斷
單純掃描多為 low–medium（偵察階段）；但若緊接對開放服務的攻擊（如 RDP 暴力），應整體升級。

## 8. AI 分析重點
來源 IP 是否外部/攻擊網段、掃描廣度（埠數/主機數）、時間集中度、是否為後續攻擊的前奏。

## 9. 儀表板呈現方式
Top 可疑來源 IP、掃描活動時間線、埠命中熱圖（若有網路資料）。

## 10. 使用者可能詢問的問題
「有沒有人在掃描我們？」「這個外部 IP 在做什麼？」

## 11. AI 回答範例
「外部 <IP> 於 <時間窗> 對靶機多個埠發起連線嘗試，型樣符合連接埠掃描（T1046）。目前為偵察階段，建議觀察其是否升級為服務攻擊。」（值為佔位。）

## 12. 建議處置方式
確認來源合法性；封鎖/限速可疑外部來源（依環境）；加強暴露服務的存取控制。

## 13. 誤判可能性
弱點掃描器、資產盤點工具、監控探針、負載平衡健康檢查都會產生類似流量。

## 14. 需要進一步確認的資料
是否採集網路層日誌、防火牆事件對應的 Wazuh 規則、掃描來源是否授權。

## 相關文件
[[scn-suspicious-external-connection]]、[[doc-network-topology]]、[[doc-detection-logic-overview]]

## 建議查證來源
Wazuh 官方文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
連接埠掃描、port scan、service discovery、偵察、T1046、T1595。
