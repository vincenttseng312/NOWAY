---
type: entity
title: "DeepCode AI"
tags: [appsec, sast, security-tools]
sources: [ai-security-tools-research-2026-07-16]
created: 2026-07-16
updated: 2026-07-16
---

# DeepCode AI

## 工具簡介

DeepCode AI 是 Snyk 平台用於程式安全分析的技術名稱，不是可單獨下載的掃描器。實際操作入口是 **Snyk Code**：它可從 IDE、Git repository pull request、Snyk CLI、CI/CD 或 API 分析自有原始碼，協助找出、排序與修補程式安全問題。

它適合把安全檢查放進開發流程，特別是 Dashboard、RAG connector、alert parser 或 MCP service 開始有 Git repository 與 CI/CD 時。不適合拿來解釋 Wazuh 告警、取代動態測試，或在未完成原始碼資料外送審查前直接掃描敏感專案。和一般規則式 SAST 相比，Snyk Code 的重點是語意、資料流與控制流分析；但所有發現與 AI 修補建議都仍要經過 code review 和測試。

## 核心功能與運作流程

Snyk Code 會分析程式的 API 使用、資料流、控制流、型別與可疑 sink/source，將問題依嚴重性與優先度呈現。典型資料流程如下：

```text
本機 IDE / Git PR / CI 工作區
        ↓
Snyk Code 分析與資料流建模
        ↓
漏洞、說明、修補脈絡與優先排序
        ↓
開發者驗證 → 修補 → 測試 → PR review
```

標準 SaaS 工作流會將符合條件的程式檔送往 Snyk；不能外送原始碼時，可評估 Snyk Code Local Engine，但官方文件說明其維護負擔較高、更新較慢。

## 適用情境

1. 在提交 RAG connector 或 API 後端的 PR 前，找出可疑資料流與不安全 API 使用。
2. 在 CI/CD 產生 JSON 或 SARIF 結果，交由既有安全平台或 code review 流程追蹤。
3. 在 IDE 中即時檢查新寫的 API handler，避免問題累積到部署後才發現。

## 安裝前準備

- 需要 Snyk 帳號，且組織已啟用 Snyk Code。
- Snyk 官方要求 CLI 版本至少為 1.716.0，並建議使用最新版。
- Windows 可使用官方 standalone executable 或 Scoop；官方文件明確表示 WSL 不是原生支援環境。
- 不要把 `SNYK_TOKEN`、掃描輸出中的原始碼片段或 `.env` 提交至 Git。

