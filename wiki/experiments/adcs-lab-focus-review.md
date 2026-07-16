---
id: exp-adcs-lab-focus-review
type: experiment
topic: "MOND.local AD CS 偵測實驗室建置基線"
status: completed
hypothesis: "若先明確列出 Host、AD DS 與 AD CS 的身分、權限、遙測和回復欄位，並把 CA 稽核事件送進 Wazuh，便可把 AD CS 從高風險黑箱轉成可安全驗證的防禦實驗室。"
result: partial
confidence: medium
verified_on_this_machine: false
code_paths: []
sources: [adcs-lab-focus-architecture, adcs-lab-focus-research]
created: 2026-07-15
updated: 2026-07-15
related: [adcs-esc-detection-baseline, wazuh-ad-soc-architecture-review]
---

# 實驗：MOND.local AD CS 偵測實驗室建置基線

## H - Hypothesis

目前圖的 AD CS 方塊沒有 CA 類型、範本權限、稽核或 Web Enrollment 狀態。若將這些欄位與 Wazuh 事件收集納入設計，便能以防禦視角觀測憑證生命週期與權限變更。

## I - Implementation

- 轉錄圖片中的 `MOND.local`、帳號、SMB、RDP、SQL service user 與 GPO 設計意圖。
- 查證 Server 2019 AD DS 功能等級、AD CS audit policy／audit filter、Web Enrollment、Wazuh Windows event channel、Windows 11 與 OPNsense 版本。
- 建立 [[adcs-esc-detection-baseline]] 與子專案的 AD CS 環境基線，所有未實測值標記為 `env-specific` 或待驗證。

## V - Verification

| ID | 檢查 | 結果 |
|---|---|---|
| V1 | 圖片元素是否完整轉成待填欄位 | 通過；DC、AD CS、帳號與主機欄位均已列出 |
| V2 | 版本與功能等級是否有官方依據 | 通過；Server 2019 使用 Windows Server 2016 FFL/DFL，Wazuh/OPNsense/Windows 版本已記錄來源 |
| V3 | CA 稽核事件是否已送入 Wazuh | 待實機驗證；尚未取得 CA、GPO、Agent 或 Dashboard 存取 |
| V4 | 測試範本是否限制於專用群組且可回復 | 待實機驗證 |

本機無 Python、VM、AD CS、OPNsense 或 Wazuh 存取；本輪只完成文件與來源層驗證，沒有宣稱服務已安裝或事件已到達。

## R - Reflection

- CA audit filter 不是完整偵測；範本與 ACL 的 AD 物件變更也需要 DC 端稽核。
- 單一 Server 2019 同時承載 DC 與 Enterprise Root CA 可用於隔離的課堂 lab，但不是生產 PKI 架構；日後擴大時應拆出 CA 主機並採離線 Root CA／線上 Issuing CA。
- 版本號應有「選定版本」及「實際 build/patch／安裝日期」兩欄，否則拓撲圖很快過期。

## K - Knowledge Ingestion

- 圖片來源：[[adcs-lab-focus-architecture]]
- 官方研究：[[adcs-lab-focus-research]]
- 可複用概念：[[adcs-esc-detection-baseline]]

## C - Code Preservation

尚未建立任何 CA、GPO、Wazuh 或 OPNsense 設定檔，因此 `code_paths` 為空。後續實作時，應保存去敏後的 GPO 匯出、Wazuh Agent 設定、CA 稽核設定與 OPNsense 規則到 `code/YYYY-MM-DD/adcs-lab/`，並附 manifest、回復步驟與實機驗證證據。

## Next Questions

1. `DC01` 的實際 IP、VLAN、DNS 與 Wazuh Manager FQDN 是什麼？
2. AD CS 是否只作單機隔離 lab，或要規劃日後分離的 CA01？
3. 哪些 template 是安全基線，哪一份是有時限、可回復的偵測測試 template？
4. CA Security log、Directory Service log 與 template 變更事件是否已在 Wazuh 可查？
