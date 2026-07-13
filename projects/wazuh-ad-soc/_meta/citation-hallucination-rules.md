# 引用與防幻覺規則（本 KB 的命脈）

本檔規範 AI 在使用本知識庫回答時，如何引用、如何標註不確定、以及**絕不可編造什麼**。SCHEMA.md 第 2 節指向本檔。

## 1. 絕不編造清單

以下若無明確依據，**一律不得臆造具體值**，改標「（需依實際環境確認）」或「（需依官方文件確認）」：

- Wazuh **數字 `rule.id`**（如「規則 60122」）——ruleset 版本／部署相關。
- Wazuh `rule.level` 的**具體門檻對應**、decoder 名稱、group 名稱的完整清單。
- **Windows Event ID** 與其精確語意——除非屬業界穩定且高把握（見第 3 節白名單），否則標「需依 Microsoft 官方文件確認」。
- **MITRE technique id**——不確定就不寫 id，只描述行為並標「需查 MITRE 官方確認對應」。
- Wazuh／Windows／AD 的**產品功能、設定項、欄位是否存在**。

## 2. verification_status 語意

| 值 | 意義 | AI 回答時的義務 |
|---|---|---|
| `verified` | 業界穩定、可自信陳述 | 正常引用，附 source_refs |
| `needs-verification` | 合理但未經本專案環境確認 | 回答須顯式加註「需查證」 |
| `env-specific` | 值隨部署/ruleset 改變（rule.id、門檻） | 回答須說「以你的實際環境為準」，不給死值 |

## 3. 業界穩定白名單（可自信陳述，仍附 source_refs）

- **常見 Windows Security Event ID**：4624（登入成功）、4625（登入失敗）、4634/4647（登出）、4648（明確憑證登入）、4672（特殊權限）、4688（程序建立）、4720（建立帳號）、4722/4725（啟用/停用帳號）、4728/4732/4756（加入群組）、4740（帳號鎖定）、1102（稽核日誌被清除）。**RDP、防火牆、PowerShell 4104 等的精確 ID/type 需個別確認**。
- **MITRE 戰術名**與常見技術（T1110 Brute Force、T1059.001 PowerShell、T1078 Valid Accounts、T1136 Create Account、T1098 Account Manipulation、T1021.001 RDP、T1046 Network Service Discovery、T1562 Impair Defenses、T1105 Ingress Tool Transfer）。
- **Wazuh alert JSON 欄位路徑**（`rule.id`、`rule.level`、`rule.mitre.*`、`agent.name`、`data.win.system.eventID`、`data.win.eventdata.*` 等）——欄位存在性穩定；欄位內的**值**仍視情況標註。

> 白名單 = 「可陳述事實」，不等於「免附來源」。仍在 `source_refs` 標建議查證來源。

## 4. 固定建議查證來源

```
- Wazuh 官方文件
- Microsoft Windows Security Auditing 文件
- MITRE ATT&CK 官方網站
```

## 5. 資料不足時的回答方式

1. 明說缺什麼（缺即時 Wazuh 資料連線 / 缺該事件在本 KB 的頁 / 需環境確認）。
2. 只回 KB 能支持的一般性內容，並標明界線。
3. 提出「要補齊此答案需要哪些資料/欄位」。
4. **不要**用看似精確的假值填補（假 rule.id、假統計數字、假 IP）。

## 6. 引用格式（回答中）

- 引用 KB 頁：標頁 `title` 或 slug（對應 `related_docs`）。
- 陳述事件/技術事實：附「（來源：Microsoft/MITRE 官方，建議查證）」。
- 陳述 env-specific 值：附「（需依實際環境確認）」。
