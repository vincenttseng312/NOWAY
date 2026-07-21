---
id: exp-threat-hunting-range-evolution-review
type: experiment
title: "從課程實作到可重放偵測驗證靶場的演進"
topic: "從課程實作到可重放偵測驗證靶場的演進"
tags: [experiment, threat-hunting, detection-engineering, wazuh]
status: completed
hypothesis: "把期中／期末的單次成功展示重新編譯成 ground truth、重放與四態評分，可形成更可重現的偵測驗證方法。"
result: partial
confidence: medium
verified_on_this_machine: true
code_paths: []
sources: [range-main, threat-hunting-course-midterm-report, threat-hunting-course-final-report]
created: 2026-07-20
updated: 2026-07-20
related: [detection-validation-range, soc-lab-segmentation-and-telemetry, windows-event-log-and-sysmon, ioc-ttp-and-detection-engineering, threat-hunting-course-to-detection-range-evolution]
---

# 實驗：威脅獵捕課程到偵測驗證靶場的演進

## 1. 假設 Hypothesis

### H1（主要）

期中與期末報告已證明多條 telemetry path 可工作；若再加入 `range-main` 的 ground truth、artifact 保存、重放與四態評分，就能把「成功截圖」提升成可回歸的 detection engineering 流程。

信心為 Medium：來源間的設計方向一致，但目前沒有執行中的 `range-main` 環境或完整 corpus 可做端到端重跑。

### H2（替代）

`range-main` 可能只是規格層重新包裝，若沒有可執行角色、資料 schema 與自動評分，並不會自然提升可重現性。

區分 H1／H2 的方法：完成一條 TTP run，保存規定 artifacts，重放到固定版本規則，再由獨立 scorecard 比對預期與實際結果。

## 2. 實作 Implementation

- 讀取 `range-main` 的 README、SPEC、Phase 0 checklist 與各模組 README，盤點實作完整度。
- 逐頁抽取並視覺檢查兩份 PDF 的架構、Sysmon、OPNsense、MCP、Wazuh 與 ET-BERT 證據。
- 把來源主張分成：已展示的實作、文件可驗證的設計、尚待實機證明的效能。
- 建立 [[detection-validation-range]]，並以 [[threat-hunting-course-to-detection-range-evolution]] 彙整版本演進。

### Code Preservation

本輪沒有建立或修改可執行攻防程式、規則或部署設定，因此 `code_paths` 為空。`range-main` 原始 skeleton 保留於 `raw/`，但它不是本輪產生的 code artifact。日後若實作 recorder、parser、scorecard 或 Sigma regression runner，應保存於 `code/YYYY-MM-DD/<topic>/` 並附 manifest。

## 3. 驗證 Verification

`verified_on_this_machine: true` 只表示本機完成來源讀取、PDF 視覺核對與 repository 結構檢查，不代表靶場、規則或模型已在本機實跑。

| 編號 | 驗證問題 | 方法 | 實際結果 | 判定 |
|---|---|---|---|---|
| V1 | `range-main` 的設計是否形成一致方法 | 比對 SPEC、checklist 與模組 README | 架構、phase、artifacts 與四態評分一致 | 通過 |
| V2 | `range-main` 是否已可部署 | 檢查實作目錄與可執行內容 | 多數目錄僅有 `.gitkeep`／README | 未通過；仍是 Phase 0 skeleton |
| V3 | 期中／期末是否展示端到端訊號 | 檢查 OPNsense、Wazuh、Sysmon 與測試截圖 | 可支持若干管線曾成功，但缺 raw artifact 與重跑證據 | 部分通過 |
| V4 | MCP hard gating 是否已穩定 | 比對模型觀察、prompt 與問題範例 | 僅有作者觀察，缺完整 tool trace、成功率與固定測試集 | 證據不足 |
| V5 | ET-BERT 效能是否成立 | 檢查資料切分與評估指標 | 有訓練／推論流程，無 F1、confusion matrix 或 leakage 檢查 | 證據不足 |
| V6 | 四態評分是否已自動化 | 檢查 scoring 目錄 | 只有 README，未見 schema／runner／實際 scorecard | 待實作 |

結果為 `partial`：方法假設受到來源支持，但尚未以完整 run 重放證明。

## 4. 反思 Reflection

- 「Agent active」「看到告警」「AI 能回答」都只是局部通過條件，不等於整體偵測已驗證。
- 最關鍵的知識更新是把漏報拆成 telemetry gap、detection gap 與 rule bypass；三者需要不同修復方式。
- 期末的模型比較和 ET-BERT 結果具有研究線索價值，但缺少固定資料集與量化方法，不能升格為產品選型結論。
- 高權限 remote command、Active Response、Indexer listener 與 Drop 規則應晚於可觀測性和回復流程。
- 規格完整度與實作完整度必須分開記錄；README 中的 planned feature 不是 deployed fact。

## 5. Knowledge Ingestion

- 來源摘要：[[range-main]]、[[threat-hunting-course-midterm-report]]、[[threat-hunting-course-final-report]]
- 原子概念：[[detection-validation-range]]
- 既有概念增量：[[soc-lab-segmentation-and-telemetry]]、[[windows-event-log-and-sysmon]]、[[ioc-ttp-and-detection-engineering]]
- 跨來源綜合：[[threat-hunting-course-to-detection-range-evolution]]
- 專題承接：`projects/wazuh-ad-soc/01-architecture/`、`06-detection-logic/` 與 `00-overview/`

## 6. 後續問題 Next Questions

1. 第一條 regression 情境要選哪一個已有合法重現方式、且同時有端點與網路遙測的 TTP？
2. Run manifest、operator log 與 scorecard 要採哪個 JSON schema，誰負責簽核 ground truth？
3. PCAP／EVTX corpus 的儲存位置、保留期限、去識別化與存取權限為何？
4. 如何固定 Wazuh／Sysmon／Suricata／Sigma 版本，並在規則更新後自動重放？
5. MCP 與 ET-BERT 各自的固定測試集、成功指標與失敗門檻為何？
