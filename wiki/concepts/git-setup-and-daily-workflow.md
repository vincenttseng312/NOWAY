---
type: concept
title: "Git 安裝設定與日常工作流程"
tags: [git]
sources: [git-github-complete-notes]
created: 2026-07-09
updated: 2026-07-09
---

# Git 安裝設定與日常工作流程

涵蓋從安裝、初始設定到每天實際使用 Git 的完整循環：建立/取得 repo、`status`/`add`/`commit`/`push`/`pull`、查看差異與歷史、commit message 規範。

## 安裝與基本設定

Windows 用 `winget install --id Git.Git -e` 或 Git for Windows；macOS 用 `brew install git`；Linux 依發行版用 `apt`/`dnf`/`pacman`。

必要的初始設定：

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
```

換行符號：Windows 建議 `core.autocrlf true`，macOS/Linux 建議 `core.autocrlf input`；更嚴謹的團隊改用 `.gitattributes` 統一控制（見 [[git-tag-release-and-repo-config]]）。

Pull 行為建議明確設定，避免 `git pull` 時不確定要 merge 還 rebase：

```bash
git config --global pull.rebase true
git config --global rebase.autoStash true
```

常用 alias 範例：`git config --global alias.st status`、`alias.lg "log --oneline --graph --decorate --all"` 等，設定後用 `git st`、`git lg` 即可。

## 建立與取得 Repository

```bash
git init                                          # 建立新的本機 repo
git clone https://github.com/USER/REPO.git        # HTTPS clone
git clone git@github.com:USER/REPO.git            # SSH clone
git clone -b develop --single-branch <url>        # 只 clone 特定 branch
git clone --depth 1 <url>                         # 淺層 clone，適合 CI，不適合完整歷史分析
```

## 日常基本流程

```bash
git status              # 查看 untracked / modified / staged
git add README.md       # 加入單一檔案
git add .                # 加入全部變更
git add -p               # 互動式加入，適合把同一檔案的不同修改拆成不同 commit
git commit -m "feat: add user login"
git push -u origin feature/login    # 第一次推新 branch，之後可簡化為 git push
```

`git fetch` 只下載遠端資訊、不改工作分支；`git pull` 約等於 `fetch` + `merge`（或設定 rebase 時等於 `fetch` + `rebase`）。遠端協作細節見 [[git-remote-collaboration]]。

## 檢查狀態與比較差異

```bash
git status -sb                       # 精簡版狀態
git diff                             # 尚未 staged 的差異
git diff --staged                    # 已 staged 的差異
git diff commitA commitB             # 比較兩個 commit
git diff --stat commitA commitB      # 只看統計
git log -- path/to/file              # 某檔案的 commit 歷史
git log -p -- path/to/file           # 含每次變動內容
git blame path/to/file               # 查看每一行最後修改者（用於理解歷史，非究責工具）
```

## Commit 寫法與歷史管理

一個好 commit：單一目的、可讀可回復、訊息清楚、不混雜格式化/重構/功能/修 bug、不含機密。

Conventional Commits 格式：`<type>(optional scope): <description>`，常見 type：

| Type | 用途 |
|---|---|
| feat | 新功能 |
| fix | 修 bug |
| docs | 文件 |
| style | 格式，不影響邏輯 |
| refactor | 重構 |
| test | 測試 |
| chore | 雜務 |
| ci | CI/CD |
| perf | 效能改善 |

範例：`feat(auth): add login endpoint`。

修改最後一次 commit：

```bash
git commit --amend                          # 修改訊息或內容
git add missing-file.txt
git commit --amend --no-edit                # 補進漏掉的檔案，訊息不變
```

**若 commit 已 push 到共享 branch，amend 會改寫歷史，需特別小心**（同樣的黃金規則也適用於 rebase，見 [[git-branching-merge-rebase]]）。

查看歷史：`git log --oneline --graph --decorate --all` 是最常用的精簡圖形視圖。

## 與其他頁面的關聯

分支與合併見 [[git-branching-merge-rebase]]；遠端推拉見 [[git-remote-collaboration]]；commit 規範也對應 GitHub 端的 [[github-repository-and-project-management]] 中的 PR 描述與 review 慣例。
