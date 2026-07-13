---
id: doc-mitre-mapping-overview
title: "MITRE ATT&CK 對應總覽"
doc_type: mitre
category: mitre
summary: "彙整本專題 14 個攻擊情境對應的 MITRE ATT&CK 戰術與技術，作為 rule.mitre.* 欄位與 technique 卡之間的樞紐。技術 id 為業界穩定值，仍以 MITRE 官方為準。"
tags: [cat:mitre, type:mitre]
related_entities: [ent-technique]
related_docs: [doc-wazuh-mitre-linkage, doc-detection-logic-overview]
mitre_attack: [t1046, t1110, t1021, t1078, t1059-001, t1136, t1098, t1562, t1070, t1548, t1204, t1105, t1071, t1570]
wazuh_sources: []
windows_event_ids: []
risk_level: ""
confidence: medium
verification_status: needs-verification
source_refs: ["MITRE ATT&CK 官方網站"]
keywords: ["MITRE ATT&CK", "對應總覽", "tactic", "technique", "attack mapping"]
last_updated: 2026-07-09
---

# MITRE ATT&CK 對應總覽

本頁是「情境 ↔ 戰術 ↔ 技術」的樞紐。Wazuh 的 `rule.mitre.*` 欄位（見 [[doc-wazuh-mitre-linkage]]）落在此表，AI 用它連到 technique 卡。**技術 id 以 MITRE 官方為準；broad 類（如提權）不臆造單一 id。**

## 對應表

| 戰術 Tactic | 技術（id） | 本專題情境 |
|---|---|---|
| Reconnaissance / Discovery | Active Scanning T1595 / Network Service Discovery [[t1046]] | [[scn-port-scan]] |
| Credential Access | Brute Force [[t1110]] | [[scn-rdp-bruteforce]]、[[scn-mass-logon-failure]]、[[scn-failed-then-success-logon]] |
| Initial Access / Persistence / Priv-Esc | Valid Accounts [[t1078]] | [[scn-ad-abnormal-logon]]、[[scn-failed-then-success-logon]] |
| Execution | PowerShell [[t1059-001]] / User Execution [[t1204]] | [[scn-suspicious-powershell]]、[[scn-malicious-file-execution]] |
| Persistence | Create Account [[t1136]] | [[scn-local-user-creation]] |
| Priv-Esc / Persistence | Account Manipulation [[t1098]] / Abuse Elevation [[t1548]] | [[scn-add-to-administrators]]、[[scn-privilege-escalation-signs]] |
| Defense Evasion | Impair Defenses [[t1562]] / Indicator Removal [[t1070]] | [[scn-firewall-modification]]、[[scn-security-tool-disable]] |
| Lateral Movement | Remote Services [[t1021]] / Lateral Tool Transfer [[t1570]] | [[scn-lateral-movement-signs]] |
| Command and Control | Application Layer Protocol [[t1071]] | [[scn-suspicious-external-connection]] |
| （前置） | Ingress Tool Transfer [[t1105]] | [[scn-malicious-file-execution]] |

## 使用方式
- **告警→技術**：AI 讀 `rule.mitre.id` → 對到上表 → 開 technique 卡 → 補偵測/處置脈絡。
- **無 mitre 欄位時**：依行為在上表找候選技術，但標「需查 MITRE 官方確認」，不硬套。
- **報告**：MITRE Mapping 章節用本表 + 實際命中的技術。

## 相關文件
[[doc-wazuh-mitre-linkage]]、[[doc-detection-logic-overview]]、technique-cards/*；跨連父層 [[ioc-ttp-and-detection-engineering]]。

## 建議查證來源
MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
MITRE ATT&CK、對應總覽、tactic、technique、attack mapping。
