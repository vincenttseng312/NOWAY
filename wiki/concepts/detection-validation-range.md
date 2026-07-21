---
type: concept
title: "可重放的偵測驗證靶場"
tags: [detection-engineering, threat-hunting, telemetry, wazuh, network-segmentation]
sources: [range-main, threat-hunting-course-midterm-report, threat-hunting-course-final-report]
created: 2026-07-20
updated: 2026-07-20
---

# 可重放的偵測驗證靶場

偵測驗證靶場不是只讓攻擊與告警「出現一次」，而是把每次授權情境轉成有版本、可重放、可比較的測試資料。其核心輸出不是截圖，而是 **ground truth + 原始遙測 + 規則版本 + 結果矩陣**。

## 兩個平面

| 平面 | 內容 | 不可混淆的原因 |
|---|---|---|
| Control plane | 部署、管理、MCP／API、規則同步、實驗起停 | 若和攻擊流量共用寬鬆權限，測試者可能同時取得監控控制權 |
| Data plane | 靶場通訊、端點事件、網路封包、sensor 輸出 | 必須保留原始來源與路徑，才能解釋漏報或錯誤歸因 |

網路邊界的細節見 [[soc-lab-segmentation-and-telemetry]]。原則上，內部分區優先使用可稽核的路由與防火牆規則；NAT 留給必要的 Internet 邊界，避免轉譯掩蓋來源與回程問題。

## Ground Truth 最小集合

一次 run 至少包含：

1. **Run manifest**：run ID、日期、環境版本、TTP／ATT&CK、參與主機、預期訊號、規則與 sensor 版本。
2. **Operator timeline**：每個步驟的 UTC timestamp、動作類別、預期 forensic point 與人工註記。
3. **原始證據**：PCAP、EVTX／Sysmon、Wazuh alert JSON、Suricata／Zeek 輸出及必要的系統設定快照。
4. **結果矩陣**：每個預期訊號在哪個 sensor 出現、是否被解析、是否觸發規則、延遲與誤報備註。

原始證據通常不進 Git；Git 保存 manifest、規則、解析後去識別 JSON、報告與 hash。資料 corpus 應獨立版本化並設存取控制。

## 四態評分

| 狀態 | 可觀測結果 | 問題定位 | 下一步 |
|---|---|---|---|
| `None` | 預期 sensor 沒有資料 | telemetry gap | 修 sensor、audit policy、路由、時間同步或保存流程 |
| `Telemetry` | 有原始資料，沒有可用規則 | detection gap | 建 parser／規則與測試樣本 |
| `Failed` | 規則存在但未命中預期行為 | rule bypass／假設錯誤 | 檢查欄位、條件、版本與 TTP 變體 |
| `Success` | 規則命中且證據可追溯 | 已覆蓋 | 加入 regression corpus，監控誤報與版本退化 |

四態不是風險分級，也不是單一告警的 severity；它描述的是「一個預期偵測點目前走到哪一步」。規則設計原則見 [[ioc-ttp-and-detection-engineering]]。

## 驗證循環

```text
定義假設與預期訊號
  → 固定環境／規則／sensor 版本
  → 執行一次授權情境並同步錄製
  → 以 ground truth 對齊各資料源
  → 四態評分與根因分類
  → 修正 sensor／parser／rule
  → 對舊 corpus 重放，確認沒有 regression
```

單一 dashboard 截圖只能證明某個時間點曾看到告警；至少要有原始事件、時間對齊與重跑結果，才能主張可重現。

## 導入階段

1. **Foundation**：先完成時間同步、端點與網路遙測、raw artifact 保存。
2. **Studio**：每次只選一條明確 TTP，建立第一份 ground truth 與 scorecard。
3. **Regression**：把已確認的 run 加入離線 corpus，對規則版本做重放。
4. **Arena／Prevention**：可觀測性與回復流程成熟後，才啟用 Active Response 或 IPS。

## AI／ML 的額外驗證要求

- LLM：記錄模型、版本、temperature、system prompt、工具 schema、輸入證據與完整 tool trace；設定進入／停止條件，缺資料時採 non-inference default。
- 流量模型：除推論筆數外，至少報告資料切分、class distribution、confusion matrix、precision／recall／F1、獨立 holdout 與 leakage 檢查。
- AI 回答與模型分類都不能取代 ground truth；它們是被驗證的元件，不是裁判本身。

## 關聯

- 規格來源：[[range-main]]
- 課程實作：[[threat-hunting-course-midterm-report]]、[[threat-hunting-course-final-report]]
- 演進分析：[[threat-hunting-course-to-detection-range-evolution]]
- 閉環驗證：[[threat-hunting-range-evolution-review]]

