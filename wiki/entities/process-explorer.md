---
type: entity
title: "Process Explorer (ProcExp)"
tags: [sysinternals, malware-analysis, dfir]
sources: [malware-dynamic-analysis, malware-static-dynamic-analysis-notes]
created: 2026-07-08
updated: 2026-07-09
---

# Process Explorer (ProcExp)

微軟 Sysinternals 工具集中的程序檢視工具，在惡意程式動態分析中用來觀察系統中所有執行中程序的父子關係與底層載入的模組（DLL），俗稱「程序照妖鏡」。

## 核心觀念：父子程序關係

系統中任何程式都由另一個程式啟動，形成樹狀的父子關係：

- **正常行為**：使用者透過雙擊檔案或開始功能表啟動的程式，其父程序應為 `explorer.exe`（檔案總管）。
- **異常行為（LOLBins／巨集病毒）**：若觀察到 `WINWORD.EXE`（Word）在背景產生出 `cmd.exe` 或 `powershell.exe` 這類子程序，高機率代表惡意巨集正在執行 —— 這是判斷「living-off-the-land」式攻擊手法的常見線索。

## 進階觀察：DLL 載入清單

ProcExp 可檢視每個程序底層載入的 DLL，用來輔助判斷程序行為是否異常：

- `ntdll.dll` 是系統核心的必經路徑，任何程式都會載入，不具判斷力。
- `ws2_32.dll`／`wininet.dll` 是掌管網路通訊的系統模組。
- 若一個本身不具備上網功能的程式（如 `notepad.exe`）底層卻載入了 `ws2_32.dll`，這種功能與載入模組的矛盾，是 [[process-hollowing]]（進程掏空）的典型訊號 —— 代表該程序極可能已被惡意代碼注入，正在進行 C2 連線或資料外洩。

## 建議觀察欄位與檢查清單

實務上建議顯示的欄位：Process Name、PID、CPU、Private Bytes、Command Line、Image Path、Verified Signer、User Name、Integrity Level、Company Name、Start Time。

觀察重點 checklist：

```text
[ ] 程序樹是否合理
[ ] 路徑是否正常
[ ] 簽章是否正常
[ ] 是否載入不合理 DLL
[ ] 是否有可疑 handles
[ ] 是否有異常 network tab
[ ] 是否有短時間消失程序
```

「異常 network tab」與「可疑 handles」是判讀 [[process-hollowing]]（進程掏空）的重要輔助證據——記憶體層面的異常（如 thread start address 不在 image section）需要搭配 Process Hacker/Volatility 等更深入的工具才能確認，ProcExp 主要提供第一層的行為與模組線索。程序鏈的正常/異常判讀原則（Command Line 比 Process Name 更重要）見 [[dynamic-behavior-analysis]]。

## 與其他頁面的關聯

DLL 載入機制的一般性說明見 [[dynamic-link-library]]；用這項工具偵測到的具體攻擊手法見 [[process-hollowing]]；使用這項工具前的安全環境建置見 [[malware-analysis-vm-setup]]；程序鏈判讀的完整方法論見 [[dynamic-behavior-analysis]]。搭配觀察系統底層行為（檔案／登錄檔／網路）的互補工具是 [[process-monitor]]。
