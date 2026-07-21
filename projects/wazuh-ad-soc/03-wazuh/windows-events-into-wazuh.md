---
id: doc-windows-events-into-wazuh
title: "Windows 事件如何進入 Wazuh"
doc_type: wazuh
category: wazuh
summary: "Windows 11 靶機/AD DC 產生的 Windows Event Log（Security、System、PowerShell 等通道）由 Wazuh Agent 讀取，送至 Manager 經 decoder 解析成 data.win.* 欄位、rule 比對後成為告警。providerName 與 location 指出事件來源。"
tags: [cat:wazuh, type:wazuh, source:windows-security]
related_entities: [ent-host-win11-target, ent-event]
related_docs: [doc-wazuh-agent, doc-wazuh-manager, evt-windows-security-overview]
keywords: ["Windows 事件", "eventchannel", "Event Log", "decoder", "data.win", "providerName", "location", "windows events into wazuh"]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "Microsoft Sysmon 官方文件", "Microsoft Windows Security Auditing 文件"]
last_updated: 2026-07-20
---

# Windows 事件如何進入 Wazuh

## 1. 路徑總覽

```
Windows Event Log 通道（Security / System / PowerShell-Operational / ...）
   │  （由 Windows 稽核政策決定產生哪些事件）
   ▼
Wazuh Agent（eventchannel 讀取）
   ▼
Wazuh Manager：decoder 解析 → data.win.system.* / data.win.eventdata.*
   ▼
rule 比對 → 產生 alert（含 rule.*、rule.mitre.*）
```

## 2. 關鍵欄位怎麼來
- `data.win.system.eventID`：原 Windows Event ID。
- `data.win.system.providerName`：事件來源提供者（如 Microsoft-Windows-Security-Auditing、Microsoft-Windows-PowerShell）——用來判斷事件屬於哪類來源。
- `data.win.eventdata.*`：事件的細節欄位（帳號、來源 IP、工作站等）。
- `location`：Wazuh 記錄的日誌來源位置/通道。

## 3. 前提：稽核政策
某事件是否出現，取決於 Windows/AD 端**是否開啟對應稽核（audit policy）**。若未開啟，該事件不會產生，Wazuh 也就收不到。這是「查無事件 ≠ 沒發生」的重要原因，AI 判讀時要考慮。

> 稽核政策設定、採集的通道、decoder 版本皆為部署相關（需依實際環境確認）。特定 Event ID 語意見 04-windows-ad-events，並依 Microsoft 官方確認。

## 4. AI 如何使用
用 `providerName`/`location` 判斷事件來源類別；用 `eventID` 連到事件頁（[[evt-windows-security-overview]]，⏳批 3）；遇到「應該有卻沒有」的事件，提示可能是稽核未開或未採集。

## 5. 需依實際環境確認
啟用的稽核政策、採集通道、decoder。

## 6. 目前規則包所需通道

`code/2026-07-20/wazuh-windows-threat-detection-rules/` 需要：

- `Microsoft-Windows-Sysmon/Operational`：Event ID 1、3、11；
- `Microsoft-Windows-PowerShell/Operational`：Event ID 4104；
- `Security`：4720、4728、4732、4697、4698、1102；
- `System`：7045、104。

Sysmon Event ID 3 預設不啟用；Security／PowerShell 事件也取決於 audit policy／GPO。通道重複配置會造成 duplicate events，合併 shared `agent.conf` 前必須先檢查 endpoint 本機 `ossec.conf`。

## 相關文件
[[doc-wazuh-agent]]、[[doc-wazuh-manager]]、[[evt-windows-security-overview]]；跨連父層 [[windows-event-log-and-sysmon]]。

## 建議查證來源
Wazuh 官方文件、Microsoft Windows Security Auditing 文件。

## 可被檢索的關鍵字（中英）
Windows 事件進入 Wazuh、eventchannel、稽核政策、audit policy、data.win、providerName、decoder。
