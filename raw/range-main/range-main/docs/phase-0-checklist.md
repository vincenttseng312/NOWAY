# Phase 0 — 地基 checklist

**目標**：拉起最小企業拓樸 + 測量儀器，能對一次手動操作完整錄到 ground-truth。
**完全不涉 core\***。設計依據：[SPEC.md](SPEC.md)。

**驗收標準**：能拉起環境 → GHOSTS 在產 baseline 噪音 → Wazuh 在收 →
你能對一次手動操作**完整錄到 PCAP + 全量 EVTX**，且控制平面流量沒污染鏡像。

---

## 1. 底座：Proxmox + Ludus

- [ ] 確認硬體（CPU/RAM/磁碟）夠拉起最小拓樸 + 之後的 GOAD 全森林
- [ ] 裝 Proxmox
- [ ] 裝 Ludus，`ludus` CLI 能拉起並銷毀一台測試 VM（先驗底座再往上疊）
- [ ] 確認 Ludus 快照回復可用

## 2. 最外層邊界：OPNsense（手動、獨立於 Ludus）

> 拓樸與接線鐵律見 [SPEC §2](SPEC.md)。

- [ ] OPNsense 裝成最外層邊界閘道，整個 Ludus 環境跑在它之後
- [ ] 打通 `WAN → OPNsense → 一個內網介面`，基本連通
- [ ] Suricata 先跑 **IDS**（被動，保住 Studio 可比較性）
- [ ] **config.xml / Suricata 規則從第一天就帶外版控**（要件 7 精神在 Ludus 之外維持）
      → 匯出到 `opnsense/config/`、`opnsense/suricata/`，commit
- [ ] 內層 OPNsense↔Ludus 走**靜態路由、不 NAT**（避免雙層 NAT 抹掉來源 IP）

## 3. 內層企業拓樸：Ludus 最小 blueprint

- [ ] blueprint 拉起 **DC + 1~2 端點**（先不上 GOAD 全森林）
- [ ] 拓樸能通、快照能回復
- [ ] blueprint YAML commit 到 `ludus/blueprints/`

## 4. 受測藍隊基礎：Wazuh

- [ ] 用現成社群 role 佈署：`aleemladha.wazuh_server_install` + `ludus_wazuh_agent`
- [ ] Wazuh 在收 DC + 端點日誌（這步最省力，優先做通）
- [ ] Wazuh 設定 commit 到 `detection/wazuh/`

## 5. 正常行為 baseline：GHOSTS

> client 端無現成 role，是本 phase 唯一要自寫一點 code 的地方。

- [ ] server 用現成 role `frack113.ludus_ghosts_server`
- [ ] **自寫 client role**（`ludus/roles/ghosts_client/`）——照 frack113 的 Windows
      agent pattern（`ludus_caldera_agent` / `ludus_aurora_agent`）改
- [ ] **Phase 0 只做 headless `Command` handler**（產生網路/認證/程序噪音就夠當 baseline，
      免互動桌面 session）；GUI 行為當增量後加
- [ ] 每個 NPC 對應報告帳戶模型的一個使用者
- [ ] 確認 baseline 噪音有真的流進 Wazuh + 鏡像

## 6. 錄音室物理前提：Port Mirror + 全量錄製

- [ ] **周邊鏡像**（OPNsense）錄南北向
- [ ] **內部鏡像**（Ludus 內）錄東西向
- [ ] 鐵律驗證：**每條南北向必過 OPNsense 鏡像、每條東西向必過內部鏡像，無繞過路徑**
- [ ] 全量錄製管線：PCAP + 全量 EVTX/Sysmon 落地（腳本進 `recording/`）
- [ ] 對一次手動操作驗一遍：能完整取回 PCAP + EVTX

## 7. 提早驗控制/資料平面分離（別等 Phase 1 攻擊機進場）

> 這是隱藏的先決驗證；等攻擊機進場才發現 PCAP 被 session 污染會很痛。

- [ ] 操作員帶外通道走 Ludus WireGuard，在 OPNsense 上 port-forward
- [ ] 驗證：`控制平面（操作員遙控流量）`**完全不落進**當 ground-truth 在錄的鏡像
- [ ] 確認 `資料平面（要錄）` 與 `控制平面（不錄）` 物理/邏輯分離成立

---

## Phase 0 交付物

- 可拉起/回復的最小企業拓樸（Ludus blueprint + 手動 OPNsense，皆版控）
- GHOSTS baseline 噪音源（headless）
- Wazuh 在收
- 驗證過的全量錄製管線 + 一份能完整取回的 ground-truth 樣本
- 控制/資料平面分離的驗證記錄

→ 具備後進 Phase 1（跑第一條 TTP、產第一張評分表）。
