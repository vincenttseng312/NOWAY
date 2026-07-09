---
type: concept
title: "GitHub 協作流程策略與分支保護"
tags: [github]
sources: [git-github-complete-notes]
created: 2026-07-09
updated: 2026-07-09
---

# GitHub 協作流程策略與分支保護

涵蓋四種常見的分支協作策略，以及保護重要分支（如 `main`）的機制：Branch Protection、Rulesets、Merge Queue。

## 四種協作流程策略

**GitHub Flow**：`main` → 建 feature branch → commit → push → 開 PR → review + CI → merge → deploy。適合 Web app、SaaS、頻繁部署的小到中型團隊。

**Fork Flow**：常見於開源專案，`upstream repo` → fork 到 `my fork` → branch → commit → PR back to upstream。需另外設定 `upstream` 遠端，同步方式見 [[git-remote-collaboration]]。

**Git Flow**：分支結構較複雜——`main`（正式版本）、`release/*`（釋出候選）、`develop`（整合開發）、`feature/*`（功能）、`hotfix/*`（緊急修正）。適合版本週期明確、需維護多個 release 的桌面軟體/嵌入式/套裝軟體；不適合超頻繁部署的小團隊。

**Trunk-based development**：大多數變更快速合併到 trunk/main，搭配 feature flags。適合高成熟度 CI/CD、測試自動化完善的大型工程團隊。

## Branch Protection

保護重要分支（`main`、`release/*`），要求合併前必須滿足條件：require PR review、require status checks、require conversation resolution、require signed commits、require linear history、restrict who can push、block force pushes、block deletions。

建議 main branch 保護規則：

```text
- Require a pull request before merging
- Require approvals: 1 或 2
- Require review from Code Owners
- Dismiss stale approvals when new commits are pushed
- Require status checks to pass
- Require branches to be up to date before merging
- Require conversation resolution
- Do not allow force pushes
- Do not allow deletions
```

## Rulesets

比傳統 Branch Protection 更可組合、可觀察、可套用多規則的政策機制，可控制 branch、tag、push 行為，包括限制檔案路徑/大小/副檔名。

| 項目 | Branch Protection | Rulesets |
|---|---|---|
| 套用方式 | 單一 branch rule | 多個 ruleset 可同時作用（可 layer） |
| 可見性 | 管理者設定 | Read access 即可看到 active rulesets |
| 適合 | 小型 repo、簡單保護 | 組織治理、多 repo、多政策 |

## Merge Queue

適合高頻 PR 專案：PR 滿足條件後排隊，並以最新 base + queue 中變更重新測試，降低 main 被多個 PR 互相破壞的機率。

## Force push 原則

禁止在 `main`/`develop`/`release/*`/共享 feature branch force push；個人 feature branch 可有限使用，並搭配 `git push --force-with-lease`（見 [[git-remote-collaboration]]）。

## 與其他頁面的關聯

CODEOWNERS review 要求與 PR review 類型見 [[github-repository-and-project-management]]；status checks 通常來自 [[github-actions-cicd]] 的 CI workflow；Fork Flow 的具體 Git 指令見 [[git-remote-collaboration]]。
