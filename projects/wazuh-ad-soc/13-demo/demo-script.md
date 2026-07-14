---
id: doc-demo-script
title: "Demo 劇本"
doc_type: demo
category: demo
summary: "專題 Demo 的完整劇本：以一條 RDP 暴力破解→成功→提權的攻擊鏈為主線，逐步展示 Wazuh 偵測、AI 分析、儀表板呈現與問答，最後產出報告。所有攻擊步驟僅為授權實驗，本劇本只描述展示流程不含武器化指令。"
tags: [cat:demo, type:demo]
related_entities: [ent-incident]
related_docs: [dsh-demo-dashboard, rpt-demo-report, qa-demo-summary]
mitre_attack: [t1110, t1078, t1136, t1098]
wazuh_sources: []
windows_event_ids: []
risk_level: ""
confidence: medium
verification_status: needs-verification
source_refs: ["MITRE ATT&CK 官方網站"]
keywords: ["Demo 劇本", "demo script", "展示流程", "專題演示"]
last_updated: 2026-07-09
---

# Demo 劇本

專題 Demo 的展示流程。主線攻擊鏈：**RDP 暴力破解 → 成功登入 → 建立帳號 → 提權**（授權實驗室環境）。本劇本只描述「展示什麼、系統如何反應」，**不含攻擊操作指令**。

## 演示前準備
- 還原到乾淨快照、確認 Wazuh 採集與稽核政策正常。
- 開好儀表板（[[dsh-demo-dashboard]]）與問答介面。
- 確認攻擊網段與靶機依 [[doc-network-topology]] 隔離。

## 演示流程（每步：攻擊面 → 系統反應）

| 步驟 | 攻擊面（授權模擬） | Wazuh 偵測 | AI／儀表板反應 | 對應技術 |
|---|---|---|---|---|
| 1 | 外部對靶機 RDP 反覆嘗試 | 大量 4625（Type 10） | 登入失敗趨勢飆升、Top 來源 IP 出現攻擊機 | T1110 |
| 2 | 猜中並登入 | 4624 成功 | AI 標記「失敗後成功」高風險、風險升 critical | T1078 |
| 3 | 建立後門帳號 | 4720 | AD 帳號異動監控告警 | T1136 |
| 4 | 加入 Administrators | 4732 | 特權群組異動告警、攻擊鏈連線標記 | T1098 |
| 5 | 提問與報告 | — | 問答「整理攻擊時間軸/給處置建議」、產出 Demo 報告 | — |

## 演示話術重點
- **偵測**：Wazuh 即時把 Windows 事件變成有 MITRE 對應的告警。
- **分析**：AI 把散落告警串成一條可解釋的攻擊鏈，並即時分級。
- **呈現**：儀表板一頁看懂；問答用自然語言即問即答。
- **處置**：AI 依 SOP（[[doc-ir-sop]]）給出處置建議，展示偵測→分析→處置閉環。

## 收尾
用 [[qa-demo-summary]] 產出摘要、[[rpt-demo-report]] 產出成果報告。

## 誠實邊界
- Demo 用實驗室實際產生的告警，**報告數據不臆造**（用真實 Demo 結果或明確佔位）。
- 具體 rule.id/門檻依實際環境；展示時如提及以「本環境為準」帶過。
- 演示不誇大偵測涵蓋（未觸發的階段就不宣稱偵測到）。

## 需依實際環境確認
Demo 時間安排、實際觸發的 rule.id 與告警、儀表板前端。

## 相關文件
[[dsh-demo-dashboard]]、[[rpt-demo-report]]、[[qa-demo-summary]]、[[doc-ir-sop]]

## 建議查證來源
MITRE ATT&CK 官方網站。

## 可被檢索的關鍵字（中英）
Demo 劇本、demo script、展示流程、攻擊鏈演示、專題演示。
