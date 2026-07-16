# Wiki 索引

這是本 wiki 所有頁面的總目錄。每一條目：一個指向頁面的 wikilink，加上一行摘要。LLM 在回答查詢時會先讀這個檔案，用一行摘要找出候選頁面。

摘要請保持精簡 —— 每頁一行。索引本身被設計成讀取成本低廉，索引一旦臃腫就會失去「先查索引」這個設計的意義。

當這個檔案超過約 300 行，或 wiki 頁面數超過約 150 頁時，請分片為 `wiki/indexes/<type>.md`，並將這個檔案改為分片目錄。分片程序請參考 `llm-wiki` 技能中的 `scaling-playbook.md`。

---

## 2026-07-14 架構研究

- [[wazuh-ad-soc-architecture-diagram]] — 使用者提供的 Wazuh × AD × OPNsense × AI SOC 架構圖轉錄；記錄七個角色、資源基線與不確定性。
- [[wazuh-ad-soc-architecture-research]] — Wazuh、Microsoft AD DS、OPNsense 官方文件研究；校正 all-in-one、Agent 與分段的可驗證事實。
- [[soc-lab-segmentation-and-telemetry]] — 將端點遙測、網段邊界、AI MCP 拆成可驗收的信任關係。
- [[wazuh-ad-soc-architecture-review]] — 完整 H-I-V-R-K-C 架構審查；文件層驗證已完成，實機驗證待執行。

## 2026-07-15 AD CS 實驗室聚焦

- [[adcs-lab-focus-architecture]] — MOND.local 的 AD DC、AD CS、帳號與主機欄位設計圖轉錄；未部署值均標為待驗證。
- [[adcs-lab-focus-research]] — Server 2019 FFL/DFL、CA 稽核、Web Enrollment 與 Wazuh/OPNsense/Windows 版本的官方研究。
- [[adcs-esc-detection-baseline]] — AD CS 憑證範本、CA 稽核、目錄變更與 Wazuh 關聯的防禦偵測基線。
- [[adcs-lab-focus-review]] — H-I-V-R-K-C：將 AD CS 轉為可安全驗證的防禦 lab。

## Sources（來源）

- [[dll-ms-learn]] — Microsoft Learn 的 DLL 技術支援文件：DLL 運作機制、依賴問題（「DLL Hell」），以及作為其後繼方案的 .NET assembly 模型。
- [[malware-dynamic-analysis]] — 惡意程式動態分析實戰筆記 Part 1：安全 VM 分析環境建置、Process Explorer 觀察程序與 DLL 異常、Process Monitor 側錄系統行為。
- [[git-github-complete-notes]] — Git 與 GitHub 最完整使用筆記：40 章手冊，涵蓋核心模型、日常指令、分支協作、GitHub 平台功能、CI/CD、安全治理、疑難排解。
- [[malware-static-dynamic-analysis-notes]] — 惡意程式靜態＋動態分析實戰筆記：PE 靜態分析、動態行為分析、Persistence、Injection、家族行為模式、Sysmon、IOC/TTP/MITRE、報告模板。
- [[adcs-lab-focus-architecture]] — MOND.local AD DC/AD CS 的設計聚焦圖與待驗證欄位。
- [[adcs-lab-focus-research]] — AD CS 稽核、Server 2019 AD DS 功能等級、Wazuh/OPNsense/Windows 版本研究。
- [[ai-security-tools-research-2026-07-16]] — 七項 AI 資安工具的官方文件與研究批次；標示產品世代、用途、風險與專題整合邊界。

## Entities（實體）

- [[process-explorer]] — Sysinternals 程序檢視工具，用來觀察父子程序關係、DLL 載入異常與建議觀察欄位。
- [[process-monitor]] — Sysinternals 系統行為側錄工具，用來觀察登錄檔／檔案／網路／程序的底層動作，含 Filter 策略與常見誤判。

### AI 資安工具

- [[pentestgpt]] — LLM 驅動的授權滲透測試 agent；原始論文與現行 agentic repo 需分開理解。
- [[burpgpt]] — Burp Suite 的 AI HTTP 流量分析工具；Community edition 已停止維護，選型應以現行 Pro 文件為準。
- [[microsoft-security-copilot]] — Microsoft Defender/Sentinel/Entra 生態的企業安全與 IT 助理。
- [[deepcode-ai]] — Snyk Code 使用的 AI 安全分析技術，可從 IDE、PR、CLI 與 CI/CD 導入。
- [[hexstrike-ai]] — 高度自動化的 MCP 攻擊工具協調框架，僅限隔離、授權的研究環境。
- [[garak]] — NVIDIA 支援的開源 LLM vulnerability scanner，適合 AI/RAG/MCP 的部署前與回歸測試。
- [[lakera-guard]] — Check Point AI Guardrails 的 runtime screening API，可防護 LLM、RAG、agent 與 tool 互動。

## Concepts（概念）

### AD CS 與防禦偵測

- [[adcs-esc-detection-baseline]] — CA、template、enrollment ACL、稽核事件與目錄變更的 AD CS ESC 防禦偵測基線。

### DLL／Windows 基礎

