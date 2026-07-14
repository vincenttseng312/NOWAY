# 知識庫索引（RAG router 第一站）

本檔是全 KB 的一行摘要目錄。AI 回答前先讀本檔選候選頁，再讀候選頁。`⏳` = 尚未生成（依 SCHEMA 第 9 節分批）。

> **KB 狀態：批 0–7 全數完成（8 批）+ 02-environment 補齊。** 上線兩個關鍵檔：[system-prompt](09-ai-analysis/system-prompt.md)（複製作 AI 助手系統提示詞）+ [rag-integration-spec](09-ai-analysis/rag-integration-spec.md)（RAG/介接設定）。唯一可選後續：填 `entities/` 的 host/account/ip 實體卡（frontmatter 已引用、頁面待建；建議接上真實環境值後再建）。

---

## 規格層 _meta/
- [rag-metadata-schema](_meta/rag-metadata-schema.md) — frontmatter/metadata 權威定義
- [taxonomy](_meta/taxonomy.md) — 標籤命名規則與登記表
- [entity-model](_meta/entity-model.md) — 實體關係模型（Host/User/IP/Alert/Event/Rule/Technique/Incident）
- [routing-rules](_meta/routing-rules.md) — 使用者問題 → 文件分類 routing
- [citation-hallucination-rules](_meta/citation-hallucination-rules.md) — 引用與防幻覺規則

## 00 總覽
- [project-overview](00-overview/project-overview.md) — 專題總覽：目標、元件、AI 角色
- [scope-and-limitations](00-overview/scope-and-limitations.md) — 範圍與限制（授權/防禦/反幻覺）
- [wazuh-role](00-overview/wazuh-role.md) — Wazuh 的角色：資料蒐集 + 初步偵測
- [ai-role](00-overview/ai-role.md) — 生成式 AI 的角色：分析與敘事層
- [dashboard-role](00-overview/dashboard-role.md) — 儀表板的角色：呈現層
- [qa-role](00-overview/qa-role.md) — 問答系統的角色：自然語言互動層

## 01 系統架構
- [system-architecture](01-architecture/system-architecture.md) — 三層架構（蒐集/分析/呈現）
- [network-topology](01-architecture/network-topology.md) — 內外網段與路由器隔離（值 env-specific）
- [host-roles](01-architecture/host-roles.md) — 五類主機職責
- [data-and-event-flow](01-architecture/data-and-event-flow.md) — 事件五段流程（產生→採集→告警→AI→呈現）

## 02 環境
- [ad-environment](02-environment/ad-environment.md) — AD 網域環境、稽核政策前提、Wazuh 監控 AD（含官方查證）
- [windows11-target](02-environment/windows11-target.md) — Win11 靶機、Agent eventchannel 採集、Script Block Logging 前提
- [host-inventory](02-environment/host-inventory.md) — 五台主機清單與屬性（值 env-specific，實體卡待建）

## 03 Wazuh
- [wazuh-architecture](03-wazuh/wazuh-architecture.md) — 四大元件（Agent/Manager/Indexer/Dashboard）
- [wazuh-agent](03-wazuh/wazuh-agent.md) — 端點採集（Windows eventchannel）
- [wazuh-manager](03-wazuh/wazuh-manager.md) — decoder + rule → alert
- [wazuh-alert-structure](03-wazuh/wazuh-alert-structure.md) — alert JSON 18 欄位分組
- [wazuh-rules-and-levels](03-wazuh/wazuh-rules-and-levels.md) — rule / level（0–15，門檻 env-specific）
- [wazuh-dashboard](03-wazuh/wazuh-dashboard.md) — 內建 Dashboard vs 自訂 SOC 儀表板
- [windows-events-into-wazuh](03-wazuh/windows-events-into-wazuh.md) — Windows 事件進入路徑與稽核政策前提
- [wazuh-field-to-ai-mapping](03-wazuh/wazuh-field-to-ai-mapping.md) — ⭐ 18 欄位 ↔ AI 分析對照表
- [alert-to-report-pipeline](03-wazuh/alert-to-report-pipeline.md) — alert → Incident → 報告的 7 步流程
- [wazuh-mitre-linkage](03-wazuh/wazuh-mitre-linkage.md) — rule.mitre.* 與 ATT&CK 對應

