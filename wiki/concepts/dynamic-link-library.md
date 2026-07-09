---
type: concept
title: "動態連結程式庫（Dynamic Link Library, DLL）"
tags: [windows, dll]
sources: [dll-ms-learn]
created: 2026-07-08
updated: 2026-07-08
---

# 動態連結程式庫（Dynamic Link Library, DLL）

DLL 是 Windows 的一種函式庫檔案，內含可供多個程式在執行期間同時共用的程式碼與資料，而不是每個程式各自靜態內嵌一份副本。這是 Windows 上絕大多數作業系統功能與應用程式功能的基礎 —— 作業系統本身，以及大部分非瑣碎的程式，都是以一組 DLL 加上一個小型可執行檔（負責載入它們）的形式發佈。

## 為什麼需要 DLL

- **節省資源**：共用程式碼只需在記憶體／磁碟中載入一份，不必每個程式各自重複。
- **模組化架構**：大型程式（例如一套會計軟體）可以拆成可獨立載入的模組發佈，只在需要時才載入,同時也能加快啟動速度。
- **部署更容易**：修補其中一個 DLL，所有使用它的程式都能受惠，不需要重新連結或重新安裝整個應用程式。

常見以 DLL 形式打包的檔案類型：ActiveX 控制項（`.ocx`）、控制台項目（`.cpl`）、裝置驅動程式（`.drv`）。

## 連結方式

應用程式呼叫 DLL 匯出函式有兩種方式：

- **載入時期動態連結（load-time dynamic linking）**：應用程式在編譯時期就連結 `.lib` import library 與 `.h` 標頭檔；匯出的函式之後可像一般本地函式一樣直接呼叫。這種方式最容易使用，但如果 DLL 遺失，整個應用程式會直接無法啟動。
- **執行時期動態連結（run-time dynamic linking）**：應用程式在執行期間明確呼叫 `LoadLibrary`/`LoadLibraryEx` 載入 DLL，再用 `GetProcAddress` 解析每個函式指標。不需要 import library。適用於在意啟動效能，或應用程式需要在執行期間分支載入不同模組（例如載入特定語系的模組）的情境 —— 若該 DLL 遺失，只有那個 DLL 載入失敗，不會拖垮整個應用程式。

## DLL 進入點（`DllMain`）

DLL 可以指定一個進入點函式，會在程序／執行緒附加或卸離時被呼叫（`DLL_PROCESS_ATTACH`、`DLL_THREAD_ATTACH`、`DLL_THREAD_DETACH`、`DLL_PROCESS_DETACH`），用來初始化或釋放資料結構（在多執行緒 DLL 中，也可用來配置執行緒本地儲存體 TLS，作為每個執行緒私有的狀態）。

值得記住的限制：進入點函式只該做簡單的初始化工作 —— **不可以**（直接或間接地）呼叫 `LoadLibrary`/`LoadLibraryEx` 或 `FreeLibrary`，且對 DLL 全域資料的存取必須跨執行緒同步。在載入時期連結下，若進入點回傳 `FALSE` 會導致整個應用程式無法啟動；而在執行時期連結下，只有該 DLL 本身載入失敗。

## 匯出函式

DLL 匯出函式有兩種機制：
- 函式關鍵字：在定義端使用 `__declspec(dllexport)`，在使用端使用 `__declspec(dllimport)`（通常透過同一個標頭檔搭配 `#ifdef` 統一處理）。
- 模組定義檔（`.def`）：宣告 `LIBRARY` 與 `EXPORTS` 陳述式 —— 不需要在函式本身加上關鍵字標註。

## DLL 搜尋順序

在依名稱解析 DLL 時，Windows 會依序搜尋：應用程式所在資料夾 → 目前工作目錄 → Windows 系統資料夾（`GetSystemDirectory`）→ Windows 資料夾（`GetWindowsDirectory`）。

## 疑難排解工具

- **Dependency Walker** —— 遞迴掃描程式的 DLL 相依關係；檢查遺失的 DLL、無效的模組、匯入／匯出函式不匹配、循環相依，以及因作業系統不符而無效的模組。隨 Visual Studio 6.0 附贈。
- **DUPS（DLL Universal Problem Solver）** —— 用來稽核、比對、記錄整台機器上 DLL 的工具組：`Dlister.exe` 列舉所有已安裝的 DLL，`Dcomp.exe` 比對兩份 DLL 清單的差異，`Dtxt2DB.exe`／`DlgDtxt2DB.exe` 將結果匯入名為「dllHell」的資料庫。
- **DLL Help 資料庫** —— 用來定位微軟產品所發佈的特定版本 DLL。

## 在惡意程式分析中的應用

DLL 的載入清單也是動態惡意程式分析中常用的判讀依據：`ntdll.dll` 幾乎任何程式都會載入、不具判斷力，但若一個本身不具備網路功能的程式（例如 `notepad.exe`）底層卻載入了 `ws2_32.dll`／`wininet.dll` 這類網路通訊 DLL，這種功能與載入模組的矛盾，是 [[process-hollowing]]（進程掏空）的典型訊號，可用 [[process-explorer]] 觀察到。詳見 [[malware-dynamic-analysis]]。

## 與其他頁面的關聯

這些工具所要診斷的「依賴關係毀損」問題，詳見 [[dll-dependency-hell]]。微軟為了徹底避開這類問題而打造的架構後繼者，見 [[dotnet-assembly]]。
