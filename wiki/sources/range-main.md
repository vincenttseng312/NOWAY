---
type: source
title: "locrian 實作規格（build-of-record）"
authors: []
url: ""
raw: "raw/range-main/range-main/"
ingested: 2026-07-20
tags: [wazuh, opnsense, detection-engineering, threat-hunting, network-segmentation]
entities: []
concepts: [detection-validation-range, soc-lab-segmentation-and-telemetry, ioc-ttp-and-detection-engineering]
created: 2026-07-20
updated: 2026-07-20
---

# locrian 實作規格摘要

`range-main` 是一份以 Proxmox／Ludus 為基礎的偵測驗證靶場規格。它把靶場定位為「錄音室」：紅隊或模擬器執行一次授權情境時，同步保存可重放的 ground truth，之後用相同資料做離線偵測回歸，而不只保留一次性的告警畫面。

## 來源性質與可信度

- 來源包含 `README.md`、完整 `docs/SPEC.md`、Phase 0 checklist，以及 Ludus、OPNsense、Sigma、錄製與評分模組的 README。
- 目前多數實作目錄只有 `.gitkeep` 或介面說明，因此可驗證的是**設計一致性與預定驗收條件**，不能據此宣稱靶場已建置完成。
- `__MACOSX`、`.DS_Store` 屬封裝雜訊；不應進入知識結論或後續版本庫。

## 核心架構

| 層次 | 角色 | 設計重點 |
|---|---|---|
| 虛擬化與編排 | Proxmox、Ludus | 建立可重建的 Windows／AD 與攻擊測試環境 |
| 邊界控制 | OPNsense、Suricata | 控制跨區流量並保存南北向網路證據 |
| 企業靶場 | GOAD、Windows、GHOSTS | 產生 AD 與使用者基線活動 |
| 端點偵測 | Sysmon、Wazuh Agent、Wazuh | 保存端點事件並產生規則告警 |
| 網路偵測 | Suricata、選配 Zeek | 取得 signature 命中與東西向通訊證據 |
| 離線分析 | Zircolite、Sigma | 對保存的 EVTX／Sysmon 資料做可重複規則測試 |
| 情境執行 | CALDERA、Kali、人工操作 | 僅在授權隔離環境執行並留下操作時間線 |

設計把 control plane 與 data plane 分開：管理、部署與控制流量不應和攻擊／靶場資料流量共用未受控路徑。內外層之間採靜態路由且不做 NAT，NAT 只留在 Internet 邊界；這使封包來源、回程與規則命中較容易解釋。規格另設兩個鏡像點：OPNsense 觀察南北向流量，內部鏡像點供 Zeek 觀察東西向流量。

## 分階段交付

1. **Phase 0 Foundation**：最小 DC、1–2 台端點、Wazuh、GHOSTS 基線、PCAP 與 EVTX／Sysmon 保存，以及 control/data plane 驗證。
2. **Phase 1 Studio**：執行第一條 TTP 情境，產出 ground truth、Wazuh／Zircolite 結果、Sigma 規則與第一份 scorecard。
3. **Phase 2 Arena**：在已有可重放驗證基線後，再評估 Active Response 或 IPS；阻擋能力不先於可觀測性。

## Ground Truth 與評分

每次 run 至少保存三類證據：

- 原始 `PCAP`；
- 完整 `EVTX`／Sysmon；
- 操作者 step log，包含 timestamp、ATT&CK 對應與預期 forensic signal。

原始 PCAP／EVTX 不進 Git；由解析器產生的 JSON 可進獨立 corpus repository。這個分層同時控制檔案體積、敏感資訊與版本可追溯性。

規格用四態評分區分問題來源：`None`（無遙測）、`Telemetry`（有資料但無規則）、`Failed`（規則存在但未命中／被繞過）、`Success`（規則命中）。這比單純 pass/fail 更能指出應先修 sensor、parser、規則還是測試設計。

## 預定訊號範圍

規格涵蓋 C2、ARP／資產發現、暴力登入、FIM、橫向移動與身分驗證、持久化、資料外傳、清除日誌、Web 攻擊、掃描與 Kerberos 票證濫用等類別。這些是**待驗證的訊號清單**，不是已完成的偵測覆蓋率。

## 安全與版本保存

- 原始封包、EVTX、憑證、金鑰、`.env` 與 secrets 必須排除於 Git。
- OPNsense 匯出設定可能含敏感資料；目前 `.gitignore` 沒有強制排除所有 XML，推送前仍需人工檢查與去識別化。
- 攻擊情境只保留 TTP、預期證據與防禦驗證需求，不把可武器化步驟寫入主 Wiki。

## 在知識庫中的位置

- 核心方法：[[detection-validation-range]]
- 網路與遙測邊界：[[soc-lab-segmentation-and-telemetry]]
- 規則工程：[[ioc-ttp-and-detection-engineering]]
- 跨版本分析：[[threat-hunting-course-to-detection-range-evolution]]
- 驗證閉環：[[threat-hunting-range-evolution-review]]