## 04 Windows/AD 事件
- [windows-security-event-overview](04-windows-ad-events/windows-security-event-overview.md) — Security 日誌與常見 Event ID 家族、Logon Type
- [ad-security-event-overview](04-windows-ad-events/ad-security-event-overview.md) — AD/DC 事件家族（Kerberos/目錄變更標需確認）
- [logon-success](04-windows-ad-events/logon-success.md) — 4624 登入成功（T1078）
- [logon-failure](04-windows-ad-events/logon-failure.md) — 4625 登入失敗（T1110，SubStatus 需確認）
- [account-lockout](04-windows-ad-events/account-lockout.md) — 4740 帳號鎖定
- [user-creation](04-windows-ad-events/user-creation.md) — 4720 新增使用者（T1136）
- [group-membership-change](04-windows-ad-events/group-membership-change.md) — 4728/4732/4756 加入群組（T1098）
- [admin-group-change](04-windows-ad-events/admin-group-change.md) — 特權群組異動（高風險，T1098）
- [powershell-suspicious](04-windows-ad-events/powershell-suspicious.md) — 4104/4688 可疑 PowerShell（T1059.001）
- [rdp-logon](04-windows-ad-events/rdp-logon.md) — RDP（LogonType 10；TerminalServices ID 需確認，T1021.001）
- [security-config-change](04-windows-ad-events/security-config-change.md) — 防火牆/防護/日誌變更（T1562，防火牆 ID 需確認）
- [account-anomaly-detection](04-windows-ad-events/account-anomaly-detection.md) — 帳號異常判斷方法論（關聯與基準偏離）

## 05 攻擊情境（14，固定 14 段模板，防禦視角）
- [port-scan](05-attack-scenarios/port-scan.md) — 連接埠掃描（T1046/T1595）
- [rdp-bruteforce](05-attack-scenarios/rdp-bruteforce.md) — RDP 暴力破解（T1110/T1021.001）
- [mass-logon-failure](05-attack-scenarios/mass-logon-failure.md) — 大量登入失敗/密碼噴灑（T1110）
- [failed-then-success-logon](05-attack-scenarios/failed-then-success-logon.md) — 失敗後成功（關聯，T1110→T1078）
- [suspicious-powershell](05-attack-scenarios/suspicious-powershell.md) — 可疑 PowerShell（T1059.001）
- [local-user-creation](05-attack-scenarios/local-user-creation.md) — 新增本機使用者（T1136.001）
- [add-to-administrators](05-attack-scenarios/add-to-administrators.md) — 加入 Administrators（T1098）
- [firewall-modification](05-attack-scenarios/firewall-modification.md) — 防火牆修改（T1562.004）
- [security-tool-disable](05-attack-scenarios/security-tool-disable.md) — 停用防護/清日誌（T1562.001/T1070）
- [ad-abnormal-logon](05-attack-scenarios/ad-abnormal-logon.md) — AD 帳號異常登入（T1078.002）
- [privilege-escalation-signs](05-attack-scenarios/privilege-escalation-signs.md) — 權限提升跡象（T1098/T1078/T1548）
- [lateral-movement-signs](05-attack-scenarios/lateral-movement-signs.md) — 橫向移動跡象（T1021/T1570）
- [malicious-file-execution](05-attack-scenarios/malicious-file-execution.md) — 惡意檔案下載/執行（T1204/T1105）
- [suspicious-external-connection](05-attack-scenarios/suspicious-external-connection.md) — 可疑外部連線/C2（T1071/T1571）

