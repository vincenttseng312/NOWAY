---
type: entity
title: "HexStrike AI"
tags: [ai-security, pentesting, mcp, security-tools]
sources: [ai-security-tools-research-2026-07-16]
created: 2026-07-16
updated: 2026-07-16
---

# HexStrike AI

HexStrike AI 是以 MCP 將 AI client 與多種安全工具相連的開源自動化框架。專案 README 宣稱 v6.0 可協調 150+ 安全工具及 12+ agent，涵蓋工具選擇、測試流程、自適應與報告；這些是維護者功能聲明，不是獨立驗證的效能保證。

## 使用方式

只在獨立、可回復且具明確書面授權的測試環境部署。依官方 README 建立隔離 Python 環境、安裝相依套件，並將 MCP server 接到已受控的 MCP client。開始前要把允許的目標、工具、頻率、帳號權限與人工作業核准寫成 allowlist；每一次 agent 要執行外部工具前，都應能被記錄、檢視與停止。

## 優點

- 對熟悉 MCP 的研究者，可把多個安全工具的啟動與結果彙整放入一致介面。
- 有多 agent、決策與報告概念，可用來研究 AI agent 的工具治理問題。
- 開源且支援多種 MCP client，實驗彈性高。

## 限制與風險

- 將 LLM 直接接上大量攻擊工具，風險遠高於單一掃描器：prompt injection、scope 擴張、錯誤參數、流量衝擊與未授權存取都可能被放大。
- 需要自行維護大量外部工具、依賴與 API，環境複雜度高。
- 不可把 README 的工具數量或 agent 名稱誤認為已驗證的漏洞發現率。

## 對專題的定位

目前不建議接到 Wazuh、AD 或專題 AI 助理。它可在日後作為「AI agent 工具治理」的隔離研究對象，並以 [[garak]] 與 guardrail 控制來測試其 MCP 風險。

## 關聯

- 來源：[[ai-security-tools-research-2026-07-16]]
- 選型：[[ai-security-tool-selection]]
- 相近工具：[[pentestgpt]]、[[burpgpt]]
