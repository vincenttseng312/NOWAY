---
id: doc-host-inventory
title: "主機清單"
doc_type: environment
category: environment
summary: "本專題五台主機的清單與屬性欄位（角色、網段、OS、是否納管）。具體主機名/IP/版本為部署相關，此處給結構與佔位，實際值填入各 entities/ent-host-* 卡。"
tags: [cat:environment, type:environment, entity:host, status:env-specific]
related_entities: [ent-host-win11-target, ent-host-dc, ent-host-wazuh-manager, ent-host-router, ent-host-attacker]
related_docs: [doc-host-roles, doc-network-topology, doc-ad-environment, doc-windows11-target]
mitre_attack: []
wazuh_sources: []
windows_event_ids: []
risk_level: ""
confidence: medium
verification_status: env-specific
source_refs: []
keywords: ["主機清單", "host inventory", "資產清單", "主機屬性"]
last_updated: 2026-07-09
---

# 主機清單

本專題五台主機的清單與屬性欄位。**具體主機名/IP/版本為部署相關（env-specific），此處為結構與佔位；實際值填入各 `entities/ent-host-*` 實體卡**（實體卡待建，見 index 狀態說明）。角色說明見 [[doc-host-roles]]，拓樸見 [[doc-network-topology]]。

## 主機清單（屬性結構）

| 主機 | 角色 | 網段 | OS | 納 Wazuh 管理 | entity 卡 |
|---|---|---|---|---|---|
| Windows 11 靶機 | 受監控端點/攻擊目標 | 內部 | Windows 11 `<build>` | 是（Agent） | `ent-host-win11-target` |
| AD Domain Controller | 網域認證/目錄 | 內部 | Windows Server `<ver>` | `<是/否，需確認>` | `ent-host-dc` |
| Wazuh Server/Manager | 告警產生 | 內部 | `<Linux 發行版>` | N/A（本身即 Manager） | `ent-host-wazuh-manager` |
| 路由器 | 內外網段區隔 | 內/外之間 | `<裝置/OS>` | `<否，通常>` | `ent-host-router` |
| 攻擊者主機 | 授權攻擊模擬 | 外部 | `<OS>` | 否 | `ent-host-attacker` |

> `<...>` 為佔位，一律以實際環境為準。DC 是否安裝 Agent 直接影響能否收到 AD 事件（見 [[doc-ad-environment]]）。

## 每台的最小屬性（填入 entity 卡）
依 `_meta/entity-model.md` 的 Host 欄位：`hostname`、`ip`、`role`、`os`、`ad_joined`、`wazuh_agent_id`（env-specific）。

## 主要實體
Host ×5（對應上表 entity 卡）。

## 可被 LLM 檢索的關鍵字
主機清單、host inventory、資產清單、主機屬性、Wazuh agent 納管。

## 相關文件連結
[[doc-host-roles]]、[[doc-network-topology]]、[[doc-ad-environment]]、[[doc-windows11-target]]

## 後續可擴充內容
建立 `entities/ent-host-*` 五張實體卡並填入實際值（接上真實環境後最有意義）；補各主機基準（正常程序/服務）以利異常判讀。
