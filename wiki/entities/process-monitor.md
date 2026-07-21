---
type: entity
title: "Process Monitor (Procmon)"
tags: [sysinternals, malware-analysis, dfir]
sources: [malware-dynamic-analysis, malware-static-dynamic-analysis-notes, sysinternals-tool-research-2026-07-16]
created: 2026-07-08
updated: 2026-07-16
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

## Windows 安裝、相容性與 trace 保存

從 Microsoft Sysinternals 官方頁或 Suite 下載後直接執行 `Procmon.exe`。2026-07-16 的官方頁列出 Process Monitor v4.04 支援 Client Windows 10+、Server 2012+；你的 Windows 10 lab 屬於此範圍，但下載日仍應重新確認版本。Procmon trace 會含路徑、帳號、命令列和檔名，應視為敏感鑑識資料。

```powershell
# 確認已由官方頁下載並解壓的 Procmon 檔案；此步驟不會啟動側錄。
$sysinternalsDir = Join-Path $HOME "Tools\Sysinternals"
New-Item -ItemType Directory -Path $sysinternalsDir -Force | Out-Null
Get-ChildItem -LiteralPath $sysinternalsDir -Filter "Procmon*.exe"
Get-FileHash -LiteralPath (Join-Path $sysinternalsDir "Procmon64.exe") -Algorithm SHA256
```

Procmon trace 可達數千萬事件和數 GB；開始前指定專用輸出資料夾、可用磁碟空間與保存期限，避免在無 filter 狀態下長時間側錄。

## 快速開始：對自有程序建立最小 PML

1. 啟動 Procmon，先停止擷取並清空既有事件。
2. 按 `Ctrl+L`，加入 `Process Name is notepad.exe Include`。
3. 啟動並操作 `notepad.exe`，例如開啟、儲存一個測試文字檔。
4. 停止擷取，檢查 Operation、Path、Result、Detail、PID 與 Time of Day。
5. 用 **File → Save** 儲存原生 PML 到案例資料夾，連同 filter、工具版本與開始/結束時間保存。

預期可看到 `CreateFile`、`ReadFile` 或 `WriteFile`。這是安全 GUI 練習，未在本機實測；不同版本的 Windows 與程式會產生不同事件。

## 證據保存與常見排解

| 問題 | 常見原因 | 處理方式 |
|---|---|---|
| 事件量暴增 | 全系統、無 filter 長時間側錄 | 停止擷取、保存/清空後，只以單一程序或路徑 Include。 |
| 大量 `NAME NOT FOUND` | 程式正常探測檔案/DLL/config | 用同一 PID 的前後事件、Detail 與時間線判讀，不單獨定性。 |
| `ACCESS DENIED` | 權限檢查或存取被拒 | 交叉比對帳號、Integrity、Security Event 與應用程式 log。 |
| 看不到 stack/程序細節 | 權限、符號設定或程序快速結束 | 記錄限制，改用 [[windows-event-log-and-sysmon]] 或隔離副本取證。 |

> [!WARNING]
> 不要為了取得資料而關閉防護、終止系統程序或在正式主機用無 filter 的 Procmon 長時間側錄。處理不可信樣本只限 [[malware-analysis-vm-setup]] 的隔離環境。

官方支援範圍、下載驗證與工具比較的研究紀錄見 [[sysinternals-tool-research-2026-07-16]]。