官方資料：[Snyk CLI 安裝](https://docs.snyk.io/developer-tools/snyk-cli/install-or-update-the-snyk-cli)、[Snyk Code CLI](https://docs.snyk.io/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-snyk-code)、[`snyk code test`](https://docs.snyk.io/developer-tools/snyk-cli/commands/code-test)。

## Windows PowerShell 安裝與驗證

先確認目前工作階段能找到 Scoop；若尚未安裝 Scoop，請依其官方安裝文件完成 bootstrap，不要對不明來源的 `Invoke-Expression` 指令直接執行。

```powershell
# 確認 Scoop 已存在；找不到時會顯示空白結果。
Get-Command scoop -ErrorAction SilentlyContinue

# 加入官方 Snyk bucket，安裝 CLI，並確認版本。
scoop bucket add snyk https://github.com/snyk/scoop-snyk
scoop install snyk
snyk --version
```

成功時最後一行應輸出 Snyk CLI 版本。若組織不能使用 Scoop，改從 Snyk 官方 GitHub Releases 取得 Windows standalone executable，放進受管理的工具目錄並加入目前使用者的 PATH；不要從非官方鏡像下載執行檔。

登入會開啟瀏覽器授權流程：

```powershell
# 在自有開發帳號完成登入；完成後回到 PowerShell。
snyk auth
```

## 快速開始：掃描一個自有程式碼資料夾

下列步驟只掃描目前資料夾的原始碼，不會建立或修改原始碼。它需要有效帳號、已啟用 Snyk Code，且尚未在本機實測。

```powershell
# 建立一個空白示範資料夾；把自己的非敏感測試專案放入後再掃描。
New-Item -ItemType Directory -Path "$HOME\snyk-code-demo" -Force | Out-Null
Set-Location "$HOME\snyk-code-demo"

# 執行 SAST，並把機器可讀結果寫入檔案。
snyk code test --json-file-output .\snyk-code-results.json
```

預期結果是主控台顯示掃描摘要；若找到問題，命令通常以 exit code `1` 結束，這是「需要處理」而非 CLI 壞掉。若沒有受支援的程式碼，可能得到 exit code `3`。CI 必須依官方 exit code 規則處理，不可把任何非零值都當成系統錯誤。

## 設定與安全實務

- 以 `snyk auth`、CI 的 secrets 或受管理 service account 提供身分，不要把 token 寫入程式碼。
- 使用 `.snyk`、`.gitignore` 與 `.dcignore` 前，先確認排除規則不會漏掉正式程式碼。
- 對 `--report` 指令設定明確的專案名稱和權限，因它會將掃描快照送至 Snyk Web UI。
- 在 PR/CI 中輸出 SARIF/JSON 時，將檔案當作可能含程式路徑或安全資訊的產物管理。

## 常用指令

| 指令 | 用途 | 備註 |
|---|---|---|
| `snyk --version` | 驗證 CLI 版本 | 安裝或升級後先跑。 |
| `snyk auth` | 互動式登入 | 需要瀏覽器與帳號。 |
| `snyk code test` | 掃描目前資料夾的原始碼 | SAST，不是 dependency scan。 |
| `snyk code test --json-file-output .\result.json` | 輸出 JSON | 若無發現，Snyk Code 不一定建立 JSON 檔。 |
| `snyk code test -d` | 輸出偵錯資訊 | 上傳至 issue 前先遮罩敏感路徑與內容。 |

## 常見錯誤與排解

### 找不到 `snyk`

原因通常是安裝位置未加入 PATH，或 PowerShell 是在安裝前開啟。先關閉並重開 PowerShell，再執行 `Get-Command snyk`；若仍失敗，依官方 standalone/Scoop 安裝說明重新確認路徑，不要複製未知 DLL 或 exe 到系統目錄。

### `snyk code test` 回傳 exit code 3

這表示 CLI 沒有發現受支援的程式專案。確認目前目錄、程式語言支援度、`.gitignore`/`.dcignore` 排除規則與檔案大小限制；不要用假的 manifest 檔強迫掃描。

### 403 或未授權

重新執行 `snyk auth`，確認帳號屬於正確組織且 Snyk Code 已啟用。只有在要使用 `--report` 時，再確認 token 具備官方文件要求的 project ignore 檢視權限。

## 工具比較與重點整理

| 工具 | 強項 | 主要限制 | 適合情境 |
|---|---|---|---|
| Snyk Code / DeepCode AI | IDE、PR、CLI、CI/CD 的程式安全分析 | SaaS 資料邊界與修補仍需人工驗證 | 專題程式碼進入 Git 後。 |
| [[garak]] | LLM/RAG/agent 失效模式測試 | 不分析一般應用程式原始碼 | AI 助理上線前。 |
| [[lakera-guard]] | LLM 互動的執行期防護 | 不取代 SAST 或 code review | AI 助理已處理真實資料時。 |

完成本頁後，應能分辨 DeepCode AI 與 Snyk Code、在 Windows 安裝並驗證 Snyk CLI、正確解讀 Snyk Code exit code，並將掃描放進 PR/CI 而不是把它當成一次性檢查。

## 關聯

- 來源：[[ai-security-tools-research-2026-07-16]]
- 選型：[[ai-security-tool-selection]]、[[wiki-content-strengthening-audit-2026-07-16]]
- 專題流程：[[ai-analysis-pipeline]]
