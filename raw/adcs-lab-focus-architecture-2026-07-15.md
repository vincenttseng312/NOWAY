# AD CS 實驗室聚焦圖轉錄（2026-07-15）

## 來源與限制

- 使用者提供圖片：`codex-clipboard-83fe7efa-2f25-4773-85ad-4c91cea8d79d.png`
- 性質：設計意圖；除非有實機證據，不代表已部署或已開放。

## 圖中明示內容

- Windows Server 2022：2 vCPU @ 1 GHz、8 GB RAM、64 GB SSD。
- Windows 11 Enterprise：2 vCPU @ 1 GHz、4 GB RAM、64 GB SSD。
- AD DC（building）：網域 `MOND.local`，管理帳號 `Administrator`。
- AD CS（planned）：未列 CA 類型、名稱、憑證範本、權限或稽核。
- domain/Users（planned）：PC `CELL`；帳號 `MOND/Jean`、`MOND/Klee`。
- special settings（planned）：SMB share `C:\copy2D`、SQL service user `MOND/SQLuser`、RDP low privilege user `MOND/Klee`、GPO。

## 研究問題

1. 如何把主機、AD DC、AD CS 方塊改成可部署且可驗證的欄位集合？
2. Windows Server 2022 的可用 AD DS 功能等級為何？
3. 如何以防禦目的建立 AD CS ESC 憑證濫用偵測實驗室，而不把危險設定當成常態？
4. 元件的穩定版本及其版本證據應如何記錄？

## 關聯

- 官方研究：[[adcs-lab-focus-research]]
- 防禦概念：[[adcs-esc-detection-baseline]]
- H-I-V-R-K-C：[[adcs-lab-focus-review]]
