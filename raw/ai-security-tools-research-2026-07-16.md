# AI Security Tools Official Research Ledger (2026-07-16)

> 這是為 LLM Wiki 產生的研究來源清冊，不是官方文件的逐字副本。每一項結論應回查下列原始頁面；產品版本、授權與功能可能隨時間改變。

## 研究範圍

- PentestGPT
- BurpGPT
- Microsoft Security Copilot
- Snyk DeepCode AI / Snyk Code
- HexStrike AI
- NVIDIA garak
- Lakera Guard / Check Point AI Guardrails

## 原始資料與擷取重點

### PentestGPT

- GitHub: https://github.com/GreyDGL/PentestGPT
  - 現行 README 標示為 agentic penetration testing framework v1.0；分階段處理 CTF 或滲透測試，並支援 session persistence。
  - 2026-07-16 重新查核的 README 強調 Docker-first 與 Docker 前置需求；實作說明可能隨版本變動，Windows 應以 Docker isolation 為優先而非假設有原生流程。
- 論文: https://arxiv.org/abs/2308.06782
  - 原始研究指出 LLM 可處理局部子任務，但難維持完整測試情境；論文版本以三個互動模組緩解 context loss。

### BurpGPT

- Community repository: https://github.com/aress31/burpgpt
  - README 明示 Community edition 已不再維護且不再可用；舊版會將 Burp 流量送至使用者指定的 OpenAI 模型，且產出仍需人工 triage。
- Pro documentation: https://docs.burpgpt.app/
  - 現行文件描述其為 Burp Suite extension，支援雲端模型供應商與 Ollama/Hugging Face 本地模型；流程含設定供應商、分析 HTTP 流量與檢視 GPT 結果。
- Installation: https://docs.burpgpt.app/getting-started/installation
  - 2026-07-16 擷取的文件要求 Burp Suite Professional 2025.6.5+ 與 Java 21+；Pro JAR 由購買流程交付，Community repository 已標示停維護。

### Microsoft Security Copilot

- 官方文件: https://learn.microsoft.com/en-us/copilot/security/microsoft-security-copilot
  - 可獨立使用或嵌入 Defender XDR、Sentinel、Intune、Entra 等 Microsoft Security 產品。
  - 使用案例涵蓋警報調查、KQL、惡意腳本分析、風險與設定管理、報告及 agent 擴充。
- Onboarding: https://learn.microsoft.com/en-us/copilot/security/get-started-security-copilot
  - E5 included 與非 E5 included 的租戶走不同 onboarding；後者需佈建 Security Compute Units (SCUs)。
- Roles: https://learn.microsoft.com/en-us/copilot/security/authentication
  - Copilot 存取與後端服務 RBAC 是不同層次；官方建議以 security groups 指派角色。

### DeepCode AI / Snyk Code

- 產品頁: https://snyk.io/platform/deepcode-ai/
  - DeepCode AI 是 Snyk 安全平台的 AI 技術名稱，不應視為獨立 SAST 產品；其宣稱以多模型、符號式與生成式 AI 協助找出、修復與排序程式問題。
- Snyk Code 文件: https://docs.snyk.io/scan-with-snyk/snyk-code
  - Snyk Code 可從 IDE、SCM PR、CLI、CI/CD 與 API 使用，並支援資料流與控制流等程式分析；標準 SaaS 流程會將符合條件的程式檔送往 Snyk，另有 Local Engine 的 no-upload 選項。
- CLI install/test: https://docs.snyk.io/developer-tools/snyk-cli/install-or-update-the-snyk-cli and https://docs.snyk.io/developer-tools/snyk-cli/commands/code-test
  - 官方列出 Windows standalone executable/Scoop 方式；`snyk code test` 的 exit code 0/1/2/3 有不同語意，CI 不可一概視為系統錯誤。

### HexStrike AI

- GitHub: https://github.com/0x4m4/hexstrike-ai
  - README 自稱為 MCP cybersecurity automation framework，串接 MCP 相容 AI client、150+ 工具與 12+ agent，功能包含工具選擇、執行與報告。
  - 文件列出 Python 虛擬環境、相依套件及 MCP client 整合。此為高度自動化的攻擊面，任何使用僅限明確授權與隔離範圍。
  - 安全重點不在工具數量，而在 MCP client/server、外部工具、allowlist、log、egress 與人工停止點是否可控。

### garak

- GitHub: https://github.com/NVIDIA/garak
  - garak 是開源 LLM vulnerability scanner，可探測 prompt injection、資料外洩、jailbreak、幻覺與其他失效模式；以 generator、probe、detector 等元件測試模型或對話系統。
- 論文: https://arxiv.org/abs/2406.11036
  - 論文強調 LLM 安全是情境相關、持續變動的問題；掃描結果應用於風險政策與人工審查，不是單一通用安全分數。

### Lakera Guard / Check Point AI Guardrails

- Guard API: https://docs.lakera.ai/docs/api/guard
  - `/v2/guard` 可依專案 policy 篩檢 user、assistant、agent 與 tool 互動；任何 detector flag 即回傳 `flagged: true`，呼叫端決定阻擋、警告或建立內部告警。
  - 文件建議在將回應交給使用者或下游系統前進行 runtime screening，並可在 RAG 文件匯入時做離線掃描。

## 研究限制

- 本清冊以 2026-07-16 可取得的官方文件、官方 GitHub README 與同行研究為準；未自行安裝、付費、連接 API 或對任何目標執行掃描。
- 專案 README 的功能與版本屬維護者聲明，未當作獨立效能驗證。
- 所有滲透測試或攻擊模擬工具均必須先取得資產所有者的書面授權，並設定明確的 scope、速率與停止條件。
