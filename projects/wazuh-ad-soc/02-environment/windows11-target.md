---
id: doc-windows11-target
title: "Windows 11 靶機說明"
doc_type: environment
category: environment
summary: "本專題受監控的 Windows 11 端點：加入 AD 網域、安裝 Wazuh Agent，是攻擊模擬的目標與大多數事件的來源。Agent 透過 eventchannel 採集 Security/System/Application，PowerShell 需另開 Script Block Logging。"
tags: [cat:environment, type:environment, entity:host, source:windows-security]
related_entities: [ent-host-win11-target]
related_docs: [doc-host-roles, doc-ad-environment, doc-wazuh-agent, doc-windows-events-into-wazuh]
mitre_attack: []
wazuh_sources: []
windows_event_ids: []
risk_level: ""
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "Microsoft Windows Security Auditing 文件"]
keywords: ["Windows 11 靶機", "受監控端點", "Wazuh Agent", "eventchannel", "Script Block Logging", "windows11 target"]
last_updated: 2026-07-09
---

# Windows 11 靶機說明

## 1. 主機概述
本專題內部網段的 **Windows 11 端點**，具三個身分：
1. **受監控端點**：安裝 Wazuh Agent，回傳事件（見 [[doc-wazuh-agent]]）。
2. **網域成員**：已加入 AD 網域（見 [[doc-ad-environment]]），故也產生網域相關認證活動。
3. **攻擊目標**：外部攻擊者主機的攻擊模擬落點，是大多數告警的來源。

> 主機名、IP、Windows 11 版本/組建、Wazuh Agent id 皆為部署相關（需依實際環境確認），填入 `entities/ent-host-win11-target` 卡。

## 2. Wazuh Agent 採集什麼（官方事實）
依 Wazuh 官方文件：
- Agent 透過 **Windows Eventchannel** 採集事件；**預設監控的通道為 System、Security、Application**。
- 設定位於 `C:\Program Files (x86)\ossec-agent\ossec.conf` 的 `localfile` 區塊，`log_format` 設為 `eventchannel`，`location` 指定通道名稱。
- 可用 **XPATH 查詢**過濾 eventchannel 事件（例如依 EventID、LogonType 篩選 Security 通道），減少雜訊。

> 本專題實際採集哪些通道、是否加裝 Sysmon，需依實際 `ossec.conf` 確認。

## 3. PowerShell 記錄的前提
依 Wazuh/Microsoft：要看到 PowerShell 腳本內容，需**開啟 Script Block Logging**，事件會進 `Microsoft-Windows-PowerShell/Operational` 通道，並在 agent 設定中加入該通道的監控。未開啟時只能從程序建立（4688）看到命令列、看不到解碼後內容（見 [[evt-powershell-suspicious]]）。

## 4. 這台機器會產生哪些事件
登入/登出、帳號/群組、程序建立、RDP、PowerShell、安全設定變更等——即 04-windows-ad-events 各頁的來源。攻擊情境（05-attack-scenarios）多以此機為落點。

## 5. 主要實體
Host（本靶機，`ent-host-win11-target`）、其上的本機/網域 Account。

## 6. 可被 LLM 檢索的關鍵字
Windows 11 靶機、受監控端點、Wazuh Agent、eventchannel、ossec.conf、localfile、Script Block Logging、windows11 target。

## 7. 相關文件連結
[[doc-host-roles]]、[[doc-ad-environment]]、[[doc-wazuh-agent]]、[[doc-windows-events-into-wazuh]]、[[evt-powershell-suspicious]]

## 8. 建議查證來源
- Wazuh：How to collect Windows logs、localfile (ossec.conf) reference、Detecting PowerShell exploitation techniques（wazuh.com / documentation.wazuh.com）。
- Microsoft：Windows Security Auditing 文件。

## 9. 後續可擴充內容
實際 OS 版本/IP/主機名、採集通道清單、是否裝 Sysmon、稽核政策（填入後提升 verification_status）。
