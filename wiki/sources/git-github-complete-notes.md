---
type: source
title: "Git 與 GitHub 最完整使用筆記"
authors: []
url: ""
raw: "raw/git_github_complete_notes.md"
ingested: 2026-07-09
tags: [git, github, ci-cd, devops]
entities: []
concepts: [git-core-concepts, git-setup-and-daily-workflow, git-branching-merge-rebase, git-remote-collaboration, git-undo-and-recovery, git-tag-release-and-repo-config, git-hooks-worktree-submodule-lfs, git-advanced-commands, github-repository-and-project-management, github-workflow-strategies-and-branch-protection, github-actions-cicd, github-cli-and-security]
---

# Git 與 GitHub 最完整使用筆記

使用者的個人筆記（版本 2026-07-09），定位為「從 Git 基礎原理、日常指令、分支協作、GitHub 平台功能、CI/CD、安全治理，到疑難排解」的長期查閱手冊。全文 40 章 + 5 個附錄，組織良好、範例豐富，內容密度接近一本完整的內部教材，而非單篇文章。以下依原文章節分組摘要，詳細內容已拆分進對應的 concept 頁。

## 核心心智模型（Ch 0-2）

Git 是分散式版本控制系統，GitHub 是建立在 Git 之上的雲端協作平台——兩者常被混為一談，但可完全獨立使用。Git 的核心不是「存 diff」，而是每次 commit 都是一份完整快照；四個核心資料類型是 Objects（blob/tree/commit/tag）、References（branch/tag）、Index（staging area）、Reflog。Branch 本質上只是指向某個 commit 的可移動指標，這個心智模型是理解 merge/rebase 的基礎。詳見 [[git-core-concepts]]。

## 設定與日常流程（Ch 3-7）

安裝、`user.name`/`user.email`/`init.defaultBranch`/`core.autocrlf`/`pull.rebase` 等設定、常用 alias；建立/clone repo；`status`/`add`/`commit`/`push`/`pull` 的日常循環；`diff`/`log`/`blame` 查看差異與歷史；Conventional Commits 格式（`feat`/`fix`/`docs`/`refactor`/...）與 `commit --amend`。詳見 [[git-setup-and-daily-workflow]]。

## 分支、合併、救援（Ch 8-13）

Branch 建立/切換/刪除/命名規範；merge（fast-forward vs three-way）與 rebase 的差異及「黃金規則」（不 rebase 已共享的 branch）；interactive rebase、cherry-pick、revert、reset 三種模式（soft/mixed/hard）；衝突處理與 ours/theirs；完整的 undo/recovery「救援大全」（reflog 是核心救命工具）；stash。詳見 [[git-branching-merge-rebase]] 與 [[git-undo-and-recovery]]。

## 遠端協作（Ch 10）

`origin` 只是慣例命名、fetch 不動本機分支、`push --force-with-lease` 優於 `--force`、tracking branch 設定、`fetch --prune`。詳見 [[git-remote-collaboration]]。

## Tag、Release 與 Repo 設定檔（Ch 14-15）

Lightweight vs annotated tag、Semantic Versioning、GitHub Release 流程；`.gitignore`/`.gitattributes`/換行符號統一設定。詳見 [[git-tag-release-and-repo-config]]。

## Hooks、Worktree、Submodule、LFS（Ch 16-19）

pre-commit/commit-msg/pre-push hooks 與團隊共享方案（Husky/Lefthook/`core.hooksPath`）；worktree 讓同一 repo 同時 checkout 多個 branch 到不同資料夾；submodule vs subtree 的取捨；Git LFS 處理大型二進位檔。詳見 [[git-hooks-worktree-submodule-lfs]]。

## 進階指令（Ch 20）

`bisect` 二分搜尋找 bug、`grep`/`blame` 搜尋與追溯、`archive`/`bundle` 打包搬移、sparse checkout / partial clone 適合大型 repo、bare repository、`fsck`/`gc`。詳見 [[git-advanced-commands]]。

## GitHub 專案管理（Ch 21-24, 27）

Repository 基礎功能（public/private/internal、README、LICENSE、topics、wiki、discussions）；repo 設定與三種 PR 合併方式（merge commit/squash/rebase）；Issues/Labels/Milestones/Projects；PR 與 code review 的完整實務（checklist、描述模板、review 類型、PR 大小建議）；CODEOWNERS 與 PR template。詳見 [[github-repository-and-project-management]]。

## 協作流程與分支保護（Ch 25-26）

GitHub Flow / Fork Flow / Git Flow / Trunk-based development 四種策略的適用情境比較；Branch Protection 與更靈活的 Rulesets、Merge Queue、force push 原則。詳見 [[github-workflow-strategies-and-branch-protection]]。

## CI/CD（Ch 28-30）

GitHub Actions 核心概念（workflow/event/job/step/action/runner/matrix/artifact/cache/environment）、Node.js/Python CI 範例、job 依賴與條件執行、Secrets vs Variables、`GITHUB_TOKEN` 最小權限原則、GitHub Pages 發布。詳見 [[github-actions-cicd]]。

## CLI 與安全治理（Ch 31-34）

`gh` CLI 操作 repo/PR/issue/workflow/secret/release；Dependabot/CodeQL/Secret Scanning/Push Protection；Repository roles 與最小權限原則、Organization/Team；SSH key/PAT/commit signing。詳見 [[github-cli-and-security]]。

## 疑難排解、實戰範本、速查表、學習路線圖（Ch 35-40 + 附錄）

這幾章是前面內容的濃縮重組，未獨立開頁，重點摘要如下：

- **常見錯誤**（Ch 35）：`non-fast-forward`、detached HEAD、誤 commit secret（需 revoke + 清歷史，刪檔不等於從歷史消失）、大檔 push 被拒、SSH `Permission denied`、密碼驗證已被 GitHub 移除等，對應解法散落於 [[git-undo-and-recovery]] 與 [[github-cli-and-security]]。
- **實戰工作流範本**（Ch 36）：個人專案最小流程、團隊 feature branch 流程、hotfix 流程、開源 fork 貢獻流程、release 流程、monorepo 基本策略，本質是前述章節指令的組合應用，已內嵌在對應 concept 頁的範例中。
- **指令速查表**（Ch 37）與**團隊規範模板**（Ch 38）：純粹是前面章節指令與規範的彙整重排，不含新資訊。
- **學習路線圖**（Ch 39）：初學者 → 協作 → 進階 → 維護者 → DevOps/Security 五階段，可作為未來排定學習或 lab 順序的參考。
- **參考資料**（Ch 40）：指向 Git 官方文件與 GitHub 官方文件的連結清單。
- **附錄 A-E**：一頁式工作流圖、危險指令警戒表、`.gitignore`/`.gitattributes` 起手式、最小安全 GitHub Repo Baseline——皆為前述內容的速查版本，內容已併入相關 concept 頁（危險指令警戒表併入 [[git-undo-and-recovery]]，安全 baseline 併入 [[github-cli-and-security]]）。

## 與其他頁面的關聯

- [[git-core-concepts]]
- [[git-setup-and-daily-workflow]]
- [[git-branching-merge-rebase]]
- [[git-remote-collaboration]]
- [[git-undo-and-recovery]]
- [[git-tag-release-and-repo-config]]
- [[git-hooks-worktree-submodule-lfs]]
- [[git-advanced-commands]]
- [[github-repository-and-project-management]]
- [[github-workflow-strategies-and-branch-protection]]
- [[github-actions-cicd]]
- [[github-cli-and-security]]
