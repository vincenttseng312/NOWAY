---
id: evt-account-anomaly-detection
title: "帳號異常行為判斷方式"
doc_type: event
category: windows-ad-event
summary: "本頁是方法論，非單一事件：說明如何綜合登入成功/失敗、鎖定、群組異動、時間與來源，判斷帳號是否異常。核心原則是「單一事件弱，關聯與基準偏離才是訊號」。"
tags: [cat:event, type:event, source:windows-security, mitre-technique:t1078]
event_source: security
windows_event_ids: ["4624", "4625", "4740", "4732"]
wazuh_sources: []
related_entities: [ent-account, ent-ip]
related_docs: [evt-logon-success, evt-logon-failure, evt-account-lockout, evt-admin-group-change, scn-ad-abnormal-logon]
risk_level: ""
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: ["帳號異常", "行為判斷", "基準偏離", "關聯分析", "account anomaly", "baseline", "T1078"]
last_updated: 2026-07-09
---

# 帳號異常行為判斷方式

## 1. 事件用途
提供「如何判斷帳號是否異常」的方法論，貫穿本資料夾各事件頁。呼應父層 [[malware-analysis-methodology]] 的核心原則：**不要只看單一證據，要把事件串成故事線**。

## 2. 可能代表的安全意義
帳號異常常是入侵的第一個可觀測面（憑證被盜、內部濫用），對映 MITRE **T1078 Valid Accounts**。

## 3. 判斷維度（綜合多事件，非單一 Event ID）

| 維度 | 觀察 | 相關事件 |
|---|---|---|
| 時間 | 非慣用時段登入 | 4624 |
| 來源 | 罕見/外部 IP、地理跳躍 | 4624/4625 ipAddress |
| 頻率 | 短時間大量失敗 | 4625、4740 |
| 序列 | 失敗×N 後成功 | 4625→4624（[[scn-failed-then-success-logon]]） |
| 權限 | 一般帳號突獲特權群組 | 4732/4728（[[evt-admin-group-change]]） |
| 行為 | 登入後異常程序/持久化 | 4688、持久化事件 |

## 4. 在 Wazuh Alert 中可能出現的欄位
跨事件關聯所需：`targetUserName`、`ipAddress`、`logonType`、`timestamp`、`eventID`、`rule.level`。

## 5. AI 分析時應注意的欄位
以**帳號**為主體，聚合其一段時間內的所有事件；建立「該帳號的正常基準」（慣用來源/時段/主機），再看偏離。基準需資料累積，冷啟動時信心較低要說明。

## 6. 儀表板可以如何視覺化
單一帳號行為時間線、帳號風險評分、異常維度雷達圖。

## 7. 使用者可能會問的問題
「這個帳號有沒有異常？」「哪些帳號需要優先調查？」

## 8. AI 回答範例
「<帳號> 在 <時間窗> 內：來自外部 <IP>（罕見）、<N> 次失敗後成功、隨即被加入 Administrators。三個維度同時偏離基準，綜合判定為高度異常，建議優先調查。單看任一項則不足以定論。」（值為佔位。）

## 9. 誤判情境
出差/在家登入（來源改變）、角色調整（權限變更）、新進人員無基準可比。這些都需結合情境確認，避免誤報。

## 10. 處置建議
高度異常則凍結帳號、重設憑證、檢查該帳號所有活動；並回饋調整偵測門檻以降誤報。

## 相關文件
[[evt-logon-success]]、[[evt-logon-failure]]、[[evt-account-lockout]]、[[evt-admin-group-change]]、[[scn-ad-abnormal-logon]]；跨連父層 [[malware-analysis-methodology]]。

## 建議查證來源
Microsoft Windows Security Auditing 文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
帳號異常、行為判斷、基準偏離、關聯分析、account anomaly、baseline、T1078。
