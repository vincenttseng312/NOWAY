---
type: concept
title: "Git 分支管理、Merge、Rebase 與衝突處理"
tags: [git]
sources: [git-github-complete-notes]
created: 2026-07-09
updated: 2026-07-09
---

# Git 分支管理、Merge、Rebase 與衝突處理

涵蓋分支的建立/切換/刪除/命名、merge 與 rebase 的差異與黃金規則、cherry-pick/revert/reset，以及合併衝突的處理方式。

## Branch 管理

```bash
git switch -c feature/login       # 建立並切換（新語法，取代 git checkout -b）
git switch main                   # 切換分支
git branch -a                     # 查看全部分支（本機 + 遠端）
git branch -d feature/login       # 刪除已合併的本機分支
git branch -D feature/login       # 強制刪除
git push origin --delete feature/login   # 刪除遠端分支
git branch -m old-name new-name   # 重新命名
```

命名規範建議：`feature/login-page`、`fix/api-timeout`、`hotfix/payment-crash`、`release/v1.2.0`；避免 `new`、`fix`、`test123`、`final-final` 這類無意義名稱。

## Merge

Merge 把另一個分支的變更整合進目前分支：

- **Fast-forward merge**：若 base 分支沒有分岔，Git 只把指標往前移，不產生 merge commit。
- **Three-way merge**：若兩邊都有新 commit，Git 找共同祖先，產生一個 merge commit。

```bash
git switch main
git merge feature/login
```

## Rebase

Rebase 把目前分支的 commit 重新套用到另一個 base 上，產生線性歷史，但會改寫目前分支的 commit（新 commit 的 hash 會變）：

```bash
git switch feature/login
git rebase main
```

| 項目 | Merge | Rebase |
|---|---|---|
| 歷史 | 保留分岔與合併 | 線性歷史 |
| 是否改寫 commit | 不改寫 | 改寫目前分支 commits |
| 適合 | 共享分支、保留脈絡 | 個人 feature branch 整理歷史 |

**Rebase 黃金規則：不要 rebase 已經推送且多人共用的 branch**（`main`/`develop`/`release`/共用分支不可 rebase；只能 rebase 自己的、尚未被他人基於它開發的分支）。

Interactive rebase 可整理最近幾個 commit：`git rebase -i HEAD~3`，操作包含 `pick`（保留）、`reword`（改訊息）、`edit`（停下修改）、`squash`（合併並保留訊息）、`fixup`（合併並丟棄訊息）、`drop`（移除）。

## Cherry-pick 與 Revert

```bash
git cherry-pick <commit>    # 把某個 commit 套用到目前分支，常用於 hotfix 從 main 搬到 release branch
git revert <commit>         # 建立新 commit 反向取消某 commit 的變更，適合已 push 到共享 branch 的情境
```

## Reset

`reset` 會移動目前分支指標，三種模式影響範圍不同：

| 模式 | Commit | Staging | Working Tree |
|---|---|---|---|
| `--soft` | 回到前一個 | 保留 | 保留 |
| `--mixed` | 回到前一個 | 取消 staged | 保留 |
| `--hard` | 回到前一個 | 取消 | **丟掉** |

> ✅ 此表已於 2026-07-09 用真實 git 實測驗證（六驗證點全中），信心 High。實驗與可重跑腳本見 [[git-reset-modes]]。記憶法：三模式 **Commit 一定退**，差別只在兩個開關——`--soft` 兩開關全保留、`--mixed` 關掉 staging、`--hard` 兩個都關（連 working tree 一起丟）。

`--hard` 會丟掉未保存的變更，使用前務必先 `git status` 確認。

## 衝突處理

衝突發生於兩個分支修改同一段內容，Git 無法自動判斷保留哪一邊：

```text
<<<<<<< HEAD
目前分支的內容
=======
被合併進來的內容
>>>>>>> feature/login
```

解衝突流程（merge）：`git status` → 編輯衝突檔案 → `git add <file>` → `git commit`。Rebase 情境則是 `git add <file>` → `git rebase --continue`（放棄用 `git rebase --abort`／`git merge --abort`）。也可用 `git checkout --ours file.txt` / `--theirs file.txt` 快速選邊——**注意 rebase 情境下 ours/theirs 的直覺可能與 merge 相反，操作前務必先確認**。

減少衝突的方法：小步 commit、常同步 main、避免多人同時大改同一檔案、格式化與功能 commit 分開、使用 code ownership、PR 不要太大。

## 與其他頁面的關聯

Reset/rebase 出錯時的救援方式見 [[git-undo-and-recovery]]（核心工具是 reflog，見 [[git-core-concepts]]）；遠端 push/pull 的 force push 原則見 [[git-remote-collaboration]]；GitHub 端的合併方式對應（squash/merge commit/rebase and merge）見 [[github-repository-and-project-management]]。
