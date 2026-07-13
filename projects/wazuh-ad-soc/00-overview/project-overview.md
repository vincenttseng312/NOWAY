---
id: doc-project-overview
title: "專題總覽"
doc_type: overview
category: overview
summary: "本專題以 Wazuh 蒐集 AD 環境的 Windows／網路安全事件，串接生成式 AI 產出攻擊摘要、時間軸、風險分級、MITRE 對應與處置建議，並以儀表板與自然語言問答呈現。"
tags: [cat:overview, type:overview]
related_entities: [ent-host-win11-target, ent-host-dc, ent-host-wazuh-manager]
related_docs: [doc-scope-and-limitations, doc-system-architecture, doc-data-and-event-flow, doc-wazuh-role, doc-ai-role]
keywords: ["專題總覽", "Wazuh", "Active Directory", "生成式 AI", "資安監控", "SIEM", "SOC", "MITRE ATT&CK", "AD security monitoring"]
confidence: high
verification_status: verified
source_refs: ["Wazuh 官方文件", "Microsoft Windows Security Auditing 文件", "MITRE ATT&CK 官方網站"]
last_updated: 2026-07-09
---

# 專題總覽

## 1. 文件目的
提供本知識庫的最高層視角：專題要解決什麼問題、由哪些元件組成、資料如何流動、AI 扮演什麼角色。作為 RAG／聊天機器人回答「這個專題在做什麼」類問題的首選來源。

## 2. 背景說明
傳統 SOC 面對大量 Wazuh 告警與 Windows／AD 事件時，人工判讀成本高、關聯困難、報告耗時。本專題在一個**授權實驗室環境**中，讓 Wazuh 負責蒐集與初步告警，再由生成式 AI 依告警與日誌自動產出：
- 攻擊摘要、攻擊時間軸
- 風險分級、MITRE ATT&CK 對應
- 受影響主機／帳號／來源 IP
- 建議處置方式、儀表板資料
- 使用者自然語言問答

## 3. 與本專題的關聯
本頁是所有其他頁的入口。系統怎麼組成見 [[doc-system-architecture]]；資料如何從日誌走到 AI 見 [[doc-data-and-event-flow]]；各子系統的角色見 [[doc-wazuh-role]]、[[doc-ai-role]]、[[doc-dashboard-role]]、[[doc-qa-role]]；能做與不能做的界線見 [[doc-scope-and-limitations]]。

## 4. 主要實體
Host（Windows 11 靶機、AD DC、Wazuh Manager、路由器、攻擊者主機）、Account（AD 網域帳號）、IP（內部／外部／攻擊者網段）、Alert、Event、Rule、Technique、Incident。定義見 `_meta/entity-model.md`。

## 5. 可被 LLM 檢索的關鍵字
專題總覽、系統目標、Wazuh、AD 資安監控、生成式 AI 分析、SOC、SIEM、事件分析、attack summary、risk grading、MITRE mapping、natural language Q&A。

## 6. 相關文件連結
- [[doc-scope-and-limitations]]、[[doc-system-architecture]]、[[doc-network-topology]]、[[doc-host-roles]]、[[doc-data-and-event-flow]]
- 子系統角色：[[doc-wazuh-role]]、[[doc-ai-role]]、[[doc-dashboard-role]]、[[doc-qa-role]]

## 7. 後續可擴充內容
- 專題成員與分工、時程表（需依實際專題確認）。
- 成效指標（偵測涵蓋率、平均分析時間等），可連到 08-severity 與儀表板。
