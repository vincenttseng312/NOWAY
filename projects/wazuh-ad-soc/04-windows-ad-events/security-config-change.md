---
id: evt-security-config-change
title: "防火牆或安全設定變更事件"
doc_type: event
category: windows-ad-event
summary: "關閉防火牆、停用防護、清除稽核日誌等安全設定變更常是攻擊者削弱防禦（Defense Evasion）的跡象。稽核政策變更 4719、日誌清除 1102 較穩定；Windows 防火牆變更的具體 Event ID 需依 Microsoft 官方文件確認。"
tags: [cat:event, type:event, source:windows-security, mitre-technique:t1562]
event_source: security
windows_event_ids: ["4719", "1102", "防火牆變更 ID (需確認)", "5025 (需確認)"]
wazuh_sources: []
related_entities: [ent-host-win11-target]
related_docs: [scn-firewall-modification, scn-security-tool-disable]
risk_level: high
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件"]
keywords: ["防火牆變更", "安全設定", "停用防護", "1102", "4719", "defense evasion", "T1562"]
last_updated: 2026-07-09
---

# 防火牆或安全設定變更事件

## 1. 事件用途
偵測防禦機制被削弱：防火牆規則/服務變更、安全防護停用、稽核政策變更、稽核日誌清除。

## 2. 可能代表的安全意義
對映 MITRE **T1562 Impair Defenses**。攻擊者在取得存取後常先削弱防禦以降低被偵測機率。**清除稽核日誌（1102）尤其可疑**（幾乎沒有正當的日常理由）。

## 3. 可能涉及的 Windows Event ID
| Event ID | 意義 | 驗證 |
|---|---|---|
| 1102 | 稽核日誌被清除 | 以 Microsoft 官方為準（高可疑） |
| 4719 | 系統稽核政策變更 | 以 Microsoft 官方為準 |
| 防火牆規則新增/修改/刪除 | Windows Filtering Platform / 防火牆相關 | **需依 Microsoft 官方文件確認（如 4946/4947/4948/4950 系列）** |
| 5025 | 防火牆服務停止 | **需依 Microsoft 官方文件確認** |

> 防火牆與防護停用的精確 Event ID 因來源（Windows Firewall、WFP、Defender）而異，本頁一律標「需確認」，不記死數字。Defender 相關事件可能落在其他日誌通道（需確認）。

## 4. 在 Wazuh Alert 中可能出現的欄位
`eventID`、`data.win.system.providerName`、變更內容/操作者欄位（若擷取）、`full_log`（兜底）。

## 5. AI 分析時應注意的欄位
變更類型、操作者、時間點（是否緊接可疑登入/程序）、是否為批次削弱（多項防護同時被關）。

## 6. 儀表板可以如何視覺化
安全設定變更告警卡（高優先）、防護狀態時間線、日誌清除獨立醒目告警。

## 7. 使用者可能會問的問題
「有沒有人關掉防火牆/防護？」「稽核日誌被清除過嗎？」

## 8. AI 回答範例
「<時間> 偵測到稽核日誌被清除（1102），操作者 <subject>，主機 <host>。此為 Defense Evasion 高可疑訊號（T1562），且會影響後續調查的證據完整性，建議立即調查並保全其他來源日誌。」（值為佔位。）

## 9. 誤判情境
IT 正常的政策調整、安全軟體升級/重裝、維運期間暫時停用防護（應有變更紀錄）。

## 10. 處置建議
確認變更授權；未授權則還原防護、保全日誌、隔離主機、擴大調查（防護被關期間可能有未記錄行為）。

## 相關文件
[[scn-firewall-modification]]、[[scn-security-tool-disable]]；跨連父層 [[ioc-ttp-and-detection-engineering]]。

## 建議查證來源
Microsoft Windows Security Auditing 文件。

## 可被檢索的關鍵字（中英）
防火牆變更、安全設定、停用防護、1102、4719、defense evasion、T1562。
