---
id: doc-wazuh-agent
title: "Wazuh Agent 說明"
doc_type: wazuh
category: wazuh
summary: "Wazuh Agent 裝於 Windows 11 靶機，透過 Windows Eventchannel 採集 Security/System/PowerShell 等事件與主機狀態，回傳 Manager。採集哪些通道由設定決定（env-specific）。"
tags: [cat:wazuh, type:wazuh, source:windows-security, entity:host]
related_entities: [ent-host-win11-target]
related_docs: [doc-wazuh-manager, doc-windows-events-into-wazuh, doc-windows11-target]
keywords: ["Wazuh Agent", "端點採集", "eventchannel", "Windows Event Log", "log collection", "agent"]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "Microsoft Windows Security Auditing 文件"]
last_updated: 2026-07-09
---

# Wazuh Agent 說明

## 1. 這是什麼
安裝於受監控端點的採集程式。本專題中裝在 Windows 11 靶機上（該機同時加入 AD 網域）。

## 2. 在本專題中的角色
是絕大多數事件的第一手來源：把 Windows 安全相關日誌與主機狀態送到 Manager。對映實體為該台 Host（`agent.name`／`agent.ip`）。

## 3. 採集什麼（概念）
- **Windows Eventchannel**：讀取 Windows Event Log 的通道，如 Security、System、Application、PowerShell/Operational 等（實際採集哪些通道由 agent 設定決定，需確認）。
- 也可含檔案完整性監控（FIM）、主機清點等（是否啟用需確認）。

> 具體 `ossec.conf` 設定、採集的通道清單、agent id 皆為部署相關（需依實際環境確認）。

## 4. AI 如何使用
Agent 本身不產生分析；但「採集了哪些通道」決定 AI 看得到哪些事件。若某事件未被採集，AI 應說明「該來源可能未納入監控」而非臆測。

## 5. 需依實際環境確認
採集通道清單、FIM 是否啟用、agent 版本與 id、與 Manager 的連線設定。

## 相關文件
[[doc-wazuh-manager]]、[[doc-windows-events-into-wazuh]]、[[doc-windows11-target]]；跨連父層 [[windows-event-log-and-sysmon]]。

## 建議查證來源
Wazuh 官方文件、Microsoft Windows Security Auditing 文件。

## 可被檢索的關鍵字（中英）
Wazuh Agent、端點、採集、eventchannel、Windows 事件、log collector、endpoint agent。
