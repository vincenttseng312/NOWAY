# 實體關係模型（ERM）

RAG 關聯、儀表板聚合、問答實體解析的共用骨架，也是「Wazuh alert JSON → 文件/實體」的對映依據。

## 實體（節點）與最小欄位

| 實體 | id 前綴 | 最小欄位（放 entity 卡 `attributes`） |
|---|---|---|
| Host | `ent-host-` | hostname, ip, role, os, ad_joined, wazuh_agent_id `(env-specific)` |
| Account | `ent-acct-` | sam_account, domain, privilege_level, is_admin |
| IP | `ent-ip-` | address, zone(`internal`/`external`/`attacker`), reputation `(需外部查證)` |
| Event | `evt-` | event_id, source, meaning |
| Alert | `ent-alert-` | rule_id `(env-specific)`, level, timestamp, agent, technique |
| Rule | `ent-rule-` | rule_id `(env-specific)`, level, groups, description |
| Technique | `ent-tech-` | technique_id, tactic, name |
| Incident | `ent-inc-` | id, severity, status, related_alerts[], timeline[] |
| Scenario | `scn-` | 攻擊情境頁本身（14 段模板） |

## 關係（邊）

```
Alert    —triggered_by→  Rule
Rule     —maps_to→       Technique   —belongs_to→ Tactic
Alert    —derived_from→  Event
Event    —raised_on→     Host
Alert    —involves→      Account | IP
Host     —member_of→     Domain(AD)
Account  —had_logon_from→IP
Incident —aggregates→    Alert (1..n)
Scenario —detected_by→   Rule | Event(型樣)
```

在 entity 卡與各頁 frontmatter 用 `relationships: ["triggered_by:ent-rule-xxx", ...]` 表達。

## Wazuh alert JSON → 實體對映（關鍵）

一筆 alert 進來時，AI 依下列欄位解析實體並連到對應文件：

| Wazuh 欄位 | 對映實體 | 對映到的文件 |
|---|---|---|
| `agent.name` / `agent.ip` | Host | `entities/ent-host-*` |
| `data.win.eventdata.targetUserName` | Account | `entities/ent-acct-*` |
| `data.win.eventdata.ipAddress` | IP | `entities/ent-ip-*` |
| `data.win.system.eventID` | Event | `04-windows-ad-events/*` |
| `rule.id` `(env-specific)` / `rule.description` | Rule/Alert | `03-wazuh/wazuh-rules-and-levels` |
| `rule.mitre.id` | Technique | `07-mitre-attack/technique-cards/*` |
| `rule.groups` | Scenario 型樣 | `05-attack-scenarios/*` |

> 具體 `rule.id` 數字、`eventID` 對應的規則觸發，屬部署/ruleset 相關，AI 使用時標「需依實際環境確認」。

## 用途

- **問答**：從問題抽實體（主機/帳號/IP）→ 查 entity 卡 → 一跳鄰居擴充（相關 alert/technique）。
- **儀表板**：以實體為聚合維度（Top Host / Top IP / Top Account）。
- **報告**：Incident 聚合多個 Alert + timeline，套 report 模板。
