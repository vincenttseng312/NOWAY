---
type: concept
title: "Git 核心心智模型"
tags: [git]
sources: [git-github-complete-notes]
created: 2026-07-09
updated: 2026-07-09
---

# Git 核心心智模型

Git 是分散式版本控制系統：它把專案在不同時間點的狀態記錄成一連串 commit，讓使用者可以比較、回復、分支開發、合併協作。GitHub 則是建立在 Git 之上的雲端協作平台，提供 Pull Request、Issue、Actions、Pages、Security 等團隊開發功能——Git 可完全離線、不依賴 GitHub 使用；`git commit` 只在本機建立版本，必須 `git push` 才會上傳。

## Git 最重要的四個區域

```text
Working Tree  --git add-->  Index/Staging Area  --git commit-->  Local Repository  --git push-->  Remote Repository
```

| 區域 | 代表意思 | 常用指令 |
|---|---|---|
| Working Tree | 目前正在編輯的檔案狀態 | `git status`, `git diff` |
| Index / Staging Area | 準備進入下一個 commit 的內容 | `git add`, `git restore --staged` |
| Local Repository | 本機 `.git` 中的 commit 歷史 | `git commit`, `git log`, `git reset` |
| Remote Repository | GitHub 等遠端 repo | `git fetch`, `git pull`, `git push` |

## 快照模型，不是差異模型

一般人容易誤以為 Git 每次只存 diff；實際上每次 commit 是整個專案目錄的一份快照（Git 內部透過物件、壓縮與 packfile 提升儲存效率）。

## 四種核心資料與 Blob/Tree/Commit/Tag

Git 的資料模型可理解成四類：Objects（commit/tree/blob/tag object）、References（branch/tag/remote-tracking branch）、Index（staging area）、Reflog（reference 變動記錄）。

| 物件 | 用途 | 類比 |
|---|---|---|
| Blob | 儲存檔案內容，不含檔名 | 一份檔案的內容 |
| Tree | 儲存目錄結構，指向 blob 或其他 tree | 資料夾快照 |
| Commit | 指向一個 tree，並記錄作者、時間、訊息、父 commit | 一次版本紀錄 |
| Tag object | 標記特定 commit，通常用於 release | 版本標籤 |

## Branch 本質上是指標

Branch 不是一份複製的資料夾，而只是指向某個 commit 的可移動指標：

```text
main -> C1 -> C2 -> C3
                  ↑
               feature
```

在 `feature` 分支 commit 時，新 commit 接在該分支指標後面，`main` 不受影響。這個心智模型是理解 [[git-branching-merge-rebase]] 中 merge/rebase 差異的基礎。

## HEAD 是什麼

`HEAD` 表示目前所在位置，通常是「目前 checkout 到某分支，該分支指向某 commit」。若直接 `git switch --detach <commit>` checkout 到某個 commit 而非分支，會進入 **detached HEAD** 狀態——不是錯誤，但若在此狀態下 commit 又沒建立分支保存，之後可能難以找回（此時要用到 reflog，見下）。

## Index / Staging Area

Index 是「下一個 commit 的草稿」。`git add file.txt` 不是上傳也不是 commit，只是把目前檔案內容放入 staging area；`git commit` 才會把 staging area 的內容寫成一個 commit。

## Reflog：Git 的救命繩

Reflog 記錄本機 reference（如 `HEAD`、branch tip）曾經指到哪裡。當 reset、rebase、amend、誤刪 branch 時，通常可以用 `git reflog` 找回，再用 `git switch -c rescue <commit-hash>` 救回。完整救援流程見 [[git-undo-and-recovery]]。

## 設定層級

Git 設定分三層：`system`（全系統）、`global`（目前使用者所有 repo）、`local`（目前 repo），用 `git config --list --show-origin` 可查看每項設定實際來自哪一層。基本安裝與設定指令見 [[git-setup-and-daily-workflow]]。

## 與其他頁面的關聯

這裡的心智模型是理解 [[git-branching-merge-rebase]]（merge/rebase/reset）與 [[git-undo-and-recovery]]（reflog 救援）的基礎；GitHub 平台功能見 [[github-repository-and-project-management]]。
