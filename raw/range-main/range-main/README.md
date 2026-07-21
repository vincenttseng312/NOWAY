# README

偵測驗證 + 紅隊測試用的數位靶場——實作 repo。

> 偵測驗證 + 紅隊測試數位靶場，供團隊照 [docs/SPEC.md](docs/SPEC.md) 落地實作。

## 這個 repo 是什麼

偵測靶場的**實作規格與運維產物**,自足可施作——照 [docs/SPEC.md](docs/SPEC.md) 做,
**不需開任何外部 repo**。內容:Ludus blueprint、Ansible role、OPNsense config、
Suricata / Sigma 規則、錄音室錄製管線、擴充四態評分工具。

**實作依據 = [docs/SPEC.md](docs/SPEC.md)（build-of-record）**：目標、兩層網路拓樸、
元件選型、七要件對映、三條 TTP、十一類鑑識點、錄音室機制、評分法、分階段路線圖全在裡面。
動手前先讀它。SPEC 是唯一權威——**施作不依賴任何外部文件或 repo**。

## artifact 語料存哪（不在本 repo）

依設計的「母帶 vs 語料」分層，ground-truth 產物**不放這個 git repo**：

| 內容 | 放哪 |
|---|---|
| Ludus / Ansible / OPNsense config / Sigma 規則（本 repo） | 一般 git |
| 解析後 JSON 事件語料（atomic/compound + ATT&CK manifest） | 獨立語料 repo（照 Security-Datasets 慣例） |
| 原始 EVTX / PCAP 母帶 | 物件儲存 / NAS，按保留期，不進 git 歷史 |

## 目錄結構

```
ludus/            Ludus blueprint（內層企業內網）+ 自寫 Ansible role
  blueprints/     range YAML（DC / 端點 / 之後的 GOAD / DMZ）
  roles/
    ghosts_client/  自寫 GHOSTS client role（Phase 0 先 headless Command handler）
opnsense/         最外層邊界閘道，手動建、獨立於 Ludus，帶外版控
  config/         config.xml 匯出
  suricata/       Suricata 規則
detection/        受測偵測層
  sigma/          十一類鑑識點的 Sigma 規則
  wazuh/          Wazuh 設定 / decoder（受測偵測層核心：SIEM/HIDS）
recording/        錄音室錄製管線（PCAP + 全量 EVTX/Sysmon + 重放）
scoring/          擴充四態評分表 schema 與工具
docs/             phase checklist 等落地文件
```

## 目前階段

Phase 0（地基）。逐步 checklist 見 [docs/phase-0-checklist.md](docs/phase-0-checklist.md)。

路線圖總覽（詳見 [docs/SPEC.md](docs/SPEC.md) §10）：

- **Phase 0 — 地基**：Ludus + OPNsense + Wazuh + GHOSTS baseline + 全量錄製。
- **Phase 1 — Studio**：跑一條 TTP、錄 artifact、對 Wazuh + Zircolite 產第一張擴充四態評分表、寫 Sigma 規則。
- **Phase 2 — Arena**：現成工具啟用反制迴路（Wazuh active response / Sysmon EID 27/28 / OPNsense 切 IPS）。
