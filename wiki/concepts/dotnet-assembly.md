---
type: concept
title: ".NET Assembly"
tags: [dotnet, windows]
sources: [dll-ms-learn]
created: 2026-07-08
updated: 2026-07-08
---

# .NET Assembly

Assembly 是 .NET 共通語言執行環境（Common Language Runtime, CLR）所執行的邏輯功能單元。實體上它仍然是一個 `.dll` 或 `.exe` 檔案，但內部結構與 Win32 DLL 截然不同，其設計目的正是為了消除 [[dll-dependency-hell]] 中所描述的依賴問題。

## 結構

一個 assembly 包含一份 **assembly manifest**，加上型別中繼資料、Microsoft Intermediate Language（MSIL）程式碼，以及其他資源。MSIL 無法直接執行 —— 必須交由 CLR 管理執行。Manifest 讓 assembly 具備自我描述能力，內含：assembly 名稱、版本資訊、文化（culture）資訊、strong name 資訊、assembly 內的檔案清單、型別參照資訊，以及相依的 assembly 資訊。

預設情況下，assembly 是該應用程式的私有資源；若要將其設為共用，需要賦予它 strong name，並發佈到 global assembly cache 中。

## 與 Win32 DLL 的差異

| 特性 | Win32 DLL | .NET Assembly |
|---|---|---|
| 自我描述 | 沒有 —— 沒有相依項目的 manifest | 有 —— manifest 列出所有相依的 assembly |
| 版本控管 | 作業系統不強制執行；仰賴開發者的紀律 | 由 CLR 記錄並強制執行，並可套用版本政策 |
| 並存部署（Side-by-side） | 可透過私有 DLL／搜尋順序技巧達成（見 [[dll-dependency-hell]]） | 原生支援 —— 不同應用程式可同時使用同一 assembly 的不同版本 |
| 隔離性 | 部分具備（私有 DLL、Windows File Protection） | 內建支援 —— 可做到自我完備、零影響的安裝 |
| 執行方式 | 直接以原生方式執行 | 在 CLR 控管下，依 manifest 中的安全性權限執行 |
| 語言 | 依編譯該 DLL 所用的語言而定 | 語言無關 —— 任何 .NET 語言都能產生與使用同一個 assembly（例如用 C# 撰寫，在 VB.NET 中使用） |

## 與其他頁面的關聯

來源文件將這個模型定位為對 [[dll-dependency-hell]] 中所列問題的直接架構回應；與其對照的一般 DLL 運作機制見 [[dynamic-link-library]]。