- [[dynamic-link-library]] — DLL 是什麼、載入時期（load-time）與執行時期（run-time）連結的差異、進入點／匯出機制、搜尋順序、疑難排解工具、惡意程式分析中的應用。
- [[dll-dependency-hell]] — 共用 DLL 更新／移除如何破壞依賴它的程式，以及 Windows 的緩解措施（WFP、私有 DLL）。
- [[dotnet-assembly]] — .NET assembly 模型，以及它如何在結構上取代 DLL Hell 問題。

### 惡意程式分析

- [[malware-analysis-vm-setup]] — 建置安全的惡意程式動態分析 VM 環境：整體架構、繞過 OOBE、封印防護、快照分層、樣本處理安全規則、規避 Anti-VM 的檔案傳輸法。
- [[malware-analysis-methodology]] — 分析核心心法（IOC vs TTP、不要只看單一證據）、分析總流程、樣本接收與證據保存。
- [[pe-static-analysis]] — Windows PE 結構、Sections/Entropy/Import-Export Table 分析、簽章與 Overlay Data、靜態分析模板。
- [[script-and-document-malware-analysis]] — PowerShell/VBScript/JavaScript 腳本與 Office/PDF/LNK/MSI/壓縮檔的靜態分析重點。
- [[packers-and-anti-analysis]] — Packer、Obfuscation、Anti-VM、Anti-Debug 的靜態跡象。
- [[dynamic-behavior-analysis]] — 動態分析流程、程序／檔案／Registry／網路行為的觀察與判讀原則。
- [[persistence-mechanisms]] — 九種持久化類型（Run Key/Scheduled Task/Service/WMI/COM Hijacking 等）的證據鏈與工具觀察。
- [[lolbin-and-powershell-abuse]] — LOLBin 濫用判讀原則、高風險程序鏈、PowerShell 動態觀察與可疑命令線索。
- [[process-hollowing]] — 進程掏空技術：概念流程、相關 API、可疑證據清單、記憶體異常觀察工具、DLL 載入矛盾間接偵測。
- [[malware-behavior-patterns]] — Dropper/Loader/RAT/Info Stealer/Ransomware/Crypto Miner/Wiper 七種家族行為模式。
- [[windows-event-log-and-sysmon]] — Windows Security/System Event ID 與 Sysmon 22 種常見 Event ID、ProcessGuid 關聯分析。
- [[ioc-ttp-and-detection-engineering]] — IOC 類型與穩定性、MITRE ATT&CK 對應表、Detection Engineering 思維、Sigma/YARA 模板。
- [[malware-analysis-report-template]] — Malware Analysis Report 15 節完整結構與各節撰寫要點。

### Git／GitHub

- [[git-core-concepts]] — Git 心智模型：四個區域、快照模型、blob/tree/commit/tag、branch 指標、HEAD、staging area、reflog。
- [[git-setup-and-daily-workflow]] — 安裝設定、建立/clone repo、日常 add-commit-push-pull 循環、commit message 規範。
- [[git-branching-merge-rebase]] — 分支管理、merge vs rebase 差異與黃金規則、cherry-pick/revert/reset、衝突處理。
- [[git-remote-collaboration]] — origin/fetch/pull/push、tracking branch、force-with-lease、fork flow 遠端設定。
- [[git-undo-and-recovery]] — Undo/Recovery 救援大全（reflog 為核心）、stash、危險指令警戒表。
- [[git-tag-release-and-repo-config]] — Tag/Semantic Versioning/GitHub Release、`.gitignore`／`.gitattributes`。
- [[git-hooks-worktree-submodule-lfs]] — Git Hooks、Worktree、Submodule vs Subtree、Git LFS。
- [[git-advanced-commands]] — bisect/grep/blame/archive/bundle、sparse checkout、partial clone、bare repo、fsck/gc。
- [[github-repository-and-project-management]] — Repo 基礎功能與設定、Issues/Labels/Milestones/Projects、PR 與 Code Review、CODEOWNERS。
- [[github-workflow-strategies-and-branch-protection]] — GitHub Flow/Fork Flow/Git Flow/Trunk-based 比較、Branch Protection、Rulesets、Merge Queue。
- [[github-actions-cicd]] — GitHub Actions 核心概念、workflow 範例、Secrets/Variables/GITHUB_TOKEN 權限、GitHub Pages。
- [[github-cli-and-security]] — `gh` CLI、Dependabot/CodeQL/Secret Scanning、Organization/Team 權限、SSH/PAT/Commit Signing。

### AI 系統安全

- [[ai-security-tool-selection]] — 將滲透測試、SAST、SOC 助理、LLM 紅隊與 runtime guardrail 放入不同控制點的選型與專題整合順序。

## Experiments（實驗）

- [[git-reset-modes]] — 實測 git reset --soft/--mixed/--hard 對 Commit/Staging/Working Tree 的影響；假設 supported，信心 High。
- [[adcs-lab-focus-review]] — MOND.local AD CS 偵測 lab 的 H-I-V-R-K-C 設計與待實機驗證清單。

## Synthesis（綜合分析）

- [[ai-security-tool-selection]] — 七項 AI 資安工具的角色比較、採用順序與 Wazuh × AD × AI 專題整合邊界。
