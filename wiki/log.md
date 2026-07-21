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
## [2026-07-16] audit + strengthen | 文件內容強化第一批（進行中）
   pages: wiki/synthesis/wiki-content-strengthening-audit-2026-07-16.md (new); wiki/entities/deepcode-ai.md、wiki/entities/garak.md、wiki/entities/lakera-guard.md、wiki/entities/burpgpt.md、wiki/entities/microsoft-security-copilot.md (expanded)
   result: 盤點 55 個父層 wiki 頁與 137 個 Wazuh 專題文件；補入 Windows 前置檢查、可驗證快速開始、設定/金鑰管理、排錯與工具比較。Python/API 實測未宣稱完成。
## [2026-07-16] ingest + strengthen | Sysinternals 官方研究與工具頁補強
   pages: raw/sysinternals-tool-research-2026-07-16.md；wiki/sources/sysinternals-tool-research-2026-07-16.md；wiki/entities/process-explorer.md、wiki/entities/process-monitor.md (expanded)
   result: 補入官方支援矩陣、Windows 下載驗證、GUI 快速開始、filter/PML 證據保存與排錯；Process Explorer 最新官方頁僅列 Windows 11+，Windows 10 lab 須自行驗證相容性。
## [2026-07-16] strengthen | PentestGPT 與 HexStrike AI 工具治理補強
   pages: wiki/entities/pentestgpt.md、wiki/entities/hexstrike-ai.md (expanded); raw/ai-security-tools-research-2026-07-16.md (updated)
   result: 補入 Docker/Python 前置檢查、隔離/allowlist/人工停止點、MCP agent 控制流與常見排錯；未提供對任何目標執行掃描或利用的操作指令。
## [2026-07-16] lint | 文件內容強化批次手動驗證
   checked: 11 個新增或擴寫頁面；frontmatter 0 failures、wikilink 0 broken、oversized 0、索引缺漏 0；兩份 research raw 均存在。
   limitation: 專案未發現 package.json、pyproject.toml 或文件網站設定，且本機無可用 Python；未執行建置、Markdown lint 或第三方工具實機測試。
## [2026-07-16] lint | 資料庫大保養（手動全庫掃描 wiki + projects/wazuh-ad-soc）
   斷鏈：修 20 條前綴/命名不一致（doc-→dsh- ×17、doc-windows-security-event-overview→evt-windows-security-overview、evt-ad-abnormal-logon→scn-ad-abnormal-logon、rpt-full-report→qa-full-report），跨 11 檔；連帶消除 4 個假孤兒。最終 0 斷鏈。
   版本：依使用者裁決將 Server 版本統一為 2019（規劃期，可能再調；raw 保留草稿值 2022/2025 作 ground truth）。修正 version-sed 誤壓的 1 處功能等級事實（adcs-environment：Server 2019 無專屬功能等級，最高採 Windows Server 2016 FFL/DFL）。log 歷史條目維持原值不改。
   其餘：0 重複 id、0 超大頁（皆 <350 行）、Jul15 adcs 與 Jul16 AI 工具頁均已收錄、db 三檔一致。誤報排除 [[slug]]/[[wikilink]]/[[wikilinks]]（模板文字範例）。
   cadence 訊號：專案（projects/）應每完成一個 batch 就跑一次「專案內」lint，勿只掃 wiki/——本次 20 條斷鏈皆為只掃 wiki 時漏掉的專案內部積累。
## [2026-07-17] ingest + experiment | 兩篇密碼學論文（循環移位對稱密碼、量子/後量子密碼）
   pages: wiki/sources/crypto-circular-shift-cipher-paper.md、wiki/sources/quantum-crypto-hybrid-xor-paper.md（new）; wiki/concepts/circular-shift-symmetric-cipher.md、wiki/concepts/post-quantum-cryptography.md（new）; wiki/experiments/circular-shift-cipher-verification.md（new）; code/2026-07-17/circular-shift-cipher/（cipher.py+README+manifest）
   result: 首個本機 Python(3.12.10) 實測實驗。論文一密碼 round-trip 可逆、金鑰生成重現 Table I（supported），但揭露金鑰整數表示對低 nibble≥10 失真 + Table I 表頭 typo（partial）。論文二「量子」多為綜述/future work，實作僅古典 XOR；其統計數字一律標「宣稱、未佐證」。紀律：可逆≠安全。
## [2026-07-17] ingest | OPNsense Reflection and Hairpin NAT 官方文件
   pages: raw/opnsense-reflection-hairpin-nat.md（new）；wiki/sources/opnsense-reflection-hairpin-nat.md（new）；wiki/concepts/nat-reflection-and-hairpin-nat.md（new）；wiki/concepts/soc-lab-segmentation-and-telemetry.md、wiki/SCHEMA.md、wiki/index.md（updated）
   result: 區分一般路由／Port Forward、Reflection DNAT 與同網段 Hairpin DNAT + SNAT；納入單一 Attacker VPN + `.40` 觀測網架構判斷，並保留 NAT 非安全控制、手動可稽核規則與除錯證據。
## [2026-07-17] ingest | 惡意程式動態分析實戰筆記增量（Lab 5–7）
   pages: wiki/sources/malware-dynamic-analysis.md；wiki/concepts/windows-event-log-and-sysmon.md、dynamic-link-library.md、process-hollowing.md、dynamic-behavior-analysis.md、malware-analysis-vm-setup.md；wiki/entities/process-explorer.md；wiki/SCHEMA.md、wiki/index.md（updated）；new pages: 0
   result: 整合 Sysmon EID 1/7、DLL Sideloading 與 Process Hollowing；以官方文件校正 DLL 搜尋順序、Python ctypes 與 MITRE 行為鏈，並把單一父子程序／DLL 訊號降為待驗證假設。標題與 callout 顏色規則已正式化。
