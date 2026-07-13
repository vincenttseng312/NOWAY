---
id: doc-host-roles
title: "主機角色說明"
doc_type: architecture
category: architecture
summary: "本專題五類主機的職責：Windows 11 靶機（受監控/被攻擊）、AD DC（網域認證）、Wazuh Manager（告警）、路由器（隔離）、攻擊者主機（授權模擬）。"
tags: [cat:overview, type:architecture, entity:host]
related_entities: [ent-host-win11-target, ent-host-dc, ent-host-wazuh-manager, ent-host-router, ent-host-attacker]
related_docs: [doc-network-topology, doc-host-inventory, doc-ad-environment, doc-windows11-target]
keywords: ["主機角色", "靶機", "Domain Controller", "Wazuh Manager", "路由器", "攻擊者主機", "host roles"]
confidence: high
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "Microsoft Windows Security Auditing 文件"]
last_updated: 2026-07-09
---

# 主機角色說明

## 1. 文件目的
逐台說明主機在專題中的職責與監控/威脅意義，作為 entity host 卡的來源。

## 2. 背景說明

| 主機 | 網段 | 角色 | 監控/威脅意義 |
|---|---|---|---|
| Windows 11 靶機 | 內部 | 受監控端點、被攻擊目標；加入 AD 網域、裝 Wazuh Agent | 大多數 Windows/AD 事件的來源；攻擊落點 |
| AD Domain Controller | 內部 | 網域認證與目錄服務 | 帳號登入、群組異動等 AD 安全事件來源 |
| Wazuh Server/Manager | 內部 | 接收 Agent 資料、解碼比對規則、產生告警 | 告警與 MITRE 對應的產生點，見 [[doc-wazuh-role]] |
| 路由器 | 內/外之間 | 區隔內部與攻擊網段 | 跨界流量的觀察點 |
| 攻擊者主機 | 外部 | 授權實驗中的攻擊模擬來源 | 外部可疑來源 IP 的來源 |

> 各主機的主機名、IP、OS 版本、Wazuh Agent ID 皆為部署相關（需依實際環境確認），填入 `entities/ent-host-*` 卡。

## 3. 與本專題的關聯
主機是最主要的實體維度（儀表板 Top 被攻擊主機、問答的主機解析）。拓樸見 [[doc-network-topology]]；AD 細節見 [[doc-ad-environment]]（⏳）；靶機細節見 [[doc-windows11-target]]（⏳）。

## 4. 主要實體
Host ×5，對應 `entities/ent-host-*`。

## 5. 可被 LLM 檢索的關鍵字
主機角色、靶機、DC、Domain Controller、Wazuh Manager、路由器、攻擊者主機、endpoint、host inventory。

## 6. 相關文件連結
- [[doc-network-topology]]、[[doc-host-inventory]]、[[doc-ad-environment]]、[[doc-windows11-target]]

## 7. 後續可擴充內容
- 每台主機的 entity 卡（含 env-specific 屬性）。
- 主機基準（正常程序/服務）以利異常判讀，可跨連父層 [[dynamic-behavior-analysis]]。
