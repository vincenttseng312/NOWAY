---
id: doc-adcs-environment
title: "AD CS 防禦偵測實驗室基線"
doc_type: environment
category: environment
summary: "MOND.local 的 AD CS 建置欄位、版本基線、CA 稽核與 Wazuh 遙測設計；所有值均為設計值，待實機驗證。"
tags: [cat:environment, type:environment, source:adcs, status:env-specific]
related_entities: [ent-host-dc, ent-host-wazuh-manager, ent-account]
related_docs: [doc-ad-environment, doc-host-inventory, doc-windows-events-into-wazuh, doc-architecture-baseline-validation]
mitre_attack: []
wazuh_sources: [Security, Application, System]
windows_event_ids: ["4882", "4885", "4886", "4887", "4888", "4890", "4891", "4892", "4896", "4898"]
risk_level: high
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft AD DS functional levels", "Microsoft Audit Certification Services", "Wazuh Windows event channel"]
keywords: ["AD CS", "CA", "certificate template", "ESC detection", "AuditFilter", "MOND.local"]
last_updated: 2026-07-15
---

# AD CS 防禦偵測實驗室基線

## 1. 適用範圍

此頁是 `MOND.local` 課堂／授權實驗室的設計基線，不是部署完成宣告。圖片顯示 AD CS 為 planned，IP、實際 OS build、CA 設定、範本、ACL、GPO、Agent ID 與事件抵達狀態都必須由實機證據填寫。

## 2. 最推薦的第一版建置

| 區塊 | 推薦基線 | 理由與限制 |
|---|---|---|
| AD DC | `DC01.mond.local`；Windows Server 2019 Standard Evaluation/GUI；AD DS、DNS、Global Catalog；FFL/DFL `Windows Server 2016` | 規劃版本 Server 2019（草稿曾為 2022/2025，raw 保留原值，可能再調）；Server 2019 無專屬 AD 功能等級，最高採 Windows Server 2016 FFL/DFL |
| AD CS | `MOND-ROOT-CA`，Enterprise Root CA，暫與 `DC01` 同機 | 單機可降低課堂 lab 成本；**僅限隔離 lab**。生產或擴大版應採離線 Root CA + 獨立 Issuing CA |
| Client | Windows 11 Enterprise 25H2；安裝日套用最新累積更新 | 既有 VM 可直接採用，支援期較 24H2 長；不要把單一 build 號寫死 |
| Wazuh | all-in-one Wazuh 4.14.6；Ubuntu Server 24.04 LTS；4 vCPU/8 GB RAM/200 GB disk | 4.14.6 是研究時官方文件可見的穩定 4.x；不以 5.0 beta 做專題基線 |
| OPNsense | CE 26.1.11；2 vCPU/8 GB RAM/120 GB disk | 研究時官方 release 可見的最新 patch；部署日仍需再檢查 release 頁 |
| AI Server | Ubuntu Server 24.04 LTS；4 vCPU/16 GB RAM/100 GB disk；不加入網域 | 僅保留到整合層的只讀 RAG/MCP 存取，不給 DC 或 Wazuh 管理權限 |

## 3. 主機方塊必填欄位

所有 Server 2019、Windows 11、Wazuh、OPNsense、AI Server 方塊均依 `_meta/entity-model.md` 的 Host 基礎欄位擴充如下：

| 欄位群 | 應直接填在圖上的內容 | 範例／規則 |
|---|---|---|
| 身分 | hostname、FQDN、role、status | `DC01` / `dc01.mond.local` / `AD DS+DNS+AD CS (lab)` / building |
| 網路 | IP/CIDR、zone/VLAN、gateway、DNS | `10.10.20.10/24`、`VLAN20-AD`；皆為 proposed，實作後換成實際值 |
| 平台 | OS edition、version、build、CPU/RAM/disk | `Windows Server 2019 / 20348.x`；build 以實機 `winver`／更新紀錄為準 |
| 遙測 | Wazuh agent、agent ID、版本、採集 channel | `installed / env-specific / Security,System,Application,Sysmon`；OPNsense 標 `agentless syslog` |
| 稽核 | 已啟用 audit policy／log retention | DC：帳號、Kerberos、DS change、policy change、Certification Services；端點：Logon、Process Creation、PowerShell、Sysmon |
| 相依 | AD join、DNS 指向、log destination、管理來源 | Client 指向 `DC01` DNS 並加入 `MOND.local`；Windows Agent 指向 Wazuh Manager；AI 只讀整合層 |
| 維運 | owner、backup/snapshot、last verified、status | 不把「planned」與「done」混用；每次改版記錄日期與證據 |

