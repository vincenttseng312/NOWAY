---
id: doc-host-inventory
title: "主機清單"
doc_type: environment
category: environment
summary: "本專題七個設計角色的清單與屬性欄位（角色、網段、OS、是否納管）。具體主機名/IP/版本為部署相關；最新架構圖提供資源基線，但實際值仍需填入 entity 卡並驗證。"
tags: [cat:environment, type:environment, entity:host, status:env-specific]
related_entities: [ent-host-win11-target, ent-host-dc, ent-host-wazuh-manager, ent-host-router, ent-host-attacker]
related_docs: [doc-host-roles, doc-network-topology, doc-ad-environment, doc-adcs-environment, doc-windows11-target]
mitre_attack: []
wazuh_sources: []
windows_event_ids: []
risk_level: ""
confidence: medium
verification_status: env-specific
source_refs: []
keywords: ["主機清單", "host inventory", "資產清單", "主機屬性"]
last_updated: 2026-07-15
---

# 主機清單

本專題七個設計角色的清單與屬性欄位。**具體主機名/IP/版本為部署相關（env-specific）**；2026-07-14 的架構圖提供資源與用途基線，但主機名、IP、版本、Agent ID 與實際設定仍須填入各 `entities/ent-host-*` 實體卡。角色說明見 [[doc-host-roles]]，拓樸見 [[doc-network-topology]]，驗收條件見 [[doc-architecture-baseline-validation]]。

## 主機清單（設計基線）

| 主機 | 角色 | 圖中資源基線 | 網段 | 納 Wazuh 管理 | entity 卡 |
|---|---|---|---|---|---|
| Windows 11 A | 一般受監控端點 | 2 vCPU / 4 GB RAM / 64 GB SSD | 內部 | 應納管，待驗證 | `ent-host-win11-target-a` |
| Windows 11 B | RDP/WinRM 與本機群組測試端點 | 2 vCPU / 4 GB RAM / 64 GB SSD | 內部 | 應納管，待驗證 | `ent-host-win11-target-b` |
| AD Domain Controller | 網域認證／目錄／ADCS | Windows Server 2019；2 vCPU / 8 GB RAM / 64 GB SSD | 內部 | 應納管，待驗證 | `ent-host-dc` |
| Wazuh Server | all-in-one 候選：Server/Indexer/Dashboard | 4 vCPU / 8 GB RAM / 200 GB SSD | 內部或管理區 | N/A（中央元件） | `ent-host-wazuh-manager` |
| OPNsense | 內外區分段、firewall/IDS/VPN | 2 vCPU @ 1.5 GHz / 8 GB RAM / 120 GB SSD | 邊界 | agentless log source，待驗證 | `ent-host-opnsense` |
| AI Server | MCP/RAG/告警分析服務 | 未標註 | AI/管理區 | 不以 Agent 為前提，待驗證 | `ent-host-ai-server` |
| attacker | 授權攻擊模擬 | 未標註 | 外部測試區 | 否 | `ent-host-attacker` |

> `<...>` 為佔位，一律以實際環境為準。DC 是否安裝 Agent 直接影響能否收到 AD 事件（見 [[doc-ad-environment]]）。

## 每台的最小屬性（填入 entity 卡）
依 `_meta/entity-model.md` 的 Host 欄位：`hostname`、`ip`、`role`、`os`、`ad_joined`、`wazuh_agent_id`（env-specific）。對於 AD CS／Wazuh／OPNsense／AI 等主機，另補 FQDN、zone/VLAN、OS build、採集 channel、audit policy、DNS/AD/log 相依與 status；完整欄位與版本基線見 [[doc-adcs-environment]]。

## 主要實體
Host ×7（對應上表 entity 卡：Win11 A/B、DC、Wazuh、OPNsense、AI Server、attacker）。

## 可被 LLM 檢索的關鍵字
主機清單、host inventory、資產清單、主機屬性、Wazuh agent 納管。

## 相關文件連結
[[doc-host-roles]]、[[doc-network-topology]]、[[doc-ad-environment]]、[[doc-adcs-environment]]、[[doc-windows11-target]]

## 後續可擴充內容
建立 `entities/ent-host-*` 七張實體卡並填入實際值（接上真實環境後最有意義）；補各主機基準（正常程序/服務）以利異常判讀。
