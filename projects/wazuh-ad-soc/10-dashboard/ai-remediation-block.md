---
id: dsh-ai-remediation-block
title: "AI 建議處置區塊"
doc_type: dashboard
category: dashboard
summary: "在事件詳細頁嵌入的 AI 處置建議：依事件類型給出隔離、封鎖、重設憑證、移除持久化等步驟，取自對應情境頁的處置段與 SOP。"
tags: [cat:dashboard, type:dashboard, cat:ai]
data_fields: []
ai_inputs: ["remediation", "risk_level"]
viz_type: "block"
filters: []
related_docs: [doc-ir-sop, dsh-ai-summary-block, doc-ai-analysis-pipeline]
confidence: medium
verification_status: needs-verification
source_refs: []
keywords: ["AI 處置建議", "ai remediation", "處置步驟", "回應建議"]
last_updated: 2026-07-09
---

# AI 建議處置區塊

## 1. 元件目的
給出可執行的處置建議，縮短從偵測到回應的時間。

## 2. 使用情境
「請給我處置建議」；事件詳細頁的行動指引。

## 3. 需要的資料欄位
（消費 AI 輸出 + 對應情境頁處置段）

## 4. 對應 Wazuh 欄位
間接：處置建議依事件類型（由告警欄位判定）而定。

## 5. 對應 AI 分析輸出
`remediation`（步驟清單）、`risk_level`（決定急迫性）。

## 6. 視覺化建議
勾選式步驟清單 + 急迫性標示；每步連到來源（情境頁處置段 / [[doc-ir-sop]]）。

## 7. 使用者可互動功能
勾選完成、指派負責人、展開為完整回應報告。

## 8. 篩選條件
（單一區塊，不適用）

## 9. 排序方式
依急迫性/執行順序。

## 10. 範例資料格式
```json
{"risk":"critical","steps":["隔離主機","重設<帳號>憑證","移除持久化","封鎖<IP>","擴大調查"],"source":["scn-failed-then-success-logon","doc-ir-sop"]}
```
（值為佔位。）

## 11. 注意事項
處置建議取自 KB 情境頁與 SOP，屬一般性指引；實際執行須依組織政策與授權（env-specific）。不含攻擊性操作。

## 相關文件
[[doc-ir-sop]]、[[dsh-ai-summary-block]]、[[doc-ai-analysis-pipeline]]
