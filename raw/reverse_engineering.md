# 逆向工程 Wiki：支援惡意程式分析

> 版本：v1.0  
> 適用情境：Malware Analysis / DFIR / Threat Hunting 前置逆向能力  
> 範圍：靜態逆向、Debugging、PE Unpacking、Shellcode 分析、Process Hollowing 逆向證據  
> 安全界線：本筆記只用於合法授權、隔離環境與防禦分析。不提供可直接濫用的惡意程式碼、payload、繞防部署或攻擊操作流程。

---

## 目錄

- [0. 這份 Wiki 的定位](#0-這份-wiki-的定位)
- [1. 逆向工程的核心問題](#1-逆向工程的核心問題)
- [2. 逆向分析總流程](#2-逆向分析總流程)
- [3. 工具地圖](#3-工具地圖)
- [4. 組語與 CPU 心智模型](#4-組語與-cpu-心智模型)
- [5. 函式、呼叫慣例與 Stack Frame](#5-函式呼叫慣例與-stack-frame)
- [6. Windows PE 逆向必懂結構](#6-windows-pe-逆向必懂結構)
- [7. 從 Import / String / Resource 找行為線索](#7-從-import--string--resource-找行為線索)
- [8. Decompiler 工作流](#8-decompiler-工作流)
- [9. Debugger 工作流](#9-debugger-工作流)
- [10. Shellcode 逆向分析](#10-shellcode-逆向分析)
- [11. Packer / Unpacking 逆向筆記](#11-packer--unpacking-逆向筆記)
- [12. Process Hollowing 的逆向補強](#12-process-hollowing-的逆向補強)
- [13. Anti-Analysis 的辨識，而不是繞過](#13-anti-analysis-的辨識而不是繞過)
- [14. 從逆向結果回填動態分析報告](#14-從逆向結果回填動態分析報告)
- [15. 小型 Lab 路線](#15-小型-lab-路線)
- [16. 速查表](#16-速查表)
- [17. 逆向報告模板](#17-逆向報告模板)
- [18. 參考資料](#18-參考資料)

---

# 0. 這份 Wiki 的定位

你前面的動態分析筆記已經能回答：

- 樣本啟動了什麼程序？
- 寫了哪些檔案？
- 寫了哪些 Registry？
- 建立了哪些 Persistence？
- 有沒有網路連線？
- 有沒有可疑 API 與行為鏈？

但要更深入分析 Process Hollowing、Loader、Dropper、Packed Malware、Shellcode，還需要逆向工程補上下面幾件事：

```text
動態分析看到「發生什麼」
逆向工程追問「為什麼會發生、程式如何做到、真正 payload 藏在哪」
```

這份 Wiki 不追求包羅萬象，而是針對 Malware Analyst 最常用到的逆向能力：

```text
Assembly 基礎
↓
PE 結構
↓
Imports / Strings / Sections
↓
Decompiler 閱讀
↓
Debugger 觀察
↓
Unpacking 概念
↓
Shellcode 辨識
↓
Process Hollowing 逆向證據
↓
回填分析報告
```

---

# 1. 逆向工程的核心問題

## 1.1 逆向工程在惡意程式分析中的目的

逆向不是為了把整個程式「還原成原始碼」，而是回答調查問題：

| 問題 | 逆向要找的答案 |
|---|---|
| 這個樣本是什麼類型？ | Dropper、Loader、Stealer、Ransomware、Backdoor、Downloader |
| 真正 payload 在哪？ | Resource、Overlay、Section、加密 blob、網路下載、記憶體解包 |
| 它如何啟動 payload？ | CreateProcess、LoadLibrary、反射載入、Injection、Hollowing |
| 它怎麼持久化？ | Registry、Service、Scheduled Task、WMI、Startup Folder |
| 它怎麼隱藏？ | Packer、Obfuscation、API hashing、String encryption、Anti-debug |
| 它連去哪裡？ | 解密後的 domain、IP、URI、User-Agent、C2 path |
| 它能產生什麼 IOC？ | Hash、檔名、路徑、Registry key、Mutex、Domain、URL、YARA strings |
| 它對應什麼 TTP？ | MITRE ATT&CK technique mapping |

## 1.2 逆向分析不是線性流程

實務上常常是來回交叉：

```text
靜態看到可疑 import
→ 動態驗證有沒有真的呼叫
→ Debugger 找呼叫點
→ Decompiler 看參數來源
→ 發現字串是加密的
→ 找解密函式
→ 解出 C2 / path / mutex
→ 回到動態分析確認
```

## 1.3 逆向工程的三種層次

| 層次 | 你在看什麼 | 目標 |
|---|---|---|
| Surface-level | 字串、Imports、Sections、Entropy | 快速分類 |
| Behavior-level | 函式、API call、控制流程 | 理解功能 |
| Mechanism-level | Unpacking、Shellcode、Memory mapping、Injection | 找真正 payload 與執行機制 |

---

# 2. 逆向分析總流程

## 2.1 安全前置

所有逆向樣本都應該在隔離環境進行。

最低限度：

```text
[Host]
- 不直接雙擊樣本
- 不解壓到同步雲端資料夾
- 不把樣本放到 Downloads / Desktop
- 樣本加密壓縮保存

[VM]
- Host-only 或 Internal Network
- Snapshot
- 無共享剪貼簿
- 無共享資料夾
- 使用 ISO 或專用隔離傳輸法
- 工具與樣本分開保存
```

## 2.2 樣本接收流程

```text
1. 建立 Case ID
2. 計算 hash
   - MD5
   - SHA1
   - SHA256
3. 記錄檔案大小
4. 記錄原始檔名
5. 記錄來源
6. 記錄時間
7. 只讀保存原始樣本
8. 複製一份進入分析資料夾
```

## 2.3 第一輪快速 triage

先不要急著進 Debugger。

```text
1. file type
2. hash
3. strings
4. PE headers
5. sections
6. imports
7. resources
8. entropy
9. certificates
10. overlay
11. packer hints
```

## 2.4 第二輪行為假設

根據靜態結果建立假設：

| 靜態發現 | 初步假設 |
|---|---|
| Import 有 WinInet / WinHTTP / ws2_32 | 可能有網路功能 |
| Import 只有 LoadLibrary / GetProcAddress | 可能動態解析 API 或 packed |
| 高 entropy section | 可能加密或壓縮 |
| Resource 很大 | payload 可能藏在 resource |
| Overlay 很大 | 可能附加資料或第二階段 payload |
| 字串有 `cmd.exe` / `powershell` | 可能執行 LOLBin |
| 字串有 Registry Run key | 可能持久化 |
| 字串有 `vssadmin` | 可能勒索軟體行為 |
| 字串很少 | 可能 packer、加密字串、混淆 |

## 2.5 第三輪深度逆向

```text
1. 載入 Ghidra / IDA / Binary Ninja
2. 修正 function boundaries
3. 命名重要函式
4. 找 main / WinMain / DllMain
5. 找 API wrapper
6. 找 string decoder
7. 找 config parser
8. 找 payload extraction
9. 找 persistence function
10. 找 network function
11. 找 injection / hollowing function
```

## 2.6 第四輪動態驗證

```text
1. Procmon 驗證 file / registry
2. ProcExp 驗證 process tree / DLL
3. TCPView / Wireshark 驗證 network
4. Sysmon 驗證 process / network / file / registry
5. Debugger 驗證解密後字串與 payload
6. Memory dump 驗證 unpacked code
```

---

# 3. 工具地圖

## 3.1 靜態工具

| 工具 | 用途 |
|---|---|
| Detect It Easy / PEStudio | PE triage、packer hint、imports、sections |
| PE-bear / CFF Explorer | PE header、sections、data directories |
| strings / FLOSS | 字串抽取、stack strings、簡單解碼 |
| capa | 以 capability 角度推測功能 |
| YARA | 寫檔案特徵規則 |
| Ghidra | 反組譯、反編譯、函式分析 |
| IDA Free / IDA Pro | 反組譯、圖形化控制流程 |
| Binary Ninja | 反組譯與中介表示分析 |
| radare2 / rizin | CLI 型逆向分析 |
| CyberChef | 解碼、轉換、字串處理 |
| HxD / 010 Editor | Hex 檢視、結構模板 |

## 3.2 動態 / Debugging 工具

| 工具 | 用途 |
|---|---|
| x64dbg | Windows user-mode debugger，常用於 malware reversing |
| WinDbg | Microsoft debugger，適合符號、crash、深度 Windows 分析 |
| Process Monitor | 檔案、Registry、Process/Thread、Network 事件 |
| Process Explorer | Process tree、DLL、handles、signer、integrity |
| Autoruns | Persistence 全景圖 |
| TCPView | Process 對應網路連線 |
| Wireshark | 封包分析 |
| FakeNet-NG / INetSim | 隔離環境模擬網路服務 |
| Sysmon | 事件紀錄與 SOC 視角 |

## 3.3 記憶體與 dump 工具

| 工具 | 用途 |
|---|---|
| ProcDump | dump process memory |
| PE-sieve | 掃描記憶體中可疑 PE / injection 痕跡 |
| hollows_hunter | Hollowing / injection 記憶體檢查 |
| Volatility 3 | 記憶體取證 |
| Scylla | IAT 修復概念工具 |
| x64dbg dump view | 記憶體觀察 |

> 注意：dump 與 IAT 修復應只在授權分析環境中使用，目的為還原樣本真實行為與產出偵測。

---

# 4. 組語與 CPU 心智模型

## 4.1 逆向時你看到的是什麼？

原始碼經過編譯後會變成機器碼。反組譯器把機器碼轉成人類較可讀的 assembly。

```text
C / C++ source
↓ compile
Machine code
↓ disassemble
Assembly
↓ decompile
Pseudo-C
```

Decompiler 不是時光機。它通常無法完整還原：

- 原始變數名稱
- 原始註解
- 類別設計意圖
- 完整型別資訊
- 巨集
- 編譯前結構
- 開發者命名習慣

所以你要學會從 pseudo-C 與 assembly 推回「行為」。

## 4.2 Register 是什麼？

Register 是 CPU 裡最快速的小型儲存空間。

x64 常見暫存器：

| 暫存器 | 常見用途 |
|---|---|
| RAX | 回傳值、運算暫存 |
| RBX | 一般用途，常被保存 |
| RCX | 第 1 個整數/指標參數 |
| RDX | 第 2 個整數/指標參數 |
| R8 | 第 3 個整數/指標參數 |
| R9 | 第 4 個整數/指標參數 |
| RSP | Stack pointer |
| RBP | Base/frame pointer，有時用於 stack frame |
| RSI | source index / 一般用途 |
| RDI | destination index / 一般用途 |
| RIP | instruction pointer，指向下一條指令 |

x86 常見暫存器：

| 暫存器 | 常見用途 |
|---|---|
| EAX | 回傳值 |
| EBX | 一般用途 |
| ECX | counter / this pointer |
| EDX | 一般用途 |
| ESP | Stack pointer |
| EBP | Stack frame base |
| ESI | source index |
| EDI | destination index |
| EIP | instruction pointer |

## 4.3 常見 Assembly 指令

| 指令 | 意義 | 逆向觀察 |
|---|---|---|
| `mov` | 搬移資料 | 變數賦值、參數準備 |
| `lea` | 載入有效位址 | 取地址、計算指標 |
| `push` | 壓入 stack | x86 傳參、保存值 |
| `pop` | 從 stack 取出 | 還原值 |
| `call` | 呼叫函式 | 找功能邊界 |
| `ret` | 函式返回 | 函式結尾 |
| `cmp` | 比較 | if / switch / loop 前置 |
| `test` | 位元測試 | 常用於判斷是否為 0 |
| `jz / je` | zero/equal jump | 條件分支 |
| `jnz / jne` | not zero/not equal jump | 條件分支 |
| `jmp` | 無條件跳轉 | 控制流程、packer 跳 OEP |
| `xor` | XOR 運算 | 清零、解密、混淆 |
| `add / sub` | 加減 | 指標偏移、計數 |
| `and / or` | 位元運算 | flag、mask |
| `shl / shr` | 位移 | 編碼、hash、加密前處理 |
| `rol / ror` | 旋轉 | API hashing 常見 |
| `rep movs` | 批量複製 | memory copy |
| `nop` | 空操作 | padding、patch 痕跡 |

## 4.4 `xor eax, eax` 為什麼常見？

```asm
xor eax, eax
```

通常代表把 `eax` 清成 0。

理由：

- 指令短
- 執行快
- 不需要額外常數
- 編譯器常用

逆向解讀：

```text
eax = 0
```

不要看到 XOR 就立刻以為是加密。

## 4.5 `call` 的逆向意義

看到 `call` 時要問：

```text
這是呼叫 Windows API？
這是呼叫內部函式？
呼叫前參數怎麼準備？
呼叫後回傳值怎麼使用？
失敗時走哪條路？
成功時走哪條路？
```

## 4.6 條件跳轉與控制流程

常見模式：

```text
cmp eax, 0
jz  fail_path
```

Pseudo-C：

```c
if (eax == 0) {
    fail_path();
}
```

或：

```text
test eax, eax
jnz success_path
```

Pseudo-C：

```c
if (eax != 0) {
    success_path();
}
```

## 4.7 逆向時最重要的不是背指令

更重要的是辨識模式：

```text
參數準備
→ call
→ 檢查回傳值
→ 成功路徑
→ 失敗路徑
```

例如：

```text
準備檔案路徑
→ CreateFileW
→ 判斷 handle 是否有效
→ WriteFile
→ CloseHandle
```

這代表「寫檔行為」。

---

# 5. 函式、呼叫慣例與 Stack Frame

## 5.1 函式在 Assembly 中長什麼樣？

典型 x86 function prologue：

```asm
push ebp
mov ebp, esp
sub esp, 0x40
```

意思：

```text
保存舊的 frame pointer
建立新的 stack frame
保留 local variables 空間
```

典型 epilogue：

```asm
mov esp, ebp
pop ebp
ret
```

## 5.2 x64 Windows 呼叫慣例重點

在 Windows x64，前四個整數或指標參數常放在：

```text
1st → RCX
2nd → RDX
3rd → R8
4th → R9
```

回傳值通常在：

```text
RAX
```

更多參數會放到 stack。

### 例子：概念化

如果 pseudo-C 是：

```c
CreateFileW(path, access, share, sec, creation, flags, template);
```

在 x64 逆向時，常見觀察：

```text
RCX = path
RDX = access
R8  = share
R9  = security attributes
其他參數在 stack
call CreateFileW
RAX = handle
```

## 5.3 x86 呼叫慣例重點

x86 常見是透過 stack 傳參：

```asm
push arg3
push arg2
push arg1
call Function
```

注意 push 順序通常是反向。

## 5.4 為什麼呼叫慣例對 Malware Analyst 重要？

因為你要知道 API 的參數是什麼。

例如你看到：

```text
call VirtualAlloc
```

你要追：

```text
lpAddress 是多少？
dwSize 是多少？
flAllocationType 是什麼？
flProtect 是什麼？
```

如果 `flProtect` 是 executable 權限，或後續又把資料寫入該區域，就可能是解包、載入、注入或 shellcode staging 的一部分。

## 5.5 Stack Frame 觀察重點

在 debugger 中看到 stack 時，問：

```text
這些值是 return address？
是 API 參數？
是 local buffer？
是解密後字串？
是 shellcode 暫存？
是 embedded payload 指標？
```

## 5.6 Return Address 的重要性

Return address 表示函式執行完會回去哪裡。

逆向時可用於：

- 確認 call chain
- 找出誰呼叫了可疑函式
- 判斷跳轉是否異常
- 觀察 unpacking stub 最後跳到哪個 OEP

---

# 6. Windows PE 逆向必懂結構

## 6.1 PE 是什麼？

PE，全名 Portable Executable，是 Windows 可執行檔、DLL、driver 等常見 binary 格式。

常見副檔名：

```text
.exe
.dll
.sys
.ocx
.scr
cpl
```

## 6.2 PE 結構鳥瞰

```text
DOS Header
DOS Stub
PE Signature
COFF File Header
Optional Header
Data Directories
Section Headers
Sections
Overlay
```

## 6.3 DOS Header

開頭通常是：

```text
MZ
```

關鍵欄位：

| 欄位 | 意義 |
|---|---|
| `e_magic` | MZ signature |
| `e_lfanew` | 指向 PE header 的 offset |

如果不是 `MZ`，可能是：

- 不是 PE
- 被加殼或嵌入
- shellcode
- raw data
- 損壞檔案

## 6.4 PE Signature

通常是：

```text
PE\0\0
```

代表真正 PE header 開始。

## 6.5 COFF File Header

常看欄位：

| 欄位 | 觀察 |
|---|---|
| Machine | x86 / x64 / ARM |
| NumberOfSections | section 數量 |
| TimeDateStamp | 編譯時間，可能被偽造 |
| Characteristics | EXE / DLL / large address aware 等 |

## 6.6 Optional Header

雖然叫 Optional，但對 PE 很重要。

常看欄位：

| 欄位 | 意義 |
|---|---|
| AddressOfEntryPoint | 程式入口點 RVA |
| ImageBase | 預期載入基底 |
| SectionAlignment | 記憶體對齊 |
| FileAlignment | 檔案對齊 |
| SizeOfImage | 映像載入大小 |
| Subsystem | Console / GUI |
| DataDirectory | Import、Export、Resource、Reloc、TLS 等 |

## 6.7 Entry Point

Entry Point 是程式開始執行的位置。

但對 packed malware 來說：

```text
Entry Point 可能只是 unpacking stub
真正 payload 的 OEP 在解包後才出現
```

觀察重點：

| 情況 | 可能意義 |
|---|---|
| EP 在 `.text` | 常見 |
| EP 在奇怪 section | 可能 packed |
| EP 在高 entropy section | 可能 unpacking stub |
| EP 附近大量跳轉/解碼 loop | 可能 packer |
| EP 很快呼叫 VirtualAlloc/VirtualProtect | 可能解包或載入 payload |

## 6.8 Sections

常見 section：

| Section | 常見用途 |
|---|---|
| `.text` | 程式碼 |
| `.rdata` | 唯讀資料、字串、import |
| `.data` | 可寫資料 |
| `.rsrc` | Resource |
| `.reloc` | Relocation |
| `.pdata` | x64 exception/unwind info |

可疑 section 特徵：

```text
名稱奇怪
權限 RWE
高 entropy
raw size 很小但 virtual size 很大
section 數量極少
section 數量異常多
entry point 落在非典型 section
```

## 6.9 RVA、VA、File Offset

逆向 PE 常遇到三種地址：

| 名稱 | 意義 |
|---|---|
| VA | Virtual Address，程式載入記憶體後的地址 |
| RVA | Relative Virtual Address，相對於 ImageBase 的地址 |
| File Offset | 在檔案中的偏移 |

關係：

```text
VA = ImageBase + RVA
```

但 File Offset 與 RVA 需要透過 section header 換算。

## 6.10 Import Table

Import Table 告訴你程式會用哪些外部 DLL/API。

例如：

| DLL | 可能意義 |
|---|---|
| kernel32.dll | 檔案、程序、記憶體、基本系統 API |
| advapi32.dll | Registry、Service、權限 |
| user32.dll | GUI、視窗、鍵盤滑鼠 |
| ws2_32.dll | Socket 網路 |
| wininet.dll | HTTP/FTP 等高階網路 |
| winhttp.dll | HTTP client |
| crypt32.dll | 憑證、編碼、加解密支援 |
| bcrypt.dll | CNG crypto |
| ntdll.dll | Native API、syscall 入口 |
| shell32.dll | Shell 操作 |
| ole32.dll | COM/OLE |

## 6.11 Export Table

DLL 會匯出函式給別人呼叫。

對 malware 分析重要情境：

```text
惡意 DLL 可能只有少數 export
export 名稱可能偽裝成合法元件
rundll32.exe 執行 DLL 時會指定 export
service DLL 可能由 svchost 載入
```

## 6.12 Resource

Resource 可放：

```text
icon
manifest
version info
bitmap
dialog
embedded file
encrypted payload
configuration blob
```

Dropper 常把第二階段藏在 resource。

## 6.13 Relocation

如果 PE 無法載入預設 ImageBase，就需要 relocation 修正地址。

對 unpacking / hollowing 重要：

```text
手動載入 PE 時，如果 ImageBase 不一致，就需要處理 relocation。
分析時可觀察 payload 是否有 relocation table。
```

## 6.14 TLS Callback

TLS callback 可能在 Entry Point 前執行。

逆向時要注意：

```text
有些樣本把 anti-debug 或 unpacking stub 放在 TLS callback。
```

檢查：

```text
PE Data Directory → TLS
```

## 6.15 Overlay

Overlay 是 PE 正常結構後面額外附加的資料。

可能是：

```text
installer data
signature
archive
encrypted payload
configuration
junk data
```

Dropper / Loader 可能把 payload 放在 overlay。

---

# 7. 從 Import / String / Resource 找行為線索

## 7.1 Import 分析不是定罪

看到某 API 不代表一定惡意。

但 Import 能建立假設：

```text
CreateFile + WriteFile
→ 可能寫檔

RegSetValueEx
→ 可能寫 Registry

CreateProcess
→ 可能啟動子程序

VirtualAlloc + VirtualProtect
→ 可能動態記憶體執行

LoadLibrary + GetProcAddress
→ 可能動態載入 API

InternetOpenUrl / HttpSendRequest
→ 可能連網

CryptEncrypt / BCryptEncrypt
→ 可能加密

OpenProcess + WriteProcessMemory + CreateRemoteThread
→ 可能 injection 行為
```

## 7.2 Import 太少的意義

如果 PE imports 只有：

```text
LoadLibrary
GetProcAddress
VirtualAlloc
VirtualProtect
ExitProcess
```

可能是：

- packer
- shellcode loader
- API 動態解析
- 手寫 import resolver
- 加殼保護
- benign small runtime

要搭配 sections、entropy、dynamic behavior 判斷。

## 7.3 String 類型

常見有價值字串：

| 字串類型 | 例子 |
|---|---|
| 檔案路徑 | `%APPDATA%`, `%TEMP%`, `C:\ProgramData` |
| Registry | `Software\Microsoft\Windows\CurrentVersion\Run` |
| 網路 | `http`, domain, URI, User-Agent |
| 命令 | `cmd.exe`, `powershell.exe`, `schtasks.exe` |
| Persistence | `Run`, `Services`, `Startup`, `WMI` |
| Crypto | `AES`, `RSA`, `CryptAcquireContext` |
| Debug | `IsDebuggerPresent`, `CheckRemoteDebuggerPresent` |
| VM | `VBox`, `VMware`, `QEMU` |
| Error | log message, internal debug string |
| Mutex | `Global\...`, `Local\...` |

## 7.4 字串很少怎麼辦？

可能原因：

```text
packed
string encryption
stack strings
runtime decoding
wide strings
custom encoding
resource hidden
configuration encrypted
```

下一步：

```text
1. 找解密 loop
2. 找大量 XOR / ROL / ADD / SUB
3. 找記憶體中解密後字串
4. 用 FLOSS 類工具輔助
5. Debug 到解密函式 return 後觀察 buffer
```

## 7.5 Resource 分析流程

```text
1. 列出 resource type
2. 看每個 resource size
3. 匯出大型 resource
4. 檢查 magic bytes
5. 檢查 entropy
6. 檢查是否 embedded PE
7. 檢查是否壓縮或加密
8. 找程式碼中 FindResource / LoadResource / LockResource
9. 追蹤 resource 被複製到哪裡
10. 追蹤是否被解密、寫檔或載入記憶體
```

---

# 8. Decompiler 工作流

## 8.1 載入 Ghidra 後先做什麼？

不要一進去就從第一個函式硬看。

建議流程：

```text
1. 確認架構 x86/x64
2. 確認 compiler hint
3. 執行 auto-analysis
4. 檢查 Entry Point
5. 找 main / WinMain / DllMain
6. 檢查 imports
7. 找 cross references
8. 標記可疑 API 的 caller
9. 重新命名函式
10. 建立功能區塊筆記
```

## 8.2 函式重新命名策略

不要用 `function1`、`bad_func`。

用「行為 + 證據」命名：

| 原本 | 建議命名 |
|---|---|
| `FUN_140001230` | `resolve_imports_by_hash` |
| `FUN_1400028A0` | `decode_config_xor_loop` |
| `FUN_140003100` | `write_payload_to_temp` |
| `FUN_140004200` | `create_run_key_persistence` |
| `FUN_140005500` | `http_beacon_loop` |
| `FUN_140006700` | `inject_payload_into_child_process` |

## 8.3 變數命名策略

| 模糊變數 | 建議命名 |
|---|---|
| `local_28` | `payload_size` |
| `param_1` | `encoded_config_ptr` |
| `iVar1` | `api_resolve_status` |
| `puVar2` | `payload_buffer` |
| `local_res8` | `output_path_w` |

## 8.4 Cross References 是核心技能

看到有價值字串或 API 後：

```text
Right click → References / Xrefs
```

要問：

```text
誰使用這個字串？
哪個函式呼叫這個 API？
這個函式又被誰呼叫？
這條路徑是否只在某條件成立時執行？
```

## 8.5 從 API 反推功能

範例：

```text
RegCreateKeyExW
RegSetValueExW
```

推論：

```text
可能建立或修改 Registry
```

但還要追參數：

```text
hKey 是 HKCU 還是 HKLM？
subkey 是哪裡？
value name 是什麼？
value data 是什麼？
```

## 8.6 從常數反推行為

常見 Windows 常數：

| 常數 | 可能意義 |
|---|---|
| `0x40` | PAGE_EXECUTE_READWRITE |
| `0x20` | PAGE_EXECUTE_READ |
| `0x1000` | MEM_COMMIT |
| `0x2000` | MEM_RESERVE |
| `0x80000000` | GENERIC_READ |
| `0x40000000` | GENERIC_WRITE |
| `0x2` | CREATE_ALWAYS 或 FILE_SHARE_WRITE，需看 API context |
| `0x4` | OPEN_ALWAYS 或其他，需看 API context |

注意：常數值必須搭配 API 參數位置解讀，不能單看數字。

## 8.7 逆向時的筆記法

每個函式都用固定格式：

```markdown
### Function: `decode_config_xor_loop`

Address:
- `0x1400028A0`

Called by:
- `main_init`
- `load_embedded_config`

Calls:
- `memcpy`
- `strlen`

Purpose:
- 疑似解密 embedded config

Evidence:
- 對 buffer 做 XOR
- key 長度固定
- return 後出現可讀 URL / path

Output:
- decoded C2
- decoded mutex

Confidence:
- Medium / High
```

---

# 9. Debugger 工作流

## 9.1 Debugger 的用途

Debugger 不是用來「盲目執行樣本」，而是用來驗證：

```text
API 參數
解密後字串
unpacked payload
memory permission
branch condition
OEP
child process
injection target
```

## 9.2 Debugger 基本概念

| 名詞 | 意義 |
|---|---|
| Breakpoint | 中斷點 |
| Step Into | 進入 call |
| Step Over | 執行 call 但不進去 |
| Run / Continue | 繼續執行 |
| Registers | CPU 暫存器 |
| Stack | 呼叫堆疊與參數 |
| Memory Dump | 記憶體檢視 |
| Modules | 已載入模組 |
| Threads | 執行緒 |
| Exception | 例外，中斷或錯誤事件 |

## 9.3 什麼時候設 Breakpoint？

常見觀察點：

| 類型 | API / 位置 |
|---|---|
| 檔案 | CreateFile, WriteFile, DeleteFile, MoveFile |
| Registry | RegCreateKey, RegSetValue, RegDeleteValue |
| 程序 | CreateProcess, ShellExecute |
| 記憶體 | VirtualAlloc, VirtualProtect, HeapAlloc |
| DLL | LoadLibrary, GetProcAddress |
| 網路 | connect, send, recv, InternetOpenUrl, HttpSendRequest |
| Resource | FindResource, LoadResource, LockResource |
| Injection 概念證據 | OpenProcess, WriteProcessMemory, CreateRemoteThread |
| Hollowing 概念證據 | CreateProcess suspended, NtUnmapViewOfSection, SetThreadContext, ResumeThread |

> 這些 breakpoint 用於分析與偵測，不代表所有出現都惡意。

## 9.4 Debugger 觀察 API 參數

在 x64 Windows：

```text
RCX, RDX, R8, R9
```

是前四個參數。其餘看 stack。

在 x86：

```text
看 stack 上 push 的參數。
```

## 9.5 Debugging 安全原則

```text
1. 不在 Host debug 未知樣本
2. 不給 VM 外網
3. 不使用真實帳號資料
4. 不放真實文件
5. 每次分析後還原快照
6. 不把分析過程中產生的檔案帶回 Host 執行
7. 不 patch 樣本後隨意執行
8. 不使用繞過防護的操作去部署 payload
```

## 9.6 Debugger 與動態工具搭配

```text
Debugger：看程式內部如何決定
Procmon：看決定造成什麼系統事件
ProcExp：看程序與 DLL 狀態
Sysmon：看 SOC 會收到什麼事件
Wireshark：看網路資料
```

---

# 10. Shellcode 逆向分析

## 10.1 Shellcode 是什麼？

在逆向語境中，shellcode 指一段可直接在記憶體中執行的機器碼。它不一定真的開 shell；很多 malware shellcode 的目標是：

```text
API resolver
下載第二階段
解密 payload
反射載入 PE
建立 C2
注入其他程序
```

## 10.2 Shellcode 與 PE 的差別

| 項目 | PE | Shellcode |
|---|---|---|
| Header | 有 MZ / PE | 通常沒有 |
| Import Table | 通常有 | 通常沒有 |
| Relocation | 可能有 | 通常 position-independent |
| 載入方式 | Windows loader | 程式自行跳入記憶體 |
| 分析方式 | PE parser + disassembler | 指定架構與 base address 反組譯 |
| API 使用 | Import table | PEB traversal / API hashing / GetProcAddress |

## 10.3 Shellcode 常見特徵

```text
沒有 MZ/PE header
大量短跳轉
call-pop 取得目前位址
RIP-relative addressing
PEB traversal
API hashing
stack strings
XOR/ADD/SUB 解碼 loop
解密後才出現字串
直接呼叫動態解析出的 API address
```

## 10.4 Position Independent Code

Shellcode 常不知道自己會被載入哪個地址，所以必須 position-independent。

常見技巧：

```text
call-pop
RIP-relative addressing
用目前 RIP/ESP/RSP 推算資料位置
不依賴固定 ImageBase
```

分析重點：

```text
它如何取得自身位置？
它如何找到 embedded data？
它如何定位 API？
```

## 10.5 API Resolver

Shellcode 通常不能直接用 Import Table，因此會自己找 API。

常見高階邏輯：

```text
1. 找 PEB
2. 走 loader data
3. 找已載入 module，例如 kernel32.dll / ntdll.dll
4. 解析 export table
5. 用名稱或 hash 找 API
6. 呼叫解析出的 API address
```

逆向重點：

```text
hash 演算法是什麼？
hash 對應哪些 API？
module 名稱是否被硬編碼或 hash 化？
解析後的 API 被保存到哪裡？
```

## 10.6 API Hashing

API hashing 是把 API 名稱轉成 hash，避免在字串中直接出現：

```text
VirtualAlloc
LoadLibraryA
GetProcAddress
WinExec
InternetOpenA
```

逆向時看到：

```text
大量 rotate / xor / add
逐字元處理 export name
和常數比較
```

可能就是 API hashing。

分析目標不是重寫惡意 loader，而是建立 mapping：

| Hash 常數 | 解析出的 API | 用途 |
|---|---|---|
| `0x???????` | `VirtualAlloc` | 配置記憶體 |
| `0x???????` | `LoadLibraryA` | 載入 DLL |
| `0x???????` | `GetProcAddress` | 解析 API |
| `0x???????` | `CreateProcessA` | 建立程序 |

## 10.7 Decoder Stub

很多 shellcode 前段是 decoder stub。

高階流程：

```text
encoded payload
↓
decoder loop
↓
decoded payload
↓
jump to decoded payload
```

常見跡象：

```text
小型 loop
每次處理 1/2/4/8 bytes
XOR/ADD/SUB/ROL/ROR
處理固定長度
完成後 jmp 到 buffer
```

## 10.8 Stack Strings

有些 shellcode 會把字串一段段寫到 stack。

例如概念上：

```text
push "cmd"
push ".exe"
```

逆向看到的是數字常數，但記憶體中組合後才變成字串。

分析方法：

```text
1. 看 push / mov 到 stack 的常數
2. 轉成 ASCII / UTF-16LE
3. 注意小端序
4. 在執行後觀察 stack / memory
5. 把組合後字串記到報告
```

## 10.9 Shellcode 分析流程

```text
1. 確認架構：x86 / x64
2. 確認起始 offset
3. 指定 base address 載入 disassembler
4. 找 decoder stub
5. 找 API resolver
6. 找解密後區域
7. 找字串與 API mapping
8. 找 network / process / memory / file 行為
9. 找最終 payload 是否為 PE
10. 產出 IOC 與行為摘要
```

## 10.10 Shellcode 報告該寫什麼？

```markdown
### Shellcode Analysis

Architecture:
- x86 / x64

Entry Offset:
- `0x...`

Major Components:
- decoder stub
- API resolver
- payload loader
- network routine

API Resolution:
- Method: PEB traversal + API hashing
- Resolved APIs:
  - VirtualAlloc
  - LoadLibraryA
  - GetProcAddress

Decoded Strings:
- ...

Payload:
- Type: raw shellcode / embedded PE / downloader
- Evidence:
  - ...

Behavior Summary:
- ...
```

---

# 11. Packer / Unpacking 逆向筆記

## 11.1 Packer 是什麼？

Packer 把原始程式壓縮、加密或包裝起來，讓靜態分析看到的是「殼」，不是原始程式。

高階結構：

```text
Packed file on disk
↓
Packer stub runs
↓
Decompress / decrypt original code
↓
Resolve imports
↓
Transfer execution to OEP
```

## 11.2 為什麼 malware 常用 packer？

```text
隱藏字串
隱藏 imports
改變 hash
阻礙靜態分析
延遲真正 payload 顯現
混淆控制流程
增加分析成本
```

## 11.3 靜態 packer 跡象

| 跡象 | 可能意義 |
|---|---|
| 高 entropy section | 壓縮或加密 |
| Imports 極少 | 執行期動態解析 |
| Entry Point 在奇怪 section | unpacking stub |
| Section 權限 RWE | 解包後執行 |
| Raw size 與 virtual size 差距大 | 執行期填充 |
| 字串極少 | 字串被加密或壓縮 |
| Known packer signature | UPX / Themida / VMProtect 等 |
| Overlay 大 | 可能附加 payload |

## 11.4 動態 unpacking 證據

動態分析可能看到：

```text
VirtualAlloc / VirtualProtect
寫入記憶體 buffer
記憶體權限改成 executable
解密 loop
LoadLibrary / GetProcAddress
跳轉到新區域
原本沒有的 imports 行為出現
記憶體中出現 MZ/PE
```

## 11.5 OEP 是什麼？

OEP，Original Entry Point，指原始程式真正入口點。

對 packed file：

```text
Entry Point = packer stub 入口
OEP = 解包後原始程式入口
```

Unpacking 的核心目標之一是找到 OEP。

## 11.6 典型 unpacking stub 流程

```text
1. 啟動於 packer entry point
2. 檢查環境或 anti-debug
3. 配置記憶體
4. 解壓或解密原始程式碼
5. 修復 imports
6. 修正 relocation
7. 改記憶體權限
8. 跳到 OEP
```

## 11.7 如何判斷「可能跳到 OEP」

常見跡象：

```text
大量解密/解壓 loop 結束
記憶體中出現可讀字串
Import resolving 完成
程式跳到不同 section 或新配置區域
stack 狀態接近正常程式啟動
開始呼叫真實功能 API
```

## 11.8 IAT 修復的概念

IAT，Import Address Table，是 PE 載入外部 API 的重要結構。

Packed malware 可能：

```text
原始 IAT 被隱藏
執行時才 LoadLibrary / GetProcAddress
動態填入 API address
```

分析時的目標：

```text
知道解包後程式實際使用哪些 API
把動態解析 API 對應回可讀名稱
在報告中列出 capability
```

不一定每次都要產出可執行的 unpacked binary。

## 11.9 Unpacking 分析目標

| 目標 | 是否必要 |
|---|---|
| 找出真正 payload 類型 | 必要 |
| 解出字串 / config | 常常必要 |
| 確認 OEP | 很有用 |
| 產出可重新執行的 unpacked EXE | 不一定 |
| 完美修復 IAT | 不一定 |
| 完整還原原始碼 | 不現實 |

## 11.10 Unpacking 報告模板

```markdown
### Packing / Unpacking Analysis

Static Indicators:
- High entropy: yes/no
- Suspicious sections:
- Import table:
- Entry point section:
- Overlay:

Dynamic Indicators:
- Allocated executable memory:
- Runtime API resolving:
- Memory region containing PE:
- Jump to unpacked code:

OEP Candidate:
- Address:
- Evidence:

Recovered Artifacts:
- Strings:
- Imports:
- Config:
- Payload hash if dumped:

Conclusion:
- Packed with known/unknown packer
- Payload appears to be ...
```

---

# 12. Process Hollowing 的逆向補強

## 12.1 你已經知道的動態證據

動態分析中，Process Hollowing 常見證據鏈：

```text
Parent process
↓
CreateProcess with suspended child
↓
Unmap original image
↓
Allocate memory in child
↓
Write payload PE into child memory
↓
Set thread context
↓
Resume thread
↓
Child process image on disk ≠ memory code actually executing
```

可疑 API 清單：

```text
CreateProcess
NtUnmapViewOfSection / ZwUnmapViewOfSection
VirtualAllocEx
WriteProcessMemory
GetThreadContext
SetThreadContext
ResumeThread
```

## 12.2 逆向要補的是什麼？

動態證據告訴你「疑似 hollowing 發生」。

逆向要補：

```text
payload 從哪裡來？
payload 是否 embedded PE？
payload 是否解密？
payload 是否壓縮？
payload 的 ImageBase / EntryPoint 是什麼？
payload imports 是什麼？
payload config 在哪？
hollowed target 為什麼選這個程序？
```

## 12.3 Hollowing Loader 逆向切入點

在 decompiler 中找：

```text
CreateProcessW / CreateProcessA
VirtualAllocEx
WriteProcessMemory
SetThreadContext
ResumeThread
```

然後用 cross references 回推：

```text
WriteProcessMemory 的 buffer 來自哪裡？
buffer 是 resource？
是 overlay？
是網路下載？
是解密函式輸出？
是硬編碼 blob？
```

## 12.4 找 embedded PE

常見位置：

```text
resource
.data section
.rdata section
overlay
heap buffer
解密後的 memory buffer
```

尋找特徵：

```text
MZ
PE\0\0
This program cannot be run in DOS mode
section names
import strings
```

注意：

```text
MZ 可能被 XOR 或壓縮，靜態看不到。
```

## 12.5 逆向 Hollowing Loader 的資料流

建議畫出資料流：

```text
[encoded blob]
      ↓
[decode/decompress function]
      ↓
[payload PE buffer]
      ↓
[parse PE headers]
      ↓
[allocate remote memory]
      ↓
[write headers]
      ↓
[write sections]
      ↓
[set entrypoint]
      ↓
[resume target thread]
```

## 12.6 觀察 PE loader 行為

如果 loader 自己手動載入 PE，常會做：

```text
讀 DOS header
讀 NT headers
讀 section headers
複製 PE headers
逐 section 複製 raw data
處理 relocation
處理 imports
設定 entrypoint
```

逆向時看到大量 PE header 欄位存取，就要提高注意。

## 12.7 Hollowed Payload 的重點欄位

對 embedded payload：

| 欄位 | 分析目的 |
|---|---|
| Machine | x86 / x64 |
| ImageBase | 是否需要 relocation |
| EntryPoint | 真正開始執行位置 |
| Sections | payload 結構 |
| Imports | payload 能力 |
| Resources | 是否還有下一階段 |
| Strings | IOC / config |
| Compile timestamp | 低可信但可記錄 |

## 12.8 Hollowing 分析報告模板

```markdown
### Process Hollowing Reverse Engineering Notes

Suspicious API Chain:
- CreateProcess with suspended flag:
- NtUnmapViewOfSection:
- VirtualAllocEx:
- WriteProcessMemory:
- SetThreadContext:
- ResumeThread:

Target Process:
- Image:
- Command line:
- Reason chosen / hypothesis:

Payload Source:
- Resource / Overlay / Section / Download / Unknown

Payload Transformation:
- Decryption:
- Decompression:
- Copy routine:

Embedded Payload:
- MZ/PE found:
- Architecture:
- EntryPoint:
- Imports:
- Strings:
- Config:

Memory vs Disk Mismatch:
- Disk image:
- Memory image:
- Evidence:

Conclusion:
- Confidence: Low / Medium / High
```

## 12.9 與 Sysmon / EDR 的連結

逆向補強能解釋為什麼 SOC 看到：

```text
合法程序名稱
但異常網路連線
但不尋常 parent
但 command line 正常
但記憶體區域可疑
但 DLL / imports 與行為不一致
```

例如：

```text
notepad.exe 連外
```

動態只說「可疑」。

逆向可以補：

```text
notepad.exe 是 hollowing target。
真正執行的是 embedded PE payload。
payload 從 resource 解密後寫入 notepad.exe 記憶體。
```

---

# 13. Anti-Analysis 的辨識，而不是繞過

## 13.1 常見 Anti-Analysis 類型

| 類型 | 目標 |
|---|---|
| Anti-debug | 偵測 debugger |
| Anti-VM | 偵測虛擬機 |
| Anti-sandbox | 偵測沙箱環境 |
| Anti-disassembly | 干擾反組譯 |
| Anti-decompilation | 讓 pseudo-C 混亂 |
| Timing check | 偵測單步執行或沙箱加速 |
| API hashing | 隱藏 imports |
| String encryption | 隱藏 IOC |
| Control-flow flattening | 混淆流程 |
| Opaque predicate | 製造假分支 |

## 13.2 Anti-debug 常見 API

```text
IsDebuggerPresent
CheckRemoteDebuggerPresent
NtQueryInformationProcess
OutputDebugString
GetTickCount / QueryPerformanceCounter
```

分析重點：

```text
它是否只是在檢查？
檢查失敗後會退出？
會走假 payload？
會延遲執行？
會刪除自身？
```

## 13.3 Anti-VM 字串

常見線索：

```text
VBox
VirtualBox
VMware
QEMU
Hyper-V
VBOX__
VMTools
SbieDll
```

## 13.4 Anti-disassembly 跡象

```text
大量 junk code
不合理 jump
重疊指令
間接跳轉
大量 exception-driven flow
永遠不會成立的條件
```

## 13.5 報告重點

不要寫：

```text
已成功繞過 anti-debug
```

應寫：

```text
樣本包含 anti-debug 檢查。
在 function X 中呼叫 IsDebuggerPresent。
若偵測到 debugger，程式走向 early exit path。
這可能導致動態沙箱漏報。
```

---

# 14. 從逆向結果回填動態分析報告

## 14.1 逆向結果如何支援動態分析？

| 動態觀察 | 逆向補強 |
|---|---|
| 寫入 `%TEMP%\abc.exe` | Resource 內嵌 PE 被解密後寫出 |
| 建立 Run Key | 找到 persistence function 與 value data |
| powershell.exe 啟動 | 找到命令列建構邏輯 |
| notepad.exe 連外 | 找到 hollowed payload |
| 字串看不到 C2 | 找到 string decoder |
| imports 很少 | 找到 runtime API resolver |
| 高 entropy | 找到 unpacking stub |
| 快速退出 | 找到 anti-debug / anti-VM branch |

## 14.2 逆向產出的 IOC

```text
解密後 domain
解密後 URI
User-Agent
Mutex
檔案路徑
Registry key
Service name
Scheduled task name
Embedded payload hash
YARA strings
API hash mapping
Config structure
```

## 14.3 逆向產出的 TTP

```text
T1055 Process Injection
T1095 Non-Application Layer Protocol
T1059 Command and Scripting Interpreter
T1547 Registry Run Keys / Startup Folder
T1053 Scheduled Task
T1027 Obfuscated Files or Information
T1105 Ingress Tool Transfer
```

## 14.4 報告語氣

避免絕對化：

```text
❌ 這一定是 Process Hollowing
✅ 觀察到與 Process Hollowing 一致的 API chain 與 memory/disk mismatch，信心程度 High
```

---

# 15. 小型 Lab 路線

> 所有 Lab 都應使用 benign 自製程式、公開教學 crackme、CTF binary，或隔離樣本。不要使用真實惡意程式作為初學材料。

## Lab RE-1：組語與函式呼叫

目標：

```text
理解 mov/call/cmp/jmp/ret
理解 x64 前四個參數
能看懂簡單函式
```

材料：

```text
自己寫的 hello world
自己寫的加法函式
自己寫的 if/else
```

觀察：

```text
main
function call
return value
branch
```

## Lab RE-2：PE 結構觀察

目標：

```text
認識 MZ、PE、sections、imports、entrypoint
```

材料：

```text
notepad.exe
自製 hello.exe
一個 benign DLL
```

工具：

```text
PE-bear
CFF Explorer
Detect It Easy
Ghidra
```

## Lab RE-3：Imports 與行為假設

目標：

```text
從 import table 推測功能
```

材料：

```text
自製會讀寫文字檔的小程式
自製會讀 Registry 的小程式
```

觀察：

```text
CreateFile
ReadFile
WriteFile
RegOpenKey
RegQueryValue
```

## Lab RE-4：Ghidra 函式命名

目標：

```text
練習從 API caller 命名函式
```

任務：

```text
找 main
找字串
找 xrefs
重命名函式
寫函式筆記
```

## Lab RE-5：Debugger 基礎

目標：

```text
用 x64dbg / WinDbg 看 registers、stack、breakpoint
```

材料：

```text
notepad.exe
自製 benign 程式
```

觀察：

```text
breakpoint
step over
registers
stack
memory dump
```

## Lab RE-6：String Decoder 模擬

目標：

```text
理解解碼 loop 與解密後字串
```

材料：

```text
自製 benign 程式：內含 XOR 編碼的普通字串，例如 HelloLab
```

觀察：

```text
encoded bytes
decode loop
decoded buffer
xrefs
```

## Lab RE-7：Packed 樣本概念觀察

目標：

```text
理解 packed vs unpacked 差異
```

材料：

```text
自製 benign 程式
使用合法 packer 對自製程式加殼
```

觀察：

```text
entropy
imports
entrypoint
runtime strings
memory
```

## Lab RE-8：Shellcode 只讀分析

目標：

```text
理解 raw bytes 如何被反組譯
```

材料：

```text
安全教學用 shellcode dump 或 CTF raw bytes
不執行，只反組譯
```

觀察：

```text
architecture
entry offset
decoder loop
API resolver 概念
strings
```

## Lab RE-9：Process Hollowing 報告演練

目標：

```text
把動態證據與逆向證據合併成報告
```

材料：

```text
範例 log
範例 pseudo-code
範例 memory map
```

任務：

```text
判斷 payload source
判斷 API chain
判斷 target process
寫 confidence
```

---

# 16. 速查表

## 16.1 API 類別速查

### 檔案

```text
CreateFile
ReadFile
WriteFile
DeleteFile
MoveFile
CopyFile
GetTempPath
GetTempFileName
```

### Registry

```text
RegOpenKey
RegCreateKey
RegSetValue
RegQueryValue
RegDeleteValue
```

### 程序

```text
CreateProcess
ShellExecute
WinExec
TerminateProcess
OpenProcess
```

### 記憶體

```text
VirtualAlloc
VirtualAllocEx
VirtualProtect
VirtualProtectEx
ReadProcessMemory
WriteProcessMemory
```

### DLL / API Resolution

```text
LoadLibrary
GetProcAddress
LdrLoadDll
LdrGetProcedureAddress
```

### Thread

```text
CreateThread
CreateRemoteThread
GetThreadContext
SetThreadContext
ResumeThread
SuspendThread
```

### 網路

```text
socket
connect
send
recv
InternetOpen
InternetConnect
InternetOpenUrl
HttpOpenRequest
HttpSendRequest
WinHttpOpen
WinHttpConnect
WinHttpSendRequest
```

### Crypto / Encoding

```text
CryptAcquireContext
CryptCreateHash
CryptHashData
CryptDeriveKey
CryptEncrypt
CryptDecrypt
BCryptOpenAlgorithmProvider
BCryptEncrypt
BCryptDecrypt
```

## 16.2 可疑組合速查

| API 組合 | 可能行為 |
|---|---|
| CreateFile + WriteFile | 寫檔 / drop payload |
| RegSetValue + Run key | Registry persistence |
| CreateProcess + powershell | Script execution / LOLBin |
| VirtualAlloc + VirtualProtect + call buffer | unpacking / shellcode |
| LoadLibrary + GetProcAddress | dynamic API resolving |
| OpenProcess + WriteProcessMemory + CreateRemoteThread | injection-like behavior |
| CreateProcess suspended + SetThreadContext + ResumeThread | hollowing-like behavior |
| FindResource + LoadResource + WriteFile | resource dropper |
| GetProcAddress + API hashing loop | import hiding |
| CryptDecrypt + network string | encrypted config |

## 16.3 逆向判斷信心程度

| Confidence | 條件 |
|---|---|
| Low | 只有單一可疑字串或單一 API |
| Medium | 多個靜態線索互相支持 |
| High | 靜態 + 動態 + 逆向資料流一致 |
| Confirmed | 已觀察參數、payload、行為與 log 完整閉環 |

---

# 17. 逆向報告模板

```markdown
# Reverse Engineering Notes

## 1. Sample Metadata

- File name:
- SHA256:
- File type:
- Architecture:
- Compile timestamp:
- Packer:
- Analysis date:
- Analyst:

## 2. Executive Summary

簡短描述樣本功能、風險、主要技術。

## 3. Static Triage

### PE Structure

- Sections:
- Entry point:
- Imports:
- Resources:
- Overlay:
- Entropy:

### Strings

- File paths:
- Registry:
- Network:
- Commands:
- Debug / VM:
- Other:

## 4. Decompiler Findings

### Important Functions

| Address | Name | Purpose | Confidence |
|---|---|---|---|
| | | | |

### Function Notes

#### Function: `...`

- Address:
- Called by:
- Calls:
- Purpose:
- Evidence:
- Output:
- Confidence:

## 5. Debugging Findings

- Breakpoints:
- API parameters:
- Decoded strings:
- Memory regions:
- Runtime behavior:

## 6. Packing / Unpacking

- Packer indicators:
- Runtime unpacking:
- OEP candidate:
- Unpacked payload:
- IAT/API resolving:

## 7. Shellcode Analysis

- Architecture:
- Entry offset:
- Decoder:
- API resolver:
- Strings:
- Payload:
- Behavior:

## 8. Process Hollowing / Injection Evidence

- API chain:
- Target process:
- Payload source:
- Payload transformation:
- Memory vs disk mismatch:
- Confidence:

## 9. IOC

### File

| Type | Value |
|---|---|
| SHA256 | |
| Dropped file | |

### Registry

| Key | Value |
|---|---|
| | |

### Network

| Type | Value |
|---|---|
| Domain | |
| URL | |
| IP | |
| User-Agent | |

### Mutex / Other

| Type | Value |
|---|---|
| Mutex | |

## 10. MITRE ATT&CK Mapping

| Technique | Evidence | Confidence |
|---|---|---|
| | | |

## 11. Detection Opportunities

### YARA Ideas

- Stable strings:
- PE section traits:
- Config structure:
- Embedded payload markers:

### Sigma / SIEM Ideas

- Process tree:
- Command line:
- Sysmon Event ID:
- Registry:
- Network:

## 12. Conclusion

- Final classification:
- Primary behavior:
- Payload:
- Recommended containment:
- Recommended detection:
```

---

# 18. 參考資料

## 官方與主要工具文件

- Microsoft PE/COFF Format  
  https://learn.microsoft.com/en-us/windows/win32/debug/pe-format

- Microsoft x64 Calling Convention  
  https://learn.microsoft.com/en-us/cpp/build/x64-calling-convention

- Microsoft WinDbg User-Mode Debugging  
  https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/getting-started-with-windbg

- Ghidra 官方專案  
  https://github.com/NationalSecurityAgency/ghidra

- Ghidra Documentation  
  https://ghidradocs.com/

- x64dbg 官方網站  
  https://x64dbg.com/

- x64dbg GitHub  
  https://github.com/x64dbg/x64dbg

- The Official Radare2 Book  
  https://book.rada.re/

- YARA Documentation  
  https://yara.readthedocs.io/

- MITRE ATT&CK - Process Injection T1055  
  https://attack.mitre.org/techniques/T1055/

## 建議延伸學習方向

```text
1. x86/x64 Assembly
2. Windows Internals
3. PE Loader
4. Ghidra function analysis
5. x64dbg debugging
6. String deobfuscation
7. API hashing identification
8. PE unpacking concepts
9. Shellcode reverse engineering
10. Memory forensics
```

---

# 結語

逆向工程不是要你一開始就把整個 malware 反完，而是逐步回答關鍵問題：

```text
它真正的 payload 在哪？
它如何解密或解包？
它呼叫哪些 API？
它如何建立 persistence？
它如何執行其他程序？
它是否注入或 hollowing？
它解出哪些 IOC？
它的行為能否被 log 與偵測規則捕捉？
```

當你能把：

```text
Procmon / Sysmon 的行為證據
+
Ghidra / x64dbg 的逆向證據
+
MITRE ATT&CK 的 TTP 描述
+
IOC / Detection logic
```

串成一份報告，你就不只是「會看工具」，而是已經進入真正 Malware Reverse Engineering 的分析思維。
