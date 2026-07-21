# opnsense/

最外層邊界閘道的**帶外版控**。OPNsense 手動建、**獨立於 Ludus**——整個 Ludus 環境
跑在它之後，Ludus 不控制它。

> 為什麼獨立：把 Ludus 整合摩擦溶掉（免自建 template/包 role），且更擬真企業
> defense-in-depth。完整拓樸與接線鐵律見 [SPEC §2](../docs/SPEC.md)。

## 分層

- OPNsense 顧**周邊 + DMZ + Suricata**（IDS 給 Studio、切 IPS 給 Arena）。
- Ludus 內部 router 顧**企業內部 VLAN**（user / server 段）。

## 內容

- `config/` — config.xml 匯出。⚠️ 可能含機敏，push 前審過（見 `.gitignore` 註解）。
- `suricata/` — Suricata 規則。

## 鐵律（要件 5 / 7）

- OPNsense↔Ludus 內網走**靜態路由、不 NAT**（避免雙層 NAT 抹掉來源 IP）。
- 每條南北向必過 OPNsense 鏡像、無繞過 Suricata 的路徑。
- config / 規則**帶外版控**——要件 7 精神在 Ludus 之外維持，別手動點忘。
- 攻擊段掛 OPNsense 一個獨立隔離介面（非真 WAN），「攻擊者在外、穿 OPNsense 進企業」。
