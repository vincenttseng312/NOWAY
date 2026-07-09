---
type: concept
title: "進程掏空（Process Hollowing）"
tags: [malware-analysis, dfir, windows]
sources: [malware-dynamic-analysis, malware-static-dynamic-analysis-notes]
created: 2026-07-08
updated: 2026-07-09
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

## Process Hollowing 概念流程

```text
1. 建立一個看似正常的程序，通常是 suspended state
2. 移除或覆蓋原本記憶體映像
3. 放入惡意 payload
4. 修改執行緒 context
5. resume thread
6. 外觀看起來是合法程序，實際跑的是另一段程式碼
```

分析核心原則：**程序名稱看起來正常，不代表記憶體內容正常**——要比對 disk image、memory image、loaded modules、thread start address、network 行為。

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

## 如何在動態分析中發現特徵矛盾（DLL 載入訊號）

依 [[malware-dynamic-analysis]] 的紀錄，判斷是否發生 Process Hollowing 的一個實用線索是「載入的 DLL 與程序本身的正常功能不符」：

- 用 [[process-explorer]] 觀察目標程序底層載入的 DLL 清單。
- `ntdll.dll` 幾乎任何程式都會載入，不具判斷力。
- 但如果一個**本身不該有網路功能**的純文字程式（例如 `notepad.exe`）底層卻載入了 `ws2_32.dll` 或 `wininet.dll`（這兩者是掌管網路通訊的系統 [[dynamic-link-library|DLL]]），這種「功能與載入模組不匹配」的矛盾，就是該程序已被惡意代碼注入、正在進行 C2 連線或資料外洩的高機率訊號。

這是一種間接、基於行為觀察的偵測手法，而非直接偵測注入動作本身；配合 [[process-monitor]] 側錄該程序的檔案／登錄檔／網路行為，可以進一步佐證。

## 與其他頁面的關聯

- [[dynamic-link-library]] —— DLL 載入機制本身
- [[process-explorer]] —— 用來觀察程序 DLL 清單與 handles/threads 的工具
- [[process-monitor]] —— 用來佐證程序實際行為的工具
- [[dynamic-behavior-analysis]] —— 程序行為分析的通用方法
- [[ioc-ttp-and-detection-engineering]] —— 對應的 MITRE ATT&CK Technique
- [[windows-event-log-and-sysmon]] —— Sysmon EID 8/10 的關聯分析
