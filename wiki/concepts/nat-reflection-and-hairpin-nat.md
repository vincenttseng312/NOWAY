---
type: concept
title: "NAT Reflection 與 Hairpin NAT"
tags: [opnsense, networking, nat, firewall, network-segmentation]
sources: [opnsense-reflection-hairpin-nat]
created: 2026-07-17
updated: 2026-07-17
---

# NAT Reflection 與 Hairpin NAT

NAT Reflection 與 Hairpin NAT 都處理「內部用戶端使用外部 IP 存取內部服務」的情境，但兩者的 Layer 2 位置與回程需求不同。判斷關鍵不是服務名稱，而是用戶端與伺服器是否位於同一子網，以及回應是否必須被迫回到 OPNsense。

## 快速判斷

| 情境 | 用戶端與伺服器 | 必要轉譯 | 原因 |
|---|---|---|---|
| 一般內部路由 | 不同子網，直接使用內部 IP | 不一定需要 NAT | OPNsense 依路由與防火牆規則轉送 |
| 一般 Port Forward | 外部／WAN 來源使用 OPNsense 外部 IP | DNAT | 把外部目的位址轉到內部服務 |
| Reflection NAT | 內部來源與伺服器在不同子網，但使用外部 IP | DNAT | OPNsense 已在雙向路由路徑上 |
| Hairpin NAT | 內部來源與伺服器在同一子網，且使用外部 IP | DNAT + SNAT | 強制伺服器經 OPNsense 回覆，避免非對稱路徑 |

## 封包路徑

Reflection NAT 的概念路徑：

```text
LAN Client
  -> public/WAN IP:443
  -> OPNsense DNAT
  -> DMZ Server internal IP:443
  -> OPNsense
  -> LAN Client
```

Hairpin NAT 的概念路徑：

```text
Same-subnet Client
  -> public/WAN IP:443
  -> OPNsense DNAT + SNAT
  -> Same-subnet Server:443
  -> OPNsense interface address
  -> Client
```

Hairpin 的 SNAT 讓伺服器看到 OPNsense 介面位址作為來源，因此回應不會直接繞過防火牆送回同網段用戶端。

## OPNsense 建議實作原則

依 [[opnsense-reflection-hairpin-nat]]，優先採用手動、可見的規則：

1. 停用舊式全域自動 Reflection 選項，避免產生不透明的隱含規則。
2. 在所有可能收到該外部目的 IP 的介面上建立明確 DNAT。
3. 僅在相同子網 Hairpin 情境增加 Outbound NAT／SNAT。
4. 建立可見的關聯防火牆規則，並確認其目的位址是 DNAT 後的內部主機。
5. 來源、目的與連接埠應縮限到實際需求；官方教學中的 `Any` 是示例，不應直接當成專題安全基線。

## 安全邊界

- NAT 只做轉譯，不代表允許，也不提供身分驗證或最小權限。
- VPN 使用者可存取哪些內部主機，仍由 VPN 身分、路由與防火牆規則決定。
- 啟用全域自動 Reflection 可能讓規則關係變得不透明；在 SOC Lab 中，流量控制必須能由 GUI、設定匯出與防火牆日誌交叉驗證。
- NAT 在防火牆過濾前處理，因此除錯時要同時檢查原始目的、轉譯後目的與實際命中的 filter rule。

## 套用到目前單一 VPN 架構

目前規劃可按下列方式判斷：

| 路徑 | 分類 | 建議 |
|---|---|---|
| `.40` 觀測機以靜態路由連 Wazuh 內部 IP | 一般路由 | 以來源 IP + HTTPS 防火牆規則限制，不用 Reflection |
| `.40` 觀測機連 OPNsense WAN 位址，再轉到 Wazuh | 一般 DNAT | 只允許觀測機固定 IP，避免對整個 `.40` 開放 |
| VPN Attacker 直接連 Win10 內部 IP | VPN 路由 | 在 VPN 介面明確放行靶機與測試服務，預設拒絕其他內網 |
| 內部不同子網使用外部 IP 存取 Wazuh | Reflection NAT | 建立手動 DNAT與可見的 filter rule |
| 與 Wazuh 同子網的主機使用外部 IP 存取 Wazuh | Hairpin NAT | 除 DNAT 外增加精確 SNAT，驗證雙向路徑 |

因此，「只使用一組 Attacker VPN」與是否需要 NAT Reflection 是兩個不同決策。單一 VPN 架構可以成立；NAT 類型應由服務被存取的位址與實際封包回程決定。

## 驗證與除錯清單

- 檢查用戶端解析到的 IP：內部 IP、OPNsense WAN IP，還是其他公開 IP。
- 確認用戶端與伺服器是否在同一子網。
- 檢查 OPNsense 的 NAT 規則、filter rule、Live View 與 Sessions。
- 確認伺服器的預設閘道與回程介面。
- 必要時於三個節點擷取封包，檢查 SYN、SYN-ACK 與來源／目的位址變化。

## 關聯

- 官方來源摘要：[[opnsense-reflection-hairpin-nat]]
- 網段與遙測邊界：[[soc-lab-segmentation-and-telemetry]]
- 整體架構研究：[[wazuh-ad-soc-architecture-research]]

