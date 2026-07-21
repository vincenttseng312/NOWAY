---
type: entity
title: "BurpGPT"
tags: [ai-security, pentesting, appsec, security-tools]
sources: [ai-security-tools-research-2026-07-16]
created: 2026-07-16
updated: 2026-07-16
---

# BurpGPT

## 工具簡介

BurpGPT 是整合在 Burp Suite Professional 中的 AI 輔助 HTTP 流量分析工具。它將範圍內 request/response 與使用者設定的提示詞交給雲端或本地模型，產生需要人工驗證的候選安全問題與分析說明。它不是獨立桌面程式，也不是可以取代 Burp Suite Professional 的掃描器。

使用前必須分清產品世代：官方 Community repository 已由維護者標示為停止維護且不再可用；目前選型與安裝應以 BurpGPT Pro 的文件、授權交付方式及相容性要求為準。它適合已授權的 Web 應用測試與人工 triage，不適合直接攔截正式使用者的敏感流量、未經核准地把 token/個資送到雲端模型，或把 AI 文字當成已證實漏洞。

## 核心功能與運作原理

```text
瀏覽器 / 測試 client → Burp Suite Professional proxy
        ↓
範圍內 HTTP request / response
        ↓
BurpGPT prompt + 雲端或本地 LLM provider
        ↓
候選發現、流量解釋與報告草稿
        ↓
測試人員在原始流量中重現、判讀與記錄
```

它的價值在於輔助理解商業語境與自訂提示下的流量，而不是繞過 Burp Scope、驗證流程、負責任揭露或人工確認。BurpGPT Pro 文件列出雲端模型供應商與 Ollama/Hugging Face 等本地處理選項；選用本地模型可降低外送風險，但不會自動消除 endpoint、prompt 或存取控制問題。

## 適用情境

1. 對自己的測試 Web API，在 Burp Scope 內摘要一批已遮罩的 request/response，協助人工找出邏輯不一致處。
2. 在已授權的 staging 站台中，以自訂 prompt 協助檢查 API 回應是否暴露不該出現的欄位。
3. 用本地模型測試時，讓敏感流量不離開隔離環境，但仍由測試人員確認結論。

## 安裝前準備

- 依目前官方 Pro 文件，需要 **Burp Suite Professional 2025.6.5 或更新版本**、有效 Pro 授權與 **Java 21+**。較舊 Burp 版本可能有相容性錯誤。
- Pro 的 JAR 由購買流程交付，不能從 Community repository 假設取得相同檔案。
- 使用 Local LLM 功能時，文件另列 Python 3.13.5、`flask`、`flask-cors`、`transformers` 等相依套件；安裝前先確認模型硬體需求與資料處理政策。
- 測試前完成書面 scope、Burp Scope、帳號與 API key 的資料遮罩規則。不要把正式 session cookie、Authorization header 或真實客戶資料交給未核准的 provider。

