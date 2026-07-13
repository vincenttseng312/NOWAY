---
id: doc-severity-classification
title: "事件嚴重性分級"
doc_type: severity
category: severity
summary: "本專題風險分為 info/low/medium/high/critical 五級。以 Wazuh rule.level 為基礎分，再依「是否成功、是否關聯成鏈、資產/帳號敏感度、是否削弱防禦、來源」等因子升降。所有具體門檻為 env-specific。"
tags: [cat:severity, type:severity, status:env-specific]
related_entities: [ent-alert, ent-incident]
related_docs: [doc-wazuh-rules-and-levels, doc-correlation-rules, doc-ai-analysis-pipeline]
mitre_attack: []
wazuh_sources: []
windows_event_ids: []
risk_level: ""
confidence: medium
verification_status: env-specific
source_refs: ["Wazuh 官方文件"]
keywords: ["嚴重性分級", "風險等級", "severity", "risk level", "critical", "分級判準"]
last_updated: 2026-07-09
---

# 事件嚴重性分級

## 1. 五級定義

| 等級 | 意義 | 典型 |
|---|---|---|
| info | 資訊，無明顯威脅 | 正常登入、例行事件 |
| low | 低風險，觀察即可 | 零星失敗、單純掃描 |
| medium | 需關注，可能為攻擊前期 | 大量失敗、可疑但未成功 |
| high | 高風險，需調查 | 可疑成功登入、提權跡象、防禦被削弱 |
| critical | 極高，需立即處置 | 暴力破解成功、建帳號+提權鏈、確認 C2 |

## 2. 分級方法：基礎分 + 升降因子

**基礎分**：以 `rule.level`（一般 0–15，見 [[doc-wazuh-rules-and-levels]]）映射到初始等級——**映射門檻為 env-specific，不記死**。

**升級因子**（命中則往上調）：
- 攻擊由「嘗試」變「成功」（如失敗→成功登入）。
- 命中關聯型樣（[[doc-correlation-rules]] 的 C1–C5）。
- 涉及特權帳號 / 關鍵資產（如 DC）。
- 伴隨削弱防禦（清日誌、關防護）。
- 來源為外部/攻擊網段。

**降級因子**：
- 有合理業務解釋、命中已知誤判型樣（見各情境「誤判可能性」段）。
- 屬授權活動（維運/測試，有變更紀錄）。

## 3. AI 使用原則
- 分級要**可解釋**：說明「基礎分 + 哪些因子」得到結論，而非只給一個等級。
- 單一告警的 `rule.level` 只是起點；關聯後常需升級（呼應「單一證據弱」原則）。
- 門檻與資產清單為 env-specific，AI 應標「依實際環境設定」。

## 4. 需依實際環境確認
`rule.level`→等級的映射門檻、關鍵資產/特權帳號清單、各升降因子的權重。

## 相關文件
[[doc-wazuh-rules-and-levels]]、[[doc-correlation-rules]]、[[doc-ai-analysis-pipeline]]；跨連父層 [[ioc-ttp-and-detection-engineering]]。

## 建議查證來源
Wazuh 官方文件。

## 可被檢索的關鍵字（中英）
嚴重性分級、風險等級、severity、risk level、critical、分級判準。
