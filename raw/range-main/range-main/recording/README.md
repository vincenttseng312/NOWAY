# recording/

錄音室錄製管線。**現場人工打一次 → 產出版本化 artifact 語料 → 改規則就對語料離線重放
做回歸**。這是化解「偵測回歸需可重現 vs 人工紅隊不可重放」張力的核心機制。

## 一次演練要錄的三類 ground-truth

1. **全流量 PCAP** — Port Mirror（周邊鏡像 + 內部鏡像）。
2. **全量端點日誌** — EVTX / Sysmon。
3. **操作員逐步驟日誌** — 打時間戳、對應 ATT&CK 與十一類鑑識點。
   - 入侵後：CALDERA operation report（Phase 1+）。
   - 初始存取那一跳：Kali VM 本機 instrument（script/asciinema/shell history 或 RedELK）。

## 母帶 vs 語料（存哪，見根 README）

- **原始 EVTX/PCAP = 母帶**：重、選擇性保留，不進本 git（見 `.gitignore`）。
- **解析後 JSON 事件 = 版本化語料**：小、可 diff，經 `kafkacat` / 重放工具送進你的日誌管線或 SIEM ingest。

## 待實測

- 重放（`kafkacat` / 其他）進你的日誌管線的 topic / 格式對接。
- 「存解析後 / 存原始 / 兩者都存」最終取捨——原則：存的格式要對得上你的偵測引擎重新 ingest 入口。
- 控制平面（操作員遙控）不得污染資料平面鏡像——Phase 0 就要驗（見 phase-0-checklist）。
