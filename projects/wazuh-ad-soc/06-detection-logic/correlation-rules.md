---
id: doc-correlation-rules
title: "關聯偵測規則"
doc_type: detection
category: detection
summary: "彙整本專題的跨事件關聯型樣：失敗後成功、建帳號後加管理員、Office 生腳本後連線等。每個型樣描述觸發條件、涉及事件與可調參數；具體門檻（時間窗/次數）為 env-specific。"
tags: [cat:detection, type:detection, status:env-specific]
related_entities: [ent-alert, ent-incident]
related_docs: [doc-detection-logic-overview, scn-failed-then-success-logon, scn-add-to-administrators, scn-suspicious-powershell]
mitre_attack: []
wazuh_sources: []
windows_event_ids: []
risk_level: ""
confidence: medium
verification_status: env-specific
source_refs: ["Wazuh 官方文件", "MITRE ATT&CK 官方網站"]
keywords: ["關聯規則", "correlation", "行為型樣", "時間窗", "attack chain", "detection"]
last_updated: 2026-07-09
---

# 關聯偵測規則

跨事件的行為型樣。每條列出「觸發條件 / 涉及事件 / 可調參數 / 對應情境」。**時間窗與次數門檻皆為 env-specific**，此處給邏輯不給死值。

## C1 暴力破解成功
- 觸發：同帳號或同來源，時間窗內 4625×N 後出現 4624。
- 涉及：[[evt-logon-failure]] → [[evt-logon-success]]。
- 參數：時間窗、失敗次數 N（env-specific）。
- 情境：[[scn-failed-then-success-logon]]、[[scn-rdp-bruteforce]]。

## C2 持久化+提權鏈
- 觸發：時間窗內 4720（建帳號）→ 4732/4728（加特權群組）→（選）4624（新帳號登入）。
- 涉及：[[evt-user-creation]] → [[evt-admin-group-change]]。
- 情境：[[scn-local-user-creation]]、[[scn-add-to-administrators]]。

## C3 Office → 腳本 → 外連
- 觸發：Office 程序生出腳本宿主（powershell/cmd/wscript）→ 隨後對外連線或寫檔。
- 涉及：[[evt-powershell-suspicious]] + 網路/檔案事件。
- 情境：[[scn-suspicious-powershell]]、[[scn-malicious-file-execution]]、[[scn-suspicious-external-connection]]。

## C4 削弱防禦後的活動
- 觸發：1102/4719/防護停用 後，同主機出現可疑登入/程序。
- 涉及：[[evt-security-config-change]] + 後續事件。
- 情境：[[scn-security-tool-disable]]、[[scn-firewall-modification]]。

## C5 帳號基準偏離
- 觸發：帳號自罕見來源/時段登入，或短時間跨多主機。
- 涉及：[[evt-account-anomaly-detection]]。
- 情境：[[scn-ad-abnormal-logon]]、[[scn-lateral-movement-signs]]。

## 實作歸屬與注意
- 關聯可由 Wazuh 關聯規則或後端 AI 完成（依環境，需確認）。
- 門檻設太緊會漏、太鬆會吵；需以實際資料調校並記錄（呼應父層 [[ioc-ttp-and-detection-engineering]]）。
- AI 使用這些型樣時，仍要用實際欄位驗證「同一性」（同帳號/同來源/時間合理），不可只憑型樣名下結論。

## 相關文件
[[doc-detection-logic-overview]]、以及上列各情境與事件頁。

## 建議查證來源
Wazuh 官方文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
關聯規則、correlation、行為型樣、時間窗、attack chain、detection。