官方資料：[BurpGPT Pro installation](https://docs.burpgpt.app/getting-started/installation)、[BurpGPT FAQ](https://docs.burpgpt.app/help-and-faq/faq/can-burpgpt-editions-be-used-as-standalone-applications-operating-independently)、[專案 repository](https://github.com/aress31/burpgpt)。

## Windows PowerShell 前置檢查

BurpGPT 的安裝本身是 Burp Suite GUI 操作，不應硬寫成不存在的 PowerShell 安裝命令。下列只檢查 Java 與已取得的 JAR，執行後不會啟動測試或傳送任何流量。

```powershell
# 確認 Java 可用；版本應為 21 或更新。
java -version

# 將路徑換成購買流程交付、由你自己下載的 Pro JAR。
$burpGptJar = "$HOME\Downloads\BurpGPT-Pro.jar"
Test-Path -LiteralPath $burpGptJar
Get-FileHash -LiteralPath $burpGptJar -Algorithm SHA256
```

`Test-Path` 應回傳 `True`；雜湊可用於比對供應商提供的值或團隊內部的受控軟體清單。不要從論壇、訊息附件或不明雲端硬碟取得 JAR。

## 快速開始：載入並安全驗證

1. 開啟已授權的 Burp Suite Professional。
2. 到 **Extensions** → **Installed** → **Add**，選擇由正式交付取得的 JAR。
3. 成功時 Pro 應顯示 `BurpGPT Pro` 分頁；若沒有，先看 Burp Extensions output/error，而不是重複安裝多個 JAR。
4. 先設定一個只含測試主機的 Burp Scope，再選擇模型 provider 和最小提示詞。
5. 對不含真實帳密的測試 request 做一次分析；回到原始 request/response 驗證每個候選發現。

這是 GUI 產品的最小驗證流程；本機沒有 Burp Suite Pro 或 BurpGPT 授權，未在此機實測。

## 設定與資料安全

- Cloud provider：先取得資料處理、保留與跨境傳輸核准；必要時在送出前遮罩 Cookie、Bearer token、個資與內部主機名。
- Local model：確認模型服務執行位置、GPU/RAM、存取控制與 log 落點；「本地」不代表使用者都可讀取內容。
- Prompt：把工作範圍限制在「協助找候選問題並引用 request/response 證據」，避免要求工具自動攻擊或自動判定嚴重性。
- 將 provider key 放在 BurpGPT 受保護設定或受管理 secret 中；不要寫入 prompt、PowerShell history 或 Git。

## 常用操作

| 操作 | 用途 | 驗證方式 |
|---|---|---|
| Burp Scope | 限制可分析的主機與路徑 | Scope 只顯示書面授權目標。 |
| Extensions output/error | 查 Extension 載入或 Java 相容性錯誤 | 無未處理例外，且顯示 Pro 分頁。 |
| Provider test | 驗證模型設定 | 用無敏感資料的測試 request。 |
| 原始流量比對 | 驗證 AI 發現 | 每一項候選都能回指 request/response。 |

## 常見錯誤與排解

### JAR 無法載入或出現 `NoSuchMethodError`

常見原因是 Burp 或 Java 版本低於目前文件要求，或誤把 Community JAR 當作 Pro JAR。先在 Extensions output 檢查完整錯誤，再確認 Burp Suite Pro、Java 21+ 與 JAR 世代；不要從不同版本的 Gradle build 產物混用檔案。

### AI 結果沒有內容或 provider 驗證失敗

確認 provider key、模型名稱、網路/代理設定與 token 限制；再用最小、去識別的 request 測試。不要在 error report 中貼出完整 Authorization header。

### 結果看起來像漏洞但無法重現

把它標記為 false positive 或需要更多證據，而不是提高嚴重性。AI 對 HTTP 語意的推測不等於服務端行為；回到 request、response、伺服器端 log 與授權測試案例做驗證。

## 工具比較與重點整理

| 工具 | 優點 | 限制 | 適合情境 |
|---|---|---|---|
| BurpGPT Pro | 在 Burp 流量上提供 AI 輔助 triage，可選本地模型 | 需 Burp Pro、授權與嚴格資料治理 | 已授權 Web AppSec。 |
| [[pentestgpt]] | 多階段的測試 agent 工作流 | 不等同 Web proxy/HTTP 人工分析 | 隔離 CTF 或授權 lab。 |
| [[hexstrike-ai]] | MCP 串接多種安全工具 | 自動化風險高，不宜直接接核心系統 | 受控工具治理研究。 |

完成本頁後，應能辨識 Community 與 Pro 的差異、在 Windows 先驗證 Java/JAR、以 Burp Scope 和資料遮罩保護流量，並把 AI 結果正確視為人工驗證前的候選假設。

## 關聯

- 來源：[[ai-security-tools-research-2026-07-16]]
- 選型與盤點：[[ai-security-tool-selection]]、[[wiki-content-strengthening-audit-2026-07-16]]
- 相近工具：[[pentestgpt]]、[[hexstrike-ai]]
