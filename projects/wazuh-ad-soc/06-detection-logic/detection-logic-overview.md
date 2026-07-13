---
id: doc-detection-logic-overview
title: "偵測邏輯總覽"
doc_type: detection
category: detection
summary: "本專題偵測分兩層：單點規則（Wazuh 依單一事件觸發告警）與關聯偵測（跨事件/時間的行為型樣，多由後端 AI 或關聯規則完成）。好的偵測強調行為鏈與基準偏離，而非單一指標。"
tags: [cat:detection, type:detection]
related_entities: [ent-alert, ent-rule]
related_docs: [doc-correlation-rules, doc-wazuh-rules-and-levels, doc-ioc-ttp-detection]
mitre_attack: []
wazuh_sources: []
windows_event_ids: []
risk_level: ""
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "MITRE ATT&CK 官方網站"]
keywords: ["偵測邏輯", "detection logic", "單點規則", "關聯偵測", "行為鏈", "detection engineering"]
last_updated: 2026-07-09
---

# 偵測邏輯總覽

## 1. 兩層偵測
- **單點規則（Wazuh）**：單一事件符合規則即告警（如某 Event ID + 條件），賦予 `rule.level`。強項是即時、明確；弱點是單點易誤報、看不到脈絡。
- **關聯偵測（AI／關聯規則）**：跨多事件、跨時間、跨實體的行為型樣（如「失敗×N→成功」「建帳號→加管理員」）。強項是貼近真實 TTP、誤報低；由後端 AI 或 Wazuh 關聯規則完成（依環境）。詳見 [[doc-correlation-rules]]。

## 2. 偵測分級的品質原則
（呼應父層 [[ioc-ttp-and-detection-engineering]] 的 Detection Engineering 思維）

```
低品質：單一指標即告警（如 process_name = powershell.exe）
較佳：  父程序 + 命令列 + 條件的組合
更佳：  行為鏈 + 時間窗（Office→PowerShell→網路→寫檔→持久化 within N 分鐘）
```

## 3. 本專題偵測地圖
每個 05-attack-scenarios 情境頁的第 3–6 段（可觀測跡象／Windows 事件／Wazuh 欄位／MITRE）就是該情境的偵測邏輯；本資料夾提供「跨情境的關聯」與「品質原則」的統整。

## 4. 與 AI 的關係
單點告警是 AI 的輸入；AI 負責做關聯、去誤報、串成事件敘事（見 [[doc-ai-role]]、[[doc-alert-to-report-pipeline]]）。

## 5. 需依實際環境確認
Wazuh 規則集、關聯是由 Wazuh 規則還是後端 AI 完成、各門檻參數。

## 相關文件
[[doc-correlation-rules]]、[[doc-wazuh-rules-and-levels]]；跨連父層 [[ioc-ttp-and-detection-engineering]]。

## 建議查證來源
Wazuh 官方文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
偵測邏輯、detection logic、單點規則、關聯偵測、行為鏈、detection engineering。
