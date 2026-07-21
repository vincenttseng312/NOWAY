---
type: synthesis
title: "從課程展示到可重放偵測驗證靶場"
tags: [threat-hunting, detection-engineering, wazuh, opnsense, ai-security]
sources: [threat-hunting-course-midterm-report, threat-hunting-course-final-report, range-main]
created: 2026-07-20
updated: 2026-07-20
---

# 從課程展示到可重放偵測驗證靶場

三份來源呈現一條清楚的成熟度路徑：期中建立 telemetry path，期末加入防火牆 agent、AI 與流量模型，`range-main` 再把分散實驗重編譯成可版本化、可重放的 detection validation range。

## 演進對照

| 面向 | 期中報告 | 期末報告 | range-main 規格 |
|---|---|---|---|
| 網路 | 多網段、VPN、OPNsense／Suricata | 延續並加入 OPNsense Agent、Alert／Drop | control/data plane 分離、內層 routing no NAT、雙鏡像點 |
| 端點 | Sysmon、Windows Audit、Wazuh 規則展示 | 延續端點與邊界訊號 | PCAP + 全量 EVTX／Sysmon + operator log |
| AI | MCP 可讀資料但回答不穩 | hard gating、模型比較、context reset 觀察 | AI 應納入可重放評估，不作 ground-truth 裁判 |
| ML | 未納入 | ET-BERT 已跑訓練／推論，效能證據不足 | corpus、版本與 scorecard 才能支持回歸 |
| 驗證 | 以截圖證明管線可通 | 增加端到端展示 | 四態評分區分 telemetry、rule 與 bypass 問題 |

## 核心判斷

1. **期中／期末是有價值的 implementation evidence**：它們證明 Sysmon、Suricata、Wazuh 與 MCP 曾被串接，而不是純概念圖。
2. **仍不是 regression evidence**：缺 raw artifacts、版本 manifest、明確 ground truth、重跑結果與量化指標，無法判定偵測品質是否穩定。
3. **range-main 的主要進步是方法學**：它把每次操作變成可比較資料，並以 `None / Telemetry / Failed / Success` 定位問題。
4. **目前最合理的整合方式**：保留現有 Wazuh × AD × OPNsense lab 作 foundation，先補錄製與驗收規格，不必一次導入 GOAD、CALDERA、Zeek 與完整 Ludus。

## 對目前 Wazuh 專題的最小改寫

- 每一個攻擊情境頁加上 `expected_signals`、`ground_truth_artifacts`、`sensor_versions` 與 `result_state`。
- Wazuh Agent onboarding、Sysmon 與 Windows Audit 驗收，不只看 Active／有事件，還要保存時間同步、config hash、EVTX 與 alert JSON。
- OPNsense 上線後先驗證 routing、firewall log 與封包路徑，再評估 Suricata Drop 或 Active Response。
- MCP 使用唯讀帳號、明確 tool allow-list、每次案件獨立 context，並保存 tool trace 供稽核。
- AI／ML 的「看起來正確」一律降為待驗證；沒有 confusion matrix 或逐筆 ground truth，不宣稱準確率。

## 風險與資料治理

- 歷史報告內的 IP、帳密、token 與 Indexer 設定不能直接遷移或公開。
- 啟用 remote command、Active Response、Indexer 對外 listener 或 Suricata Drop 都會改變風險面；每項都要有最小權限、變更紀錄、回復步驟與獨立驗收。
- 原始 PCAP／EVTX 可能含憑證、個資與內部拓樸；應放在受控 corpus，而不是一般 Git repository。

## 結論

這批資料支持的最佳下一步不是再增加工具，而是先完成 [[detection-validation-range]] 的最小閉環：選一條已授權情境，建立 run manifest、同步保存 PCAP／EVTX／Wazuh JSON，做四態評分，再重放一次確認結果。完整驗證紀錄見 [[threat-hunting-range-evolution-review]]。

