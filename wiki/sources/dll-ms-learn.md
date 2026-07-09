---
type: source
title: "Dynamic link library (DLL) - Windows Client | Microsoft Learn"
authors: ["Microsoft (kaushika-msft)"]
url: "https://learn.microsoft.com/en-us/troubleshoot/windows-client/setup-upgrade-and-drivers/dynamic-link-library"
raw: "raw/dll-ms-learn.md"
ingested: 2026-07-08
tags: [windows, dll, dotnet]
entities: []
concepts: [dynamic-link-library, dll-dependency-hell, dotnet-assembly]
---

# Dynamic link library (DLL) - Windows Client | Microsoft Learn

這是一篇 Microsoft Learn 的技術支援／疑難排解文件（KB 815065，適用於 Windows 10），內容涵蓋 DLL 是什麼、DLL 的連結與結構方式、DLL 造成的依賴問題（俗稱「DLL Hell」）、Windows 的緩解措施，以及 .NET assembly 如何被設計來取代這套模型。

## 重點主張

- DLL 是一個可供多個程式同時使用的程式碼／資料函式庫；這能減少磁碟／記憶體的重複佔用，促進模組化的程式架構，並讓各模組能獨立更新／修補，不需重新連結整個程式。
- 兩種連結方式：**載入時期動態連結（load-time dynamic linking）**（編譯時期，透過 `.h` + `.lib`，匯出的函式可像本地函式一樣直接呼叫）與**執行時期動態連結（run-time dynamic linking）**（`LoadLibrary`/`LoadLibraryEx` + `GetProcAddress`，不需要 import library，適用於在意啟動效能，或應用程式需要在執行時期分支載入不同模組的情境）。
- **DLL 依賴問題／「DLL Hell」**：當程式依賴某個 DLL，而該 DLL 之後被升級、修補、降版或移除時，依賴它的程式可能就會壞掉。Windows 2000 之後引入了 Windows File Protection（阻擋未授權變更系統 DLL）與私有 DLL（Private DLL，透過 `.local` 檔或版本資訊將程式釘選在自己的副本上）來緩解這個問題。
- 載入時的 DLL 搜尋順序：應用程式所在資料夾 → 目前工作目錄 → Windows 系統資料夾 → Windows 資料夾。
- `DllMain` 進入點負責處理程序／執行緒的附加與卸離；微軟明確警告不要在其中呼叫 `LoadLibrary`/`FreeLibrary`（進入點內只該做簡單的初始化／收尾工作）。
- 匯出函式需要 `__declspec(dllexport)`/`__declspec(dllimport)` 關鍵字，或是使用模組定義檔（`.def`）。
- 文章將 **.NET assembly** 定位為 DLL Hell 的解方（見 [[dll-ms-learn]] 本文論述脈絡）：assembly 具備自我描述能力（manifest 列出相依項目、版本、strong name）、CLR 強制執行版本控管，並支援並存部署（side-by-side deployment）——這些都是 Win32 DLL 原生不具備的特性。

## 文中提到的疑難排解工具

Dependency Walker（遞迴掃描相依 DLL 的工具）、DUPS／DLL Universal Problem Solver（Dlister.exe、Dcomp.exe、Dtxt2DB.exe、DlgDtxt2DB.exe —— 用來稽核、比對、記錄 DLL）、以及 DLL Help 資料庫（用來定位特定版本的 DLL）。這些工具在文中只是帶過的細節，並未展開成獨立頁面 —— 併入 [[dynamic-link-library]] 頁面中一併說明。

## 與其他頁面的關聯

- [[dynamic-link-library]]
- [[dll-dependency-hell]]
- [[dotnet-assembly]]
