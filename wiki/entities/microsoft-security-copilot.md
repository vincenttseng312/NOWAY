---
type: entity
title: "Microsoft Security Copilot"
tags: [ai-security, security-tools, soc]
sources: [ai-security-tools-research-2026-07-16]
created: 2026-07-16
updated: 2026-07-16
---

# Microsoft Security Copilot

Microsoft Security Copilot 是面向企業安全與 IT 團隊的生成式 AI 服務，可在獨立介面或 Microsoft Defender XDR、Sentinel、Intune、Entra 等產品的嵌入式體驗中使用。它以已授權的組織資料、外掛與威脅情報輔助調查、KQL、惡意腳本理解、風險管理與報告。

## 使用方式

先在商業雲 tenant 中完成 Security Copilot 的 onboarding、角色與資料來源權限設定；再從獨立體驗或整合產品中，以明確的事件、警報或查詢範圍提出問題。把回覆視為分析草稿，回查 Sentinel/Defender 原始事件、KQL 結果與資產資訊後才採取處置。擴充外掛或 agent 前，需先完成資料存取與最小權限審查。

## 優點

- 原生連接 Microsoft 安全產品，可將事件調查、KQL、腳本分析與報告放進既有 SOC 工作流。
- 對專題報告中常見的「事件摘要、受影響資產、建議處置」有直接對應能力。
- 支援 agent 擴充與第三方整合，適合已有 Microsoft Security 資產的組織。

## 限制與風險

- 價格、授權、tenant 條件與資料可用性受 Microsoft 商業雲與既有產品部署影響。
- 沒有良好的資料權限、事件品質與人工覆核時，AI 摘要不會自動變得可靠。
- 對目前以 Wazuh 為核心的 lab 並非即插即用；沒有 Sentinel/Defender/Entra 整合時，其優勢難以完全發揮。

## 對專題的定位

作為「企業 Microsoft SOC 的參考架構」比作為本期 lab 的基線更合適。現階段先落實 [[ai-analysis-pipeline]] 的可追溯原則；日後若接入 Sentinel 或 Defender，再比較其與自建 RAG 助理的成本、資料邊界與準確性。

## 關聯

- 來源：[[ai-security-tools-research-2026-07-16]]
- 選型：[[ai-security-tool-selection]]
- 專題流程：[[ai-analysis-pipeline]]
