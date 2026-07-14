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
