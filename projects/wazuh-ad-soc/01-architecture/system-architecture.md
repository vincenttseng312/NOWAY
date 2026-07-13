---
id: doc-system-architecture
title: "系統架構"
doc_type: architecture
category: architecture
summary: "本專題由蒐集層（Wazuh Agent/Manager）、分析層（生成式 AI + RAG 知識庫）、呈現層（儀表板 + 問答）三層組成，資料自 Windows/AD 事件流向 AI 再流向使用者介面。"
tags: [cat:overview, type:architecture]
related_entities: [ent-host-win11-target, ent-host-dc, ent-host-wazuh-manager]
related_docs: [doc-network-topology, doc-host-roles, doc-data-and-event-flow, doc-wazuh-role, doc-ai-role]
keywords: ["系統架構", "三層架構", "蒐集層", "分析層", "呈現層", "Wazuh", "LLM", "RAG", "system architecture", "pipeline"]
confidence: medium
verification_status: needs-verification
source_refs: ["Wazuh 官方文件"]
last_updated: 2026-07-09
---

# 系統架構

## 1. 文件目的
描述整體系統的分層與元件關係，作為理解資料流、主機角色與各子系統的骨架。

## 2. 背景說明
系統分三層：

```
[ 蒐集層 ]        [ 分析層 ]              [ 呈現層 ]
Windows 11 靶機    生成式 AI (LLM)         儀表板
  └ Wazuh Agent     ├ 輸入: Wazuh 告警      ├ SOC 首頁/卡片/時間軸
AD DC 事件          ├ 輸入: RAG 知識庫       └ Top IP/主機/帳號/MITRE
      │             └ 輸出: 摘要/時間軸/    使用者問答 (chatbot)
      ▼                    風險/MITRE/處置       └ 自然語言 → intent → 檢索
Wazuh Manager  ──────────►                    ◄──────────
 (decoder + rule → alert JSON)
```

- **蒐集層**：Agent 採 Windows/AD 事件 → Manager 解碼比對規則 → 產生 alert JSON。見 [[doc-wazuh-role]]。
- **分析層**：AI 以 alert + 本 KB（RAG）為輸入產出分析。見 [[doc-ai-role]]。
- **呈現層**：儀表板（[[doc-dashboard-role]]）與問答（[[doc-qa-role]]）。

## 3. 與本專題的關聯
本頁是架構總覽；網段與隔離見 [[doc-network-topology]]；每台主機職責見 [[doc-host-roles]]；資料如何逐段流動見 [[doc-data-and-event-flow]]。

## 4. 主要實體
Host（靶機、DC、Wazuh Manager、路由器、攻擊者主機）、Alert、Event、Rule、Technique。

## 5. 可被 LLM 檢索的關鍵字
系統架構、三層、蒐集/分析/呈現、pipeline、Wazuh Manager、LLM、RAG、SOC 架構。

## 6. 相關文件連結
- [[doc-network-topology]]、[[doc-host-roles]]、[[doc-data-and-event-flow]]
- [[doc-wazuh-role]]、[[doc-ai-role]]、[[doc-dashboard-role]]、[[doc-qa-role]]

## 7. 後續可擴充內容
- 各元件的部署方式（容器/VM）、版本與資源需求（需依實際環境確認）。
- 高可用/擴充性考量、資料保存策略。
