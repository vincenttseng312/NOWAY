---
type: source
title: "AI Security Tools: Official Documentation Research Batch (2026-07-16)"
authors: ["OpenAI Codex research synthesis"]
tags: [ai-security, llm-security, pentesting, appsec, sast, guardrails, mcp]
raw: raw/ai-security-tools-research-2026-07-16.md
ingested: 2026-07-16
created: 2026-07-16
updated: 2026-07-16
entities: [pentestgpt, burpgpt, microsoft-security-copilot, deepcode-ai, hexstrike-ai, garak, lakera-guard]
concepts: [ai-security-tool-selection]
---

# AI 資安工具官方文件研究批次

這批工具不能只用「AI 資安工具」統稱。PentestGPT、BurpGPT 與 HexStrike AI 協助已授權的攻擊面測試；Microsoft Security Copilot 支援 Microsoft 生態的 SOC 調查；DeepCode AI 是 Snyk Code 的 AppSec 分析技術；garak 針對 LLM 或 LLM 應用做紅隊評估；Lakera Guard 則是在執行期篩檢 AI 互動的防護 API。

## 重要現況與邊界

- PentestGPT 的 2024 論文原型與目前 GitHub 的 v1.0 agentic framework 有演進差異。採用時應以當前 README 的依賴與安全限制為準，不把論文實驗結果直接延伸為現代模型的效能保證。
- BurpGPT 有 Community 與 Pro 的產品世代差異。Community repository 已由維護者標明停維護且不再可用；學習或選型應使用 Pro 文件確認當前能力，不能依舊版安裝說明做決策。
- BurpGPT Pro 目前文件列出 Burp Suite Professional 2025.6.5+、Java 21+ 與授權交付 JAR；部署時先審查 HTTP 流量是否可交給所選模型供應商。
- DeepCode AI 是 Snyk 平台的技術與品牌名稱；實際導入介面是 Snyk Code 的 IDE、SCM、CLI、CI/CD 或 API，而非另找一個名為「DeepCode AI」的獨立工具。
- Security Copilot 的 onboarding 取決於 E5 included 狀態或 SCU 佈建，且 Copilot role 不會取代 Defender/Sentinel 等後端資料權限。
- HexStrike AI 將 LLM 與大量安全工具透過 MCP 連結，便利性也提高未授權動作、指令注入、錯誤 scope 與資源耗盡的風險。它不適合直接接上本專題的日常 SOC 或 AI 助理。
- garak 與 Lakera Guard 處理的是 AI 系統安全，而不是 Windows/AD/Wazuh 的傳統端點偵測；前者偏部署前或迭代測試，後者偏執行期防護，兩者可互補。

## 對 Wazuh × AD × AI 專題的意義

目前專題應先完成 Wazuh 告警的欄位品質、關聯規則與人工可判讀的事件流程。接著以 garak 針對自己的 RAG/AI 助理做受控紅隊測試，並在 AI 助理將內容回傳使用者前，以 Lakera Guard 或同類 guardrail 加入輸入、輸出與 RAG 文件防護。Security Copilot 只在專題未來接入 Microsoft Sentinel、Defender 或 Entra 資料後才值得進行正式評估。

## 關聯

- 工具實體：[[pentestgpt]]、[[burpgpt]]、[[microsoft-security-copilot]]、[[deepcode-ai]]、[[hexstrike-ai]]、[[garak]]、[[lakera-guard]]
- 選型比較：[[ai-security-tool-selection]]
- 既有專題流程：[[ai-analysis-pipeline]]、[[rag-integration-spec]]、[[system-prompt]]
