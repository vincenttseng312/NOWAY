---
type: concept
title: "動態行為分析（程序／檔案／Registry／網路）"
tags: [malware-analysis, dfir]
sources: [malware-static-dynamic-analysis-notes]
created: 2026-07-09
updated: 2026-07-09
---

# 動態行為分析

在隔離環境執行樣本並觀察真實行為：程序鏈、檔案寫入、Registry 寫入、網路連線。核心工具 Process Explorer 與 Process Monitor 的操作細節見 [[process-explorer]]、[[process-monitor]]；本頁聚焦「該觀察什麼、如何判讀」。

## 動態分析流程

前置準備 checklist：還原乾淨 snapshot、確認 VM 隔離（無 Host shared folder/clipboard）、記錄 VM 時間與樣本 hash、開啟 ProcExp/Procmon（清空事件）/TCPView/Wireshark、確認 Event Viewer/Sysmon logging。

六步流程：**Baseline**（觀察乾淨系統正常背景程序）→ **Pre-execution**（設定工具、開始 capture、記錄 T0）→ **Execution**（執行樣本，觀察程序樹/檔案/Registry/network）→ **Observation Window**（等待數十秒至數分鐘，注意 delayed execution/sleep，必要時互動）→ **Collection**（存 Procmon PML/Event Logs/PCAP/dropped files/截圖/IOC）→ **Reset**（還原 snapshot）。

觀察矩陣（面向 → 工具）：Process 用 ProcExp/Procmon/Sysmon EID 1；File 用 Procmon/Sysmon EID 11/23/26；Registry 用 Procmon/Autoruns/Sysmon EID 12/13/14；Network 用 TCPView/Wireshark/Sysmon EID 3/22；Memory 用 Process Hacker/Volatility（見 [[process-hollowing]]）。

## 程序行為分析

追蹤欄位：Process Name、PID/PPID、Parent Image、Command Line、User、Integrity Level、Start Time、Signer、Loaded DLLs、Child Processes。

正常程序鏈：`explorer.exe -> notepad.exe`、`services.exe -> svchost.exe`。可疑程序鏈：`WINWORD.EXE -> powershell.exe`（Office 不應啟動腳本解譯器）、`notepad.exe -> cmd.exe`（Notepad 不應啟動 shell）、`notepad.exe -> outbound network`（純文字編輯器對外連線異常，這正是既有 [[dynamic-link-library]] 頁「惡意程式分析應用」小節提到的 DLL 載入矛盾訊號的行為面對照）。

**Command Line 比 Process Name 更重要**：同樣是 `powershell.exe`，`-NoP -W Hidden -EncodedCommand <base64>` 風險遠高於單純 `powershell.exe`。判讀原則：Process Name 告訴你「誰」、Command Line 告訴你「它想做什麼」、Parent Process 告訴你「它為什麼出現」。

偽裝系統程序名稱（`svhost.exe` vs `svchost.exe`、`explore.exe` vs `explorer.exe`）——真正要看的是 Image Path + Signer + Parent + Command Line + Hash 的組合，而非單看名稱是否眼熟。

## 檔案系統行為分析

高風險路徑：`%TEMP%`、`%APPDATA%`、`%LOCALAPPDATA%`、`%PROGRAMDATA%`、`Downloads`、`Startup`。

Procmon Operation 對照：`CreateFile`（開啟/建立，**不一定代表建立新檔**，要看 Disposition 欄位：Open/Create/OpenIf/Overwrite）、`WriteFile`（dropped payload/config/ransom note）、`SetRenameInformationFile`（改名，ransomware 常見）、`SetDispositionInformationFile`（標記刪除，自刪或清痕跡）。

Dropped file 分析流程：記錄路徑 → 算 hash → 判斷類型 → 觀察是否被執行 → 觀察是否被寫入 persistence（見 [[persistence-mechanisms]]）→ 分析與原始樣本關係。

Ransomware 檔案行為特徵：大量 QueryDirectory/ReadFile/WriteFile/Rename、每個資料夾建立 ransom note、刪除 shadow copy 命令、停止資料庫/備份/安全服務——詳細行為階段見 [[malware-behavior-patterns]]。

## Registry 行為分析

常見 hive：HKLM（系統層級）、HKCU（目前使用者）、HKCR（檔案關聯，實際合併自 HKLM/HKCU）。

Procmon Registry Operation：`RegSetValue`/`RegCreateKey`（建立/寫入，最需要關注）、`RegQueryValue`（查詢，不代表修改）。

分析方法：Procmon filter 設 `Operation begins with Reg` → 先看 `RegSetValue`/`RegCreateKey` → 看 Path 是否落在自啟/安全/網路/瀏覽器相關 key → 對照程序鏈與時間 → 用 Autoruns 驗證是否變成自啟點 → 用 Sysmon EID 12/13/14 交叉驗證。五類常見 persistence registry key（Run/Winlogon/IFEO/AppInit_DLLs/Shell Open Command Hijack）詳見 [[persistence-mechanisms]]。

## 網路行為分析

要回答：哪個程序連線、連到哪個 domain/IP/port、DNS query 是什麼、HTTP method/User-Agent 是什麼、是否 beacon、是否下載第二階段。

工具分工：TCPView（process ↔ connection 快速對應）、Wireshark（封包級）、FakeNet-NG/INetSim（隔離環境模擬回應）、Sysmon EID 3（連線）/EID 22（DNS）。

TCPView 可疑情境：`notepad.exe -> remote 443`、`rundll32.exe -> unknown IP`、短命程序快速連線後退出。DNS 可疑特徵：隨機長字串 domain、大量 NXDOMAIN、新註冊 domain、罕見 TLD、DGA pattern。HTTP 可疑特徵：POST 到奇怪 URI、User-Agent 偽裝但格式錯誤、固定時間間隔 beacon、回傳 PE/script-like binary。HTTPS 無法看內容時仍可觀察 SNI、憑證 subject/issuer、目的 IP/ASN、timing/size pattern。

**Beaconing**（定期回連 C2）觀察特徵：固定間隔或帶 jitter、小封包、相同 URI pattern/User-Agent、失敗後重試、先 DNS 後 HTTP——分析不要只看單一連線，要看時間序列。

## 與其他頁面的關聯

工具具體操作見 [[process-explorer]]、[[process-monitor]]；持久化的完整分類見 [[persistence-mechanisms]]；PowerShell/LOLBin 專門的行為判讀見 [[lolbin-and-powershell-abuse]]；日誌層面的交叉驗證見 [[windows-event-log-and-sysmon]]；靜態分析階段建立的假設見 [[pe-static-analysis]]。
