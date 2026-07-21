---
type: concept
title: "IOC、TTP、MITRE ATT&CK 與 Detection Engineering"
tags: [malware-analysis, dfir]
sources: [malware-static-dynamic-analysis-notes, range-main, threat-hunting-course-final-report]
created: 2026-07-09
updated: 2026-07-20
---

# IOC、TTP、MITRE ATT&CK 與 Detection Engineering

分析結束後如何把發現轉化為可用的偵測與封鎖依據。IOC vs TTP 的基本區分見 [[malware-analysis-methodology]]；本頁聚焦具體的分類、對應框架與規則撰寫。

## IOC 類型與穩定性

| IOC 類型 | 例子 | 穩定性 |
|---|---|---|
| Hash | SHA256 | 低到中，改檔即失效 |
| File path | `%APPDATA%\abc.exe` | 中，容易改 |
| Registry key | HKCU Run value | 中 |
| Domain | example.com | 中 |
| IP | 1.2.3.4 | 低，CDN/雲端常變 |
| Mutex | Global\abc | 中到高，視家族而定 |
| Certificate | signer/serial | 中 |
| **Behavior chain** | Office -> PowerShell -> network | **高**（TTP 層級最穩定） |

IOC 表格模板分 File / Network / Host Indicators 三類，各含 Type/Value/Description/Confidence 欄位。

## MITRE ATT&CK 常見對應

| 行為 | ATT&CK Technique |
|---|---|
| 使用者執行惡意檔案 | T1204 User Execution |
| PowerShell / cmd | T1059 Command and Scripting Interpreter |
| Registry Run Key | T1547.001 Registry Run Keys / Startup Folder |
| Scheduled Task | T1053.005 |
| Service persistence | T1543.003 Windows Service |
| WMI Event Subscription | T1546.003 |
| Process Injection | T1055 |
| **Process Hollowing** | **T1055.012**（見 [[process-hollowing]]） |
| Ingress Tool Transfer | T1105 |
| Data encrypted for impact | T1486（見 [[malware-behavior-patterns]] 的 Ransomware） |
| Indicator removal | T1070 |
| Credential access to LSASS | T1003.001（僅作偵測概念） |

這張對照表是 [[malware-analysis-report-template]] 中「MITRE ATT&CK Mapping」章節的依據，每種 [[persistence-mechanisms]] 類型也都有對應的 Technique ID。

## Detection Engineering 思維

偵測規則不應只靠單點判斷，品質分三級：

```text
低品質：alert when process_name = powershell.exe

較佳：alert when
  ParentImage in WINWORD.EXE/EXCEL.EXE/OUTLOOK.EXE
  AND Image = powershell.exe
  AND CommandLine contains suspicious flags or network download behavior

更佳：Office process spawns script interpreter
  followed by network connection
  followed by file write to user-writable path
  followed by persistence registry modification
  within 5 minutes
```

這正是把 [[dynamic-behavior-analysis]] 中觀察到的程序鏈、網路、檔案、Registry 證據串成單一偵測邏輯的具體實作方式。

## 偵測規則的四態驗證

規則有沒有命中不能只用 pass/fail 表示。依 [[detection-validation-range]]，每個預期 forensic signal 應按證據分成：

| 狀態 | 判斷依據 | 工程含義 |
|---|---|---|
| `None` | 原始 sensor 資料不存在 | 先修 telemetry，不應先改規則 |
| `Telemetry` | 原始事件存在，但沒有規則／告警 | 建立 parser、field mapping 或偵測邏輯 |
| `Failed` | 規則存在，但對 ground truth 未命中 | 檢查條件、欄位版本、門檻與 TTP 變體 |
| `Success` | 命中且能追溯至 ground truth | 納入 regression corpus，持續檢查誤報與退化 |

每次規則更新都應對固定的 PCAP／EVTX／解析後事件 corpus 重放，並記錄規則 hash、sensor 版本、預期訊號與結果差異。這才是 detection regression；單一 dashboard 截圖只能證明某次曾命中。

## Sigma Rule 概念模板

```yaml
title: Office Spawns Script Interpreter
logsource:
  product: windows
  category: process_creation
detection:
  selection_parent:
    ParentImage|endswith: ['\WINWORD.EXE', '\EXCEL.EXE', '\OUTLOOK.EXE']
  selection_child:
    Image|endswith: ['\powershell.exe', '\cmd.exe', '\wscript.exe', '\mshta.exe']
  condition: selection_parent and selection_child
falsepositives: [legitimate Office add-ins, enterprise automation]
level: high
```

## YARA Rule 撰寫原則

```text
[ ] 避免只用一個常見字串
[ ] 使用多個 family-specific marker
[ ] 搭配 PE 條件（例如 uint16(0) == 0x5A4D 判斷 MZ magic bytes）
[ ] 避免過度寬鬆造成 false positive
[ ] 記錄測試樣本與誤報樣本
```

## 與其他頁面的關聯

IOC/TTP 的分析思維基礎見 [[malware-analysis-methodology]]；具體行為模式與其 Technique 對應見 [[malware-behavior-patterns]] 與 [[persistence-mechanisms]]；本頁內容是撰寫 [[malware-analysis-report-template]] 中 IOC 與 Detection Opportunities 章節的直接依據；可重放驗證與 scorecard 見 [[detection-validation-range]]。
