---
id: doc-architecture-baseline-validation
title: "架構基線與驗證矩陣（2026-07-14）"
doc_type: architecture
category: architecture
summary: "依使用者架構圖建立七角色實驗室基線：DC、兩台 Windows 11、Wazuh all-in-one、OPNsense、AI Server、攻擊端；將 Agent、跨網段、MCP、RDP/WinRM 拆成可驗證的信任邊界，未確認值均標 env-specific。"
tags: [cat:overview, type:architecture, status:env-specific]
related_entities: [ent-host-win11-target, ent-host-dc, ent-host-wazuh-manager, ent-host-router, ent-host-attacker]
related_docs: [doc-system-architecture, doc-network-topology, doc-host-inventory, doc-data-and-event-flow, doc-rag-integration-spec]
mitre_attack: []
wazuh_sources: []
windows_event_ids: []
risk_level: ""
confidence: medium
verification_status: partial
source_refs: ["使用者提供架構圖（2026-07-14）", "Wazuh Architecture 官方文件", "Microsoft AD DS overview", "OPNsense Firewall/VPN 官方文件"]
keywords: ["架構基線", "驗證矩陣", "Wazuh", "OPNsense", "MCP", "AI Server", "RDP", "WinRM", "network segmentation"]
last_updated: 2026-07-14
---

# 架構基線與驗證矩陣（2026-07-14）

## 1. 文件目的

把目前的設計圖轉成可部署、可檢查、可回溯的實驗室基線。這不是已完成部署的宣告；沒有實機證據的值一律維持 `env-specific` 或 `needs-verification`。

## 2. 七角色設計基線

| 角色 | 圖中設定 | 架構定位 | 驗證狀態 |
|---|---|---|---|
| AD Domain Controller | Windows Server 2019；2 vCPU、4 GB RAM、64 GB SSD；AD DS/ADCS、RDP、SMB、NetBIOS | 網域身分與權限事件來源 | 需確認 VM、AD DS/ADCS、稽核與 Agent 狀態 |
| Windows 11 A | 2 vCPU、4 GB RAM、64 GB SSD | 一般受監控端點 | 需確認網域加入與 Agent |
| Windows 11 B | 同上；Administrators、Remote Desktop Users、Remote Management Users | RDP/WinRM 與本機群組變更測試端點 | 需確認群組成員、稽核與 Agent |
| Wazuh Server | 4 vCPU、8 GB RAM、200 GB SSD | 小型 lab 的 all-in-one 候選節點（Server/Indexer/Dashboard） | 需確認實際部署型式與版本 |
| OPNsense | 2 vCPU @ 1.5 GHz、8 GB RAM、120 GB SSD；firewall/IDS/VPN | 內外區與 AI 區的唯一分段控制點 | 需確認介面、規則、IDS/VPN 與日誌匯入 |
| AI Server | 圖示為經 MCP 與 Wazuh 連接 | 告警輔助分析與 RAG/AI 服務 | 需確認 MCP transport、認證、授權與 audit |
| attacker | 位於實驗外部區，經標示 RDP 路徑測試 | 僅限授權測試流量來源 | 需確認來源範圍、時間限制與還原程序 |

## 3. 信任邊界與最小連線

| 流量 | 方向 | 最小設計 | 證據 |
|---|---|---|---|
| Wazuh Agent | DC/Windows 11 → Wazuh | 僅允許已註冊 Agent 到 Manager；官方預設 TCP 1514，實機值可不同 | Agent active、接收事件、設定檔 |
| Agent enrollment | DC/Windows 11 → Wazuh | 僅在註冊期間允許；官方預設 TCP 1515 | 註冊紀錄與註冊後規則 |
| OPNsense logs | OPNsense → Wazuh | 啟用前先定義 Syslog/TLS、來源介面與保留政策 | 防火牆／IDS 事件可被關聯 |
| RDP 測試 | attacker → Windows 11 B | 只對授權來源、測試帳號與時段開放；完成後關閉 | OPNsense log + Windows/AD logon 事件 |
| WinRM 管理 | 管理者 → Windows 11 B | 不等同攻擊測試流量；限制在管理區與核准帳號 | 群組、規則、PowerShell/事件紀錄 |
| AI MCP | Wazuh/整合層 → AI Server | 只讀、最小欄位、強認證與可稽核；不假設固定連接埠 | connector 設定、權杖範圍、audit log |

> 圖中的 RDP 和 MCP 標籤描述的是設計意圖，不能直接推論規則已開放或服務已運作。

## 4. 建議部署順序

1. 建立 OPNsense 的區域與預設拒絕規則，先保存設定備份。
2. 建立 DC 與兩台 Windows 11，完成網域、最小測試帳號與安全稽核設定。
3. 部署 Wazuh all-in-one，依序註冊 DC、Windows 11 A、Windows 11 B，確認端點資料可見。
4. 導入 OPNsense firewall/IDS 日誌後，建立跨端點與邊界的關聯偵測。
5. 最後以只讀資料契約接上 AI Server/MCP，先驗證資料最小化與 audit，再開放任何自動化功能。

## 5. 驗證矩陣

| ID | 驗證 | 成功證據 | 現況 |
|---|---|---|---|
| A1 | 七角色與資源規格已被文件化 | 本頁、拓撲、主機清冊一致 | 已完成文件層驗證 |
| A2 | DC/兩台端點都有 Wazuh 遙測 | Dashboard 顯示 active + 可追溯測試事件 | 待實機驗證 |
| A3 | 跨區規則最小化 | OPNsense 規則、命中日誌、非允許流量被拒絕 | 待實機驗證 |
| A4 | RDP/WinRM 為受限測試面 | 來源/帳號/時段 allow-list 與事件證據 | 待實機驗證 |
| A5 | MCP 無過度權限 | 只讀工具白名單、最小資料、可查 audit | 待實機驗證 |

## 6. 與既有 KB 的關聯

- 三層資料流：[[doc-system-architecture]]、[[doc-data-and-event-flow]]
- 網段與主機：[[doc-network-topology]]、[[doc-host-inventory]]
- AI/RAG 資料契約：[[doc-rag-integration-spec]]
- 父層 H-I-V-R-K-C 實驗：`../../../wiki/experiments/wazuh-ad-soc-architecture-review.md`

## 7. 後續可擴充內容

- 填入實際 CIDR、IP、VLAN、主機名與 OPNsense 介面。
- 建立七張 Host entity 卡，讓告警中的 agent/host/IP 可一跳關聯。
- 保存 Wazuh、OPNsense、MCP 的去敏設定檔與 manifest，並以實機證據更新 A2–A5。
