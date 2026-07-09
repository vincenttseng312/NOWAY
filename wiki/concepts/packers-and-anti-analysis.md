---
type: concept
title: "Packer、Obfuscation 與 Anti-Analysis 靜態跡象"
tags: [malware-analysis, dfir]
sources: [malware-static-dynamic-analysis-notes]
created: 2026-07-09
updated: 2026-07-09
---

# Packer、Obfuscation 與 Anti-Analysis 靜態跡象

惡意程式常用打包（packing）、混淆（obfuscation）與反分析（anti-VM/anti-debug）技術延遲真正 payload 暴露、阻礙逆向分析。這些技術本身不等於惡意（商業軟體也用 packer 保護），但出現在可疑樣本上時是重要的加權訊號。

## Packer

Packer 把原始程式壓縮、加密或包裝，執行時再解開真正 payload，目的包含減少檔案大小、保護商業軟體、阻礙逆向、改變 hash、隱藏 strings/imports、延遲真正 payload 暴露。

Packed 樣本常見跡象（多項疊加才有意義，單項不足）：

```text
[ ] Entropy 很高
[ ] Strings 很少
[ ] Imports 很少
[ ] Section 名稱異常（UPX0/.vmp0/.aspack 等，見 pe-static-analysis）
[ ] Entry point 位於奇怪 section
[ ] Raw Size / Virtual Size 差距大
[ ] RWX section
[ ] Overlay data 很大
[ ] Detect It Easy 顯示 packer/compiler 異常
[ ] 程式執行後記憶體中出現更多 strings / imports（需動態驗證）
```

## Obfuscation 靜態跡象

| 類型 | 跡象 |
|---|---|
| 字串加密 | 靜態 strings 幾乎沒有有意義內容 |
| API hashing | imports 少，但程式仍有複雜功能 |
| Control-flow flattening | 反編譯流程很亂 |
| Junk code | 大量無意義指令或函式 |
| Name obfuscation | 變數、函式名稱亂碼 |
| Layered payload | 多層 base64/gzip/xor/resource |

## Anti-VM 靜態跡象

可能出現的字串：`VMware`/`VirtualBox`/`VBox`/`QEMU`/`Hyper-V`/`sandbox`/`procmon`/`procexp`/`wireshark`/`fakenet`。可能查詢的環境特徵：Registry 中 VM driver/service、BIOS/motherboard string、MAC address vendor、CPU core count、RAM/Disk size、Running processes、User interaction。

**分析原則：看到 Anti-VM 字串不代表一定會逃避分析**——要動態觀察樣本是否因環境而停止、sleep、改變行為（呼應「不要只看單一證據」原則，見 [[malware-analysis-methodology]]）。分析環境的具體隔離措施見 [[malware-analysis-vm-setup]]。

## Anti-Debug 靜態跡象

常見 API/字串：`IsDebuggerPresent`、`CheckRemoteDebuggerPresent`、`NtQueryInformationProcess`、`OutputDebugString`、`BeingDebugged`（PEB 欄位）。分析重點：樣本是否偵測 debugger 後退出、是否對時間差敏感、是否檢查 breakpoint 或 process name。

## 與其他頁面的關聯

Entropy/section/import 的完整靜態分析脈絡見 [[pe-static-analysis]]；動態驗證這些靜態假設（例如樣本是否真的因偵測到 VM 而改變行為）見 [[dynamic-behavior-analysis]]；分析 VM 本身如何避免被偵測（ISO 掛載法等）見 [[malware-analysis-vm-setup]]。
