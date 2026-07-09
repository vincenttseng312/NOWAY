---
type: concept
title: "Windows PE 靜態分析"
tags: [malware-analysis, dfir, windows]
sources: [malware-static-dynamic-analysis-notes]
created: 2026-07-09
updated: 2026-07-09
---

# Windows PE 靜態分析

PE（Portable Executable）是 Windows 可執行檔、DLL、驅動程式常見格式（`.exe`/`.dll`/`.sys`/`.scr`/`.ocx`/`.cpl`/`.drv`）。**不要相信副檔名，要看 magic bytes 與結構**（開頭 `MZ`，PE Header 附近有 `PE\0\0`）。

## 靜態分析總覽與順序

目標：這是什麼、看起來想做什麼、是否偽裝/壓縮/混淆、可能需要哪些系統功能、可能連到哪裡、能否推測 malware family、應如何安全地動態觀察。

建議順序：不開啟不執行先算 hash → 判斷真實檔案類型 → 看檔案大小/metadata → 看 strings → 看 packer/entropy → PE 則看 headers/sections/imports/resources/signature → script 則先格式化解碼但不執行 → Office/PDF/LNK 用專用工具抽取 payload → 整理初步 IOC → 寫出動態分析假設。

常用工具：檔案類型（`file`/TrID/Detect It Easy）、Strings（strings/FLOSS）、PE 結構（PEStudio/PE-bear/CFF Explorer）、簽章（sigcheck）、YARA、Office（oletools/oledump）、PDF（pdfid/pdf-parser）、LNK（LECmd）、MSI（lessmsi/Orca）。

## PE 結構總覽

```text
DOS Header / DOS Stub / PE Signature / COFF File Header / Optional Header / Section Table
Sections: .text .rdata .data .rsrc .reloc (+ custom/packed sections)
Data Directories: Import/Export/Resource/Relocation/TLS/Exception/Certificate Table
Overlay Data
```

## Header 分析重點

| Header | 關鍵欄位 | 可疑跡象 |
|---|---|---|
| DOS Header | `e_lfanew`（指向 PE header） | 結構破損、指向奇怪位置 |
| COFF File Header | Machine、NumberOfSections、TimeDateStamp、Characteristics | section 數過少/過多；編譯時間是 1970/1992/2099 或同批樣本完全相同（不可單靠此判斷真偽） |
| Optional Header | AddressOfEntryPoint、ImageBase、Subsystem、SizeOfImage、DllCharacteristics | Entry point 落在 `.rsrc` 或自訂亂名 section 高度可疑；落在 packed section（如 UPX0）常見於加殼 |

## Sections 分析

| Section | 內容 | 備註 |
|---|---|---|
| `.text` | 程式碼 | 通常可執行 |
| `.rdata` | read-only data / imports | 字串、常數 |
| `.rsrc` | 資源 | icon、version、dialog |

可疑 section 名稱：`UPX0`/`UPX1`、`.aspack`、`.vmp0`/`.vmp1`、`.themida`、`.petite`、`MPRESS`、亂碼名稱、空名稱。

Section 權限：R/RX/RW 都常見，**RWX（可讀可寫可執行）高度可疑**——同一段記憶體可寫又可執行，常見於 packer、shellcode loader、self-modifying code。

Raw Size vs Virtual Size：Virtual Size 遠大於 Raw Size，代表執行時可能解壓/解密/填充 payload。

## Entropy 熵值

| Entropy | 可能意義 |
|---|---|
| 低 | 重複資料、空白、未壓縮 |
| 中 | 一般程式碼/資料 |
| 高 | 壓縮、加密、packed |

高 entropy 不一定惡意（正常壓縮檔、遊戲資源也高），要和 imports、sections、strings 一起判讀（見 [[packers-and-anti-analysis]]）。

## Import / Export / Resource / 簽章分析

Import Table 顯示可能呼叫哪些 DLL/API：`ws2_32.dll`/`wininet.dll`/`winhttp.dll`（網路）、`advapi32.dll`（Registry/Service）、`crypt32.dll`/`bcrypt.dll`（加解密）、`ntdll.dll`（Native API，任何程式都會載入不具判斷力）。API 類型速查涵蓋程序建立（`CreateProcess`）、記憶體（`VirtualAllocEx`/`WriteProcessMemory`，注入跡象見 [[process-hollowing]]）、Persistence（`CreateService`）、Anti-analysis（`IsDebuggerPresent`）等分類。

**Imports 很少**可能代表樣本簡單、packed 未解開、使用 dynamic import resolution 或 API hashing、或本身只是 loader。判讀公式：`Imports 少 + Entropy 高 + Section 異常 + Strings 少 = 高度疑似 packed/obfuscated`。

Export Table（DLL 適用）：檢查名稱是否正常、是否偽裝系統 DLL、是否只有 ordinal 沒名稱——**合法 signed EXE 載入同目錄下 unsigned DLL** 是常見的 DLL side-loading 攻擊情境，DLL 載入機制本身見 [[dynamic-link-library]]。

Resource 可能含 icon/version info/manifest，或內嵌另一個 MZ/PE（entropy 高）；可疑點包括 icon 偽裝成 PDF/Word、version info 偽裝 Microsoft 但簽章者不符。

數位簽章：unsigned 不代表惡意，signed 不代表安全；要核對簽章是否有效、簽章者是否與檔案聲稱一致、是否為被竊憑證簽署。

PDB path（如殘留 `C:\Users\dev\...\payload.pdb`）可能洩漏開發者/專案/campaign 線索，但也可能被偽造。Overlay Data（PE 結構結束後附加的資料）若很大或 entropy 高，可能是 installer data、packed payload 或另一個 stage。

## 靜態 PE 分析筆記模板

```markdown
# PE Static Analysis
## Basic Info / Signature / Sections / Imports / Exports / Resources
## Strings of Interest（URL / Path / Registry / API / Mutex）
## Suspicion Summary（Packed / Network / Persistence / Injection / Anti-analysis）
## Dynamic Analysis Hypothesis
```

## 與其他頁面的關聯

Packer/obfuscation/anti-VM/anti-debug 的完整跡象清單見 [[packers-and-anti-analysis]]；動態驗證靜態假設的流程見 [[dynamic-behavior-analysis]]；DLL 匯入的一般機制見 [[dynamic-link-library]]；注入相關 API 的深入說明見 [[process-hollowing]]。
