---
type: entity
title: "garak"
tags: [ai-security, llm-security, security-tools]
sources: [ai-security-tools-research-2026-07-16]
created: 2026-07-16
updated: 2026-07-16
---

# garak

garak（Generative AI Red-teaming & Assessment Kit）是 NVIDIA 支援的開源 LLM vulnerability scanner。它以 generator、probe、detector 與 harness 組合，針對模型或對話系統檢查 prompt injection、資料外洩、jailbreak、幻覺、毒性與其他失效模式。

## 使用方式

在隔離的 Python 環境安裝 garak，先選定受測的自有模型、API 或 staging chatbot，再從少量且與風險政策相關的 probes 開始。每次測試需記錄 model/version、system prompt、工具權限、probe 集合、重試次數、判定 threshold 與成本。掃描完成後閱讀 HTML/結構化報告，人工抽查 FAIL 樣本，將確認的弱點轉成修補項與回歸測試；不要對不屬於自己的公開服務進行紅隊掃描。

## 優點

- 專注 LLM 應用的失效模式，與傳統網路掃描器的目的不同。
- 支援多種模型介面與 REST connector，能用同一個評估框架比較部署前後的差異。
- 探針與偵測器可擴充，適合把專題特有的 RAG 或工具使用政策轉成測試。

## 限制與風險

- FAIL 代表某個 probe/detector 組合發現可疑輸出，不等於完整風險評估或可直接推論真實攻擊成功率。
- 模型會更新，prompt 攻擊也會演化；基準和結果需附日期、版本與設定。
- 雲端模型測試可能產生 API 成本、速率限制與敏感資料傳輸問題。

## 對專題的定位

這是本專題最值得後續導入的 AI 安全評估工具：用它測試 [[system-prompt]]、RAG 引用規則及未來 MCP connector 對 prompt injection、資料外洩與不當工具使用的抵抗力。它是測試層，不是執行期防護層；後者由 [[lakera-guard]] 或同類方案負責。

## 關聯

- 來源：[[ai-security-tools-research-2026-07-16]]
- 選型：[[ai-security-tool-selection]]
- 執行期防護：[[lakera-guard]]
