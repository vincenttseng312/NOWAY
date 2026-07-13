# 問題 → 文件分類 Routing 規則

聊天機器人收到自然語言問題後，先分類 `intent`，再依下表 route 到候選文件分類做檢索。每個 `11-qa-chatbot/` 問答條目的 frontmatter 都帶 `intent`。

## Intent 分類（8 類）

| intent | 使用者問法（例） | route 目標分類 | 主要 Wazuh 欄位 |
|---|---|---|---|
| `triage-priority` | 今天有哪些高風險事件？哪些主機要優先調查？ | 08-severity + 即時 alert 聚合 | `rule.level`, `timestamp` |
| `entity-ranking` | 哪台主機被攻擊最多？哪個 IP 最可疑？比較兩個 IP | entities + 聚合查詢 | `agent.name`, `data.win.eventdata.ipAddress` |
| `timeline` | 最近一小時攻擊？整理攻擊時間軸 | 01-architecture/data-flow + alert 時序 | `timestamp`, `rule.mitre.tactic` |
| `alert-explain` | 這筆 Alert 是什麼意思？對應哪個 ATT&CK？ | 03-wazuh + 07-mitre | `rule.id`(env), `rule.description`, `rule.mitre.*` |
| `account-anomaly` | 這帳號異常登入？有暴力破解？失敗後成功？ | 04-events + 05-scenarios | `targetUserName`, `eventID`, `ipAddress` |
| `report-gen` | 給我事件摘要/完整報告/Demo 整理 | 12-report-templates | 依報告模板 required_inputs |
| `remediation` | 處置建議？這會是誤判嗎？ | 05-scenarios（處置/誤判段）+ 12-sop | — |
| `audience-adapt` | 用主管看得懂/用資安人員看得懂的方式 | 12-report（manager/analyst 版） | 同資料，換模板 |

## Routing 流程

```
問題 → 抽實體(主機/帳號/IP/時間範圍) + 分類 intent
     → 依上表選候選分類 → 讀 index.md 選候選頁 → 讀候選頁
     → 用 entity-model 做一跳鄰居擴充
     → 組答案（套對應 answer template / report template）
     → 附引用(related_docs) 與不確定性標註
```

## Fallback（資料不足或無對應）

- 無對應 intent → 回到 `index.md` 一行摘要做語意比對；仍無 → 明說「本知識庫尚未涵蓋」，不臆造。
- 需要即時 Wazuh 資料但無資料連線 → 說明「需連線實際 Wazuh 資料源確認」，只回可從 KB 得到的一般性說明。
- 詳見 `citation-hallucination-rules.md`。
