---
type: concept
title: "AI 資安工具選型與專題整合邊界"
tags: [ai-security, llm-security, pentesting, appsec, guardrails]
sources: [ai-security-tools-research-2026-07-16]
created: 2026-07-16
updated: 2026-07-16
---

# AI 資安工具選型與專題整合邊界

AI 資安工具的價值取決於它位於哪個控制點：程式碼進版前、Web 測試中、SOC 調查時、AI 上線前，或 AI 執行期。把不同控制點的工具硬接在一起，通常只會增加資料外洩與誤動作風險。

## 工具地圖

| 工具                             | 主角色                    | 最適合的階段                     | 對本專題的建議                  |
| ------------------------------ | ---------------------- | -------------------------- | ------------------------ |
| [[pentestgpt]]                 | 授權滲透測試 agent           | 隔離 lab 的攻擊模擬               | 後期、人工核准後使用               |
| [[burpgpt]]                    | Burp HTTP 流量的 AI 輔助    | 授權 Web AppSec 測試           | 僅在另建 Web 靶場時評估           |
| [[microsoft-security-copilot]] | Microsoft SOC/IT 助理    | Defender/Sentinel/Entra 生態 | 作為企業參考，不是目前 Wazuh lab 基線 |
| [[deepcode-ai]]                | Snyk Code 的 AI SAST 技術 | IDE、PR、CI/CD               | 專題有程式碼與 CI 後優先評估         |
| [[hexstrike-ai]]               | MCP 攻擊工具協調             | 隔離研究與工具治理實驗                | 現階段不接入專題核心               |
| [[garak]]                      | LLM 紅隊與弱點評估            | AI/RAG/MCP 上線前與回歸測試        | 建議列為 AI 助理的下一個安全驗證工作     |
| [[lakera-guard]]               | AI 互動執行期防護             | LLM 輸入、輸出、RAG、tool call    | AI 助理接實際資料後再評估導入         |

## 建議採用順序

1. 先完成 [[ai-analysis-pipeline]]：讓每一個 AI 結論能回指 Wazuh alert、關聯規則與 KB 來源，沒有足夠資料就明示限制。
2. 專題開始寫 Dashboard、RAG connector 或 MCP 程式碼後，用 [[deepcode-ai]] 或同類 SAST 加入 IDE/PR/CI 的程式碼檢查。
3. AI 助理有 staging endpoint 後，用 [[garak]] 建立少量、與專題風險相符的紅隊基準，重點是 prompt injection、RAG poisoning、敏感告警資料外洩與不當 tool use。
4. 若 AI 助理要服務其他使用者、讀取外部文件或能呼叫工具，再評估 [[lakera-guard]] 等執行期 guardrail，並將被攔截事件記錄到監控系統。
5. [[pentestgpt]]、[[burpgpt]]、[[hexstrike-ai]] 僅放在隔離與授權的攻擊模擬環境；其生成的流量可以用於驗證 Wazuh 偵測，但不可成為 AI 助理的自動執行能力。

## 不應混淆的能力

- `garak` 發現模型在特定 probe 下的失效，不代表它會在 runtime 阻擋攻擊。
- `Lakera Guard` 在 runtime 做 policy-based screening，不代表它已涵蓋所有新型攻擊；仍需要 garak 類的持續測試。
- `Security Copilot` 是完整 Microsoft 生態的助理，不等同於可直接讀取 Wazuh 的通用 LLM。
- `DeepCode AI` 保護程式碼，不負責分析網路告警；`PentestGPT`/`HexStrike AI` 產生或協調測試行為，也不等同於防禦偵測。

## 專題的最小安全架構

```text
Wazuh alert + 受控 RAG
        |
        v
可追溯的 AI 分析流程
        |
        +--> garak：上線前／改版後的紅隊回歸測試
        |
        +--> Guardrail：輸入、輸出、RAG 文件、tool call 的執行期篩檢
        |
        v
人工覆核與事件處置
```

## 關聯

- 來源：[[ai-security-tools-research-2026-07-16]]
- 既有流程：[[ai-analysis-pipeline]]、[[rag-integration-spec]]、[[system-prompt]]
- 工具實體：[[pentestgpt]]、[[burpgpt]]、[[microsoft-security-copilot]]、[[deepcode-ai]]、[[hexstrike-ai]]、[[garak]]、[[lakera-guard]]
