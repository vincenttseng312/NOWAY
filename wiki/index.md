# Wiki 索引

這是本 wiki 所有頁面的總目錄。每一條目：一個指向頁面的 wikilink，加上一行摘要。LLM 在回答查詢時會先讀這個檔案，用一行摘要找出候選頁面。

摘要請保持精簡 —— 每頁一行。索引本身被設計成讀取成本低廉，索引一旦臃腫就會失去「先查索引」這個設計的意義。

當這個檔案超過約 300 行，或 wiki 頁面數超過約 150 頁時，請分片為 `wiki/indexes/<type>.md`，並將這個檔案改為分片目錄。分片程序請參考 `llm-wiki` 技能中的 `scaling-playbook.md`。

---

## Sources（來源）

- [[dll-ms-learn]] — Microsoft Learn 的 DLL 技術支援文件：DLL 運作機制、依賴問題（「DLL Hell」），以及作為其後繼方案的 .NET assembly 模型。
- [[malware-dynamic-analysis]] — 惡意程式動態分析實戰筆記 Part 1：安全 VM 分析環境建置、Process Explorer 觀察程序與 DLL 異常、Process Monitor 側錄系統行為。
- [[git-github-complete-notes]] — Git 與 GitHub 最完整使用筆記：40 章手冊，涵蓋核心模型、日常指令、分支協作、GitHub 平台功能、CI/CD、安全治理、疑難排解。
- [[malware-static-dynamic-analysis-notes]] — 惡意程式靜態＋動態分析實戰筆記：PE 靜態分析、動態行為分析、Persistence、Injection、家族行為模式、Sysmon、IOC/TTP/MITRE、報告模板。

## Entities（實體）

- [[process-explorer]] — Sysinternals 程序檢視工具，用來觀察父子程序關係、DLL 載入異常與建議觀察欄位。
- [[process-monitor]] — Sysinternals 系統行為側錄工具，用來觀察登錄檔／檔案／網路／程序的底層動作，含 Filter 策略與常見誤判。

## Concepts（概念）

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

## Experiments（實驗）

- [[git-reset-modes]] — 實測 git reset --soft/--mixed/--hard 對 Commit/Staging/Working Tree 的影響；假設 supported，信心 High。

## Synthesis（綜合分析）

（隨著查詢結果歸檔而填入）
