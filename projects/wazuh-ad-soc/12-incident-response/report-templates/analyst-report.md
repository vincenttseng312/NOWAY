---
id: rpt-analyst-report
title: "技術人員分析報告"
doc_type: report
category: report
summary: "給資安人員的技術報告：含 Event ID、Wazuh 欄位證據、程序/登入鏈、MITRE 技術 id、IOC、偵測機會與處置。是完整事件報告的技術主體。對應 audience-adapt(analyst)。"
audience: analyst
required_inputs: ["data.win.system.eventID", "rule.mitre.id", "agent.name", "timestamp"]
optional_inputs: ["rule.id", "data.win.eventdata.targetUserName", "data.win.eventdata.ipAddress", "full_log"]
related_docs: [qa-explain-for-analyst, qa-full-report, doc-ioc-ttp-detection]
tags: [cat:report, type:report]
confidence: medium
verification_status: needs-verification
source_refs: ["MITRE ATT&CK 官方網站", "Microsoft Windows Security Auditing 文件"]
keywords: ["技術分析報告", "analyst report", "IOC", "偵測機會"]
last_updated: 2026-07-09
---

# 技術人員分析報告

## 1. 報告目的
提供資安人員可據以行動的技術分析。

## 2. 適用情境
事件調查、SOC 分析、偵測改進。對應問答 [[qa-explain-for-analyst]]。

## 3. 必要輸入欄位
`eventID`、`rule.mitre.id`、`agent.name`、`timestamp`。

## 4. 可選輸入欄位
`rule.id`（標 env-specific）、`targetUserName`、`ipAddress`、`full_log`。

## 5. 報告產出格式
```markdown
### 技術分析報告
- 事件鏈：<Event ID 序列 + 程序/登入鏈>
- 欄位證據：<關鍵 data.win.* 值>
- MITRE：<T-id 清單（戰術→技術）>
- IOC：<來源 IP / 帳號 / 檔案 hash（若有）>
- 偵測機會：<對應的關聯規則 / 建議規則>
- 誤判評估：<可能的良性解釋>
- 處置：<技術步驟>
- 待確認：<env-specific / 需官方查證項>
```

## 6. 嚴重性判斷方式
依 [[doc-severity-classification]]，並說明「基礎分 + 因子」的推導。

## 7. MITRE ATT&CK 對應方式
完整列 technique id 與戰術鏈；無對應處標「需查官方確認」。

## 8. 建議處置格式
技術步驟（隔離/封鎖/重設/移除持久化）+ 偵測改進建議。

## 9. 範例輸入
完整告警集 + full_log（佔位）。

## 10. 範例輸出
```markdown
### 技術分析報告
- 事件鏈：4625×N(Type10,src<ip>)→4624→4720→4732
- 欄位證據：targetUserName=<u>, ipAddress=<ip>
- MITRE：T1110→T1078→T1136→T1098
- IOC：src IP <ip>、新建帳號 <u>
- 偵測機會：C1 暴力破解成功 + C2 持久化提權關聯規則
- 誤判評估：來源為外部、節奏規律，誤判低
- 處置：隔離、重設憑證、移除帳號、封鎖 IP
- 待確認：rule.id（env-specific）、Kerberos 事件是否採集
```
（值為佔位。）

## 相關文件
[[qa-explain-for-analyst]]、[[qa-full-report]]；跨連父層 [[ioc-ttp-and-detection-engineering]]。
