---
type: concept
title: "SOC 實驗室的網段分割與遙測邊界"
tags: [wazuh, active-directory, opnsense, network-segmentation, telemetry]
sources: [wazuh-ad-soc-architecture-diagram, wazuh-ad-soc-architecture-research, opnsense-reflection-hairpin-nat, range-main, threat-hunting-course-midterm-report, threat-hunting-course-final-report]
created: 2026-07-14
updated: 2026-07-20
---

# SOC 實驗室的網段分割與遙測邊界

資安實驗室不應只畫出「攻擊者、靶機、Wazuh、AI」之間的箭頭；每一條線都要被拆成資料目的、發起端、協定、身分、允許來源與可觀測證據。這能同時降低誤設的暴露面，也讓偵測結果可被重現與解釋。

## 三個邊界

| 邊界 | 元件 | 目的 | 必要控制 |
|---|---|---|---|
| 資料平面 | Windows 11、DC、Wazuh | 端點與 AD 安全事件進入分析流程 | Agent 註冊、加密傳輸、最小事件通道與可查詢的接收證據 |
| 網路邊界 | OPNsense、攻擊端、管理端 | 控制跨網段與測試流量 | 預設拒絕、明確來源/目的/連接埠、限時測試規則與 firewall log |
| AI 整合平面 | Wazuh、AI Server、MCP | 讓 AI 讀取經篩選的告警與知識 | 只讀權限、強認證、欄位最小化、請求與回應稽核 |

## 最小資料流模型

1. Windows 端點與 DC 將已授權的遙測送往 Wazuh；Wazuh 官方文件的預設 Agent 通道為 TCP 1514，但本機設定必須另外驗證。
2. OPNsense 只允許文件化的跨區域流量，並在需要時把網路安全日誌送入監控流程。
3. Wazuh 告警再提供給 AI；MCP 是應用整合名稱，不是網路安全設計本身，仍需定義 transport、認證與授權。
4. 攻擊端對 RDP／WinRM 的測試必須侷限於授權範圍；遙測應同時覆蓋端點事件與邊界設備日誌。

## 驗收證據

- Wazuh Dashboard 顯示各預期 Agent 為 active，且測試事件可追到來源主機。
- OPNsense 規則與日誌可證明只有允許的來源、目的與服務跨越網段。
- MCP 存取紀錄可對應到 AI 查詢，並證明它沒有取得未授權的管理控制能力。
- RDP／WinRM 的測試帳號、來源與時間可以從 AD/Windows 事件和網路日誌交叉對應。

## Control Plane、Data Plane 與錄製邊界

[[range-main]] 進一步把實驗室拆成兩個操作面：control plane 承載部署、管理、規則同步與 AI／API 控制；data plane 承載靶場通訊、端點事件與網路封包。兩者必須有不同的帳號、路徑與 firewall policy，避免取得測試資料面權限的主機同時控制 sensor 或監控平台。

內部分區若能以靜態路由與明確防火牆規則連接，通常比額外 NAT 更容易保存真實來源與對稱路徑；NAT 只留在必要的 Internet 邊界。南北向封包可在 OPNsense／Suricata 錄製，東西向流量則需內部 mirror／sensor。端點 EVTX／Sysmon、PCAP 與 operator timeline 應共享 run ID 與 UTC 時間基準，才能形成 [[detection-validation-range]] 所需的 ground truth，而不只是各自獨立的告警截圖。

## NAT 與分段的界線

NAT 只改寫位址或連接埠，不等於網段隔離、存取授權或 VPN 身分控制。依 [[nat-reflection-and-hairpin-nat]]，不同子網的內部主機若使用外部 IP 存取內部服務，可能需要 Reflection DNAT；相同子網的 Hairpin 情境則需額外 SNAT 維持對稱回程。無論使用何種轉譯，仍須以來源、目的、服務與介面上的防火牆規則限制流量，並保留可供 Wazuh／SOC 關聯的規則命中紀錄。

## 關聯

- 設計來源：[[wazuh-ad-soc-architecture-diagram]]
- 官方研究：[[wazuh-ad-soc-architecture-research]]
- OPNsense NAT 路徑：[[nat-reflection-and-hairpin-nat]]
- 架構審查閉環：[[wazuh-ad-soc-architecture-review]]
- 可重放驗證：[[detection-validation-range]]
- 課程到靶場演進：[[threat-hunting-course-to-detection-range-evolution]]
