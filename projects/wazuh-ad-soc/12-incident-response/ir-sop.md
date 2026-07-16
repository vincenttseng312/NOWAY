---
id: doc-ir-sop
title: "事件回應 SOP"
doc_type: sop
category: incident-response
summary: "本專題的事件回應標準流程：準備→偵測與分級→控制→根除→復原→檢討六階段。是各情境頁「處置」段與 AI 建議處置的統整依據，屬防禦性流程，具體授權與工具依環境。"
tags: [cat:sop, type:sop, cat:incident-response]
related_entities: [ent-incident]
related_docs: [doc-severity-classification, doc-alert-to-report-pipeline, dsh-ai-remediation-block]
mitre_attack: []
wazuh_sources: []
windows_event_ids: []
risk_level: ""
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
keywords: ["事件回應", "SOP", "incident response", "containment", "eradication", "六階段"]
last_updated: 2026-07-09
---

# 事件回應 SOP

本專題的事件回應標準流程。各情境頁的「建議處置」與 [[dsh-ai-remediation-block]] 都應對齊本 SOP。**屬防禦性流程；實際授權、工具、聯絡窗口為 env-specific。**

## 六階段

### 1. 準備（Preparation）
確保 Wazuh 採集正常、稽核政策已開、快照/基準已建、聯絡窗口與授權界線明確。

### 2. 偵測與分級（Detection & Triage）
- 從告警/儀表板/問答發現事件。
- 依 [[doc-severity-classification]] 分級（基礎分 + 升降因子）。
- 用 [[doc-correlation-rules]] 判斷是否為關聯鏈（如暴力破解成功、提權鏈）。
- 保全證據：記錄告警、full_log、時間、涉及實體（避免被清日誌 1102 破壞）。

### 3. 控制（Containment）
- 隔離受影響主機（限制其網路，依環境）。
- 封鎖可疑外部來源 IP（依環境）。
- 凍結/停用被濫用或新建的帳號。
- **先保全 volatile 證據再動作**（若事件仍在進行）。

### 4. 根除（Eradication）
- 移除持久化（新建帳號、Run key、排程、服務等，見 [[persistence-mechanisms]]）。
- 清除 dropped 檔案/惡意程式。
- 還原被削弱的防禦（防火牆/防護/稽核）。

### 5. 復原（Recovery）
- 重設受影響帳號憑證。
- 驗證主機乾淨後回復服務；必要時由快照/重灌還原（若完整性無法信任）。
- 加強監控該主機/帳號一段時間。

### 6. 檢討（Lessons Learned）
- 回饋偵測規則（調門檻、補關聯規則，見 [[ioc-ttp-and-detection-engineering]]）。
- 更新 IOC、撰寫報告（見 12-report-templates）。
- 記錄時間線與處置成效。

## 分流：依風險決定急迫性
critical（如破解成功+提權）→ 立即進入控制；high → 儘速調查；medium/low → 排程調查與觀察。分級見 [[doc-severity-classification]]。

## 需依實際環境確認
隔離/封鎖的實際手段與權限、聯絡窗口、法遵/通報義務、快照/重灌政策。

## 相關文件
[[doc-severity-classification]]、[[doc-alert-to-report-pipeline]]、[[dsh-ai-remediation-block]]；跨連父層 [[persistence-mechanisms]]、[[ioc-ttp-and-detection-engineering]]。

## 建議查證來源
Wazuh 官方文件；事件回應方法論可另參考業界框架（如 NIST IR 生命週期，需自行查證）。

## 可被檢索的關鍵字（中英）
事件回應、SOP、incident response、containment、eradication、recovery、六階段。
