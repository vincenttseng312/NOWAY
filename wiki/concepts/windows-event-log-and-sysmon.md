---
type: concept
title: "Windows Event Log 與 Sysmon 分析"
tags: [malware-analysis, dfir, windows, sysinternals]
sources: [malware-static-dynamic-analysis-notes]
created: 2026-07-09
updated: 2026-07-09
---

# Windows Event Log 與 Sysmon 分析

動態分析的日誌層面：Windows 內建 Event Log 提供基礎程序/登入/服務事件，Sysmon（Sysinternals 工具）以 service+driver 常駐方式提供更細緻的遙測，是 malware analysis、threat hunting、DFIR 與 SIEM 的重要資料來源。

## Windows Event Log 常見來源

| Log | 用途 |
|---|---|
| Security | 登入、程序建立、權限使用、物件存取 |
| System | 服務、驅動、系統事件 |
| PowerShell | PowerShell engine / script block |
| TaskScheduler | Scheduled Task activity |
| WMI-Activity | WMI 操作 |
| Sysmon/Operational | Sysmon telemetry |

## Windows Security 重要 Event ID

| Event ID | 意義 |
|---:|---|
| 4624 / 4625 | 登入成功 / 失敗 |
| 4648 | 使用明確憑證登入 |
| 4672 | 高權限登入 |
| **4688** | **程序建立**（啟用相關稽核後可含 command line，是動態分析最常用的 Security log 事件） |
| 4689 | 程序結束 |
| 4697 | 服務安裝 |
| 4698 / 4702 | Scheduled task 建立 / 修改 |
| **1102** | **Security log 被清除**（高風險，常見於清痕跡行為） |

Event ID 4688 重要欄位：New Process Name、Process Command Line、Creator Process Name、Subject User Name、Token Elevation Type、Mandatory Label。注意：command line 欄位需額外啟用稽核設定，否則可能為空。

System Log 重要 Event ID：7036/7040（服務狀態/啟動類型改變）、**7045（新服務被安裝，Service persistence 分析時非常重要，見 [[persistence-mechanisms]]）**。

PowerShell Logs：400/403（engine 啟停）、4103（module logging）、4104（script block logging，若啟用可看到被執行的腳本內容），詳見 [[lolbin-and-powershell-abuse]]。

## Sysmon

Sysmon 是 Sysinternals 工具，以 service 與 driver 方式常駐，把更細緻的系統活動寫入 Windows Event Log。

常見 Sysmon Event ID：

| ID | 名稱 | 分析用途 |
|---:|---|---|
| 1 | Process Create | 程序建立、命令列、父程序 |
| 2 | File creation time changed | timestomping 跡象 |
| 3 | Network Connection | 程序對外連線 |
| 6 | Driver Loaded | Driver 載入 |
| 7 | Image Loaded | DLL 載入 |
| **8** | **CreateRemoteThread** | **remote thread，injection 跡象，見 [[process-hollowing]]** |
| **10** | **ProcessAccess** | **跨程序存取，例如 LSASS access / injection prep** |
| 11 | FileCreate | 檔案建立 |
| 12/13/14 | Registry 建立/刪除/寫入/更名 | 見 [[persistence-mechanisms]] |
| 22 | DNS Query | DNS 查詢 |
| 23/26 | File Delete (archived/detected) | 檔案刪除 |

Event ID 1 重要欄位：`ProcessGuid`、`Image`、`CommandLine`、`ParentProcessGuid`、`ParentImage`、`ParentCommandLine`、`IntegrityLevel`、`Hashes`。**關鍵：`ProcessGuid` 比 PID 更適合跨事件關聯，因為 PID 會被系統重複使用。**

## Sysmon 關聯分析範例

```text
Event ID 1: WINWORD.EXE starts powershell.exe        (同 ProcessGuid)
Event ID 22: powershell.exe queries suspicious domain (同 ProcessGuid)
Event ID 3: powershell.exe connects to remote IP:443  (同 ProcessGuid)
Event ID 11: powershell.exe writes payload.exe to AppData
Event ID 1: payload.exe starts
Event ID 13: payload.exe writes HKCU Run key
```

這就是一條完整的行為證據鏈——串接程序建立、DNS、網路連線、檔案寫入、Registry 寫入六個事件，呼應 [[malware-analysis-methodology]] 中「把證據串成故事線」的核心原則。日誌時間線模板欄位：`Time UTC | Source | Event ID | ProcessGuid | Process | Parent | Action | Target | Notes`。

## 與其他頁面的關聯

Injection/Hollowing 對應的 Sysmon EID 8/10 見 [[process-hollowing]]；Registry persistence 對應的 EID 12/13/14 見 [[persistence-mechanisms]]；PowerShell 專屬日誌見 [[lolbin-and-powershell-abuse]]；日誌證據最終如何組成 Timeline 章節見 [[malware-analysis-report-template]]。
