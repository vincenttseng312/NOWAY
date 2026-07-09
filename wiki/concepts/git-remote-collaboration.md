---
type: concept
title: "Git 遠端協作"
tags: [git]
sources: [git-github-complete-notes]
created: 2026-07-09
updated: 2026-07-09
---

# Git 遠端協作

涵蓋 origin、fetch/pull/push、tracking branch，以及 force push 的安全做法。

## origin 只是慣例命名

`origin` 不是 Git 或 GitHub 的保留字，只是 `git clone` 時 Git 預設幫遠端 repo 取的名稱：

```bash
git remote -v                                   # 查看目前遠端
git remote add origin git@github.com:USER/REPO.git
git remote set-url origin <new-url>             # 更換遠端 URL
```

## Fetch / Pull / Push

```bash
git fetch origin        # 只更新遠端追蹤分支（如 origin/main），不改本機分支
git pull                 # 約等於 fetch + merge，或設定 rebase 時等於 fetch + rebase
git pull --rebase        # 建議團隊統一策略，避免多餘的 merge commit
git push origin main
git push -u origin feature/login   # 第一次推分支並設定 upstream
```

## Tracking branch / upstream

```bash
git branch -vv                                      # 查看每個本機分支追蹤哪個遠端分支
git branch --set-upstream-to=origin/main main        # 手動設定 upstream
```

## Force push 的安全做法

```bash
git push --force              # 危險：直接覆蓋遠端歷史
git push --force-with-lease   # 較安全：會先檢查遠端是否有你不知道的新 commit，降低覆蓋他人工作的風險
```

Force push 原則：**禁止**在 `main`/`develop`/`release/*`/共享 feature branch 上使用；只能在個人 feature branch、且尚未被他人基於它開發時，搭配 `--force-with-lease` 有限使用。

## Prune 清掉已刪除的遠端分支參照

```bash
git fetch --prune
git config --global fetch.prune true   # 設定自動 prune
```

避免本機一直看到早已在遠端刪除、但本機還殘留追蹤參照的分支。

## Fork Flow 中的遠端協作

開源貢獻常見設定第二個遠端 `upstream`：

```bash
git remote add upstream https://github.com/ORIGINAL_OWNER/REPO.git
git fetch upstream
git switch main
git merge upstream/main      # 或 git pull upstream main --rebase
git push origin main
```

完整流程比較見 [[github-workflow-strategies-and-branch-protection]]。

## 與其他頁面的關聯

Merge/rebase 的機制本身見 [[git-branching-merge-rebase]]；`--force` 誤用後的救援見 [[git-undo-and-recovery]]；GitHub 端的分支保護（阻擋 force push/deletion）見 [[github-workflow-strategies-and-branch-protection]]；SSH/PAT 等驗證方式見 [[github-cli-and-security]]。
