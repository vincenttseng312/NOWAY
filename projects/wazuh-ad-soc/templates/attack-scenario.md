---
id: scn-<slug>
title: ""
doc_type: attack-scenario
category: attack-scenario
summary: ""
tags: []                    # cat:attack-scenario, mitre-tactic:*, source:*, risk:*, status:*
related_entities: []
related_docs: []
mitre_attack: []            # technique id, 如 t1110；不確定不臆造
wazuh_sources: []           # rule.groups / decoder；數字 rule.id 標 env-specific
windows_event_ids: []       # 逐項可帶「(需確認)」
risk_level:                 # info|low|medium|high|critical
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件", "Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
keywords: []                # 中英
last_updated: YYYY-MM-DD
---

# <頁面標題>

## 1. 情境說明
（防禦視角描述此情境是什麼、在本專題環境如何發生。**不含可武器化指令**。）

## 2. 攻擊者可能目標
（想達成什麼：探測、取得憑證、提權、橫向移動…）

## 3. 防禦方可觀測跡象
（在靶機/DC/網路上會留下哪些可觀測痕跡。）

## 4. 可能出現的 Windows / AD 事件
| Event ID | 意義 | 驗證 |
|---|---|---|
| | | verified / 需確認 |

## 5. 可能出現的 Wazuh 告警欄位
（`rule.description`、`rule.groups`、`rule.mitre.*`、相關 `data.win.*`。數字 rule.id 標 env-specific。）

## 6. MITRE ATT&CK 對應
| Tactic | Technique | ID | 備註 |
|---|---|---|---|

## 7. 風險等級判斷
（依 08-severity 判準；單一 vs 關聯後的等級差異。）

## 8. AI 分析重點
（AI 應抽哪些欄位、關聯哪些實體、注意哪些前後關係。）

## 9. 儀表板呈現方式
（對應 10-dashboard 的哪個元件、用哪些欄位。）

## 10. 使用者可能詢問的問題
（連到 11-qa-chatbot 對應 intent。）

## 11. AI 回答範例
（一段示範回答；含不確定性標註。）

## 12. 建議處置方式
（偵測後的防禦/回應建議，連到 12-incident-response。）

## 13. 誤判可能性
（正常業務/管理行為造成的 false positive 情境。）

## 14. 需要進一步確認的資料
（哪些 event id / rule / 門檻需依實際環境或官方文件確認。）

## 相關文件
## 建議查證來源
## 可被檢索的關鍵字（中英）
