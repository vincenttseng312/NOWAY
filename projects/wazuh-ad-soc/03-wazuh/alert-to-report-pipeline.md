---
id: doc-alert-to-report-pipeline
title: "Wazuh Alert 到事件報告的轉換流程"
doc_type: wazuh
category: wazuh
summary: "定義一或多筆 Wazuh alert 如何被 AI 轉成事件報告：欄位解析→實體對映→關聯聚合成 Incident→風險分級→MITRE 對應→套報告模板。是 report-gen 類問答與 12-report 模板的依據。"
tags: [cat:wazuh, type:wazuh, cat:report]
related_entities: [ent-alert, ent-incident]
related_docs: [doc-wazuh-field-to-ai-mapping, doc-data-and-event-flow, doc-severity-classification, doc-ai-role]
keywords: ["alert 到報告", "事件報告流程", "incident", "報告生成", "pipeline", "alert to report"]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "MITRE ATT&CK 官方網站"]
last_updated: 2026-07-09
---

# Wazuh Alert 到事件報告的轉換流程

## 1. 流程

```
① 取得 alert(s)      單筆或一段時間/一主機的多筆
      ▼
② 欄位解析          依 [[doc-wazuh-field-to-ai-mapping]] 取核心欄位
      ▼
③ 實體對映          agent.name→Host, targetUserName→Account, ipAddress→IP, rule.mitre.id→Technique
      ▼
④ 關聯聚合          同主機/帳號/IP/時間窗的 alert 聚成 Incident；套用關聯規則（如失敗×N 後成功）
      ▼
⑤ 風險分級          依 [[doc-severity-classification]]（結合 rule.level 與關聯）
      ▼
⑥ MITRE 對應        彙整 rule.mitre.* → 戰術/技術清單
      ▼
⑦ 套報告模板        依對象選 manager/analyst 版（12-report）
```

## 2. 每步的注意
- ②③ 不臆造缺失欄位；缺就標「未提供」。
- ④ Incident 的時間軸用 `timestamp` 排序。
- ⑤ 分級門檻 env-specific。
- ⑦ 報告中的 `rule.id`、統計數字只反映實際 alert，不虛構。

## 3. AI 如何使用
這是 report-gen 類問答（「請產出事件報告」）的骨幹；answer 由 12-incident-response/report-templates 的模板承接。

## 4. 需依實際環境確認
關聯規則的具體參數（時間窗、次數門檻）、分級門檻。

## 相關文件
[[doc-wazuh-field-to-ai-mapping]]、[[doc-data-and-event-flow]]、[[doc-severity-classification]]、[[doc-ai-role]]、12-incident-response/report-templates/*（⏳批 6）

## 建議查證來源
Wazuh 官方文件、MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
alert 到報告、事件報告流程、incident 聚合、報告生成、pipeline、alert to report。
