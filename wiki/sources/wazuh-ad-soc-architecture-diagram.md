---
type: source
title: "Wazuh × AD × AI SOC 專題架構圖"
tags: [wazuh, active-directory, opnsense, mcp, network-segmentation]
sources: [raw/wazuh-ad-soc-architecture-diagram-2026-07-14.md]
raw: raw/wazuh-ad-soc-architecture-diagram-2026-07-14.md
ingested: 2026-07-14
created: 2026-07-14
updated: 2026-07-14
---

# Wazuh × AD × AI SOC 專題架構圖

這份使用者提供的設計圖把專題具體化為 AD／Windows 端點、Wazuh、OPNsense、AI Server 與授權攻擊端。監控區包含 Windows Server 2019 DC、兩台 Windows 11 與 Wazuh；OPNsense 擔任 firewall、IDS、VPN 與網段邊界；AI Server 以標示為 MCP 的介面取得 Wazuh 資料；攻擊端以 RDP 路徑作授權情境測試。

## 可直接採用的設計結論

- DC 是 AD 驗證與權限事件來源，應納入遙測與保護範圍。
- 兩台 Windows 11 應分別紀錄用途；其中一台明確承載本機 Administrators、RDP 與 WinRM 群組測試。
- Wazuh 的 4 vCPU／8 GB RAM／200 GB SSD 是本實驗室 all-in-one 節點的資源設計值，非效能驗證結果。
- OPNsense 是唯一應跨越區域的控制點；各通訊要落到明確的 allow-list 規則。

## 不可由圖片斷言的事項

圖中沒有 IP/CIDR/VLAN、Wazuh Agent 狀態、防火牆規則、MCP 服務定義、RDP／WinRM 開放範圍或憑證設定。這些均標記為 `env-specific`，需在實機驗證後才能作為事實使用。

## 關聯

- 架構研究：[[wazuh-ad-soc-architecture-research]]
- 概念整理：[[soc-lab-segmentation-and-telemetry]]
- H-I-V-R-K-C：[[wazuh-ad-soc-architecture-review]]
