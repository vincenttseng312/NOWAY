# 標籤 Taxonomy（命名規則與登記表）

命名空間化標籤，避免標籤爆炸。規則：全小寫、連字號、每頁 ≤ 8 個、新標籤先登記於本檔。

## 命名空間

| 命名空間 | 意義 | 範例 |
|---|---|---|
| `cat:` | 內容分類 | `cat:attack-scenario`、`cat:wazuh`、`cat:event`、`cat:dashboard`、`cat:qa` |
| `type:` | 文件型別（= doc_type） | `type:detection`、`type:report`、`type:entity` |
| `entity:` | 涉及實體型別 | `entity:host`、`entity:account`、`entity:ip`、`entity:rule`、`entity:technique` |
| `source:` | 日誌/告警來源 | `source:windows-security`、`source:sysmon`、`source:powershell`、`source:terminal-services`、`source:wazuh-rule`、`source:ad` |
| `mitre-tactic:` | ATT&CK 戰術 | `mitre-tactic:credential-access`、`mitre-tactic:lateral-movement`、`mitre-tactic:privilege-escalation`、`mitre-tactic:defense-evasion`、`mitre-tactic:discovery`、`mitre-tactic:persistence`、`mitre-tactic:execution`、`mitre-tactic:initial-access` |
| `mitre-technique:` | ATT&CK 技術（id 小寫連字號） | `mitre-technique:t1110`、`mitre-technique:t1059-001`、`mitre-technique:t1078`、`mitre-technique:t1021-001` |
| `risk:` | 風險等級 | `risk:info`、`risk:low`、`risk:medium`、`risk:high`、`risk:critical` |
| `status:` | 可信度/驗證 | `status:verified`、`status:needs-verification`、`status:env-specific` |

## 已登記標籤

（隨內容生成增補。初始只列命名空間；實際採用的值在此追加，附一行說明，保持精簡有紀律。）

- `cat:*`、`type:*` — 依 SCHEMA 第 3 節 doc_type 對應。
- `source:wazuh-rule` — 內容涉及 Wazuh 規則觸發。
- `status:env-specific` — 內容含部署相關值（rule.id、門檻），必須經環境確認。

## MITRE 戰術對照（本專題常用，穩定值，仍以官方為準）

initial-access / execution / persistence / privilege-escalation / defense-evasion / credential-access / discovery / lateral-movement / command-and-control / impact。技術 id 見各 technique 卡與攻擊情境頁 frontmatter；**不在此臆造未確認的 technique id**。

> 建議查證來源：MITRE ATT&CK 官方網站。
