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

## 運作原理與適用情境

HexStrike AI 的核心不是單一掃描器，而是 MCP server 將 AI client、決策/agent 層與多種外部安全工具串接。資料與控制流因此是：使用者/模型提示 → MCP server → 工具選擇與參數 → 外部工具執行 → 結果回傳模型。每個箭頭都可能成為 prompt injection、scope 擴張、敏感資料回流或不當工具呼叫的控制點。

它適合研究「MCP agent 如何被 allowlist、審計和停止」的隔離實驗；不適合讓聊天機器人直接控制正式網路、AD、Wazuh 或任何未授權資產。README 的工具與 agent 數量是維護者聲明，不是安全保證或成效基準。

## Windows 安裝前檢查

官方 README 列出 Python virtual environment、相依套件與 MCP client 整合，但本機沒有可用 Python，且未驗證其外部工具鏈。以下只檢查本機能力，不會安裝套件或啟動 server：

```powershell
python --version
git --version
Get-Command docker -ErrorAction SilentlyContinue
```

若 Python 不存在，先不要以系統管理員權限隨意安裝大量滲透測試工具。應先準備 disposable VM、網路 egress 規則、資產 allowlist、可回復快照與測試授權，再依官方 README 在隔離環境完成安裝。

## 最小安全治理流程

1. 將 MCP server 和被測 lab 放在獨立網段，不允許到公司網路或個人資料。
2. MCP client 只連到自建、受控 server；工具選擇、目標與頻率以 allowlist 限制。
3. 所有 tool call 要有可稽核 log，且提供人工中止開關；機密不能回傳到模型 context。
4. 用 [[garak]] 針對 tool description、外部文件與使用者提示做 injection/不當工具使用測試。
5. 測試後刪除短期 token、還原 lab snapshot，審查 egress 與工具執行紀錄。

## 常見錯誤與排解

| 現象 | 原因 | 處理方式 |
|---|---|---|
| MCP client 無法連線 | 設定檔、Python runtime 或 transport 不一致 | 先看官方 README 的相容 client/版本，不要猜測 JSON 欄位。 |
| agent 選到不允許的工具 | 沒有 policy/allowlist，或模型把不可信文字當指令 | 預設拒絕、建立顯式 allowlist，並保存 tool call 證據。 |
| 依賴安裝失敗 | 工具鏈複雜、OS/套件版本不同 | 在 disposable VM 逐項記錄，避免污染日常工作站。 |

## 最佳實務與延伸閱讀

- 將 HexStrike 視為 MCP 安全研究對象，不是本專題的 production component。
- 不將資料庫、AD、Wazuh manager 或 API key 掛給 agent；最小權限和網路隔離優先於 prompt 限制。
- 以 [[lakera-guard]] 或同類 runtime guardrail 審查輸入/輸出，但不把它視為唯一防線。
- 官方資料：[HexStrike AI repository](https://github.com/0x4m4/hexstrike-ai)。

## 關聯

- 來源：[[ai-security-tools-research-2026-07-16]]
- 選型：[[ai-security-tool-selection]]
- 相近工具：[[pentestgpt]]、[[burpgpt]]