建議圖上先保留邏輯區域，實際 CIDR 待 OPNsense 建置時填入：`VLAN10-MGMT`、`VLAN20-AD`、`VLAN30-CLIENT`、`VLAN40-SOC`、`VLAN50-AI`、`VLAN90-ATTACK`。預設拒絕跨區流量，只為 DNS/AD、Wazuh Agent、必要管理與只讀 AI 整合建立 allow-list。

## 4. AD DC 方塊必填欄位

| 欄位 | 第一版建議 |
|---|---|
| Domain / NetBIOS | `MOND.local` / `MOND` |
| DC | `DC01` / `dc01.mond.local`；單 DC 時同時為 Global Catalog |
| AD DS 功能等級 | Forest functional level：`Windows Server 2016`；Domain functional level：`Windows Server 2016` |
| DNS 與站台 | AD-integrated DNS；`TAIPEI-01` site；填入對應 AD subnet／CIDR |
| 高價值帳號 | `MOND\\Administrator`：標記「高價值目標→重點監控」；日常操作另用個人管理帳號，不以內建 Administrator 做一般管理 |
| 測試帳號 | `MOND\\Jean`、`MOND\\Klee`、SQL 專用 service identity；服務帳號不可登入互動式桌面，日後可改用 gMSA |
| 核心 GPO | Advanced Audit Policy、PowerShell Script Block Logging、Process Creation、Wazuh Agent 配置、RDP/WinRM 來源限制 |
| Wazuh 事件 | Security、System、Application、Directory Service、DNS Server、Sysmon（若部署）；記錄 Agent ID 與 Manager FQDN |

## 5. AD CS 方塊必填欄位與安全預設

| 欄位 | 第一版建議 |
|---|---|
| CA type / name / host | Enterprise Root CA / `MOND-ROOT-CA` / `DC01.mond.local`；在圖上明示 `LAB ONLY` |
| Crypto / validity | RSA 3072 + SHA-256；CA 5 年、issued certificate 1 年，需連同實際值和理由記錄 |
| Template inventory | template name、OID/version、EKU、subject/SAN 規則、manager approval、enrollment/autoenrollment ACL、owner、是否啟用 |
| 權限安全線 | 安全基線範本只給必要群組；不得把寬鬆 enrollment 權限或可任意指定身分設定當成常態 |
| ESC 偵測測試 | 另建專用、短期、可回復的 lab template，只授權非特權測試群組；測完停用或刪除，保留前後 ACL／事件證據 |
| CA auditing | GPO：`Object Access > Audit Certification Services` Success + Failure；CA audit filter：全部類別；記錄啟用日期與執行者 |
| 監控事件 | 高優先 4882、4885、4890–4892、4896；生命週期 4886–4888、4870；基線 4898 與其他 4868–4898 事件 |
| Web Enrollment | `Disabled / Not installed` 為預設；若要測試，另記錄 HTTPS、隔離範圍、認證、Wazuh 事件與關閉／回復日期 |
| Wazuh | CA 主機的 Agent 送出 Security、System、Application；告警可關聯 CA、template、requester、帳號與來源主機 |

> AD CS 的範本與 ACL 也是 AD 物件。除 CA Security events 外，還要以 DC 的 Directory Service Changes／Access 稽核與變更管理追蹤範本異動。

## 6. 驗收與回復

1. 驗收 `DC01` 的 FQDN、DNS、FFL/DFL、站台／subnet、GPO 和 Wazuh Agent active 狀態。
2. 驗收 CA audit policy 與 CA audit filter，然後以合法測試申請確認 4886／4887 可在 Wazuh 查到。
3. 比對 template 清冊與 ACL；測試範本只能由指定 lab 群組申請。
4. 驗收 OPNsense 只允許必要跨區流量；AI 無權直接管理 AD、CA 或 Wazuh。
5. 完成每次測試後停用測試範本、移除暫時規則、保存去敏設定與驗收證據。

## 7. 關聯

- AD 環境：[[doc-ad-environment]]
- 主機清冊：[[doc-host-inventory]]
- 架構驗證：[[doc-architecture-baseline-validation]]
- 父層概念：[[adcs-esc-detection-baseline]]
