# Wiki 紀錄（Log）

只增不改的時間序紀錄，記錄對這個 wiki 執行過的所有操作。每一條目開頭為 `## [YYYY-MM-DD] <op> | <description>`，方便用簡單指令解析（例如 `grep "^## \[" log.md | tail -N`）。

操作類型：
- `ingest` — 收錄並處理了一個新來源。
- `query` — 針對 wiki 回答了一個問題（通常只有答案被歸檔為 synthesis 時才記錄）。
- `experiment` — 執行了一個 H-I-V-R 學習單元（假設→實作→驗證→反思）。
- `lint` — 執行了一次健康檢查。
- `schema` — 修改了 schema。
- `shard` — 索引被分片。

以下條目為 2026-07-08 語言改版前所留下的原始紀錄，維持英文原樣以保留歷史紀錄的準確性：

---

## [2026-07-08] schema | Wiki initialized (manual bootstrap; Python unavailable, so init_wiki.py could not run)
## [2026-07-08] ingest | Dynamic link library (DLL) - Windows Client | Microsoft Learn
   pages: wiki/sources/dll-ms-learn.md (new); wiki/concepts/dynamic-link-library.md (new); wiki/concepts/dll-dependency-hell.md (new); wiki/concepts/dotnet-assembly.md (new)
## [2026-07-08] schema | 將 wiki 骨架、既有內容頁與 CLAUDE.md 全數翻譯為繁體中文；自此對話與 wiki 正文語言改為繁體中文（frontmatter 欄位名稱、tags、slug、程式碼識別字維持英文，詳見 wiki/SCHEMA.md「語言慣例」）
## [2026-07-08] schema | 專案主路徑改為 C:\Users\vincenttseng\LLM_Wiki（此前為 C:\Users\vincenttseng\tt，兩處內容於改版時已一致，之後以 LLM_Wiki 為準）
## [2026-07-08] ingest | 惡意程式動態分析實戰筆記 (Part 1)
   pages: wiki/sources/malware-dynamic-analysis.md (new); wiki/concepts/malware-analysis-vm-setup.md (new); wiki/concepts/process-hollowing.md (new); wiki/entities/process-explorer.md (new); wiki/entities/process-monitor.md (new); wiki/concepts/dynamic-link-library.md (updated — 新增「在惡意程式分析中的應用」小節)
## [2026-07-09] ingest | Git 與 GitHub 最完整使用筆記
   pages: wiki/sources/git-github-complete-notes.md (new); 12 concept 頁 (new) — git-core-concepts, git-setup-and-daily-workflow, git-branching-merge-rebase, git-remote-collaboration, git-undo-and-recovery, git-tag-release-and-repo-config, git-hooks-worktree-submodule-lfs, git-advanced-commands, github-repository-and-project-management, github-workflow-strategies-and-branch-protection, github-actions-cicd, github-cli-and-security
   粒度：粗粒度分群（使用者選擇），對應 40 章原文內容
## [2026-07-09] ingest | 惡意程式靜態＋動態分析實戰筆記
   pages: wiki/sources/malware-static-dynamic-analysis-notes.md (new); 11 concept 頁 (new) — malware-analysis-methodology, pe-static-analysis, script-and-document-malware-analysis, packers-and-anti-analysis, dynamic-behavior-analysis, persistence-mechanisms, lolbin-and-powershell-abuse, malware-behavior-patterns, windows-event-log-and-sysmon, ioc-ttp-and-detection-engineering, malware-analysis-report-template
   updated: wiki/concepts/process-hollowing.md（大幅擴充 API/概念流程/證據清單）; wiki/entities/process-explorer.md（補觀察欄位/checklist）; wiki/entities/process-monitor.md（補 Filter 策略/常見誤判）; wiki/concepts/malware-analysis-vm-setup.md（補整體架構/快照分層/樣本處理安全規則）
## [2026-07-09] schema | 導入 H-I-V-R-K-C 學習閉環（加法式）：新增 templates/、db/(jsonl+schema)、code/、changelog.md、wiki/experiments/ 頁型；SCHEMA.md 記錄新流程與「無 Python → V/C 邊界」。既有 34 頁不動。詳見 changelog.md
## [2026-07-09] experiment | git reset 三模式（exp-git-reset-modes）
   假設：git-branching-merge-rebase 的 reset 對照表正確；結果：supported（本機真 git 實測 6/6 通過），信心 High
   pages: wiki/experiments/git-reset-modes.md (new); wiki/concepts/git-branching-merge-rebase.md (updated — 表格加實測標記與記憶法); code/2026-07-09/git-reset-modes/ (script+README+manifest)
   schema: wiki/SCHEMA.md 新增標籤 sysinternals/git/github/ci-cd/devops
