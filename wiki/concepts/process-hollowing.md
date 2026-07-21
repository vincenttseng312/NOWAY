---
type: concept
title: "進程掏空（Process Hollowing）"
tags: [malware-analysis, dfir, windows]
sources: [malware-dynamic-analysis, malware-static-dynamic-analysis-notes]
created: 2026-07-08
updated: 2026-07-17
---

# 進程掏空（Process Hollowing）

一種惡意程式常用的程序注入技術：攻擊者啟動一個看似合法、不具威脅性的程序（例如 `notepad.exe`），但將其記憶體內容替換或掏空，植入惡意程式碼後在其中執行 —— 讓惡意行為偽裝成一個「正常」的系統程序，以規避基於程序名稱或簽章的偵測。對應 MITRE ATT&CK **T1055.012**（Process Hollowing，屬於 T1055 Process Injection 的子技術），完整對照見 [[ioc-ttp-and-detection-engineering]]。

> 本頁只記錄概念與偵測證據，不提供實作程式碼——這也是原始筆記明確設下的安全邊界。

## Process Injection 概念與相關 API

Process Injection 是把程式碼放到另一個正在執行的程序位址空間中執行，藉此偽裝成合法程序、逃避以程序名稱為主的偵測、使用目標程序的權限或網路存取能力、隱藏真正 payload。

以下 API 在靜態或動態分析中看到時代表需要進一步觀察，但**不能單獨定罪**：

```text
OpenProcess          VirtualAllocEx        WriteProcessMemory
ReadProcessMemory     CreateRemoteThread    QueueUserAPC
SetThreadContext      ResumeThread          NtMapViewOfSection
```

## Process Hollowing 概念流程與常見 API

```text
1. CreateProcess + CREATE_SUSPENDED：建立暫停狀態的合法程序
2. NtUnmapViewOfSection / ZwUnmapViewOfSection：移除或掏空原映像
3. VirtualAllocEx：在目標程序配置記憶體
4. WriteProcessMemory：寫入替代 payload
5. SetThreadContext：把執行緒 context 指向新進入點
6. ResumeThread：恢復執行
```

這是常見分析模型，不是每個樣本都會完整使用相同 API 或順序。不同實作可能覆寫映像而不先 unmap、改用 section mapping，或使用其他執行緒操作。分析核心原則是：**程序名稱與簽章看起來正常，不代表記憶體內容正常**——需比對 disk image、memory image、PE header、thread start address 與後續行為。MITRE ATT&CK 對此技術的定義與程序範例見 [T1055.012 Process Hollowing](https://attack.mitre.org/techniques/T1055/012/)。

> [!WARNING]
> API 名稱只能形成調查方向。安裝程式、除錯器、EDR 與其他合法軟體也可能使用部分跨程序 API；必須確認目標程序、時間順序、記憶體權限與執行流是否共同符合 Hollowing。

## Hollowing 可疑證據清單

```text
[ ] 子程序以 suspended 方式建立後才開始活動
[ ] Parent process 可疑
[ ] Image path 正常但 command line 奇怪
[ ] Memory 中 PE header 與 disk 不一致
[ ] Thread start address 不在 image section
[ ] Legitimate-looking process 載入不合理 DLL
[ ] Legitimate-looking process 對外連線或寫入 persistence
```

Injection 更廣義的證據（不限 Hollowing）：A 程序開啟 B 程序 handle、A 對 B 寫入記憶體、B 出現可疑 remote thread、thread start address 不在正常 module 範圍、記憶體區域是 private/executable、**Sysmon Event ID 8（CreateRemoteThread）／10（ProcessAccess）出現可疑關聯**（見 [[windows-event-log-and-sysmon]]）。

## 記憶體異常觀察工具

| 工具 | 可觀察 |
|---|---|
| Process Explorer | DLL、handles、threads、network、signer，見 [[process-explorer]] |
| Process Hacker / System Informer | memory regions、thread start address |
| Volatility | process list、dll list、malfind、netscan、cmdline |
| EDR | cross-process activity、memory injection telemetry |
| Sysmon | ProcessAccess / CreateRemoteThread 類事件 |

## 如何使用 DLL 載入訊號建立假設

依 [[malware-dynamic-analysis]] 的紀錄，判斷是否發生 Process Hollowing 的一個實用線索是「載入的 DLL 與程序本身的正常功能不符」：

- 用 [[process-explorer]] 觀察目標程序底層載入的 DLL 清單。
- `ntdll.dll` 幾乎任何程式都會載入，不具判斷力。
- 如果一個**依既有基線不應有網路功能**的程序（例如一般情況下的 `notepad.exe`）載入 `ws2_32.dll` 或 `wininet.dll`，可把「功能與載入模組不匹配」列為待查異常。但 DLL 可能由合法相依元件間接載入，這個現象本身不能證明注入、C2 或資料外洩。

這是一種間接線索，而非注入證據。應進一步確認 DLL 完整路徑、簽章與雜湊，並交叉比對實際網路連線、Sysmon EID 8／10、EDR cross-process telemetry、memory image 與 thread start address；[[process-monitor]] 可補充檔案與 Registry 行為，但不等同記憶體鑑識。

## 與其他頁面的關聯

- [[dynamic-link-library]] —— DLL 載入機制本身
- [[process-explorer]] —— 用來觀察程序 DLL 清單與 handles/threads 的工具
- [[process-monitor]] —— 用來佐證程序實際行為的工具
- [[dynamic-behavior-analysis]] —— 程序行為分析的通用方法
- [[ioc-ttp-and-detection-engineering]] —— 對應的 MITRE ATT&CK Technique
- [[windows-event-log-and-sysmon]] —— Sysmon EID 8/10 的關聯分析
