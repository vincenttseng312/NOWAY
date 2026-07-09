---
type: concept
title: "GitHub Repository 與專案管理（Issues／PR／Code Review／CODEOWNERS）"
tags: [github]
sources: [git-github-complete-notes]
created: 2026-07-09
updated: 2026-07-09
---

# GitHub Repository 與專案管理

涵蓋 GitHub repository 的基礎功能與設定、Issues/Labels/Milestones/Projects、Pull Request 與 Code Review 的完整實務，以及 CODEOWNERS／PR Template。

## Repository 基礎功能

GitHub repository 包含 Code、Issues、Pull requests、Actions、Projects、Wiki、Security、Insights、Settings。可見性分 Public（所有人可見）、Private（僅授權者）、Internal（企業內部，需 Enterprise）。

README.md 建議包含 Introduction/Features/Requirements/Installation/Usage/Configuration/Testing/Deployment/Contributing/License 各節；沒有 LICENSE 通常代表他人沒有明確權利使用、修改、散布專案。Topics 用於搜尋分類；Wiki 適合長篇文件/FAQ，若希望文件與程式碼一起 review 則建議放 repo 內 `docs/`；Discussions 適合 Q&A/RFC，Issues 則適合可追蹤、可關閉的工作項目。

## Repository 設定重點

三種 PR 合併方式：

| 方法 | 歷史特性 | 適合 |
|---|---|---|
| Create a merge commit | 保留分支與 merge commit | 想保留完整脈絡 |
| Squash and merge | PR 多個 commit 壓成一個 | 想保持 main 乾淨（小團隊常用） |
| Rebase and merge | commits 線性接到 base | 想保留 commit 但不要 merge commit |

「Automatically delete head branches」可在 PR merge 後自動刪除 feature branch，降低分支混亂。Template repository 可讓別人用相同結構建立新 repo，適合 starter kit、security baseline。

## Issues、Labels、Milestones、Projects

Issue template 放在 `.github/ISSUE_TEMPLATE/`，典型 bug report 包含 Summary/Steps to Reproduce/Expected Behavior/Actual Behavior/Environment。建議 Labels：`type: bug`、`priority: high`、`status: blocked`、`good first issue`、`security` 等。Milestone 用於追蹤一組 issue/PR（如 `v1.0.0`）。GitHub Projects 可建立看板/表格/Roadmap，常見狀態欄位：Backlog → Ready → In Progress → In Review → Blocked → Done。

## Pull Request 與 Code Review

PR 不只是合併按鈕，而是變更討論、code review、CI 檢查、安全掃描、文件審查、設計脈絡保存的載體。

開 PR 前 checklist：分支已同步最新 main、commit 訊息清楚、PR 範圍單一、測試已通過、文件已更新、沒有 secret/大檔、已自我 review diff。

PR 描述模板建議包含：Summary、Motivation、Changes、Testing、Screenshots/Evidence、Risk、Rollback Plan、Related Issues（`Closes #`）。

Review 結果三種：Comment（不阻擋）、Approve（同意合併）、Request changes（要求修改，通常阻擋 merge）。Code review 該看：正確性、可讀性、安全性、效能、測試覆蓋、錯誤處理、相容性、維護性、文件同步、團隊風格一致性。

PR 大小建議少於 300 行變更、單一目的；大型 PR 應拆成 `PR 1: refactor only` → `PR 2: add new interface` → `PR 3: implement feature` → `PR 4: add tests and docs` 的序列。Draft PR 適合提早讓隊友看到方向、CI 預跑、討論架構。

## CODEOWNERS 與 PR Template

CODEOWNERS 指定哪些人/team 負責哪些檔案，PR 修改相關檔案時 GitHub 會自動 request review。位置依序搜尋 `.github/CODEOWNERS`、`CODEOWNERS`、`docs/CODEOWNERS`。範例：

```text
* @org/core-team
/SECURITY.md @org/security-team
/.github/workflows/ @org/devops-team @org/security-team
/frontend/ @org/frontend-team
```

注意事項：owner 必須有 write 權限；team 必須 visible；**Draft PR 不會自動 request code owners**；path 大小寫要正確；CODEOWNERS 過大可能不載入；最後匹配的 pattern 通常優先。

PR Template 放在 `.github/pull_request_template.md`（或 `.github/PULL_REQUEST_TEMPLATE/<name>.md` 支援多模板），通常包含 Summary、Type of Change checklist、Checklist（測試/文件/自我 review/無 secret）、Related Issues。

## 與其他頁面的關聯

合併方式與分支保護的組合見 [[github-workflow-strategies-and-branch-protection]]；CI 檢查的具體實作見 [[github-actions-cicd]]；commit message 規範源自 [[git-setup-and-daily-workflow]]。
