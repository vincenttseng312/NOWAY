---
type: entity
title: "BurpGPT"
tags: [ai-security, pentesting, appsec, security-tools]
sources: [ai-security-tools-research-2026-07-16]
created: 2026-07-16
updated: 2026-07-16
---

# BurpGPT

BurpGPT 是將 LLM 分析接入 Burp Suite HTTP 流量的延伸工具。舊版 Community repository 的維護者已明確標示為不再維護且不再可用；目前應區分為有正式文件的 BurpGPT Pro，而不是依賴舊 Community 安裝流程。

## 使用方式

在已授權 Web 應用測試中，於 Burp Suite 安裝目前支援的 BurpGPT 版本，選擇已核准的雲端或本地模型供應商，設定資料處理與提示詞政策，再將範圍內的 HTTP 流量交給工具分析。結果應回到 Burp 的原始 request/response 逐筆驗證，確認漏洞是否可重現與影響是否成立。

## 優點

- 對具商業邏輯或語境依賴的 HTTP 流量提供額外的自然語言分析角度。
- 現行文件列出雲端與 Ollama/Hugging Face 本地模型選項；本地處理可降低流量外送疑慮。
- 可把分析結果整理為待人工確認的候選問題，協助 triage。

## 限制與風險

- Community edition 已停維護，不應部署於新的測試流程。
- 若使用雲端模型，HTTP request/response 可能含 token、個資或商業資料；需先做資料最小化、遮罩與供應商審核。
- AI 結果可能有 false positive，且不能取代 Burp 的人工驗證、授權範圍與負責任揭露流程。

## 對專題的定位

這是 Web AppSec 工具，並非 Wazuh、AD 或 AI 助理的核心元件。只有專題另建已授權 Web 靶場時，才適合作為 [[pentestgpt]] 以外的人工輔助工具。

## 關聯

- 來源：[[ai-security-tools-research-2026-07-16]]
- 選型：[[ai-security-tool-selection]]
- 相近工具：[[pentestgpt]]、[[hexstrike-ai]]
