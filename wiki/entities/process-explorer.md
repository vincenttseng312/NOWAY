---
type: entity
title: "Process Explorer (ProcExp)"
tags: [sysinternals, malware-analysis, dfir]
sources: [malware-dynamic-analysis, malware-static-dynamic-analysis-notes, sysinternals-tool-research-2026-07-16]
created: 2026-07-08
updated: 2026-07-17
---

# Process Explorer (ProcExp)

微軟 Sysinternals 工具集中的程序檢視工具，在惡意程式動態分析中用來觀察系統中所有執行中程序的父子關係與底層載入的模組（DLL），俗稱「程序照妖鏡」。

## 核心觀念：父子程序關係

系統中任何程式都由另一個程式啟動，形成樹狀的父子關係：

- **常見基線**：使用者透過桌面或開始功能表啟動一般 GUI 程式時，父程序常是 `explorer.exe`；但捷徑、排程、服務、應用程式啟動器與管理工具都可能形成其他合法父程序。
- **待查偏差（LOLBins／巨集）**：`WINWORD.EXE` 產生 `cmd.exe` 或 `powershell.exe` 是高價值調查線索，仍需比對文件來源、命令列、使用者操作與後續行為，不能只憑父子名稱定性。

## 進階觀察：DLL 載入清單

ProcExp 可檢視每個程序底層載入的 DLL，用來輔助判斷程序行為是否異常：

- `ntdll.dll` 是系統核心的必經路徑，任何程式都會載入，不具判斷力。
- `ws2_32.dll`／`wininet.dll` 是掌管網路通訊的系統模組。
- 若一個依乾淨基線不應有網路行為的程序（如一般情況下的 `notepad.exe`）載入了 `ws2_32.dll`，可先建立「相依模組、外掛、注入或異常網路功能」等競爭假設。單一 DLL 載入不能直接證明 [[process-hollowing]]、C2 或資料外洩。

> [!WARNING]
> Process Explorer 的程序樹、簽章、DLL 與 UI 顏色主要用來產生假設。結論至少要再由命令列、實際連線、Sysmon／EDR、檔案行為或記憶體證據支持。

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

## Windows 安裝、相容性與驗證

從 Microsoft Sysinternals 官方頁或受管理的 Sysinternals Suite 取得工具；直接執行 `procexp.exe`，不需要傳統安裝。2026-07-16 的官方最新頁面列 Process Explorer 支援 Client Windows 11+、Server 2016+；因此現有 Windows 10 lab 不可直接假定最新版仍受官方支援，應先在非關鍵 VM 驗證實際版本與相容性。

```powershell
# 建立目前使用者的工具資料夾，確認從 Microsoft 官方頁下載並解壓的檔案存在。
$sysinternalsDir = Join-Path $HOME "Tools\Sysinternals"
New-Item -ItemType Directory -Path $sysinternalsDir -Force | Out-Null
Get-ChildItem -LiteralPath $sysinternalsDir -Filter "procexp*.exe"

# 依實際檔名調整路徑，再計算雜湊供下載驗證或軟體清單使用。
Get-FileHash -LiteralPath (Join-Path $sysinternalsDir "procexp64.exe") -Algorithm SHA256
```

`Get-ChildItem` 應列出工具檔案；初次啟動後接受 Sysinternals EULA，成功時會看到程序樹。若只看到 `procexp.exe`，請改用其實際檔名；不要從不明鏡像下載執行檔。

## 快速開始：安全練習流程

1. 在一般 Windows VM 啟動 `notepad.exe`，再開啟 Process Explorer。
2. 找到該程序，確認 Parent、Image Path、User Name 與 Command Line 是否合理。
3. 切換下方窗格到 DLL mode，觀察載入模組；系統 DLL 本身不是惡意證據。
4. 以 Search 找一個明確檔名或 handle，確認結果能回指持有它的程序。
5. 記錄 PID、時間、完整路徑與命令列；需追查 I/O 時改用 [[process-monitor]]。

## 常見錯誤與排解

### 看不到系統程序的完整細節

可能是權限不足。只在自有 lab 或已授權系統以系統管理員身分重新啟動工具；不要在正式主機長期以高權限執行未驗證工具。

### DLL mode 資訊不足或程序已消失

確認下方窗格已開啟且模式正確。短命程序應先保存 PID/時間，再用 [[windows-event-log-and-sysmon]] 或 Procmon trace 重建時間線。

### Windows 10 啟動失敗

先確認實際版本與官方支援矩陣。不要尋找第三方「修補版」；改在支援的 Windows 11 分析 VM 測試，或依組織核准的舊版工具政策處理。

> [!TIP]
> 以 Process Explorer 產生假設，再以 Procmon、Sysmon 或其他遙測驗證。名稱、單一 DLL 或 UI 顏色都不應是結論。

官方支援範圍、下載驗證與工具比較的研究紀錄見 [[sysinternals-tool-research-2026-07-16]]。
