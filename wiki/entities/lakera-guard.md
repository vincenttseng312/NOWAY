---
type: entity
title: "Lakera Guard"
tags: [ai-security, llm-security, guardrails, security-tools]
sources: [ai-security-tools-research-2026-07-16]
created: 2026-07-16
updated: 2026-07-16
---

# Lakera Guard

Lakera Guard 是現稱 Check Point AI Guardrails 的 API 防護能力之一。其 `/v2/guard` 依專案 policy 篩檢 LLM 互動，支援 user、assistant、agent、tool 與文件內容；若任一啟用的 detector 命中，回傳 `flagged: true`，由呼叫端決定阻擋、警告、人工覆核或建立內部告警。

## 使用方式

為每個應用與環境建立獨立 project 與 policy，讓後端在 LLM 輸入送出前、模型輸出回傳使用者前，以及 agent 呼叫工具前後呼叫 Guard API。當回應被標記時，採預先定義的處置路徑，例如拒絕執行高風險工具、改走人工覆核或建立 Wazuh/事件紀錄。對 RAG 知識庫，於文件匯入時進行離線掃描，並在高風險資料流保留執行期檢查。

## 優點

- 把 prompt attack、資料外洩與 agent/tool 行為篩檢放入應用程式控制流。
- 可用不同 project/policy 管理開發、測試與正式環境的敏感度。
- 能同時處理執行期互動與 RAG 文件匯入，與 [[garak]] 的部署前測試形成互補。

## 限制與風險

- 這是外部 SaaS/API 依賴；需評估 API key 保護、成本、延遲、可用性、資料處理與供應商風險。
- detector 可能 false positive 或 false negative，policy 需要以實際誤報與漏報持續調校。
- Guardrail 不能取代最小權限、MCP allowlist、資料分類、輸出引用與人工處置責任。

## 對專題的定位

當自建 AI 助理開始讀取 Wazuh 告警與 RAG 內容時，這是可評估的執行期防護層。最小整合點是「回傳 AI 摘要前」；較完整的設計則再涵蓋 RAG 文件匯入與未來 MCP 工具呼叫。

## 關聯

- 來源：[[ai-security-tools-research-2026-07-16]]
- 選型：[[ai-security-tool-selection]]
- 測試層：[[garak]]
