# ludus/

內層企業內網的 IaC。Ludus = Proxmox + Packer + Ansible 的自建取向框架。

- `blueprints/` — range YAML。Phase 0：DC + 1~2 端點。之後疊 GOAD 全森林 + DMZ。
- `roles/` — 自寫 Ansible role（現成 role 直接在 blueprint 引用，不落這裡）。

## 現成 role（直接用，不自寫）

| 元件 | role |
|---|---|
| GOAD 多域 AD 靶場 | 原生 blueprint |
| Wazuh server + agent | `aleemladha.wazuh_server_install` + `ludus_wazuh_agent` |
| CALDERA server + agent | `frack113.ludus_caldera_server` + agent |
| GHOSTS **server** | `frack113.ludus_ghosts_server` |

## 要自寫的

- `roles/ghosts_client/` — GHOSTS client 無現成 role，見該目錄 README。

## 不歸 Ludus 管的

OPNsense（最外層邊界閘道）**手動建、獨立於 Ludus**，見 `../opnsense/`。
Ludus 環境整個跑在 OPNsense 之後，Ludus 不控制它。
