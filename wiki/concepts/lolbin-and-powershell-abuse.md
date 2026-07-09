---
type: concept
title: "LOLBin 與 PowerShell 濫用行為分析"
tags: [malware-analysis, dfir, windows]
sources: [malware-static-dynamic-analysis-notes]
created: 2026-07-09
updated: 2026-07-09
---

# LOLBin 與 PowerShell 濫用行為分析

LOLBin（Living Off the Land Binary）指攻擊者濫用系統內建或合法工具達成惡意目的，藉此降低被偵測機率。這是動態分析中判讀「合法工具是否被惡意利用」的專門技巧，與 [[script-and-document-malware-analysis]] 中的 PowerShell 靜態觀察互補（一個看程式碼內容，一個看實際執行行為）。

## 常見 LOLBins

```text
powershell.exe  cmd.exe  rundll32.exe  regsvr32.exe  mshta.exe
wscript.exe  cscript.exe  certutil.exe  bitsadmin.exe  msiexec.exe
wmic.exe  schtasks.exe  reg.exe  sc.exe  installutil.exe  msbuild.exe
```

## LOLBin 分析不是背名單

**不要看到 `rundll32.exe` 就判惡意**。要看 Parent process、Command line、Target file/URL、Working directory、User、Network connection、File writes、Persistence changes、Frequency（是否符合 baseline 正常行為）。

## 高風險程序鏈

| Chain | 風險說明 |
|---|---|
| `WINWORD.EXE -> powershell.exe` | Office macro/exploit 常見 |
| `powershell.exe -> rundll32.exe` | 可能下載 DLL 後執行 |
| `wscript.exe -> powershell.exe` | Script dropper 常見 |
| `mshta.exe -> powershell.exe` | HTA 初始執行常見 |
| `regsvr32.exe -> network` | Scriptlet/remote COM 類濫用可能 |
| `certutil.exe -> file write` | 下載或解碼檔案可能（`certutil` 本用於憑證管理，常被濫用做 base64 解碼） |
| `bitsadmin.exe -> network` | 背景下載可能 |
| `wmic.exe -> process call create` | 遠端/本地程序建立可能 |

完整的程序鏈判讀原則（Command Line 比 Process Name 重要）見 [[dynamic-behavior-analysis]]。

## PowerShell 動態觀察

| 工具 | 看什麼 |
|---|---|
| ProcExp | parent / command line / signer，見 [[process-explorer]] |
| Procmon | file / registry / process activity，見 [[process-monitor]] |
| Event Viewer / Sysmon | PowerShell engine 與 script block 事件 |

PowerShell 重要 Event ID：400/403（engine 啟停）、4103（module logging）、**4104（script block logging——若啟用，可能看到被執行的腳本內容，對分析 PowerShell malware 非常有價值）**。完整 Sysmon/Event Log 對照見 [[windows-event-log-and-sysmon]]。

## 可疑 PowerShell 命令線索

```text
-NoProfile / -NoP        -ExecutionPolicy Bypass / -ep bypass
-WindowStyle Hidden / -w hidden
-EncodedCommand / -enc
IEX / Invoke-Expression   DownloadString   FromBase64String
Reflection.Assembly       Add-Type
```

判讀時要問：誰啟動 PowerShell、命令是否隱藏視窗、是否下載內容、是否從記憶體執行、是否寫入檔案、是否建立 persistence、是否是系統管理工具的正常作業（見 [[malware-analysis-methodology]] 的「不要只看單一證據」原則）。

## 與其他頁面的關聯

PowerShell 腳本本身的靜態解碼技巧見 [[script-and-document-malware-analysis]]；程序鏈與動態觀察工具見 [[dynamic-behavior-analysis]]、[[process-explorer]]、[[process-monitor]]；LOLBin 濫用對應的 MITRE ATT&CK Technique（如 T1059）見 [[ioc-ttp-and-detection-engineering]]。
