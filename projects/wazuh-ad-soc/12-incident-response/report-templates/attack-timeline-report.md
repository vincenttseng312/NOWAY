---
id: rpt-attack-timeline
title: "攻擊時間軸報告"
doc_type: report
category: report
summary: "以時間序呈現一起事件的攻擊展開，每列標時間、動作、戰術階段與證據事件，供理解攻擊全貌與撰寫事件報告的 Timeline 章節。"
audience: analyst
required_inputs: ["timestamp", "data.win.system.eventID", "agent.name", "rule.mitre.tactic"]
optional_inputs: ["data.win.eventdata.targetUserName", "data.win.eventdata.ipAddress"]
related_docs: [qa-attack-timeline, dsh-attack-timeline, doc-correlation-rules]
tags: [cat:report, type:report]
confidence: medium
verification_status: needs-verification
source_refs: ["MITRE ATT&CK 官方網站"]
keywords: ["攻擊時間軸報告", "attack timeline report", "kill chain"]
last_updated: 2026-07-09
---

# 攻擊時間軸報告

## 1. 報告目的
把事件依時間排列成可讀的攻擊展開敘事。

## 2. 適用情境
事件報告的 Timeline 章節、Demo 說明、覆盤。對應問答 [[qa-attack-timeline]]。

## 3. 必要輸入欄位
`timestamp`、`eventID`、`agent.name`、`rule.mitre.tactic`（各步）。

## 4. 可選輸入欄位
`targetUserName`、`ipAddress`。

## 5. 報告產出格式
```markdown
### 攻擊時間軸
| 時間 | 主機 | 動作/事件 | 戰術階段 | 證據 |
|---|---|---|---|---|
| <ts> | <host> | <動作> | <tactic> | <eventID/rule> |
```

## 6. 嚴重性判斷方式
以整條鏈的最終狀態分級（成功/提權 → 升級），見 [[doc-severity-classification]]。

## 7. MITRE ATT&CK 對應方式
每列標戰術；整體標出攻擊經過哪些戰術階段。

## 8. 建議處置格式
時間軸末列出「當前需採取的處置」。

## 9. 範例輸入
依 timestamp 排序的事件陣列（佔位）。

## 10. 範例輸出
```markdown
### 攻擊時間軸
| 時間 | 主機 | 動作/事件 | 戰術階段 | 證據 |
|---|---|---|---|---|
| T+00 | <host> | 大量 RDP 登入失敗 | Credential Access | 4625×N |
| T+05 | <host> | 登入成功 | Valid Accounts | 4624 |
| T+08 | <host> | 建立帳號 | Persistence | 4720 |
| T+09 | <host> | 加入 Administrators | Priv-Esc | 4732 |
```
（值為佔位；同一性須以實體欄位驗證。）

## 相關文件
[[qa-attack-timeline]]、[[dsh-attack-timeline]]、[[doc-correlation-rules]]
