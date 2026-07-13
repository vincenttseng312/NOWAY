---
id: ent-<type>-<slug>
title: ""
doc_type: entity
category: entity
entity_type:                # host | account | ip | rule | alert | technique | incident
summary: ""
tags: []                    # entity:*, ...
attributes: {}              # 依 entity-model 各實體最小欄位
relationships: []           # 如 ["member_of:domain-lab", "had_logon_from:ent-ip-x"]
related_docs: []
confidence: medium
verification_status: env-specific   # 主機/帳號/IP 多為部署相關
source_refs: []
keywords: []
last_updated: YYYY-MM-DD
---

# <實體名稱>

## 1. 實體概述
（這是什麼實體、在本專題環境中的角色。）

## 2. 屬性
（展開 frontmatter `attributes`；env-specific 值標註。）

## 3. 關係
（依 entity-model 的邊；連到相關 host/account/ip/alert/technique。）

## 4. 相關告警 / 事件
（此實體涉及的 alert / event 型樣。）

## 5. 在儀表板/問答中的用途
（作為聚合維度或實體解析目標。）

## 相關文件
