---
type: concept
title: "Persistence 持久化機制分析"
tags: [malware-analysis, dfir, windows]
sources: [malware-static-dynamic-analysis-notes]
created: 2026-07-09
updated: 2026-07-09
---

# Persistence 持久化機制分析

Persistence 是惡意程式讓自己在重開機、重新登入、服務啟動或特定事件後再次執行的能力。分析時要問：觸發條件是什麼、誰建立的、執行什麼、用誰的權限、設定存在哪裡、是否偽裝成合法項目、如何偵測與移除。

## 九種常見類型

| 類型 | 觸發 | 位置 | 權限需求 |
|---|---|---|---|
| Run Key | 使用者登入 | HKCU/HKLM Run | HKCU 較低，HKLM 較高 |
| Startup Folder | 使用者登入 | Startup folder | 使用者可寫 |
| Scheduled Task | 時間/登入/事件 | Task Scheduler | 視位置與權限 |
| Service | 開機/服務啟動 | SCM / services.exe | 通常需管理員 |
| WMI Event Subscription | WMI event | WmiPrvSE.exe | 通常需較高權限 |
| COM Hijacking | COM 物件載入 | HKCU/HKLM Classes | 視 hijack 類型 |
| DLL Search Order Hijacking | 程式載入 DLL | DLL 放置路徑 | 依目標路徑權限，機制見 [[dynamic-link-library]] |
| IFEO Debugger | 程序啟動 | IFEO registry | 通常需管理員 |
| Browser Extension | 瀏覽器啟動 | Browser profile/policy | 視瀏覽器與 policy |

## Registry 類 Persistence 細節

**Run / RunOnce**：`HKCU\Software\Microsoft\Windows\CurrentVersion\Run`（不需管理員）與對應 HKLM 路徑（通常需管理員）；惡意程式常用看似正常的 value name 偽裝。

**Winlogon**：`Winlogon\Shell`（正常應為 `explorer.exe`）、`Winlogon\Userinit`（正常應指向 `userinit.exe`）——被附加其他 executable 高風險。

**IFEO（Image File Execution Options）**：`...\Image File Execution Options\<process.exe>` 下的 `Debugger` value，原本用於除錯，可被惡意用於 hijack 特定程序啟動，或用於破壞安全工具啟動。

**AppInit_DLLs**：`...\Windows\AppInit_DLLs`，讓特定 GUI 程序載入指定 DLL，現代 Windows 有更多限制，但仍是分析時該知道的 persistence/injection 跡象。

**Shell Open Command Hijack**：`HKCR\exefile\shell\open\command`、`HKCR\txtfile\shell\open\command`——改變開啟特定檔案類型時執行的命令，可能造成每次開 EXE/TXT 都觸發惡意程式。

## 各類型的證據鏈與工具觀察

**Run Key**：`malware.exe -> RegSetValue HKCU\...\Run\<value> Data: C:\Users\...\payload.exe`。工具：Procmon（`RegSetValue` 時間與寫入程序）、Autoruns（Logon tab 新項目）、Sysmon EID 13。

**Scheduled Task**：`sample.exe -> schtasks.exe/Task Scheduler API -> 建立 task XML -> Task Scheduler service 執行 payload`。觀察 task name 是否偽裝系統名、Trigger 類型（At logon/Daily/On idle）、Action 路徑與 arguments、Run as user。

**Service**：`sample.exe -> service creation -> services.exe -> service binary path 指向 payload`。觀察 Service name/ImagePath/Start type/Account 是否偽裝 Microsoft/driver/updater、binary 是否 unsigned、路徑是否在 AppData。**Event Log 關鍵：System Log Event ID 7045（服務被安裝）**。

**WMI Event Subscription**：三要素 Event Filter + Event Consumer + Binding，常見程序 `WmiPrvSE.exe`。分析重點是清查與偵測，不應撰寫危險 payload。

## Autoruns Persistence Review Checklist

```text
[ ] Hide Microsoft Entries + Verify Code Signatures
[ ] 檢查 Logon / Scheduled Tasks / Services / Drivers
[ ] 檢查 AppInit / Image Hijacks / KnownDLLs / Winsock Providers
[ ] 檢查 Office Addins / Browser Helper Objects
[ ] 匯出 baseline 與 post-run 差異比對
```

Autoruns 分析技巧：先存 baseline → 執行樣本後再存一次 → 比較新增項目 → 檢查 signer 與路徑 → 對新增 executable 算 hash → 回到 Procmon/Sysmon 找出是誰建立它。

## 與其他頁面的關聯

Registry 操作的工具細節見 [[process-monitor]]；程序鏈判讀原則見 [[dynamic-behavior-analysis]]；DLL Search Order Hijacking 的 DLL 載入機制見 [[dynamic-link-library]]；每種 persistence 類型對應的 MITRE ATT&CK Technique 見 [[ioc-ttp-and-detection-engineering]]。