## [2026-07-20] ingest | locrian 實作規格（build-of-record）
   pages: wiki/sources/range-main.md、wiki/concepts/detection-validation-range.md、wiki/synthesis/threat-hunting-course-to-detection-range-evolution.md（new）；wiki/concepts/soc-lab-segmentation-and-telemetry.md、ioc-ttp-and-detection-engineering.md（updated）
   result: 將 detection range 的 control/data plane、ground truth、artifact 保存、重放與 None/Telemetry/Failed/Success 四態評分納入 KB；repository 多數實作目錄仍為 skeleton，未宣稱已部署。
## [2026-07-20] ingest | Threat Hunting Essential: Attack Recognition Techniques
   pages: wiki/sources/threat-hunting-course-midterm-report.md（new）；wiki/concepts/windows-event-log-and-sysmon.md、soc-lab-segmentation-and-telemetry.md（updated）
   result: 保留 Wazuh、OPNsense/Suricata、Sysmon、Windows Audit 與初期 MCP 的實作證據；截圖與環境特定 rule.id 不升格為可重現或通用結論。
## [2026-07-20] ingest | Threat Hunting Essential: Attack Recognition Techniques Part 2
   pages: wiki/sources/threat-hunting-course-final-report.md（new）；wiki/concepts/ioc-ttp-and-detection-engineering.md、projects/wazuh-ad-soc/（4 pages updated）
   result: 整合 OPNsense Agent、Alert/Drop、MCP hard gating 與 ET-BERT 實驗；模型比較與分類效能因缺固定測試集、F1/confusion matrix/leakage 檢查而標為待驗證，敏感 credential 未轉錄。
## [2026-07-20] experiment | threat-hunting-range-evolution-review
   hypothesis: 把期中／期末的單次展示重新編譯成 ground truth、重放與四態評分，可形成更可重現的偵測驗證方法。
   result: partial / medium confidence；文件與視覺驗證完成，但 range-main 尚未完整實作，MCP、ET-BERT 與自動 scorecard 均缺足夠實機證據；code_paths 為空。
## [2026-07-20] lint | range-main + Threat Hunting Essential 批次 ingest 後檢查
   checked: 主 Wiki 67 頁、Wazuh 子專案合計 207 個 Markdown；跨庫 338 個可解析目標、0 失效 wikilink；本次 6 個新頁 0 孤兒、0 frontmatter 缺漏、0 超大頁；experiments.jsonl 與 learning_log.jsonl 各 5 筆且全數可解析。
   known debt: 內建 wiki_lint 不解析 projects/，因此回報的 20 條跨庫連結已由跨庫掃描確認均有效；另有 4 個舊 experiment 缺 title/tags、5 個舊 source 缺 created/updated，皆為本批前既存 schema 債務，未在本次來源 ingest 擴大修改。
## [2026-07-20] experiment | Wazuh Windows／Sysmon 威脅偵測規則包
   code: code/2026-07-20/wazuh-windows-threat-detection-rules/（18 rules、Sysmon baseline、agent.conf snippet、README、manifest）；custom IDs 110100–110144。
   result: partial / medium confidence；3 個 XML 可解析、18 個 ID 唯一、manifest JSON 有效；Wazuh 4.14.6 `wazuh-analysisd -t`、live event 命中與一週誤報 baseline 待在實機完成，未啟用 Active Response。
## [2026-07-20] lint | Wazuh Windows／Sysmon 規則包 post-change
   checked: 27 個 PCRE2 型式 0 compile error、兩個 JSONL 0 parse error；主 Wiki 68 頁且本次新頁 0 孤兒／0 frontmatter 缺漏；主 Wiki + Wazuh 子專案共 208 個 Markdown、340 個可解析目標、0 跨庫失效連結。
   limitation: Wazuh XML 語意與 EventChannel 實際欄位只能由 Manager `wazuh-analysisd -t` 及 live-event 驗證；內建 wiki_lint 的 20 條跨庫誤報與 9 個舊頁 schema 債務維持既有紀錄。
## [2026-07-21] lint | 結構性大保養（全庫 wiki + projects，Python 腳本掃描）
   範圍：230 個 .md。斷鏈 0 真問題（[[連結]] 為 CLAUDE.md 說明文字）、超大頁 0、wiki 未索引 0、重複 id 0、db 三檔+concepts 全解析且 0 失效參照路徑。projects 26「孤兒」判為誤報（20 筆為專案頁以 markdown 連結掛 index.md 的導覽設計，非 [[ ]]）。
   清理：刪除庫根 14 個 Obsidian 殘骸——8 個 0-byte id 空 stub（doc-data-and-event-flow/doc-mitre-distribution/doc-scope-and-limitations/doc-wazuh-dashboard/doc-wazuh-field-to-ai-mapping/doc-wazuh-manager/doc-windows-events-into-wazuh/evt-ad-security-overview，真頁皆在 projects/）、未命名.md、experiments/....md（含空夾）、image1/2/3.md（貼圖 base64）。刪前確認 7 個 stub 之 id 均與真頁相符、doc-mitre-distribution 無人連結，刪除不暴露任何斷鏈。重跑後庫根僅剩 CLAUDE.md/changelog.md。
   根因與對策：Obsidian 以檔名（非 frontmatter id）解析連結，故 [[doc-xxx]] id 連結會在庫根自動生成空 stub，會週期再生；已於 CLAUDE.md §11 記錄清理 SOP（find -maxdepth 1 -size 0）。
   note：07-20 由平行 Codex agent 完成的 range-main／威脅獵捕期中期末報告 ingest（7 wiki 頁 + code/2026-07-20/）本次一併納入掃描，結構一致、無斷鏈。