## [2026-07-14] lint | 手動結構掃描：35 個內容頁皆有其他知識頁的入站連結；0 個孤兒頁、0 個失效內容 wikilink、0 個重複 slug、0 個未索引頁面。
## [2026-07-14] ingest + experiment | Wazuh × AD × OPNsense × AI SOC 架構圖與官方文件研究
   pages: raw/wazuh-ad-soc-architecture-diagram-2026-07-14.md、raw/wazuh-ad-soc-architecture-research-2026-07-14.md；wiki/sources/wazuh-ad-soc-architecture-diagram.md、wiki/sources/wazuh-ad-soc-architecture-research.md、wiki/concepts/soc-lab-segmentation-and-telemetry.md、wiki/experiments/wazuh-ad-soc-architecture-review.md
   project: projects/wazuh-ad-soc/01-architecture/architecture-baseline-and-validation.md (new); network-topology.md、host-inventory.md、system-architecture.md、index.md (updated)
   result: 文件層 H-I-V-R-K-C completed / partial；實機 Agent、OPNsense、MCP、RDP/WinRM 驗證待執行，未宣稱已部署。
## [2026-07-14] lint | post-ingest 手動結構掃描：39 個內容頁、0 個失效 wikilink、0 個重複 slug、0 個孤兒頁（排除 index/log/SCHEMA）；experiments.jsonl 與 learning_log.jsonl 皆成功解析。
## [2026-07-14] lint | 跨 agent 一致性稽核（本 session 覆核 Codex 的架構整合）：5 個新架構檔（實驗頁/基線頁/soc-lab 概念/2 來源）之 wikilink 對 305 個已知 id/slug 全數解析，0 斷鏈；概念頁遵循 KB frontmatter 慣例。修正 host-inventory 殘留：主要實體「Host ×5」→「×7」、「五張實體卡」→「七張」（合併 5→7 角色時未同步）。
## [2026-07-15] ingest + experiment | MOND.local AD CS 防禦偵測實驗室聚焦圖與官方研究
   pages: raw/adcs-lab-focus-architecture-2026-07-15.md、raw/adcs-lab-focus-research-2026-07-15.md；wiki/sources/adcs-lab-focus-architecture.md、wiki/sources/adcs-lab-focus-research.md、wiki/concepts/adcs-esc-detection-baseline.md、wiki/experiments/adcs-lab-focus-review.md
   project: projects/wazuh-ad-soc/02-environment/adcs-environment.md (new); index.md、host-inventory.md (updated)
   result: 文件層 H-I-V-R-K-C completed / partial；推薦 Server 2022 FFL/DFL 2016、Wazuh 4.14.6、OPNsense CE 26.1.11、Win11 Enterprise 25H2；CA/Agent/GPO/事件未做實機宣稱，均待驗證。
## [2026-07-16] ingest | AI Security Tools official documentation research batch
   pages: raw/ai-security-tools-research-2026-07-16.md；wiki/sources/ai-security-tools-research-2026-07-16.md；7 entity pages (pentestgpt, burpgpt, microsoft-security-copilot, deepcode-ai, hexstrike-ai, garak, lakera-guard)；wiki/concepts/ai-security-tool-selection.md
   result: 以官方文件、官方 GitHub 與同行研究區分滲透測試 agent、Web AppSec、Microsoft SOC、SAST、LLM 紅隊與 runtime guardrail；BurpGPT Community 已停維護、DeepCode AI 非獨立產品、攻擊自動化工具限已授權隔離環境。
## [2026-07-16] lint | 資料庫大保養（手動全庫掃描 wiki + projects/wazuh-ad-soc）
   斷鏈：修 20 條前綴/命名不一致（doc-→dsh- ×17、doc-windows-security-event-overview→evt-windows-security-overview、evt-ad-abnormal-logon→scn-ad-abnormal-logon、rpt-full-report→qa-full-report），跨 11 檔；連帶消除 4 個假孤兒。最終 0 斷鏈。
   版本：依使用者裁決將 Server 版本統一為 2019（規劃期，可能再調；raw 保留草稿值 2022/2025 作 ground truth）。修正 version-sed 誤壓的 1 處功能等級事實（adcs-environment：Server 2019 無專屬功能等級，最高採 Windows Server 2016 FFL/DFL）。log 歷史條目維持原值不改。
   其餘：0 重複 id、0 超大頁（皆 <350 行）、Jul15 adcs 與 Jul16 AI 工具頁均已收錄、db 三檔一致。誤報排除 [[slug]]/[[wikilink]]/[[wikilinks]]（模板文字範例）。
   cadence 訊號：專案（projects/）應每完成一個 batch 就跑一次「專案內」lint，勿只掃 wiki/——本次 20 條斷鏈皆為只掃 wiki 時漏掉的專案內部積累。
