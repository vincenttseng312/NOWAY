# Wazuh × AD × AI SOC 架構研究筆記

- 研究日期：2026-07-14
- 用途：為使用者提供的專題架構圖補足可驗證的產品行為與安全邊界。
- 限制：下列文件描述產品預設或能力；實驗室是否已採用，必須以實機設定驗證。

## 官方來源與可用結論

### Wazuh architecture

來源：<https://documentation.wazuh.com/current/getting-started/architecture.html>

- 小型環境可採 all-in-one 部署，把 Wazuh server、indexer、dashboard 安裝於單一伺服器。
- Wazuh Agent 會把端點安全資料送至 Wazuh Server；預設 Agent connection service 為 TCP 1514，Agent enrollment 為 TCP 1515。
- Server 會分析事件，經 Filebeat 送至 indexer；dashboard 以 API 與 indexer 顯示資料。
- 無法安裝 Agent 的網路設備可透過 Syslog 或 SSH 進行 agentless monitoring。

### Active Directory Domain Services

來源：<https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview>

- AD DS 保存使用者、電腦、伺服器與共享資源等目錄物件，並提供驗證、存取控制與政策式管理。
- Domain Controller 因此是身分與權限事件的重要觀察點；對其事件採集與保護應優先於一般端點。
- 本文件適用頁面明列 Windows Server 2025，但不驗證本專題 VM 的實際版本或設定。

### OPNsense firewall and VPN

來源：<https://docs.opnsense.org/manual/firewall.html>、<https://docs.opnsense.org/manual/vpnet.html>

- OPNsense 文件提供防火牆規則與 VPN 的設定說明，可作為不同網段間最小允許連線的執行控制點。
- 圖中 IDS、VPN 與 firewall 是目標能力；是否啟用、採集何種日誌、使用何個介面及規則內容均待實機確認。

## 研究導出的架構原則

1. 將資料平面（Windows／AD 事件）、控制平面（管理 RDP／WinRM／Wazuh Dashboard）與 AI 整合平面分開定義規則。
2. Wazuh 的 Agent、Syslog 與 MCP 連線不可只用「有一條箭頭」描述，必須分別記錄方向、端點、協定、認證與允許來源。
3. AI Server 對 Wazuh 的存取預設應為只讀、最小欄位、可稽核；不將其置入 AD 或端點的管理信任邊界。
4. 對外 RDP／WinRM 只作授權情境的限時測試，並將其事件與 OPNsense／Wazuh 遙測關聯驗證。
