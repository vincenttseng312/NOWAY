---
type: concept
title: "AD CS ESC 憑證濫用偵測基線"
tags: [active-directory, adcs, detection-engineering, wazuh, methodology]
sources: [adcs-lab-focus-architecture, adcs-lab-focus-research]
created: 2026-07-15
updated: 2026-07-15
---

# AD CS ESC 憑證濫用偵測基線

AD CS 的偵測目標不是只看「是否成功核發憑證」，而是將 CA、憑證範本、enrollment 權限、申請者、核發結果與後續登入行為串成可回溯證據鏈。這適合放在 [[wazuh-ad-soc-architecture-review]] 所定義的端點遙測與最小信任邊界內。

## 最小資產清冊

每個 AD CS 方塊至少記錄：CA type、CA common name、hostname/FQDN、憑證鏈、發布的 template、template OID/version、EKU、enrollment/autoenrollment 權限、是否允許申請者提供 subject/SAN、是否需 manager approval、CA audit status、Web Enrollment status、CRL/AIA 位置、負責人與回復程序。

## 偵測優先順序

1. 高優先：CA 安全權限、audit filter、CA 設定／屬性異動，例如 4882、4885、4890–4892、4896。
2. 中優先：異常憑證要求、核發或撤銷，例如 4886–4888、4870；需關聯帳號、主機、template 與時間。
3. 基線：CA 啟停、備份／還原、CRL 作業與 template 載入，例如 4871–4881、4898。
4. 目錄層：template 與 enrollment ACL 是 AD 物件，還要用 DC 的 Directory Service Access／Changes 稽核補足。

## 安全的實驗方式

- 先建立安全基線，再建立獨立、可辨識、可回復的測試範本；測試範本只授權專用的非特權 lab 群組，完成觀測後立即停用或刪除。
- 不把高權限帳號、`Domain Users` 的廣泛 enrollment 權限，或可任意指定身分的設定當成常態配置。
- `Administrator` 是高價值目標；其登入、群組／權限、憑證申請與 CA 管理動作都必須在 Wazuh 與 Windows 事件中可追溯。

## 關聯

- 來源：[[adcs-lab-focus-architecture]]、[[adcs-lab-focus-research]]
- 實驗：[[adcs-lab-focus-review]]
- AD 遙測：[[windows-event-log-and-sysmon]]
