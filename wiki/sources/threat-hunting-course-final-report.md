---
type: source
title: "Threat Hunting Essential: Attack Recognition Techniques Part 2"
authors: ["劉昱甫"]
url: ""
raw: "raw/附件6-2、校內威脅獵捕課程期末報告.pdf"
ingested: 2026-07-20
tags: [wazuh, opnsense, suricata, ai-security, machine-learning]
entities: []
concepts: [detection-validation-range, soc-lab-segmentation-and-telemetry, ioc-ttp-and-detection-engineering]
created: 2026-07-20
updated: 2026-07-20
---

# Threat Hunting Essential Part 2 期末報告摘要

這份 19 頁報告延續期中的 Wazuh、OPNsense／Suricata 與本地 AI 架構，新增 OPNsense Wazuh Agent、Suricata Alert／Drop 控制、MCP prompt 調整、模型比較，以及 ET-BERT 流量分類實驗。

## OPNsense 與 Suricata

- 報告透過 OPNsense `os-wazuh-agent` plugin 把防火牆端資料納入 Wazuh。
- 自訂 Suricata 規則可選擇只告警或阻擋；這代表 detection 與 prevention 必須分階段驗收。
- 畫面中可見 remote command 與 Active Response 類設定。這些屬高權限控制面，不應為了方便而全域啟用；必須限定來源、動作、帳號、作用範圍與回復程序。

## MCP 與本地模型觀察

作者把複雜模式提示與 few-shot 範例改為「hard gating + 明確不推論的預設值」，並以多組問題測試告警解釋、時間窗關聯、Agent 狀態、漏洞與下一個查詢工具。報告觀察到：

- `qwen3-8b` 在該次環境較符合預期，設定 temperature 0.4；
- Granite、Llama 與 DeepSeek 衍生模型曾發生 tool-call loop、誤用工具或無依據建議；
- 開新對話可降低跨任務 context 污染。

這些是作者在特定硬體、prompt、工具與資料集下的實驗觀察，不是可泛化的模型 benchmark。可複用原則是：調查模式要有進入條件、工具呼叫要有停止條件、缺欄位時不得自行補值，而且新案件應隔離 context。

## 端到端展示的解讀

報告以授權掃描展示 OPNsense 與 Wazuh 同時出現相關訊號。這能支持「網路事件可進入監控流程」，但若要稱為偵測驗證，仍需保存精確時間、sensor 規則版本、原始封包、Wazuh alert JSON、預期訊號與實際命中矩陣。

## ET-BERT 實驗

作者下載 ET-BERT 與 CSTNET-TLS1.3 資料，使用預訓練模型做 fine-tuning，並產生 58,171 筆推論結果；報告以結果與測試資料「高度吻合」描述成效。然而文件沒有提供 accuracy、precision、recall、F1、confusion matrix、獨立 holdout 或 split leakage 檢查，因此目前只能記為**已完成訓練／推論流程，偵測效能未驗證**。

## 敏感設定風險

報告截圖含 MCP／Indexer 連線欄位。知識庫不轉錄其中任何 credential；公開前應遮蔽帳密、token、內部位址與可識別主機資訊。設定值應改由環境變數或 secret store 注入，並對 AI connector 使用最小唯讀權限。

## 在知識庫中的位置

- 靶場驗證：[[detection-validation-range]]
- 偵測規則工程：[[ioc-ttp-and-detection-engineering]]
- 網路／AI 邊界：[[soc-lab-segmentation-and-telemetry]]
- 跨版本分析：[[threat-hunting-course-to-detection-range-evolution]]
- H-I-V-R-K-C：[[threat-hunting-range-evolution-review]]

