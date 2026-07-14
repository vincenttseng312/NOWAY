---
id: doc-ad-environment
title: "Active Directory 環境說明"
doc_type: environment
category: environment
summary: "本專題的 AD 網域環境：Domain Controller 提供認證與目錄服務，Windows 11 靶機加入網域。網域帳號/群組/認證事件記於 DC，經 Wazuh 蒐集。要看到這些事件，DC 端須開啟對應稽核政策（如 Audit Account Management）。"
tags: [cat:environment, type:environment, source:ad]
related_entities: [ent-host-dc, ent-host-win11-target, ent-account]
related_docs: [doc-host-roles, doc-windows11-target, evt-ad-security-overview, doc-windows-events-into-wazuh]
mitre_attack: []
wazuh_sources: []
windows_event_ids: ["4720", "4728/4732/4756", "4740", "4741 (電腦帳號建立)"]
risk_level: ""
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "Wazuh 官方文件"]
keywords: ["Active Directory", "網域環境", "Domain Controller", "網域加入", "稽核政策", "ad environment", "audit policy"]
last_updated: 2026-07-09
---

# Active Directory 環境說明

## 1. 環境概述
本專題內部網段有一台 **Active Directory Domain Controller（DC）**，提供網域認證與目錄服務；**Windows 11 靶機已加入該網域**（見 [[doc-windows11-target]]）。網域層級的帳號、群組、認證活動記錄在 DC，是本專題 AD 安全事件的主要來源（事件家族見 [[evt-ad-security-overview]]）。

> 網域名稱、DC 主機名/IP、DC 的 OS 版本（如 Windows Server 20xx）皆為部署相關（需依實際環境確認），填入 `entities/ent-host-dc` 卡。

## 2. 事件從哪裡來、前提是什麼
網域帳號活動產生 Windows 安全事件 → 由 Wazuh Agent 採集 → Manager 產生告警（路徑見 [[doc-windows-events-into-wazuh]]）。

**關鍵前提：稽核政策必須開啟。** 依 Microsoft 官方，要監控網域帳號與加入活動，需在 DC 的群組原則開啟對應的進階稽核（例如 **Audit Account Management**、**Audit Directory Service Access**）。若未開啟，相關事件不會產生，Wazuh 也收不到——這是「查無事件 ≠ 沒發生」的重要原因。

常見與 AD 相關的 Event ID（以 Microsoft 官方為準）：
- 帳號/群組管理：4720（建立帳號）、4728/4732/4756（加入群組）、4740（鎖定）。
- 電腦帳號：**4741**（電腦帳號建立，用於偵測網域加入類活動）。
- Kerberos 認證（4768/4769/4771 等）需個別確認採集與稽核設定。

## 3. Wazuh 如何監控 AD
依 Wazuh 官方，Wazuh 以「DC 上的 Windows 安全事件 + Sysmon 事件」為基礎，在 Manager 端以規則偵測 AD 相關 IOC（涵蓋帳號濫用、橫向移動、提權等）。實務上：
- Wazuh Agent 可裝在 DC 上以採集其安全/系統事件（**本專題 DC 是否納管、採集哪些通道需依實際環境確認**）。
- 部分偵測會建議在 DC 以 GPO 開啟特定稽核（例如檔案共享存取 Event ID 5145）——是否採用視需求，需確認。

> 若本專題 DC 未安裝 Agent，部分 AD 事件可能收不到，AI 判讀時應考慮此限制。

## 4. 主要實體
Host（DC、Win11 靶機）、Account（網域帳號）。對應 `entities/ent-host-dc`、`ent-acct-*`（實體卡待建）。

## 5. 可被 LLM 檢索的關鍵字
Active Directory、AD 網域、Domain Controller、網域加入、稽核政策、audit policy、Audit Account Management、4741、ad environment。

## 6. 相關文件連結
[[doc-host-roles]]、[[doc-windows11-target]]、[[doc-host-inventory]]、[[evt-ad-security-overview]]、[[doc-windows-events-into-wazuh]]；跨連父層 [[persistence-mechanisms]]。

## 7. 建議查證來源
- Microsoft：System Audit Policy recommendations、Appendix L Events to Monitor（learn.microsoft.com）。
- Wazuh：How to detect Active Directory attacks with Wazuh（wazuh.com）。

## 8. 後續可擴充內容
實際網域結構（OU/GPO/群組設計）、DC 是否納管與採集通道、啟用的稽核政策清單（填入後把 verification_status 提升）。