## 06 偵測邏輯
- [detection-logic-overview](06-detection-logic/detection-logic-overview.md) — 單點規則 vs 關聯偵測、品質原則
- [correlation-rules](06-detection-logic/correlation-rules.md) — 5 條跨事件關聯型樣（C1–C5，門檻 env-specific）

## 07 MITRE ATT&CK
- [mitre-mapping-overview](07-mitre-attack/mitre-mapping-overview.md) — 情境↔戰術↔技術對應樞紐
- technique-cards/（14 張）：[t1046](07-mitre-attack/technique-cards/t1046.md)·[t1110](07-mitre-attack/technique-cards/t1110.md)·[t1021](07-mitre-attack/technique-cards/t1021.md)·[t1078](07-mitre-attack/technique-cards/t1078.md)·[t1059-001](07-mitre-attack/technique-cards/t1059-001.md)·[t1136](07-mitre-attack/technique-cards/t1136.md)·[t1098](07-mitre-attack/technique-cards/t1098.md)·[t1562](07-mitre-attack/technique-cards/t1562.md)·[t1070](07-mitre-attack/technique-cards/t1070.md)·[t1548](07-mitre-attack/technique-cards/t1548.md)·[t1204](07-mitre-attack/technique-cards/t1204.md)·[t1105](07-mitre-attack/technique-cards/t1105.md)·[t1071](07-mitre-attack/technique-cards/t1071.md)·[t1570](07-mitre-attack/technique-cards/t1570.md)

## 08 嚴重性分級
- [severity-classification](08-severity-risk/severity-classification.md) — info/low/medium/high/critical 五級（基礎分+升降因子，門檻 env-specific）

## 09 AI 分析與 RAG
- [ai-analysis-pipeline](09-ai-analysis/ai-analysis-pipeline.md) — 告警→實體→關聯→分級→MITRE→產出
- [rag-knowledge-base-design](09-ai-analysis/rag-knowledge-base-design.md) — chunking/metadata/routing/防幻覺
- [rag-integration-spec](09-ai-analysis/rag-integration-spec.md) — ⭐ 完整整合規格（14 項，含 alert/dashboard/chatbot 介接）
- [system-prompt](09-ai-analysis/system-prompt.md) — ⭐ 最終「資安事件分析助理」system prompt（可直接複製上線）

## 10 儀表板（18，套 dashboard-widget 模板）
- [dashboard-overview](10-dashboard/dashboard-overview.md) — 元件地圖與資料分工
- [soc-home](10-dashboard/soc-home.md) — 著陸頁版面
- [high-risk-events-card](10-dashboard/high-risk-events-card.md) — 高風險即時卡片
- [attack-timeline](10-dashboard/attack-timeline.md) — 攻擊時間軸（依戰術著色）
- [top-source-ips](10-dashboard/top-source-ips.md) — Top 來源 IP
- [top-targeted-hosts](10-dashboard/top-targeted-hosts.md) — Top 被攻擊主機
- [top-affected-accounts](10-dashboard/top-affected-accounts.md) — Top 受影響帳號
- [mitre-distribution](10-dashboard/mitre-distribution.md) — MITRE 戰術/技術分布
- [severity-distribution](10-dashboard/severity-distribution.md) — 嚴重性分布
- [logon-failure-trend](10-dashboard/logon-failure-trend.md) — 登入失敗趨勢
- [rdp-attack-monitor](10-dashboard/rdp-attack-monitor.md) — RDP 攻擊監控
- [powershell-activity](10-dashboard/powershell-activity.md) — PowerShell 可疑活動
- [ad-account-change-monitor](10-dashboard/ad-account-change-monitor.md) — AD 帳號異動監控
- [event-detail-view](10-dashboard/event-detail-view.md) — 單一事件詳細（防幻覺對照點）
- [ai-summary-block](10-dashboard/ai-summary-block.md) — AI 事件摘要區塊（主管/技術版）
- [ai-remediation-block](10-dashboard/ai-remediation-block.md) — AI 建議處置區塊
- [qa-interface](10-dashboard/qa-interface.md) — 使用者問答介面
- [demo-dashboard](10-dashboard/demo-dashboard.md) — Demo 展示版面

