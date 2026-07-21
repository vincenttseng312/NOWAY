---
type: synthesis
title: "LLM_Wiki 文件內容強化盤點（2026-07-16）"
tags: [methodology, ai-security, open-question]
sources: [ai-security-tools-research-2026-07-16]
created: 2026-07-16
updated: 2026-07-16
---

# LLM_Wiki 文件內容強化盤點

## 盤點範圍與方法

本次以 Markdown/MDX 檔案清單、行數、frontmatter、現有索引與專題 `README.md`/`SCHEMA.md` 進行靜態盤點。根目錄沒有發現 `package.json`、`pyproject.toml` 或文件網站設定檔；因此目前沒有可直接執行的網站 build 或 Markdown lint 流程。父層 `wiki/` 有 55 個 Markdown 頁，`projects/wazuh-ad-soc/` 有 137 個文件頁；不是所有短頁都有問題，固定格式的 technique card、QA entry 與 template 本來就應保持精簡。

本機仍沒有可用的 Python runtime，因此 Python 工具的指令只能做文件正確性核對，不能宣稱已執行成功。這是本 wiki 的 [SCHEMA](../SCHEMA.md) 所定義的 Verification/Code Preservation 邊界。

## 待改善清單

| 優先度 | 範圍 | 發現 | 處理方式 |
|---|---|---|---|
| P0 | `wiki/entities/` 的 AI 工具頁 | 7 頁大多只有定位、優缺點與一段使用方式，缺少前置條件、Windows 步驟、設定、排錯與可驗證範例。 | 批次 1：先補 `deepcode-ai`、`garak`、`lakera-guard`、`burpgpt`、`microsoft-security-copilot`。 |
| P0 | `process-explorer`、`process-monitor` | 有分析觀念但缺下載驗證、GUI 操作流程、PML 保存、Windows 權限與常見排錯。 | 批次 2：和 `malware-analysis-vm-setup` 一起補強。 |
| P1 | `pentestgpt`、`hexstrike-ai` | 需額外說明 Windows 相容性、授權 scope、MCP/agent 工具治理；不得把高風險自動化寫成日常操作手冊。 | 批次 2：只提供隔離、授權、可中止的安裝前與驗證流程。 |
| P1 | `projects/wazuh-ad-soc/09-ai-analysis/` | `ai-analysis-pipeline`、`rag-knowledge-base-design`、`rag-integration-spec` 已有系統規格，但對 LLM/RAG/embedding/MCP 的初學者概念與最小實作不足。 | 批次 3：補概念解釋、資料流程、設定範例與可驗證介接點。 |
| P2 | MITRE technique cards 與 QA entries | 多數只有 35–49 行，是刻意的 RAG 原子頁；但可增加一致的「資料不足時回答」與官方來源連結。 | 批次 4：模板級改善，避免每張卡重複堆字。 |
| P2 | 根目錄零長度 `doc-*`/`evt-*` 檔 | 不是目前索引或專題目錄的正式內容頁，可能是舊 alias/產製殘留。 | 不刪除；後續先確認是否被其他系統引用，再決定是否補 redirect 或移除。 |

## 第一批完成定義

每個工具頁依工具適用性補上：工具定位、資料/控制流程、至少三個情境、Windows 前置檢查或明確說明「不適用」、安全的快速開始、設定與金鑰管理、常用指令、常見錯誤、最佳實務、工具比較與延伸閱讀。SaaS 或 GUI 工具不會硬塞不存在的 CLI；高風險攻擊自動化工具則不提供可武器化的操作流程。

## 已知限制

- 未安裝 Python、Snyk、Burp Suite、garak 或任何第三方 API；所有外部工具操作都維持 `verified_on_this_machine: false` 的事實邊界。
- 沒有可用的文件網站 build/lint 設定，因此以 PowerShell 手動檢查 frontmatter、wikilink、標題與頁面大小。
- 文件中的產品版本、價格、授權和雲端能力會變動；以頁面「官方資料」連結和來源研究頁為準，實際導入日必須重新確認。

## 關聯

- 本批來源：[[ai-security-tools-research-2026-07-16]]
- 工具選型：[[ai-security-tool-selection]]
- 專題 AI 流程：[[ai-analysis-pipeline]]、[[rag-integration-spec]]、[[system-prompt]]
