---
id: doc-network-topology
title: "網路拓樸"
doc_type: architecture
category: architecture
summary: "內部網段包含 Windows 11 靶機、AD DC、Wazuh Manager；外部網段為授權實驗的攻擊者主機；兩者由路由器區隔。具體網段/IP 為部署相關，需依實際環境確認。"
tags: [cat:overview, type:architecture, status:env-specific]
related_entities: [ent-host-win11-target, ent-host-dc, ent-host-wazuh-manager, ent-host-router, ent-host-attacker]
related_docs: [doc-system-architecture, doc-host-roles, doc-host-inventory]
keywords: ["網路拓樸", "內部網段", "外部網段", "路由器", "網段隔離", "攻擊網段", "network topology", "segmentation"]
confidence: medium
verification_status: env-specific
source_refs: []
last_updated: 2026-07-09
---

# 網路拓樸

## 1. 文件目的
描述實驗網路的分段與隔離，界定「防禦內網」與「攻擊外網」的邊界。

## 2. 背景說明
邏輯拓樸（具體位址為佔位，**需依實際環境確認**）：

```
[ 外部/攻擊網段 <外部網段> ]
   └─ 攻擊者主機  <attacker-ip>   (僅授權實驗用)
            │
        [ 路由器 <router> ]  ← 負責內外網段區隔
            │
[ 內部網段 <內部網段> ]
   ├─ Windows 11 靶機  <win11-ip>   (加入 AD 網域 + Wazuh Agent)
   ├─ AD Domain Controller  <dc-ip>
   └─ Wazuh Server/Manager  <manager-ip>
```

- 攻擊者主機**僅**位於外部網段，經路由器才能觸及靶機——這條路徑是攻擊模擬與偵測的觀察面。
- 內部網段承載正常網域與監控流量。

> 網段 CIDR、各主機 IP、VLAN、路由/防火牆規則皆為部署相關，一律以實際環境為準。

## 3. 與本專題的關聯
拓樸決定了「哪些流量跨越邊界」，是 05-attack-scenarios 中連接埠掃描、外部連線等情境的前提。主機職責見 [[doc-host-roles]]，清單見 [[doc-host-inventory]]（⏳）。

## 4. 主要實體
Host（含 router、attacker）、IP（zone：internal/external/attacker）。

## 5. 可被 LLM 檢索的關鍵字
網路拓樸、網段、內網、外網、攻擊網段、路由器、隔離、segmentation、DMZ、topology。

## 6. 相關文件連結
- [[doc-system-architecture]]、[[doc-host-roles]]、[[doc-host-inventory]]

## 7. 後續可擴充內容
- 實際 IP/CIDR/VLAN 表（填入後把 verification_status 提升）。
- 防火牆與路由規則、網路模擬（如 FakeNet/INetSim）配置。
