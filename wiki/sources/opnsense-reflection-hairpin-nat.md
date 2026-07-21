---
type: source
title: "Reflection and Hairpin NAT"
authors: ["OPNsense Project"]
url: "https://docs.opnsense.org/manual/how-tos/nat_reflection.html"
raw: "raw/opnsense-reflection-hairpin-nat.md"
ingested: 2026-07-17
tags: [opnsense, networking, nat, firewall, network-segmentation]
entities: []
concepts: [nat-reflection-and-hairpin-nat, soc-lab-segmentation-and-telemetry]
created: 2026-07-17
updated: 2026-07-17
---

# OPNsense Reflection 與 Hairpin NAT 官方指南摘要

這份 OPNsense 官方指南說明：當用戶端使用服務的外部 IP 存取內部伺服器時，如何利用 DNAT 與 SNAT 維持正確的轉譯與回程路徑。文件區分不同子網的 Reflection NAT 與相同子網的 Hairpin NAT，並把可見、可稽核的手動規則列為最佳實務。

## 核心結論

- **Reflection NAT**：用戶端與伺服器在不同 Layer 2 廣播域，OPNsense 位於路由路徑上；通常只需 DNAT，把外部目的 IP 改寫為內部伺服器 IP。
- **Hairpin NAT**：用戶端與伺服器在同一 Layer 2 廣播域；需要 DNAT 與 SNAT，讓回應也經過 OPNsense，避免伺服器直接回覆用戶端造成非對稱流量。
- **NAT 不是安全功能**：它只做位址或連接埠轉譯，允許或拒絕流量仍由防火牆規則決定。
- **NAT 先於防火牆過濾**：DNAT 後的關聯規則應以轉譯後的內部目的 IP 為判斷對象。
- **方法不可混用**：文件提供三種互斥方法，建議採手動 DNAT、手動 SNAT及可見的關聯防火牆規則，避免舊式自動 Reflection 產生不易稽核的隱含規則。

## 三種方法

| 方法 | DNAT | SNAT | 防火牆規則 | 官方定位 |
|---|---|---|---|---|
| Method 1 | 手動 | 手動 | 建立關聯規則 | 建議採用，規則可見且容易稽核 |
| Method 2 | 自動 | 手動 | 手動 | 保留說明，不建議作為首選 |
| Method 3 | 自動 | 自動 | 手動 | 保留說明，不建議作為首選 |

若環境使用 One-to-One NAT，也可產生 Reflection 規則；若要維持手動可見性，應停用自動 Reflection for 1:1，並依 Method 1 的概念建立規則。

## 除錯證據

文件建議從四個層次確認問題：

1. 使用 `pfctl -s nat` 查看目前實際載入的 NAT 規則。
2. 查看 `/tmp/rules.debug`，確認設定產生的規則是否已被套用。
3. 由 Firewall Live View 與 Diagnostics Sessions 檢查規則命中和工作階段。
4. 在用戶端、OPNsense 與伺服器進行封包擷取，確認 SYN／SYN-ACK 與回程路徑。

## 對目前 SOC Lab 的意義

目前設計中的 `.40` 觀測網、OPNsense 內部實驗 LAN 與 VPN Attacker 是不同安全區域。觀測機以靜態路由存取 Wazuh 內部 IP 時不需要 Reflection；以 OPNsense WAN 位址做 Port Forward 時是一般 DNAT。只有內部主機繞回外部 IP 存取內部服務時才需要評估 Reflection 或 Hairpin NAT。這項判斷應納入 [[soc-lab-segmentation-and-telemetry]]，避免把 NAT 誤當作網段隔離或 VPN 授權控制。

## 限制與待驗證

- 官方指南使用示範網段與 `Any` 來源協助說明；實際專題規則應縮限到已知觀測機、VPN pool、目標主機與必要服務。
- OPNsense 介面文字可能隨版本變動，正式部署前需在目前安裝版本核對選單與規則預覽。
- VPN 介面若綁定外部 IP，文件提示可能需要獨立規則與 `reply-to`；此項必須以實際 VPN 類型及封包路徑驗證。

## 在知識庫中的位置

- 核心概念：[[nat-reflection-and-hairpin-nat]]
- SOC 網路邊界：[[soc-lab-segmentation-and-telemetry]]
- 既有架構研究：[[wazuh-ad-soc-architecture-research]]

