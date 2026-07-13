---
id: scn-security-tool-disable
title: "安全防護遭停用偵測"
doc_type: attack-scenario
category: attack-scenario
summary: "偵測防毒/防護、稽核或 Agent 被停用等削弱偵測的行為。清除稽核日誌（1102）尤其可疑。此類動作常是攻擊者掩護後續行為的前置步驟。"
tags: [cat:attack-scenario, mitre-tactic:defense-evasion, source:windows-security, risk:high]
related_entities: [ent-host-win11-target]
related_docs: [evt-security-config-change, scn-firewall-modification]
mitre_attack: [t1562-001]
wazuh_sources: []
windows_event_ids: ["1102", "4719"]
risk_level: high
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: ["停用防護", "disable security tools", "清除日誌", "1102", "defense evasion", "T1562.001"]
last_updated: 2026-07-09
---

# 安全防護遭停用偵測

## 1. 情境說明
偵測安全防護、稽核或監控被停用/破壞。事件面見 [[evt-security-config-change]]；本頁聚焦攻擊意圖。不含停用防護的操作步驟。

## 2. 攻擊者可能目標
降低被偵測與阻擋的機率，並破壞後續調查所需的證據。

## 3. 防禦方可觀測跡象
防毒/防護狀態改變、稽核政策被關（4719）、稽核日誌被清（1102）、Wazuh Agent 停止回報（心跳中斷）。

## 4. 可能出現的 Windows / AD 事件
1102（清除稽核日誌，高可疑）、4719（稽核政策變更）；防護軟體相關事件可能落在其他通道（需確認）。見 [[evt-security-config-change]]。

## 5. 可能出現的 Wazuh 告警欄位
`eventID=1102/4719`、操作者、`agent.name`；**Agent 失聯本身**也是訊號（Wazuh 端可監測 agent 斷線，依環境）。

## 6. MITRE ATT&CK 對應
T1562.001 Impair Defenses: Disable or Modify Tools；日誌清除亦關聯 T1070 Indicator Removal。以官方為準。

## 7. 風險等級判斷
high；1102 清日誌或多項防護同時被關為 critical（證據完整性受威脅）。

## 8. AI 分析重點
被停用的防護類型、操作者、時間點（是否緊接可疑登入/程序）、是否批次削弱、Agent 是否同時失聯。

## 9. 儀表板呈現方式
防護狀態時間線、日誌清除獨立醒目告警、Agent 心跳監控。

## 10. 使用者可能詢問的問題
「有沒有防護被關掉？」「稽核日誌被清過嗎？」

## 11. AI 回答範例
「<時間> 偵測到稽核日誌被清除（1102）於 <主機>，操作者 <subject>；此為 Defense Evasion 高可疑訊號（T1562.001/T1070），且影響證據完整性。建議立即調查並改用其他來源日誌回溯。」（值為佔位。）

## 12. 建議處置方式
還原防護、保全其他來源日誌、隔離主機、擴大調查（防護關閉期間可能有未記錄行為）。

## 13. 誤判可能性
IT 維運暫停防護、防護軟體升級/重裝、測試（應有變更紀錄）。

## 14. 需要進一步確認的資料
防護軟體事件對應通道與 Event ID、變更授權性、Agent 失聯原因。

## 相關文件
[[evt-security-config-change]]、[[scn-firewall-modification]]；跨連父層 [[ioc-ttp-and-detection-engineering]]。

## 建議查證來源
Microsoft Windows Security Auditing 文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
停用防護、disable security tools、清除日誌、1102、defense evasion、T1562.001。
