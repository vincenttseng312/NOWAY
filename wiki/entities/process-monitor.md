---
type: entity
title: "Process Monitor (Procmon)"
tags: [sysinternals, malware-analysis, dfir]
sources: [malware-dynamic-analysis, malware-static-dynamic-analysis-notes]
created: 2026-07-08
updated: 2026-07-09
---

# Process Monitor (Procmon)

微軟 Sysinternals 工具集中的系統行為側錄工具，在惡意程式動態分析中用來以微秒等級的精度記錄全系統底層活動，俗稱「系統行車紀錄器」。

## 核心功能

以微秒（Microsecond）為單位側錄系統底層行為，涵蓋四大監控維度：
- 登錄檔（Registry）
- 檔案系統（File System）
- 網路（Network）
- 程序／執行緒（Process/Thread）

## 介面控制

- **放大鏡圖示**：暫停／繼續側錄。
- **橡皮擦圖示**：清空目前累積的所有事件，還原成乾淨畫布，方便針對特定操作重新開始側錄。

## 精準過濾器（Filter）是必要操作

Procmon 開啟後數秒內就會累積數十萬筆系統雜訊，若不設過濾器幾乎無法閱讀。實作方式：`Ctrl+L` 開啟 Filter 對話框，設定條件鎖定目標（例如 `Process Name` → `is` → `Notepad.exe` → `Include`），排除所有無關事件。

## 關鍵動作追蹤

分析惡意行為時的常見觀察點：
- `Operation` 欄位的 `CreateFile` 或 `WriteFile` —— 用來捕捉惡意程式釋放（Drop）木馬本體的具體時刻。
- `Path` 欄位 —— 追蹤檔案被寫入的具體路徑，例如勒索軟體加密檔案或寫入勒索信的具體犯罪證據。

## Filter 策略

四種常見鎖定方式，各有取捨：

| 策略 | 寫法 | 缺點 |
|---|---|---|
| 以 Process Name 鎖定 | `Process Name is sample.exe Include` | 樣本建立子程序時可能漏掉 child process |
| 以 PID 鎖定 | `PID is 1234 Include` | 對短命程序或重啟程序不穩 |
| 以路徑鎖定 | `Path contains AppData Include`／`Path contains CurrentVersion\Run Include` | 適合找 persistence / dropped file，見 [[persistence-mechanisms]] |
| 排除雜訊 | `Process Name is Procmon.exe Exclude` 等 | **不要一開始排除太多，否則會漏證據** |

## 常見誤判

| 現象 | 說明 |
|---|---|
| 大量 NAME NOT FOUND | 程式正常搜尋 DLL/config 也會產生 |
| `CreateFile` | 不一定建立檔案，也可能只是開啟既有檔案，見 [[dynamic-behavior-analysis]] 的 Disposition 說明 |
| `RegQueryValue` | 查詢不代表修改，見 [[persistence-mechanisms]] |
| ACCESS DENIED | 可能是正常權限測試 |
| Buffer Overflow（提示文字） | Windows 查詢長度常見，不等於 exploit |

## 與其他頁面的關聯

通常與 [[process-explorer]] 搭配使用（一個看程序關係與模組載入，一個看底層 I/O 行為），用來佐證 [[process-hollowing]] 等注入行為的實際影響。使用前的分析環境建置見 [[malware-analysis-vm-setup]]；檔案/Registry/網路事件的完整判讀方法見 [[dynamic-behavior-analysis]]；Registry 相關過濾與 persistence key 對照見 [[persistence-mechanisms]]。
