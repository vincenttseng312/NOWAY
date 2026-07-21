# OPNsense Reflection and Hairpin NAT 官方文件研究摘記

- 原始標題：Reflection and Hairpin NAT
- 官方網址：https://docs.opnsense.org/manual/how-tos/nat_reflection.html
- 擷取日期：2026-07-17
- 來源單位：OPNsense Project／Deciso B.V.
- 文件性質：OPNsense 官方操作指南

> 本檔保存來源定位與研究摘記，不取代官方頁面。內容以繁體中文重述，實際選單名稱與版本差異應回到官方網址核對。

## 文件處理的問題

內部用戶端有時會使用服務的外部 IP 或公開 DNS 名稱存取內部伺服器。由於外部 IP 通常配置在 OPNsense 的 WAN 介面上，防火牆若沒有額外轉譯規則，可能把封包視為送給自己，而不是送往內部伺服器。Reflection NAT 與 Hairpin NAT 用來處理這種路徑。

## NAT 基本名詞

- SNAT：改寫封包來源 IP，在 OPNsense 的 Outbound NAT 規則中配置。
- DNAT：改寫封包目的 IP，在 Destination NAT／Port Forward 規則中配置。
- PAT：改寫目的連接埠，也由 Destination NAT／Port Forward 規則配置。
- NAT 只負責位址或連接埠轉譯，不是安全控制；存取限制仍需防火牆規則。

## Reflection NAT 與 Hairpin NAT

- Reflection NAT：用戶端與伺服器位於不同子網，封包由 OPNsense 路由。把外部目的 IP 轉成內部伺服器 IP，通常只需要 DNAT。
- Hairpin NAT：用戶端與伺服器位於同一子網。除了 DNAT，還需要 SNAT，使伺服器的回應經過 OPNsense，避免回程直接送給用戶端造成非對稱流量。

## 官方建議

官方建議優先使用明確的手動 NAT 規則，不依賴 Advanced Settings 中的舊式自動 Reflection 選項。手動規則在 GUI 與設定匯出檔中可見，較容易檢查流量範圍及進行稽核。

官方列出三種互斥方式：

1. 手動 DNAT、手動 SNAT，並建立關聯的防火牆規則；這是建議方式。
2. 自動 DNAT、手動 SNAT與手動防火牆規則；文件保留說明，但不建議作為首選。
3. 自動 DNAT、自動 SNAT與手動防火牆規則；文件保留說明，但不建議作為首選。

應選定一種方法並一致使用，避免自動與手動規則重疊。

## 規則處理與除錯

- NAT 轉譯先於防火牆過濾；防火牆規則通常看到的是轉譯後的內部目的位址。
- `pfctl -s nat` 可查看目前載入的 NAT 規則。
- `/tmp/rules.debug` 可檢查產生後的完整規則；若設定存在但未載入，應確認是否已套用變更。
- Firewall Live View、Diagnostics Sessions 與封包擷取可用來確認規則命中、工作階段與 TCP 往返路徑。
- 外部 IP 若綁定在額外 VPN 介面，可能需要獨立的 VPN 防火牆規則及 `reply-to` 設定，不能假設一般 WAN 規則一定適用。

## 專題脈絡

在「本地觀測機位於 `.40` 上游網段、OPNsense WAN 位於 `.40`、實驗 VM 位於內部 LAN、Attacker 經單一 VPN 進入」的設計中：

- 觀測機透過靜態路由直接連到 Wazuh 內部 IP，屬一般路由與防火牆控制，不是 NAT Reflection。
- 觀測機連到 OPNsense WAN 位址，再由 Port Forward 送到 Wazuh，屬一般 DNAT。
- 內部不同子網的主機使用 OPNsense 外部 IP 存取內部服務，才是 Reflection NAT。
- 與伺服器位於相同子網的主機使用外部 IP 存取該伺服器，才需要 Hairpin NAT 的 DNAT + SNAT。
- VPN Attacker 到內部靶機原則上是路由與防火牆問題；除非使用外部位址或有特殊回程要求，不能把 NAT 當成必要條件。

