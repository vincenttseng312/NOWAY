---
id: evt-account-lockout
title: "帳號鎖定事件"
doc_type: event
category: windows-ad-event
summary: "Event 4740 記錄帳號因連續失敗達門檻而被鎖定。它常是暴力破解/密碼噴灑的副作用，也可能是舊憑證反覆重試造成的誤鎖。4767 為解鎖。"
tags: [cat:event, type:event, source:windows-security, mitre-technique:t1110]
event_source: security
windows_event_ids: ["4740", "4767"]
wazuh_sources: []
related_entities: [ent-account]
related_docs: [evt-logon-failure, scn-mass-logon-failure, scn-rdp-bruteforce]
risk_level: medium
confidence: high
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件"]
keywords: ["帳號鎖定", "4740", "account lockout", "brute force 副作用", "4767", "unlock"]
last_updated: 2026-07-09
---

# 帳號鎖定事件

## 1. 事件用途
記錄帳號因連續登入失敗達到鎖定門檻而被鎖定。核心 Event ID **4740**（4767 為解鎖；以 Microsoft 官方為準）。鎖定門檻由帳號原則決定（env-specific）。

## 2. 可能代表的安全意義
- 常是暴力破解/密碼噴灑（[[evt-logon-failure]]、T1110）的**可觀測副作用**。
- 也可能是良性誤鎖（見第 9 段）。
- 大量帳號同時被鎖，可能是噴灑攻擊或憑證外洩後的大規模嘗試。

## 3. 可能涉及的 Windows Event ID
| Event ID | 意義 | 驗證 |
|---|---|---|
| 4740 | 帳號被鎖定 | 以 Microsoft 官方為準 |
| 4767 | 帳號被解鎖 | 以 Microsoft 官方為準 |

## 4. 在 Wazuh Alert 中可能出現的欄位
`eventID=4740`、`data.win.eventdata.targetUserName`（被鎖帳號）、來源主機/呼叫者資訊（若擷取）。

## 5. AI 分析時應注意的欄位
被鎖帳號、鎖定發生前的 4625 失敗來源與次數、同時段被鎖帳號數量。鎖定門檻為 env-specific，勿假設固定值。

## 6. 儀表板可以如何視覺化
帳號鎖定次數趨勢、Top 被鎖帳號、鎖定與失敗關聯卡。

## 7. 使用者可能會問的問題
「哪些帳號被鎖定？」「這次鎖定是攻擊還是誤鎖？」

## 8. AI 回答範例
「<帳號> 於 <時間> 被鎖定（4740）。前置 <N> 次 4625 來自 <IP>，較可能為暴力破解副作用；若來源為使用者慣用裝置則可能是誤鎖。需確認來源。」（值為佔位。）

## 9. 誤判情境
舊密碼快取於手機/服務/對映磁碟反覆重試、密碼變更後未更新的自動化、多裝置同步。

## 10. 處置建議
確認鎖定來源；攻擊則封鎖來源、重設憑證；誤鎖則清除舊憑證來源再解鎖。

## 相關文件
[[evt-logon-failure]]、[[scn-mass-logon-failure]]、[[scn-rdp-bruteforce]]

## 建議查證來源
Microsoft Windows Security Auditing 文件。

## 可被檢索的關鍵字（中英）
帳號鎖定、4740、account lockout、解鎖、4767、brute force。
