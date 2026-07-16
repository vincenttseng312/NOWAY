---
type: source
title: "AD CS 實驗室聚焦官方文件研究"
tags: [active-directory, adcs, wazuh, opnsense, windows, methodology]
sources: [raw/adcs-lab-focus-research-2026-07-15.md]
raw: raw/adcs-lab-focus-research-2026-07-15.md
ingested: 2026-07-15
created: 2026-07-15
updated: 2026-07-15
---

# AD CS 實驗室聚焦官方文件研究

研究確認：Windows Server 2019 DC 應使用 Windows Server 2016 forest/domain functional level；AD CS 應同時啟用 Windows `Audit Certification Services` 與 CA audit filter，才能取得憑證要求、核發、撤銷與 CA 安全設定變更等事件。Wazuh 的 Windows Agent 預設採集 Application、Security、System，其他事件通道須明確加入設定。

版本基線採 Windows Server 2019、Windows 11 Enterprise 25H2、Wazuh 4.14.6 與 OPNsense CE 26.1.11；OS build 和 OPNsense patch 必須在安裝日重新記錄。Web Enrollment 不列為預設元件，只有在隔離測試需求與 TLS、稽核都明確時才啟用。

## 關聯

- 圖片來源：[[adcs-lab-focus-architecture]]
- 概念：[[adcs-esc-detection-baseline]]
- 實驗：[[adcs-lab-focus-review]]