## 11 使用者問答（20，套 qa-entry 模板，帶 intent）
- triage-priority：[high-risk-today](11-qa-chatbot/high-risk-today.md)、[priority-hosts](11-qa-chatbot/priority-hosts.md)
- timeline：[recent-attacks](11-qa-chatbot/recent-attacks.md)、[attack-timeline](11-qa-chatbot/attack-timeline.md)
- entity-ranking：[top-attacked-host](11-qa-chatbot/top-attacked-host.md)、[most-suspicious-ip](11-qa-chatbot/most-suspicious-ip.md)、[compare-ips](11-qa-chatbot/compare-ips.md)、[common-attack-types](11-qa-chatbot/common-attack-types.md)
- account-anomaly：[abnormal-account](11-qa-chatbot/abnormal-account.md)、[bruteforce-signs](11-qa-chatbot/bruteforce-signs.md)、[failed-then-success](11-qa-chatbot/failed-then-success.md)
- alert-explain：[explain-alert](11-qa-chatbot/explain-alert.md)、[mitre-mapping](11-qa-chatbot/mitre-mapping.md)
- report-gen：[event-summary](11-qa-chatbot/event-summary.md)、[full-report](11-qa-chatbot/full-report.md)、[demo-summary](11-qa-chatbot/demo-summary.md)
- remediation：[remediation-advice](11-qa-chatbot/remediation-advice.md)、[false-positive](11-qa-chatbot/false-positive.md)
- audience-adapt：[explain-for-manager](11-qa-chatbot/explain-for-manager.md)、[explain-for-analyst](11-qa-chatbot/explain-for-analyst.md)

## 12 事件回應
- [ir-sop](12-incident-response/ir-sop.md) — 事件回應六階段 SOP（準備→偵測→控制→根除→復原→檢討）
- report-templates/（10 份，套 report 模板，可作 LLM 回答模板）：
  - [single-alert-summary](12-incident-response/report-templates/single-alert-summary.md) / [multi-alert-aggregate](12-incident-response/report-templates/multi-alert-aggregate.md) / [attack-timeline-report](12-incident-response/report-templates/attack-timeline-report.md)
  - 情境專用：[rdp-bruteforce-report](12-incident-response/report-templates/rdp-bruteforce-report.md) / [powershell-incident-report](12-incident-response/report-templates/powershell-incident-report.md) / [ad-account-anomaly-report](12-incident-response/report-templates/ad-account-anomaly-report.md) / [host-compromise-report](12-incident-response/report-templates/host-compromise-report.md)
  - 對象分版：[manager-summary](12-incident-response/report-templates/manager-summary.md)（主管） / [analyst-report](12-incident-response/report-templates/analyst-report.md)（技術） / [demo-report](12-incident-response/report-templates/demo-report.md)（Demo）

## 13 Demo
- [demo-script](13-demo/demo-script.md) — RDP 暴力破解鏈的 Demo 劇本（攻擊面↔系統反應對照）

## templates/
- [attack-scenario](templates/attack-scenario.md) / [qa-entry](templates/qa-entry.md) / [event](templates/event.md) / [entity-card](templates/entity-card.md) / [dashboard-widget](templates/dashboard-widget.md) / [report-template](templates/report-template.md)

## 跨連結（父層既有 DFIR 概念群，引用不複製）
- `[[windows-event-log-and-sysmon]]`、`[[persistence-mechanisms]]`、`[[lolbin-and-powershell-abuse]]`、`[[ioc-ttp-and-detection-engineering]]`、`[[process-hollowing]]`、`[[dynamic-behavior-analysis]]`（位於 `../../wiki/concepts/`）
