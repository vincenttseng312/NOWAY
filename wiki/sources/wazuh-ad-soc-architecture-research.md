---
type: source
title: "Wazuh × AD × AI SOC 架構官方文件研究"
tags: [wazuh, active-directory, opnsense, network-segmentation, methodology]
sources: [raw/wazuh-ad-soc-architecture-research-2026-07-14.md]
raw: raw/wazuh-ad-soc-architecture-research-2026-07-14.md
ingested: 2026-07-14
created: 2026-07-14
updated: 2026-07-14
---

# Wazuh × AD × AI SOC 架構官方文件研究

本研究以 Wazuh、Microsoft 與 OPNsense 官方文件校正架構圖的可驗證部分。Wazuh 的小型實驗室可採 all-in-one 部署；Agent 對 Server 的預設資料通道是 TCP 1514，註冊服務預設為 TCP 1515。AD DS 是目錄物件、驗證與存取控制的核心，因此 DC 必須是監控優先對象。OPNsense 可承擔分段、防火牆與 VPN 控制，但圖中 IDS／VPN 是否啟用仍屬環境事實。

## 對架構的限制

- Wazuh Agent、Syslog 與 AI MCP 是三種不同信任關係，不能混成一條「資料流」。
- AI 整合的傳輸協定與認證並非由 Wazuh 架構文件或圖片指定；應先定義只讀查詢範圍、資料遮罩與稽核。
- 產品預設連接埠僅作規則設計與驗證清單的起點；實機可配置不同值。

## 關聯

- 使用者架構圖：[[wazuh-ad-soc-architecture-diagram]]
- 核心概念：[[soc-lab-segmentation-and-telemetry]]
- 實驗紀錄：[[wazuh-ad-soc-architecture-review]]
