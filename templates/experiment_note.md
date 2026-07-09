---
id: exp-<slug>
type: experiment
topic: ""
status: planned        # planned | running | completed | inconclusive
hypothesis: ""
result: pending        # supported | refuted | partial | pending
confidence: medium     # low | medium | high
code_paths: []
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
related: []
---

# 實驗：<名稱>

## 1. 假設 Hypothesis

### H1（主要）
我目前推測：…

理由：
- …

信心程度：Low / Medium / High
要驗證的點：…

### H2（替代）
另一種可能：…
如何區分 H1 / H2：…

## 2. 實作 Implementation

### 實驗目標
這個實驗要驗證：…

### 最小實驗設計
- 輸入：…
- 操作：…
- 預期輸出：…
- 成功條件：…
- 失敗條件：…

### 程式碼
路徑：`code/YYYY-MM-DD/<topic>/`（見 [[...]] 或 db/code_index.jsonl）

## 3. 驗證 Verification

| 編號 | 要驗證的事 | 方法 | 預期 | 實際 | 判定 |
|---|---|---|---|---|---|
| V1 | | | | ⏳待執行 | ⏳ |

> 環境備註：本 wiki 目前無 Python。凡是需要執行才有結果的驗證，「實際」欄在我無法於本機執行時一律標「⏳待執行」，**絕不填造假結果**。可用現成工具（git、bash、PowerShell）驗證的項目，才會填真實 actual。

判斷標準：
- 看到 A → 假設可能成立
- 看到 B → 假設需修正
- 看到 C → 實作可能有錯

## 4. 反思 Reflection

- 原本我以為：…
- 結果顯示：…
- 被支持的假設：…
- 被推翻／需修正的假設：…
- 心智模型更新為：…
- 下次遇到類似問題，先檢查：1… 2… 3…

## 5. 後續問題 Next Questions
1. …
2. …
