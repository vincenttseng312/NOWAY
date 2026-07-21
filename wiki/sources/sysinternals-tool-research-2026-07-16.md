---
type: source
title: "Sysinternals Process Explorer and Process Monitor Official Research (2026-07-16)"
authors: ["Microsoft Sysinternals", "OpenAI Codex research synthesis"]
tags: [sysinternals, windows, dfir, malware-analysis]
raw: raw/sysinternals-tool-research-2026-07-16.md
ingested: 2026-07-16
created: 2026-07-16
updated: 2026-07-16
entities: [process-explorer, process-monitor]
---

# Sysinternals 工具官方研究

Process Explorer 與 Process Monitor 是互補工具：前者檢視某個時間點的程序、handle、DLL 和記憶體映射檔；後者記錄一段時間內的檔案、Registry、程序/執行緒操作。兩者都不能單獨證明惡意行為，必須用命令列、簽章、路徑、事件時間線和其他遙測交叉驗證。

官方支援矩陣有差異：2026-07-16 的 Process Explorer 頁列 Windows 11+，Process Monitor 頁列 Windows 10+。在 Windows 10 分析 lab，應先驗證 Process Explorer 的實際版本與相容性。

## 關聯

- 工具：[[process-explorer]]、[[process-monitor]]
- 安全環境：[[malware-analysis-vm-setup]]
- 方法：[[dynamic-behavior-analysis]]、[[windows-event-log-and-sysmon]]
