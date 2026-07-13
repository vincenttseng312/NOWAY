---
id: dsh-rdp-attack-monitor
title: "RDP 攻擊監控圖"
doc_type: dashboard
category: dashboard
summary: "專門監控 RDP 相關活動：LogonType 10 的失敗/成功、來源 IP（尤其外部）、失敗→成功關聯。對應 RDP 暴力破解情境的即時視覺。"
tags: [cat:dashboard, type:dashboard, mitre-technique:t1021-001]
data_fields: ["data.win.eventdata.logonType", "data.win.system.eventID", "data.win.eventdata.ipAddress", "timestamp"]
ai_inputs: ["risk_level"]
viz_type: "composite"
filters: ["時間範圍", "網段(內/外)", "結果(成功/失敗)"]
related_docs: [evt-rdp-logon, scn-rdp-bruteforce, dsh-logon-failure-trend]
confidence: medium
verification_status: needs-verification
source_refs: ["Microsoft Windows Security Auditing 文件"]
keywords: ["RDP 監控", "rdp attack monitor", "LogonType 10", "T1021.001"]
last_updated: 2026-07-09
---

# RDP 攻擊監控圖

## 1. 元件目的
即時監控 RDP 攻擊面（本專題外部攻擊的重點通道）。

## 2. 使用情境
「RDP 有被暴力破解嗎」「有沒有外部 RDP 登入」。

## 3. 需要的資料欄位
LogonType 10 的成功/失敗、來源 IP、時間。

## 4. 對應 Wazuh 欄位
`logonType=10`、`eventID`（4624/4625）、`ipAddress`、`timestamp`（見 [[evt-rdp-logon]]）。

## 5. 對應 AI 分析輸出
`risk_level`、失敗→成功關聯標記。

## 6. 視覺化建議
複合圖：失敗趨勢 + 成功事件標點 + 來源 IP 排行；外部來源醒目。

## 7. 使用者可互動功能
點來源→過濾其 RDP 活動；標記封鎖。

## 8. 篩選條件
時間範圍、網段、結果。

## 9. 排序方式
時間序 / 來源計數。

## 10. 範例資料格式
```json
[{"time":"<ts>","ip":"<ip>","zone":"external","result":"fail","logon_type":10}]
```
（值為佔位。）

## 11. 注意事項
LogonType 10 與 RDP 對應以 Microsoft 官方為準；TerminalServices 通道事件需確認（見 [[evt-rdp-logon]]）；授權遠端維運會產生正常 RDP。

## 相關文件
[[evt-rdp-logon]]、[[scn-rdp-bruteforce]]、[[dsh-logon-failure-trend]]
