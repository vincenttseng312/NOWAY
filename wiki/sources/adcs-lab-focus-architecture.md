---
type: source
title: "AD CS 實驗室聚焦圖（2026-07-15）"
tags: [active-directory, adcs, wazuh, architecture, methodology]
sources: [raw/adcs-lab-focus-architecture-2026-07-15.md]
raw: raw/adcs-lab-focus-architecture-2026-07-15.md
ingested: 2026-07-15
created: 2026-07-15
updated: 2026-07-15
---

# AD CS 實驗室聚焦圖

圖片將專題焦點收斂到 `MOND.local` 的 AD DC、規劃中的 AD CS、Windows Server 2019 與 Windows 11 Enterprise。已明示的帳號與服務是 `MOND\\Jean`、`MOND\\Klee`、`MOND\\SQLuser`、SMB share、RDP 低權限帳號與 GPO；CA 類型、範本權限、稽核、主機名、IP/VLAN 和 Agent 狀態尚未指定。

本次將其轉成可驗證的建置基線：每個主機補上 Host 欄位，DC 補 AD DS/DNS／功能等級／GPO，AD CS 補 CA、範本、權限與稽核。防禦目的為偵測憑證生命週期與權限異動，而不是讓危險範本長期存在。

## 關聯

- 官方研究：[[adcs-lab-focus-research]]
- 概念：[[adcs-esc-detection-baseline]]
- 實驗：[[adcs-lab-focus-review]]
