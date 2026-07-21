---
type: entity
title: "garak"
tags: [ai-security, llm-security, security-tools]
sources: [ai-security-tools-research-2026-07-16]
created: 2026-07-16
updated: 2026-07-16
---

# garak

## 工具簡介

garak（Generative AI Red-teaming & Assessment Kit）是 NVIDIA 支援的開源 LLM vulnerability scanner。它不是網路掃描器，也不替任何模型「打安全分數」；它用可配置的測試提示、目標模型介面和結果偵測器，找出 prompt injection、資料外洩、jailbreak、幻覺、毒性或其他不符合既定政策的輸出。

它適合在自有模型、staging chatbot、RAG 或 MCP agent 上線前做回歸測試。不適合對非自己管理的公開聊天服務進行掃描，也不適合把單次 FAIL 當成已證實的重大資安事件。與 [[lakera-guard]] 的差異是：garak 偏向部署前/改版後的評估；Lakera Guard 偏向執行期攔截與政策處置。

## 核心功能與運作原理

garak 的基本架構是 generator（受測模型）、probe（測試手法）、detector（判讀輸出）和 harness（排程與結果彙整）。

```text
風險政策與選定 probes
        ↓
garak probe 產生測試輸入
        ↓
自有模型 / API / staging 應用
        ↓
detector 判讀輸出並產生 report
        ↓
人工抽查 FAIL → 修補 → 再跑回歸測試
```

重要的是先定義「什麼輸出算失敗」。例如專題的 AI 助理若不該透露系統提示詞、未引用來源就不應下結論、不可自行執行工具，這些才是有意義的測試目標。

## 適用情境

1. 在 [[system-prompt]] 改版後，確認模型不會因使用者內容而忽略資料引用與限制條件。
2. 在 RAG 匯入外部文件後，測試可疑文件文字是否能影響助理的行為或要求不當資料。
3. 在 MCP connector 加入前，驗證 AI 助理不會把未授權的文字當成工具執行指令。

## 安裝前準備

- 官方 GitHub 的開發環境說明使用 Python `>=3.10, <=3.12`；建議專用 virtual environment。
- 目標可以是自有本機模型、經授權的 API 或 staging REST endpoint。雲端模型會有成本、速率限制及資料傳輸風險。
- 先準備版本、系統提示詞、資料來源、測試範圍、成功/失敗定義和停止條件的紀錄表。
- 本機目前沒有可用 Python，因此以下流程是根據官方文件整理，`verified_on_this_machine: false`。

官方資料：[NVIDIA/garak README](https://github.com/NVIDIA/garak)、[使用者/CLI 文件](https://docs.garak.ai/)、[研究論文](https://arxiv.org/abs/2406.11036)。

## Windows PowerShell 安裝與驗證

先查版本；若 `py -3.12` 不存在，先從官方 Python 發行管道安裝受支援版本並重新開啟 PowerShell。不要用系統 Python 安裝到全域 site-packages，以免污染其他專案。

```powershell
# 驗證 Python Launcher 與版本。garak 官方開發環境限制最高 Python 3.12。
py -3.12 --version

# 建立隔離資料夾與 virtual environment。
New-Item -ItemType Directory -Path "$HOME\llm-security-lab\garak" -Force | Out-Null
Set-Location "$HOME\llm-security-lab\garak"
py -3.12 -m venv .venv

# 啟用環境，更新 pip，安裝 garak，最後只顯示說明做安全驗證。
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install garak
python -m garak --help
```

成功時最後一行應列出 `python -m garak` 的參數。若 `Activate.ps1` 被執行原則阻擋，先理解 `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` 只改目前使用者的本機指令碼政策；確認組織政策允許後才使用。也可以不啟用環境，改用 `.\.venv\Scripts\python.exe -m garak --help`。

## 快速開始：安全的安裝驗證

不要在第一次使用就跑所有 probes，也不要先對雲端模型送出測試。以下只確認套件與 CLI 可啟動，不會呼叫模型或外部 API：

```powershell
Set-Location "$HOME\llm-security-lab\garak"
.\.venv\Scripts\python.exe -m garak --help
```

下一步才是在自己的 staging 目標上，選擇單一、已核准的 probe 類別與低重試次數；模型 API key 應以目前工作階段環境變數或受管理的 secret store 提供，絕不寫進設定檔、聊天紀錄或 Git。

```powershell
# 範例只建立目前 PowerShell 工作階段的變數；請替換為自己的受管理 key。
$env:OPENAI_API_KEY = "<temporary-key-from-secret-store>"

# 實際 probe 名稱、目標型別與成本限制必須先依該版本官方 CLI 文件核對。
# 執行前應在團隊測試計畫中記錄 scope、模型版本、停止條件與預算。
```

## 設定、結果與最佳實務

- 每次測試固定記錄 model/provider/version、system prompt、RAG snapshot、probe、detector、generation 次數、threshold、日期與成本。
- 優先建立少量專題特有的測試，例如「要求忽略引用規則」「誘導未授權 tool call」，而不是追求大量 generic FAIL。
- FAIL 必須人工抽查 request、response 與 detector 理由；將確認問題寫成修補 ticket，再以相同設定回歸測試。
- 將命中內容視為敏感測試資料，保存到受管控位置，不要直接貼到 issue、chat 或公開 repo。

## 常用指令

| 指令 | 用途 | 預期結果 |
|---|---|---|
| `python -m garak --help` | 確認 CLI 可啟動 | 顯示使用說明，不呼叫模型。 |
| `python -m pip show garak` | 確認安裝位置與版本 | 顯示 package metadata。 |
| `python -m garak --target_type <type> --target_name <name> --probes <probe>` | 對已授權目標跑指定 probe | 會呼叫模型，需先核對成本與範圍。 |

## 常見錯誤與排解

### `py -3.12` 找不到

原因通常是 Python Launcher 或指定版本未安裝。確認 `py --list`，再由官方 Python 發行管道安裝符合範圍的版本；不要隨意修改全域 PATH 覆蓋既有專案。

### `Activate.ps1` 被拒絕

這是 PowerShell execution policy，不代表 garak 安裝失敗。優先使用 `.\.venv\Scripts\python.exe -m ...` 避免改政策；若必須調整，僅在 `CurrentUser` 範圍、理解 `RemoteSigned` 含義且符合組織規範時處理。

### 掃描成本過高或大量 timeout

先降低 generation/retry、只跑單一 probe family，並確認模型 API 的速率與預算。不要靠提高平行度硬壓過速率限制；保留失敗 log，判斷是網路、模型還是設定問題。

## 工具比較與重點整理

| 工具 | 主要控制點 | 優點 | 限制 |
|---|---|---|---|
| garak | 部署前/回歸測試 | 可配置的 LLM 失效測試 | 結果需人工與風險政策解讀。 |
| [[lakera-guard]] | 執行期 | 依 policy 篩檢輸入、輸出與工具互動 | 不會自動找出所有新攻擊。 |
| [[microsoft-security-copilot]] | Microsoft SOC 工作流 | Microsoft 安全產品整合 | 不是通用 LLM 紅隊工具。 |

完成本頁後，應能把 garak 正確定位為「測試工具」而非防火牆、在 Windows 使用隔離環境安裝並只做 CLI 驗證，以及將結果回灌到 [[system-prompt]] 與 [[rag-integration-spec]] 的安全需求。

## 關聯

- 來源：[[ai-security-tools-research-2026-07-16]]
- 選型與盤點：[[ai-security-tool-selection]]、[[wiki-content-strengthening-audit-2026-07-16]]
- 執行期防護：[[lakera-guard]]
