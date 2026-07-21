---
type: source
title: "Threat Hunting Essential: Attack Recognition Techniques"
authors: ["劉昱甫"]
url: ""
raw: "raw/附件6-1、校內威脅獵捕課程期中報告.pdf"
ingested: 2026-07-20
tags: [wazuh, opnsense, suricata, sysmon, threat-hunting]
entities: []
concepts: [detection-validation-range, soc-lab-segmentation-and-telemetry, windows-event-log-and-sysmon]
created: 2026-07-20
updated: 2026-07-20
---

# Threat Hunting Essential 期中報告摘要

這份 24 頁課程報告記錄一個由 Proxmox、Wazuh、OPNsense／Suricata、Windows 10、Kali、WireGuard 與 AI Server 組成的威脅獵捕實驗環境。作者歸屬依期末報告封面與參考文獻交叉確認；PDF 內嵌 metadata 不足以單獨判定版本先後。

## 實作主線

1. 將端點與網路流量導向 OPNsense／Suricata，並把邊界告警送入 Wazuh。
2. 以外部 rule server 維護自訂 Suricata 規則，再由 OPNsense 更新規則內容。
3. 在 Windows 啟用 Sysmon 與指定 Event Channel，建立 Wazuh 本機規則觀察程序、登入、RDP 與 PowerShell 活動。
4. 建立 MCP server，嘗試讓本地 LLM 讀取 Wazuh／Indexer 資料並回答事件問題。

## 報告展示的防禦訊號

- 網路面：掃描、SSH、遠端控制軟體與其他 Suricata 命中。
- 身分面：連續登入失敗與 RDP 相關事件。
- 端點面：Sysmon Process Create 與指定程序的 Wazuh 告警。
- 腳本面：PowerShell Script Block Logging 與下載工具字串的觀察。

這些畫面可證明若干「事件產生 → sensor／agent → Wazuh 呈現」路徑曾成功，但不足以證明規則的 recall、false positive、時間關聯完整性或跨版本可重現性。環境特定的 Wazuh 數字 `rule.id` 不應複製為通用知識。

## Sysmon 與 Windows Audit 的學習點

報告採用只針對單一程序的窄化 Sysmon 設定，適合驗證管線是否通，但不能代表完整 production baseline。正式驗收至少要同時記錄：實際 XML config、Sysmon 版本、Event Channel 訂閱、產生事件的方法、原始 EVTX、Wazuh alert JSON 與跨系統時間差。相關方法整合於 [[windows-event-log-and-sysmon]]。

## AI／MCP 初期結果

報告中的本地模型能讀取部分資料，但曾出現答非所問、工具使用失敗與誤解 prompt。為了讓 Indexer 可被 MCP 存取而改變 listener 綁定，也會擴大暴露面；後續必須以網段 allow-list、強認證、最小權限與 audit log 約束，不能把「可連上」當成「可安全上線」。

## 證據限制與敏感資料

- 多數結果是截圖與文字敘述，未附 raw PCAP、EVTX、alert JSON、規則版本或重跑腳本。
- 歷史 IP、帳號、憑證與密碼不得轉錄為目前環境設定，也不應進入公開 Git。
- 報告展示時間與 PDF metadata 可能不一致；版本演進應以內容差異和明確日期為準。

## 在知識庫中的位置

- 靶場方法：[[detection-validation-range]]
- 架構邊界：[[soc-lab-segmentation-and-telemetry]]
- Windows 遙測：[[windows-event-log-and-sysmon]]
- 跨來源演進：[[threat-hunting-course-to-detection-range-evolution]]
- H-I-V-R-K-C：[[threat-hunting-range-evolution-review]]

