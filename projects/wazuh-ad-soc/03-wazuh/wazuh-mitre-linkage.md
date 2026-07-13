---
id: doc-wazuh-mitre-linkage
title: "Wazuh 與 MITRE ATT&CK 的關聯"
doc_type: wazuh
category: wazuh
summary: "Wazuh 規則可帶 MITRE 對應，透過 rule.mitre.id / rule.mitre.tactic / rule.mitre.technique 呈現在告警中。AI 用這些欄位連到 technique 卡並產出 ATT&CK 對應；對應完整度依規則集，須以 MITRE 官方為準。"
tags: [cat:wazuh, type:wazuh, cat:mitre]
related_entities: [ent-technique, ent-rule]
related_docs: [doc-wazuh-rules-and-levels, doc-wazuh-field-to-ai-mapping, doc-mitre-mapping-overview]
keywords: ["Wazuh MITRE", "rule.mitre", "ATT&CK 對應", "technique", "tactic", "mitre linkage"]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "MITRE ATT&CK 官方網站"]
last_updated: 2026-07-09
---

# Wazuh 與 MITRE ATT&CK 的關聯

## 1. 這是什麼
部分 Wazuh 規則會標註對應的 MITRE ATT&CK 技術。命中這類規則時，alert 會帶：
- `rule.mitre.id`：technique id（如 `T1110`）。
- `rule.mitre.tactic`：戰術（如 Credential Access）。
- `rule.mitre.technique`：技術名稱（如 Brute Force）。

## 2. AI 如何使用
- 用 `rule.mitre.id` 連到 `07-mitre-attack/technique-cards/*` 的技術卡。
- 用 `rule.mitre.tactic` 做戰術分布圖、標記時間軸的攻擊階段。
- 在報告中把技術清單可讀化。

## 3. 重要限制（防幻覺）
- **對應完整度取決於規則集**：不是每條規則都有 MITRE 標註；「沒有 mitre 欄位」不代表「與 ATT&CK 無關」。
- AI **不得自行臆造** technique id；若 alert 未帶 `rule.mitre.*`，可依行為「建議可能對應的技術」但須標「需查 MITRE 官方確認」。
- 技術 id 與戰術名以 **MITRE ATT&CK 官方**為準。

## 4. 需依實際環境確認
規則集的 MITRE 覆蓋範圍、各規則的對應正確性。

## 5. 本專題常見對應（穩定值，仍以官方為準）
暴力破解 T1110、PowerShell T1059.001、有效帳號 T1078、建立帳號 T1136、帳號操作 T1098、RDP T1021.001、網路服務探索 T1046、削弱防禦 T1562、入口工具傳輸 T1105。逐一見 [[doc-mitre-mapping-overview]]（⏳批 5）與各 technique 卡。

## 相關文件
[[doc-wazuh-rules-and-levels]]、[[doc-wazuh-field-to-ai-mapping]]、[[doc-mitre-mapping-overview]]；跨連父層 [[ioc-ttp-and-detection-engineering]]。

## 建議查證來源
Wazuh 官方文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
Wazuh MITRE、rule.mitre、ATT&CK 對應、technique、tactic、mitre linkage。
