---
id: evt-logon-failure
title: "登入失敗事件"
doc_type: event
category: windows-ad-event
summary: "Event 4625 記錄登入失敗，其 Status/SubStatus 失敗原因碼可區分「密碼錯誤」與「帳號不存在」，是暴力破解/密碼噴灑偵測的核心。大量 4625 是關鍵訊號。SubStatus 具體代碼需以 Microsoft 官方確認。"
tags: [cat:event, type:event, source:windows-security, mitre-technique:t1110]
event_source: security
windows_event_ids: ["4625"]
wazuh_sources: []
related_entities: [ent-account, ent-ip]
related_docs: [evt-logon-success, scn-rdp-bruteforce, scn-mass-logon-failure, evt-account-lockout]
risk_level: medium
confidence: high
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件"]
keywords: ["登入失敗", "4625", "暴力破解", "密碼噴灑", "SubStatus", "failed logon", "brute force", "T1110"]
last_updated: 2026-07-09
---

# 登入失敗事件

## 1. 事件用途
記錄一次登入失敗。核心 Event ID **4625**（以 Microsoft 官方為準）。

## 2. 可能代表的安全意義
- 少量失敗常為打錯密碼。
- **大量失敗**是暴力破解（同帳號多密碼）或密碼噴灑（多帳號同密碼）的核心訊號，對映 MITRE **T1110 Brute Force**。
- 關鍵延伸：失敗後緊接成功（[[scn-failed-then-success-logon]]）。

## 3. 可能涉及的 Windows Event ID
| Event ID | 意義 | 驗證 |
|---|---|---|
| 4625 | 登入失敗 | 以 Microsoft 官方為準 |

**失敗原因碼（Status / SubStatus）**可區分失敗類型（如「密碼錯誤」vs「帳號不存在」vs「帳號被停用/鎖定」）——**具體代碼（如 0xC000006A、0xC0000064 等）需依 Microsoft 官方文件確認**，本頁不記死。此區分對「密碼噴灑 vs 帳號列舉」判讀很有價值。

## 4. 在 Wazuh Alert 中可能出現的欄位
`eventID=4625`、`data.win.eventdata.targetUserName`、`data.win.eventdata.ipAddress`、`data.win.eventdata.logonType`、失敗原因相關欄位（若 decoder 擷取）。

## 5. AI 分析時應注意的欄位
單位時間內同來源 IP / 同帳號的失敗次數；失敗原因碼分布（同帳號多密碼 = 暴力；多帳號 = 噴灑）；logonType（10 = RDP 暴力，見 [[scn-rdp-bruteforce]]）。

## 6. 儀表板可以如何視覺化
登入失敗趨勢圖、Top 失敗來源 IP、Top 被嘗試帳號、失敗→成功關聯卡。

## 7. 使用者可能會問的問題
「有沒有暴力破解跡象？」「哪個 IP 失敗最多？」

## 8. AI 回答範例
「來源 <IP> 在 <時間窗> 內對 <帳號> 產生 <N> 次 4625，logonType 10，型樣符合 RDP 暴力破解（T1110）。是否已有對應成功登入需一併檢查。」（值為佔位。）

## 9. 誤判情境
使用者忘記密碼、舊憑證快取的服務/排程重試、應用程式綁定過期密碼反覆重試。

## 10. 處置建議
高頻失敗來源可考慮封鎖/限速（依環境）；檢查是否伴隨成功；必要時鎖定帳號、重設密碼。

## 相關文件
[[evt-logon-success]]、[[scn-rdp-bruteforce]]、[[scn-mass-logon-failure]]、[[evt-account-lockout]]

## 建議查證來源
Microsoft Windows Security Auditing 文件。

## 可被檢索的關鍵字（中英）
登入失敗、4625、暴力破解、密碼噴灑、SubStatus、failed logon、brute force、T1110。
