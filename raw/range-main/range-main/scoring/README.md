# scoring/

擴充四態評分表 schema 與工具。評分結果由「離線重放打受測偵測引擎（Wazuh / Zircolite）」產生，
每次演練版本化。

## 評分態（以 MITRE ATT&CK Evaluations 校準的擴充版）

| 態 | 意義 |
|---|---|
| **None** | 連遙測都沒有 |
| **Telemetry** | 有遙測但無規則（吸收自 MITRE，讓要件 7「有訊號 vs 沒訊號」有位置） |
| **Failed** | 有規則但被繞過（**守住這個 MITRE 沒有的診斷區分**） |
| **Success** | 命中 |

> **不跟進** 2026 TES 的單一量化分——量化犧牲診斷力，守住診斷分類為主。
> 校準依據與四態完整定義見 [SPEC §9](../docs/SPEC.md)。

## Arena（Phase 2）加反制維度

偵測到但沒圍堵 / 偵測到且圍堵 / 漏掉——YAGNI，到了 Phase 2 再長。

## 待實測

- CALDERA operation report 欄位夠不夠細、能否對映此 schema。
- Kali 本機記錄要多結構化才餵得回、與 CALDERA report 時間軸如何對齊縫合。
