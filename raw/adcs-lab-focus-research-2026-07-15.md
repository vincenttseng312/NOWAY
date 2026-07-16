# AD CS 實驗室聚焦官方研究（2026-07-15）

本研究只用於課堂／授權實驗室的防禦性架構、遙測與版本選擇；不把未驗證設定寫成已部署事實。

## 官方來源與結論

1. Microsoft, AD DS functional levels
   - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels
   - Windows Server 2022 可作為 Windows Server 2016 功能等級的 DC，但不能使用 Windows Server 2025 功能等級。
   - 結論：`MOND.local` 使用 forest/domain functional level `Windows Server 2016`。

2. Microsoft, Advanced Audit Policy 與 Audit Certification Services
   - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration
   - https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/audit-certification-services
   - `Object Access > Audit Certification Services` 可記錄憑證要求、核發、撤銷、CA 設定與權限變更。
   - 重要 Security Event ID：4882、4885、4886、4887、4888、4890、4891、4892、4896、4898。

3. Microsoft, CA audit filter
   - https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn786422(v=ws.11)
   - https://learn.microsoft.com/en-us/defender-for-identity/deploy/configure-windows-event-collection
   - `AuditFilter` 有七類；`127` 表示全類別。需配合 Windows `Audit Certification Services` 成功／失敗稽核，設定後重新啟動 Certificate Services。

4. Microsoft, Certification Authority Web Enrollment
   - https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/certificate-authority-web-enrollment
   - Web Enrollment 是瀏覽器式憑證申請與續期介面，須以 TLS 保護。
   - 結論：本實驗室預設不安裝；只有隔離測試、HTTPS 與稽核設計明確時才納入。

5. Wazuh, agent、server、Windows event channel
   - https://documentation.wazuh.com/current/installation-guide/wazuh-agent/index.html
   - https://documentation.wazuh.com/current/installation-guide/wazuh-server/index.html
   - https://documentation.wazuh.com/current/user-manual/capabilities/log-data-collection/configuration.html
   - Manager 版本應大於或等於 Agent。Windows 預設採集 Application、Security、System；Sysmon 等 channel 要明確設定。
   - 官方文件研究時可見穩定 4.x 範例為 4.14.6；5.0 仍為 beta，故本課堂基線不採 beta。

6. OPNsense Releases
   - https://docs.opnsense.org/CE_releases.html
   - https://docs.opnsense.org/releases/CE_26.1.html
   - 研究時 Community Edition 最新可見版本為 26.1.11；部署日應再次確認官方 patch。

7. Microsoft, Windows 11 release information
   - https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information
   - Windows 11 Enterprise 25H2 支援至 2028-10；26H1 不提供作為既有 24H2／25H2 裝置的就地升級。
   - 結論：既有實驗室 VM 優先 Windows 11 Enterprise 25H2，於建置日套用最新累積更新，不將 build 寫死。

## 研究限制

未登入任何 VM、Wazuh、OPNsense 或 AD CS；版本、IP、VLAN、Agent ID、GPO 與事件到達狀態均待實機驗證。
