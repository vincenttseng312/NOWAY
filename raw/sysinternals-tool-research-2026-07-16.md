# Sysinternals Process Explorer and Process Monitor Official Research (2026-07-16)

> 本檔是官方資料研究清冊，不是原文副本；版本與支援作業系統須在下載日重新確認。

## Process Explorer

- 官方頁面：https://learn.microsoft.com/sysinternals/downloads/process-explorer
- 2026-07-16 擷取：Process Explorer v17.12；官方頁面列 Client Windows 11+、Server Windows Server 2016+。
- 功能：上方程序清單；下方 Handle mode 顯示開啟物件，DLL mode 顯示 DLL 與 memory-mapped files；可搜尋特定 handle/DLL。
- 安裝：直接執行 `procexp.exe`。Symbol server 設定需正確搭配 `DBGHELP.DLL` 與 `SYMSRV.DLL`。

## Process Monitor

- 官方頁面：https://learn.microsoft.com/en-us/sysinternals/downloads/procmon
- 2026-07-16 擷取：Process Monitor v4.04；官方頁面列 Client Windows 10+、Server Windows Server 2012+。
- 功能：即時檔案系統、Registry、process/thread 活動；non-destructive filters、process tree、thread stacks、native log format、同時記錄檔案與 boot logging。
- Trace 可達數千萬事件和數 GB，應先設定 filter、保存位置與磁碟配額。

## 限制

- 本機未下載或執行 Sysinternals 工具，也未處理惡意樣本。
- Windows 10 lab 不應假定最新版 Process Explorer 仍受官方支援；先在非關鍵 VM 驗證相容性。
