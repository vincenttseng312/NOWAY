---
id: exp-wazuh-windows-threat-detection-rules
type: experiment
title: "Wazuh Windows／Sysmon 威脅偵測規則包"
topic: "下載、bind shell、帳號建立與 Administrators 提權偵測"
tags: [experiment, wazuh, sysmon, detection-engineering, windows]
status: completed
hypothesis: "將命令嘗試、成功稽核事件與高可信行為鏈分層，可在不誇大單一事件的前提下偵測 Windows 常見攻擊行為。"
result: partial
confidence: medium
verified_on_this_machine: true
code_paths: [code/2026-07-20/wazuh-windows-threat-detection-rules/windows-threat-detection-rules.xml, code/2026-07-20/wazuh-windows-threat-detection-rules/sysmon-lab-baseline.xml, code/2026-07-20/wazuh-windows-threat-detection-rules/agent-conf-snippet.xml]
sources: []
created: 2026-07-20
updated: 2026-07-20
related: [windows-event-log-and-sysmon, ioc-ttp-and-detection-engineering, detection-validation-range]
---

# 實驗：Wazuh Windows／Sysmon 威脅偵測規則包

## 1. 假設 Hypothesis

若規則明確區分「命令曾被執行」「Windows 記錄成功變更」「多個訊號形成高可信行為鏈」，就能避免把單一 Sysmon Event ID 1 誤寫成攻擊成功，同時提高 Wazuh 對常見 Windows 行為的可見度。

### 替代假設

若 Sysmon 未產生 Event ID 3／11、Windows Audit 未產生 4720／4732，或 Wazuh 解析欄位與預期不同，再完整的 XML 也不會命中。規則問題與 telemetry gap 必須分開驗證。

## 2. 實作 Implementation

建立 `code/2026-07-20/wazuh-windows-threat-detection-rules/`：

- `windows-threat-detection-rules.xml`：18 條規則，ID `110100–110144`。
- `sysmon-lab-baseline.xml`：全量 ProcessCreate、聚焦 NetworkConnect／DNS、使用者可寫路徑 FileCreate 與 ProcessTampering。
- `agent-conf-snippet.xml`：Sysmon、PowerShell 與 Security Event Channel 參考片段。
- `README.md`：部署、回復、證據分層及安全驗收。
- `manifest.json`：可重現資訊與驗證邊界。

規則涵蓋可疑下載、payload staging、bind shell listener／入站連線／shell child、帳號建立命令與 4720 成功、群組修改命令與 Administrators／Domain Admins 成功、清 log、服務、排程、編碼 PowerShell 與 Defender 削弱。

## 3. 驗證 Verification

| 編號 | 驗證內容 | 方法 | 結果 | 判定 |
|---|---|---|---|---|
| V1 | 三個 XML 是否 well-formed | PowerShell XML parser | 全部可解析 | 通過 |
| V2 | Rule ID 是否唯一且在 custom range | 解析全部 `<rule id>` | 18/18 唯一；110100–110144 | 通過 |
| V3 | manifest 是否有效 JSON | `ConvertFrom-Json` | 可解析 | 通過 |
| V4 | Wazuh 4.14.6 是否接受規則語法／PCRE2 | Manager `wazuh-analysisd -t` | 尚未執行 | 待驗證 |
| V5 | 指定行為是否命中預期 rule | SLIME／CELL／VENTI-DC 實機事件 | 尚未執行 | 待驗證 |
| V6 | 一週誤報量是否可接受 | 按 rule.id、agent、使用者建立 baseline | 尚未執行 | 待驗證 |

`verified_on_this_machine: true` 僅代表 XML、ID 與 JSON 靜態驗證。整體 result 為 `partial`，不得宣稱規則已在 Wazuh 載入或已偵測到真實攻擊。

## 4. 反思 Reflection

- Sysmon 預設安裝不啟用 Event ID 3，因此「事件很少」可能是 sensor config，不是 Wazuh 規則不足。
- `4720`、`4732`、`4728` 是成功事件；命令列規則只能標示 attempt。
- 可疑 listener 接收入站連線仍不等於 bind shell 已成功互動；listener 建立 shell child 並有相符 Event 3／PCAP 才是高可信鏈。
- 直接收集所有 NetworkConnect 會產生大量事件，因此 baseline 先限制到常見工具與使用者可寫路徑。
- 目前不啟用 Active Response；需先完成誤報 baseline、rollback 與授權流程。

## 5. Knowledge Ingestion

- Windows／Sysmon 遙測：[[windows-event-log-and-sysmon]]
- Detection Engineering：[[ioc-ttp-and-detection-engineering]]
- 四態驗證：[[detection-validation-range]]
- 專題規則模型：`projects/wazuh-ad-soc/06-detection-logic/correlation-rules.md`
- Code artifact：`code/2026-07-20/wazuh-windows-threat-detection-rules/`

## 6. Code Preservation

所有可執行設定均保存於 `code_paths`，README 記錄前置條件、部署、測試與回復。未直接修改 Manager 或 endpoint，也未保存 credential、內部金鑰或惡意 payload。

## 7. 後續問題 Next Questions

1. Manager 上 `wazuh-analysisd -t` 是否接受 18 條規則與 PCRE2？
2. SLIME／CELL 的實際 Sysmon config 是否產生 Event ID 3、11、22？
3. Security 事件進入 Wazuh 後，`targetSid`、`memberSid`、`targetUserName` 的實際欄位名稱是否一致？
4. 一週 baseline 中哪些合法 IT 流程需要 allow-list？
5. 新帳號 4720 與群組 4732 的 SID 欄位是否要用後端 correlation engine 正規化後再做同一帳號關聯？

