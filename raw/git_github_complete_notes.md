# Git 與 GitHub 最完整使用筆記

> 版本：2026-07-09  
> 適用對象：初學者、開發者、資安研究者、DevOps、團隊維護者  
> 目標：從 Git 基礎原理、日常指令、分支協作、GitHub 平台功能、CI/CD、安全治理，到疑難排解，整理成一份可長期查閱的 Markdown 筆記。

---

## 目錄

- [0. 快速總覽](#0-快速總覽)
- [1. Git 與 GitHub 的差別](#1-git-與-github-的差別)
- [2. Git 核心心智模型](#2-git-核心心智模型)
- [3. 安裝與初始設定](#3-安裝與初始設定)
- [4. 建立與取得 Repository](#4-建立與取得-repository)
- [5. Git 日常基本流程](#5-git-日常基本流程)
- [6. 檢查狀態與比較差異](#6-檢查狀態與比較差異)
- [7. Commit 寫法與歷史管理](#7-commit-寫法與歷史管理)
- [8. Branch 分支管理](#8-branch-分支管理)
- [9. Merge、Rebase、Cherry-pick、Revert](#9-mergerebasecherry-pickrevert)
- [10. Remote 遠端協作](#10-remote-遠端協作)
- [11. 衝突處理](#11-衝突處理)
- [12. Undo / Recovery 救援大全](#12-undo--recovery-救援大全)
- [13. Stash 暫存未完成工作](#13-stash-暫存未完成工作)
- [14. Tag、Release 與版本管理](#14-tagrelease-與版本管理)
- [15. .gitignore、.gitattributes 與換行處理](#15-gitignoregitattributes-與換行處理)
- [16. Git Hooks](#16-git-hooks)
- [17. Git Worktree](#17-git-worktree)
- [18. Git Submodule 與 Subtree](#18-git-submodule-與-subtree)
- [19. Git LFS 大檔案管理](#19-git-lfs-大檔案管理)
- [20. 進階 Git 指令](#20-進階-git-指令)
- [21. GitHub 基礎功能](#21-github-基礎功能)
- [22. GitHub Repository 設定](#22-github-repository-設定)
- [23. GitHub Issues、Labels、Milestones、Projects](#23-github-issueslabelsmilestonesprojects)
- [24. Pull Request 與 Code Review](#24-pull-request-與-code-review)
- [25. GitHub Flow、Fork Flow、Git Flow](#25-github-flowfork-flowgit-flow)
- [26. GitHub Branch Protection 與 Rulesets](#26-github-branch-protection-與-rulesets)
- [27. CODEOWNERS 與 PR Template](#27-codeowners-與-pr-template)
- [28. GitHub Actions CI/CD](#28-github-actions-cicd)
- [29. GitHub Actions Secrets、Variables、Permissions](#29-github-actions-secretsvariablespermissions)
- [30. GitHub Pages](#30-github-pages)
- [31. GitHub CLI：gh](#31-github-cligh)
- [32. GitHub Security：Dependabot、CodeQL、Secret Scanning](#32-github-securitydependabotcodeqlsecret-scanning)
- [33. GitHub 權限、Organization、Team](#33-github-權限organizationteam)
- [34. SSH、HTTPS、PAT 與簽署 Commit](#34-sshhttpspat-與簽署-commit)
- [35. 常見錯誤與解法](#35-常見錯誤與解法)
- [36. 實戰工作流範本](#36-實戰工作流範本)
- [37. Git 指令速查表](#37-git-指令速查表)
- [38. 團隊規範模板](#38-團隊規範模板)
- [39. 學習路線圖](#39-學習路線圖)
- [40. 參考資料](#40-參考資料)

---

# 0. 快速總覽

## 0.1 一句話理解 Git

Git 是一套**分散式版本控制系統**。它不是單純備份資料夾，而是把專案在不同時間點的狀態記錄成一連串 commit，讓你可以比較、回復、分支開發、合併協作。

## 0.2 一句話理解 GitHub

GitHub 是基於 Git 的雲端協作平台。它不只放程式碼，還提供 Pull Request、Issue、Code Review、Actions、Pages、Security、Projects、Organization、Rulesets 等團隊開發功能。

## 0.3 Git 最重要的四個區域

```text
Working Tree        Index / Staging Area        Local Repository        Remote Repository
工作目錄             暫存區                       本機版本庫               遠端版本庫

你正在改檔案   ->    git add    ->              git commit    ->         git push
```

| 區域 | 代表意思 | 常用指令 |
|---|---|---|
| Working Tree | 你目前正在編輯的檔案狀態 | `git status`, `git diff` |
| Index / Staging Area | 準備進入下一個 commit 的內容 | `git add`, `git restore --staged` |
| Local Repository | 本機 `.git` 中的 commit 歷史 | `git commit`, `git log`, `git reset` |
| Remote Repository | GitHub / GitLab / Bitbucket 上的遠端 repo | `git fetch`, `git pull`, `git push` |

## 0.4 最常用的日常流程

```bash
# 1. 查看目前狀態
git status

# 2. 更新遠端變更
git pull --rebase

# 3. 建立工作分支
git switch -c feature/login-page

# 4. 修改檔案後查看差異
git diff

# 5. 加入暫存區
git add .

# 6. 建立 commit
git commit -m "feat: add login page"

# 7. 推到 GitHub
git push -u origin feature/login-page

# 8. 開 Pull Request
# GitHub 網頁或 gh pr create
```

---

# 1. Git 與 GitHub 的差別

## 1.1 Git 是工具，GitHub 是平台

| 項目 | Git | GitHub |
|---|---|---|
| 本質 | 版本控制系統 | 雲端協作平台 |
| 是否可離線 | 可以 | 不行，通常需要網路 |
| 主要用途 | 追蹤檔案歷史、分支、合併 | 儲存遠端 repo、PR、Issue、CI/CD、權限管理 |
| 安裝位置 | 本機電腦 | GitHub 伺服器 / 網站 |
| 代表指令或功能 | `git commit`, `git branch`, `git merge` | Pull Request, Issues, Actions, Pages, Security |

## 1.2 常見誤解

### 誤解 1：GitHub 就是 Git

不是。GitHub 使用 Git 作為底層版本控制，但 Git 可以完全不依賴 GitHub 使用。

### 誤解 2：`git commit` 就等於上傳到 GitHub

不是。`git commit` 只是在本機建立版本。要上傳到 GitHub，需要 `git push`。

### 誤解 3：刪掉 GitHub 上的 repo，本機就不能用 Git

不是。本機資料夾中的 `.git` 還在，就還是一個 Git repository。

### 誤解 4：Git 是雲端備份

Git 可以當作版本歷史，但不是傳統備份工具。大檔案、機密、資料庫 dump、build 產物通常不適合直接放進 Git。

---

# 2. Git 核心心智模型

## 2.1 Git 儲存的不是「檔案差異」，而是「快照」

一般人容易以為 Git 每次只存 diff。實際上 Git 的心智模型更接近：每次 commit 是專案目錄的一個快照。Git 內部會透過物件、壓縮與 packfile 提升效率。

## 2.2 Git 的四種核心資料

Git 官方資料模型可以理解成四類：

1. Objects：commit、tree、blob、tag object
2. References：branch、tag、remote-tracking branch
3. Index：也就是 staging area
4. Reflog：reference 變動記錄

## 2.3 Blob、Tree、Commit、Tag

| 物件 | 用途 | 類比 |
|---|---|---|
| Blob | 儲存檔案內容，不含檔名 | 一份檔案的內容 |
| Tree | 儲存目錄結構，指向 blob 或其他 tree | 資料夾快照 |
| Commit | 指向一個 tree，並記錄作者、時間、訊息、父 commit | 一次版本紀錄 |
| Tag object | 標記特定 commit，通常用於 release | 版本標籤 |

示意：

```text
commit
  ├── tree
  │   ├── blob: README.md
  │   ├── blob: main.py
  │   └── tree: src/
  │       └── blob: app.py
  └── parent commit
```

## 2.4 Branch 本質上是指標

Branch 不是一整份複製的資料夾。Branch 本質上只是指向某個 commit 的 movable pointer。

```text
main -> C1 -> C2 -> C3
                  ↑
               feature
```

當你在 `feature` 分支 commit，新 commit 會接在目前分支指標後面：

```text
main    -> C1 -> C2 -> C3
                         \
feature                  C4 -> C5
```

## 2.5 HEAD 是什麼

`HEAD` 表示你目前所在的位置。

常見情況：

```text
HEAD -> main -> C3
```

代表你目前 checkout 到 `main` 分支，而 `main` 指向 C3。

如果你直接 checkout 某個 commit：

```bash
git switch --detach <commit>
```

就會進入 detached HEAD：

```text
HEAD -> C2
main -> C3
```

Detached HEAD 不是錯誤，但如果在 detached 狀態下 commit，又沒有建立分支保存，之後可能難以找到。

## 2.6 Index / Staging Area 是什麼

Index 是「下一個 commit 的草稿」。

```bash
git add file.txt
```

不是把檔案上傳，也不是 commit，而是把目前的檔案內容放入 staging area。

```bash
git commit
```

才會把 staging area 的內容寫成 commit。

## 2.7 Reflog 是 Git 救命繩

Reflog 記錄本機 reference 的移動，例如 `HEAD`、branch tip 曾經指到哪裡。當你 reset、rebase、amend、誤刪 branch 時，常常可以用 reflog 找回。

```bash
git reflog
```

常見救援：

```bash
git reflog
git switch -c rescue <commit-hash>
```

## 2.8 Git 的三種重要 ID

| 名稱 | 說明 |
|---|---|
| Commit hash | commit 的雜湊值，例如 `a1b2c3d...` |
| Short hash | commit hash 前幾碼，例如 `a1b2c3d` |
| Process ID? | 不是 Git 概念，別跟 commit hash 混淆 |

---

# 3. 安裝與初始設定

## 3.1 安裝 Git

### Windows

常見方式：

```powershell
winget install --id Git.Git -e
```

或下載 Git for Windows。

建議使用：

- Git Bash
- PowerShell
- Windows Terminal
- VS Code terminal

### macOS

```bash
brew install git
```

或安裝 Xcode Command Line Tools：

```bash
xcode-select --install
```

### Linux

Debian / Ubuntu：

```bash
sudo apt update
sudo apt install git
```

Fedora：

```bash
sudo dnf install git
```

Arch：

```bash
sudo pacman -S git
```

## 3.2 查看版本

```bash
git --version
```

## 3.3 設定使用者名稱與 Email

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

查看：

```bash
git config --global --list
```

單一 repo 設定：

```bash
git config user.name "Work Name"
git config user.email "work@example.com"
```

## 3.4 設定預設分支名稱

```bash
git config --global init.defaultBranch main
```

## 3.5 設定預設編輯器

VS Code：

```bash
git config --global core.editor "code --wait"
```

Vim：

```bash
git config --global core.editor "vim"
```

Nano：

```bash
git config --global core.editor "nano"
```

## 3.6 設定換行符號

Windows 常見：

```bash
git config --global core.autocrlf true
```

macOS / Linux 常見：

```bash
git config --global core.autocrlf input
```

更嚴謹的團隊通常使用 `.gitattributes` 控制換行。

## 3.7 設定 pull 行為

避免 `git pull` 時不知道要 merge 還 rebase：

```bash
# 偏好 rebase
git config --global pull.rebase true

# 偏好 merge
git config --global pull.rebase false

# 僅允許 fast-forward
git config --global pull.ff only
```

個人建議：

```bash
git config --global pull.rebase true
git config --global rebase.autoStash true
```

## 3.8 設定常用 alias

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.sw switch
git config --global alias.br branch
git config --global alias.cm commit
git config --global alias.lg "log --oneline --graph --decorate --all"
git config --global alias.last "log -1 HEAD --stat"
```

使用：

```bash
git st
git lg
```

## 3.9 查看設定來源

```bash
git config --list --show-origin
```

設定層級：

| 層級 | 位置 | 說明 |
|---|---|---|
| system | Git 安裝層級 | 全系統 |
| global | 使用者層級 | 目前使用者所有 repo |
| local | repo 層級 | 目前 repo |

---

# 4. 建立與取得 Repository

## 4.1 建立新的本機 repo

```bash
mkdir my-project
cd my-project
git init
```

建立第一個檔案：

```bash
echo "# My Project" > README.md
git add README.md
git commit -m "docs: add README"
```

## 4.2 Clone 遠端 repo

HTTPS：

```bash
git clone https://github.com/USER/REPO.git
```

SSH：

```bash
git clone git@github.com:USER/REPO.git
```

指定資料夾名稱：

```bash
git clone https://github.com/USER/REPO.git local-folder-name
```

只 clone 特定 branch：

```bash
git clone -b develop --single-branch https://github.com/USER/REPO.git
```

淺層 clone：

```bash
git clone --depth 1 https://github.com/USER/REPO.git
```

淺層 clone 適合 CI 或只需要最新版本，但不適合完整歷史分析。

## 4.3 檢查 repo 狀態

```bash
git status
```

## 4.4 檢查遠端來源

```bash
git remote -v
```

## 4.5 新增遠端來源

```bash
git remote add origin git@github.com:USER/REPO.git
```

更換遠端 URL：

```bash
git remote set-url origin git@github.com:USER/REPO.git
```

---

# 5. Git 日常基本流程

## 5.1 修改檔案後查看狀態

```bash
git status
```

你會看到：

- untracked files：Git 尚未追蹤的新檔案
- modified：已追蹤但被修改的檔案
- staged：已加入 staging area 的變更

## 5.2 加入 staging area

加入單一檔案：

```bash
git add README.md
```

加入資料夾：

```bash
git add src/
```

加入全部變更：

```bash
git add .
```

互動式加入：

```bash
git add -p
```

`git add -p` 很重要，適合把一個檔案中的不同修改拆成不同 commit。

## 5.3 建立 commit

```bash
git commit -m "feat: add user login"
```

開啟編輯器輸入多行 commit message：

```bash
git commit
```

## 5.4 推送到遠端

第一次推新 branch：

```bash
git push -u origin feature/login
```

之後可簡化為：

```bash
git push
```

## 5.5 更新本機

```bash
git fetch
```

`fetch` 只下載遠端資訊，不改你的工作分支。

```bash
git pull
```

`pull` 約等於：

```bash
git fetch
git merge origin/current-branch
```

若設定 rebase，則約等於：

```bash
git fetch
git rebase origin/current-branch
```

---

# 6. 檢查狀態與比較差異

## 6.1 查看狀態

```bash
git status
```

精簡版：

```bash
git status -sb
```

## 6.2 查看尚未 staged 的差異

```bash
git diff
```

## 6.3 查看 staged 差異

```bash
git diff --staged
```

或：

```bash
git diff --cached
```

## 6.4 比較兩個 commit

```bash
git diff commitA commitB
```

只看檔案名稱：

```bash
git diff --name-only commitA commitB
```

只看統計：

```bash
git diff --stat commitA commitB
```

## 6.5 查看某個檔案歷史

```bash
git log -- path/to/file
```

查看每次變動內容：

```bash
git log -p -- path/to/file
```

## 6.6 查看誰改了某一行

```bash
git blame path/to/file
```

只看某個範圍：

```bash
git blame -L 10,30 path/to/file
```

注意：`git blame` 用於理解歷史，不應當成責罵工具。

---

# 7. Commit 寫法與歷史管理

## 7.1 好 commit 的原則

一個好 commit 應該：

1. 單一目的
2. 可讀、可回復
3. 訊息清楚
4. 不混雜格式化、重構、功能、修 bug
5. 不包含機密、密碼、token、私鑰

## 7.2 Commit message 建議格式

常見 Conventional Commits：

```text
<type>(optional scope): <description>

[optional body]

[optional footer]
```

範例：

```text
feat(auth): add login endpoint
```

```text
fix(api): handle empty response
```

```text
docs: update installation guide
```

## 7.3 常見 type

| Type | 用途 |
|---|---|
| feat | 新功能 |
| fix | 修 bug |
| docs | 文件 |
| style | 格式，不影響邏輯 |
| refactor | 重構，不新增功能、不修 bug |
| test | 測試 |
| chore | 雜務，例如設定、依賴 |
| build | 建置系統 |
| ci | CI/CD |
| perf | 效能改善 |
| revert | 回復 commit |

## 7.4 修改最後一次 commit message

```bash
git commit --amend
```

直接改訊息：

```bash
git commit --amend -m "fix: correct typo"
```

如果 commit 已 push 到共享 branch，amend 會改寫歷史，要非常小心。

## 7.5 把漏掉的檔案補進最後一次 commit

```bash
git add missing-file.txt
git commit --amend --no-edit
```

## 7.6 查看 commit 歷史

```bash
git log
```

精簡圖形：

```bash
git log --oneline --graph --decorate --all
```

查看統計：

```bash
git log --stat
```

查看 patch：

```bash
git log -p
```

---

# 8. Branch 分支管理

## 8.1 建立分支

```bash
git branch feature/login
```

建立並切換：

```bash
git switch -c feature/login
```

舊指令：

```bash
git checkout -b feature/login
```

## 8.2 切換分支

```bash
git switch main
```

## 8.3 查看分支

本機分支：

```bash
git branch
```

遠端分支：

```bash
git branch -r
```

全部分支：

```bash
git branch -a
```

## 8.4 刪除分支

刪除已合併本機分支：

```bash
git branch -d feature/login
```

強制刪除本機分支：

```bash
git branch -D feature/login
```

刪除遠端分支：

```bash
git push origin --delete feature/login
```

## 8.5 重新命名分支

目前分支改名：

```bash
git branch -m new-name
```

指定分支改名：

```bash
git branch -m old-name new-name
```

若遠端也要改：

```bash
git push origin --delete old-name
git push -u origin new-name
```

## 8.6 分支命名規範

建議：

```text
feature/login-page
fix/api-timeout
hotfix/payment-crash
release/v1.2.0
chore/update-deps
docs/git-guide
```

不要：

```text
new
fix
mybranch
test123
final-final
```

---

# 9. Merge、Rebase、Cherry-pick、Revert

## 9.1 Merge 是什麼

Merge 是把另一個分支的變更整合進目前分支。

```bash
git switch main
git merge feature/login
```

### Fast-forward merge

如果 main 沒有分岔，Git 只需要把 main 指標往前移。

```text
main -> C1 -> C2
feature -> C3
```

merge 後：

```text
main/feature -> C1 -> C2 -> C3
```

### Three-way merge

如果兩邊都有新 commit，Git 會找共同祖先，產生 merge commit。

```text
      C3 feature
     /
C1--C2--C4 main
```

merge 後：

```text
      C3 ----
     /       \
C1--C2--C4---M main
```

## 9.2 Rebase 是什麼

Rebase 會把目前分支的 commit 重新套用到另一個 base 上。

```bash
git switch feature/login
git rebase main
```

Rebase 前：

```text
      A---B feature
     /
C---D---E main
```

Rebase 後：

```text
C---D---E---A'---B' feature
```

注意：`A'`、`B'` 是新 commit，hash 會改變。

## 9.3 Merge vs Rebase

| 項目 | Merge | Rebase |
|---|---|---|
| 歷史 | 保留分岔與合併 | 線性歷史 |
| 是否改寫 commit | 不改寫 | 會改寫目前分支 commits |
| 適合 | 共享分支、保留脈絡 | 個人 feature branch 整理歷史 |
| 風險 | 歷史較雜 | 對已共享分支 rebase 會造成麻煩 |

## 9.4 Rebase 黃金規則

> 不要 rebase 已經推送且多人共用的 branch。

可以 rebase：

```text
自己的 feature branch
尚未被他人基於它開發的 branch
```

不要 rebase：

```text
main
develop
release
多人共用分支
```

## 9.5 Interactive rebase

整理最近 3 個 commit：

```bash
git rebase -i HEAD~3
```

常見操作：

| 指令 | 意義 |
|---|---|
| pick | 保留 commit |
| reword | 修改 commit message |
| edit | 停下來修改 commit |
| squash | 合併到前一個 commit，保留訊息 |
| fixup | 合併到前一個 commit，丟掉訊息 |
| drop | 移除 commit |

## 9.6 Cherry-pick

把某個 commit 套用到目前分支：

```bash
git cherry-pick <commit>
```

常見用途：

- hotfix 從 main 搬到 release branch
- 只挑某個 bug fix，不合併整個 feature branch

## 9.7 Revert

建立一個新的 commit，反向取消某個 commit 的變更：

```bash
git revert <commit>
```

適合已經 push 到共享 branch 的情境。

## 9.8 Reset

`reset` 會移動目前 branch 指標。

```bash
git reset --soft HEAD~1
git reset --mixed HEAD~1
git reset --hard HEAD~1
```

| 模式 | Commit | Staging | Working Tree |
|---|---|---|---|
| `--soft` | 回到前一個 | 保留 | 保留 |
| `--mixed` | 回到前一個 | 取消 staged | 保留 |
| `--hard` | 回到前一個 | 取消 | 丟掉 |

警告：`--hard` 會丟掉未保存變更，使用前先確認。

---

# 10. Remote 遠端協作

## 10.1 origin 是什麼

`origin` 只是遠端 repository 的預設名稱。不是 GitHub 的特殊保留字，只是 clone 時 Git 預設幫你命名。

查看：

```bash
git remote -v
```

## 10.2 新增遠端

```bash
git remote add origin git@github.com:USER/REPO.git
```

## 10.3 Fetch

```bash
git fetch origin
```

更新遠端追蹤分支，例如：

```text
origin/main
origin/develop
origin/feature/login
```

不會直接改你的本機分支。

## 10.4 Pull

```bash
git pull
```

等於 fetch + merge 或 fetch + rebase，取決於設定。

建議團隊統一策略：

```bash
git pull --rebase
```

## 10.5 Push

```bash
git push origin main
```

第一次推本機分支並設定 upstream：

```bash
git push -u origin feature/login
```

## 10.6 Tracking branch / upstream

查看：

```bash
git branch -vv
```

設定：

```bash
git branch --set-upstream-to=origin/main main
```

## 10.7 Force push 與 safer force push

危險：

```bash
git push --force
```

較安全：

```bash
git push --force-with-lease
```

`--force-with-lease` 會檢查遠端是否有你不知道的新 commit，降低覆蓋他人工作的風險。

## 10.8 Prune 清掉已不存在的遠端分支參照

```bash
git fetch --prune
```

設定自動 prune：

```bash
git config --global fetch.prune true
```

---

# 11. 衝突處理

## 11.1 衝突為什麼發生

當兩個分支修改同一段內容，而 Git 無法自動判斷該保留哪一邊，就會產生 conflict。

## 11.2 衝突標記

```text
<<<<<<< HEAD
目前分支的內容
=======
被合併進來的內容
>>>>>>> feature/login
```

你需要手動整理成最終內容，移除標記。

## 11.3 解 merge conflict

```bash
git status
# 編輯衝突檔案
git add conflicted-file.txt
git commit
```

若是 rebase 衝突：

```bash
git status
# 編輯衝突檔案
git add conflicted-file.txt
git rebase --continue
```

放棄 rebase：

```bash
git rebase --abort
```

放棄 merge：

```bash
git merge --abort
```

## 11.4 使用 ours / theirs

在 merge 情境：

```bash
git checkout --ours file.txt
git checkout --theirs file.txt
```

或新指令：

```bash
git restore --ours file.txt
git restore --theirs file.txt
```

注意：rebase 情境中 ours / theirs 的直覺可能相反，操作前請先確認。

## 11.5 減少衝突的方法

1. 小步 commit
2. 常常同步 main
3. 避免多人同時大改同一檔案
4. 格式化 commit 與功能 commit 分開
5. 使用 code ownership
6. PR 不要太大
7. 自動格式化在團隊中統一設定

---

# 12. Undo / Recovery 救援大全

## 12.1 還原工作目錄中的修改

丟掉單一檔案未 staged 的修改：

```bash
git restore file.txt
```

丟掉全部未 staged 修改：

```bash
git restore .
```

## 12.2 取消 staged

```bash
git restore --staged file.txt
```

取消全部 staged：

```bash
git restore --staged .
```

## 12.3 修改最後一次 commit

```bash
git commit --amend
```

## 12.4 回到上一個 commit，但保留修改

```bash
git reset --soft HEAD~1
```

## 12.5 回到上一個 commit，保留檔案但取消 staged

```bash
git reset --mixed HEAD~1
```

## 12.6 完全丟掉最後一次 commit 與修改

```bash
git reset --hard HEAD~1
```

## 12.7 已 push 的 commit 要取消

不要 reset shared branch，使用 revert：

```bash
git revert <commit>
```

## 12.8 誤刪 branch

```bash
git reflog
git switch -c recovered-branch <commit-hash>
```

## 12.9 誤 reset --hard

```bash
git reflog
git reset --hard <old-commit>
```

## 12.10 誤 rebase

```bash
git reflog
git reset --hard <before-rebase-commit>
```

## 12.11 清除 untracked files

先預覽：

```bash
git clean -n
```

刪除 untracked files：

```bash
git clean -f
```

刪除 untracked files 與 directories：

```bash
git clean -fd
```

也刪除 ignored files：

```bash
git clean -fdx
```

警告：`git clean` 很危險，請先用 `-n` 預覽。

---

# 13. Stash 暫存未完成工作

## 13.1 什麼時候用 stash

當你正在改東西，但臨時要切 branch 或 pull 最新變更，又不想 commit 半成品時，可用 stash。

## 13.2 基本用法

```bash
git stash
```

帶訊息：

```bash
git stash push -m "wip: login form"
```

包含 untracked files：

```bash
git stash -u
```

查看 stash：

```bash
git stash list
```

查看內容：

```bash
git stash show -p stash@{0}
```

套用但保留 stash：

```bash
git stash apply stash@{0}
```

套用並刪除 stash：

```bash
git stash pop
```

刪除特定 stash：

```bash
git stash drop stash@{0}
```

清空全部 stash：

```bash
git stash clear
```

## 13.3 從 stash 建立分支

```bash
git stash branch feature/from-stash stash@{0}
```

---

# 14. Tag、Release 與版本管理

## 14.1 Tag 類型

| 類型 | 指令 | 說明 |
|---|---|---|
| Lightweight tag | `git tag v1.0.0` | 像簡單指標 |
| Annotated tag | `git tag -a v1.0.0 -m "release v1.0.0"` | 有作者、日期、訊息 |

建議正式 release 使用 annotated tag。

## 14.2 建立 tag

```bash
git tag -a v1.0.0 -m "release: v1.0.0"
```

## 14.3 查看 tag

```bash
git tag
```

```bash
git show v1.0.0
```

## 14.4 推送 tag

推單一 tag：

```bash
git push origin v1.0.0
```

推全部 tag：

```bash
git push origin --tags
```

## 14.5 刪除 tag

本機：

```bash
git tag -d v1.0.0
```

遠端：

```bash
git push origin --delete v1.0.0
```

## 14.6 Semantic Versioning

格式：

```text
MAJOR.MINOR.PATCH
```

範例：

```text
1.4.2
```

| 位置 | 何時增加 |
|---|---|
| MAJOR | 不相容變更 |
| MINOR | 向下相容的新功能 |
| PATCH | 向下相容的 bug fix |

## 14.7 GitHub Release

GitHub Release 通常基於 tag 建立，包含：

- 版本標題
- Release notes
- Binary assets
- Source code archive
- Changelog

建議流程：

```bash
git tag -a v1.2.0 -m "release: v1.2.0"
git push origin v1.2.0
```

再到 GitHub 建立 Release。

---

# 15. .gitignore、.gitattributes 與換行處理

## 15.1 .gitignore 是什麼

`.gitignore` 告訴 Git 哪些未追蹤檔案不需要納入版本控制。

常見應忽略：

```text
node_modules/
dist/
build/
.env
*.log
.DS_Store
__pycache__/
*.pyc
.vscode/
.idea/
```

## 15.2 .gitignore 範例

```gitignore
# OS
.DS_Store
Thumbs.db

# Editor
.vscode/
.idea/

# Logs
*.log
logs/

# Env
.env
.env.*
!.env.example

# Node
node_modules/
dist/
coverage/

# Python
__pycache__/
*.pyc
.venv/
```

## 15.3 已被追蹤的檔案，.gitignore 不會自動生效

要先取消追蹤：

```bash
git rm --cached .env
```

再 commit：

```bash
git commit -m "chore: stop tracking env file"
```

## 15.4 全域 ignore

```bash
mkdir -p ~/.config/git
touch ~/.config/git/ignore
```

設定：

```bash
git config --global core.excludesfile ~/.config/git/ignore
```

## 15.5 .gitattributes 用途

`.gitattributes` 可控制：

- 換行符號
- 檔案類型 diff 策略
- merge 策略
- Git LFS tracking
- 語言判斷

## 15.6 換行統一設定範例

```gitattributes
* text=auto

*.sh text eol=lf
*.bat text eol=crlf
*.ps1 text eol=crlf
*.md text eol=lf
*.json text eol=lf

*.png binary
*.jpg binary
*.zip binary
```

## 15.7 重新正規化換行

```bash
git add --renormalize .
git commit -m "chore: normalize line endings"
```

---

# 16. Git Hooks

## 16.1 Hook 是什麼

Git Hooks 是在特定 Git 事件發生時自動執行的腳本。

位置：

```text
.git/hooks/
```

常見 hook：

| Hook | 觸發時機 | 用途 |
|---|---|---|
| pre-commit | commit 前 | lint、format、secret scan |
| commit-msg | commit message 建立後 | 檢查 commit 格式 |
| pre-push | push 前 | 跑測試 |
| post-merge | merge 後 | 安裝依賴、清 cache |

## 16.2 pre-commit 範例

```bash
#!/bin/sh
npm test
```

儲存為：

```text
.git/hooks/pre-commit
```

賦予執行權限：

```bash
chmod +x .git/hooks/pre-commit
```

## 16.3 團隊共享 hooks 的問題

`.git/hooks` 預設不會被 commit。團隊通常使用：

- pre-commit framework
- Husky
- Lefthook
- 自訂 scripts + core.hooksPath

設定共享 hook 路徑：

```bash
git config core.hooksPath .githooks
```

---

# 17. Git Worktree

## 17.1 Worktree 是什麼

Worktree 讓同一個 repository 可以同時 checkout 多個 branch 到不同資料夾，不用一直 stash 或切換。

## 17.2 建立 worktree

```bash
git worktree add ../my-project-hotfix hotfix/payment
```

若要建立新分支：

```bash
git worktree add -b hotfix/payment ../my-project-hotfix main
```

## 17.3 查看 worktree

```bash
git worktree list
```

## 17.4 移除 worktree

```bash
git worktree remove ../my-project-hotfix
```

清理 metadata：

```bash
git worktree prune
```

## 17.5 適合情境

- 一邊開發 feature，一邊緊急修 hotfix
- 同時比較兩個 branch
- 大型 repo 切分工作
- 避免反覆 stash

---

# 18. Git Submodule 與 Subtree

## 18.1 Submodule 是什麼

Submodule 是在一個 Git repo 中引用另一個 Git repo 的特定 commit。

適合：

- 共用 library
- 外部依賴固定版本
- 文件或 theme 作為獨立 repo

## 18.2 新增 submodule

```bash
git submodule add https://github.com/USER/LIB.git external/lib
```

初始化與更新：

```bash
git submodule update --init --recursive
```

Clone 時包含 submodule：

```bash
git clone --recurse-submodules https://github.com/USER/REPO.git
```

## 18.3 更新 submodule

```bash
cd external/lib
git pull origin main
cd ../..
git add external/lib
git commit -m "chore: update submodule lib"
```

## 18.4 Submodule 常見坑

1. 主 repo 只記錄 submodule 的 commit，不會自動跟最新版
2. clone 後忘記 `submodule update`
3. submodule 裡改了東西但沒 push
4. 權限問題導致 CI clone 失敗
5. 對初學團隊不太友善

## 18.5 Subtree 是什麼

Subtree 把另一個 repo 的內容合進目前 repo 的子目錄中。比 submodule 更像把程式碼帶進來。

常見指令：

```bash
git subtree add --prefix=vendor/lib https://github.com/USER/LIB.git main --squash
```

更新：

```bash
git subtree pull --prefix=vendor/lib https://github.com/USER/LIB.git main --squash
```

## 18.6 Submodule vs Subtree

| 項目 | Submodule | Subtree |
|---|---|---|
| 儲存方式 | 指向外部 repo commit | 把內容合入 repo |
| 使用難度 | 較高 | 較低 |
| 是否需額外 clone | 需要 init/update | 不需要 |
| 適合 | 外部依賴獨立管理 | 想簡化使用者體驗 |

---

# 19. Git LFS 大檔案管理

## 19.1 為什麼需要 Git LFS

Git 不適合頻繁變動的大型二進位檔，例如：

- PSD
- 影片
- 音訊
- 模型權重
- 大型資料集
- 遊戲素材

Git LFS 會把大檔案內容放在 LFS 儲存空間中，repo 裡保留 pointer file。

## 19.2 安裝與初始化

```bash
git lfs install
```

## 19.3 追蹤檔案類型

```bash
git lfs track "*.psd"
git lfs track "*.zip"
git lfs track "*.mp4"
```

這會修改 `.gitattributes`。

## 19.4 Commit LFS 設定

```bash
git add .gitattributes
git add assets/design.psd
git commit -m "chore: track design assets with lfs"
```

## 19.5 查看 LFS 檔案

```bash
git lfs ls-files
```

## 19.6 常見注意事項

1. 不要把大型二進位檔直接 commit 到一般 Git 歷史
2. 已 commit 的大檔即使刪掉，歷史中仍存在
3. 需要額外注意 GitHub LFS 儲存與流量限制
4. LFS 追蹤規則要在加入檔案前設定

---

# 20. 進階 Git 指令

## 20.1 bisect：找出哪個 commit 引入 bug

開始：

```bash
git bisect start
```

標記目前是壞的：

```bash
git bisect bad
```

標記某個舊版本是好的：

```bash
git bisect good v1.0.0
```

Git 會切到中間 commit，你測試後標記：

```bash
git bisect good
# 或
git bisect bad
```

結束：

```bash
git bisect reset
```

## 20.2 grep：搜尋 repo 內容

```bash
git grep "function login"
```

指定 commit：

```bash
git grep "TODO" HEAD~3
```

## 20.3 blame：行級歷史

```bash
git blame src/app.js
```

忽略空白：

```bash
git blame -w src/app.js
```

## 20.4 archive：打包原始碼

```bash
git archive --format zip --output source.zip main
```

## 20.5 bundle：離線搬移 repo

建立 bundle：

```bash
git bundle create repo.bundle --all
```

clone bundle：

```bash
git clone repo.bundle repo
```

## 20.6 sparse checkout：只 checkout 部分目錄

```bash
git sparse-checkout init --cone
git sparse-checkout set src docs
```

適合大型 monorepo。

## 20.7 partial clone

```bash
git clone --filter=blob:none https://github.com/USER/REPO.git
```

適合大型 repo，延遲下載 blob。

## 20.8 bare repository

Bare repo 沒有 working tree，常用於伺服器端。

```bash
git init --bare myrepo.git
```

## 20.9 fsck：檢查物件完整性

```bash
git fsck
```

## 20.10 gc：清理與壓縮

```bash
git gc
```

---

# 21. GitHub 基礎功能

## 21.1 Repository

GitHub repository 是專案的雲端儲存與協作空間，包含：

- Code
- Issues
- Pull requests
- Actions
- Projects
- Wiki
- Security
- Insights
- Settings

## 21.2 Public / Private / Internal

| 可見性 | 說明 |
|---|---|
| Public | 所有人可見 |
| Private | 只有授權者可見 |
| Internal | 企業內部可見，需 Enterprise |

建議：

- 開源專案：Public
- 個人私密開發：Private
- 公司內部共用：Internal 或 Private

## 21.3 README.md

README 是 repo 首頁最重要的文件。

建議包含：

```markdown
# Project Name

## Introduction

## Features

## Requirements

## Installation

## Usage

## Configuration

## Testing

## Deployment

## Contributing

## License
```

## 21.4 LICENSE

常見 license：

| License | 特性 |
|---|---|
| MIT | 寬鬆、簡短 |
| Apache-2.0 | 寬鬆，含專利授權條款 |
| GPL | 強 copyleft |
| LGPL | 較弱 copyleft |
| BSD | 寬鬆 |
| Proprietary | 私有，不開放授權 |

沒有 license 通常代表他人沒有明確權利使用、修改、散布。

## 21.5 Repository topics

Topics 可幫助搜尋與分類，例如：

```text
python
malware-analysis
windows
cli
devops
machine-learning
```

## 21.6 Wiki

適合放：

- 操作文件
- 長篇設計文件
- FAQ
- 團隊知識庫

但若你希望文件與程式碼一起 review，建議放在 repo 的 `docs/` 目錄。

## 21.7 Discussions

Discussions 適合：

- Q&A
- RFC
- 社群討論
- 想法收集

Issues 則比較適合可追蹤、可關閉的工作項目。

---

# 22. GitHub Repository 設定

## 22.1 General settings

常見設定：

- Repo name
- Description
- Website
- Topics
- Default branch
- Features：Issues、Projects、Wiki、Discussions
- Pull request merge methods
- Automatically delete head branches

## 22.2 Merge methods

GitHub PR 常見合併方式：

| 方法 | 歷史特性 | 適合 |
|---|---|---|
| Create a merge commit | 保留分支與 merge commit | 想保留完整脈絡 |
| Squash and merge | PR 多個 commit 壓成一個 | 想保持 main 乾淨 |
| Rebase and merge | 把 commits 線性接到 base | 想保留 commit 但不要 merge commit |

團隊建議：

- 小團隊：Squash and merge
- 需要完整歷史：Merge commit
- 嚴格線性歷史：Rebase and merge

## 22.3 Automatically delete head branches

PR merge 後自動刪除 feature branch，可降低分支混亂。

## 22.4 Template repository

可以把 repo 設為 template，讓別人用相同結構建立新 repo。

適合：

- starter kit
- lab template
- project boilerplate
- security baseline

---

# 23. GitHub Issues、Labels、Milestones、Projects

## 23.1 Issues

Issue 可用於：

- bug report
- feature request
- task tracking
- question
- incident follow-up

## 23.2 Issue template

位置：

```text
.github/ISSUE_TEMPLATE/
```

Bug report 範例：

```markdown
## Summary

## Steps to Reproduce
1.
2.
3.

## Expected Behavior

## Actual Behavior

## Environment
- OS:
- Version:

## Additional Context
```

## 23.3 Labels

建議 labels：

```text
type: bug
type: feature
type: docs
type: chore
priority: high
priority: medium
priority: low
status: blocked
status: needs-review
good first issue
help wanted
security
```

## 23.4 Milestones

Milestone 適合追蹤一組 issue / PR，例如：

```text
v1.0.0
Q3 Roadmap
MVP
Security Hardening
```

## 23.5 GitHub Projects

GitHub Projects 可建立看板、表格、Roadmap。

常見欄位：

- Status
- Assignee
- Priority
- Sprint
- Due date
- Repository
- Milestone

常見狀態：

```text
Backlog
Ready
In Progress
In Review
Blocked
Done
```

---

# 24. Pull Request 與 Code Review

## 24.1 PR 是什麼

Pull Request 是請求把某個 branch 的變更合併到另一個 branch。它是 GitHub 協作的核心。

PR 不只是合併按鈕，而是：

- 變更討論
- code review
- CI 檢查
- 安全掃描
- 文件審查
- 設計脈絡保存

## 24.2 開 PR 前 checklist

```markdown
- [ ] 分支已同步最新 main
- [ ] commit 訊息清楚
- [ ] PR 範圍單一
- [ ] 測試已通過
- [ ] 文件已更新
- [ ] 沒有 secret / token / 私鑰
- [ ] 沒有不必要的大檔
- [ ] 已自我 review diff
```

## 24.3 PR 描述模板

```markdown
## Summary

說明這個 PR 做了什麼。

## Motivation

為什麼需要這個變更？

## Changes

- 
- 
- 

## Testing

- [ ] Unit tests
- [ ] Integration tests
- [ ] Manual test

## Screenshots / Evidence

## Risk

## Rollback Plan

## Related Issues

Closes #
```

## 24.4 Review 類型

| Review 結果 | 意義 |
|---|---|
| Comment | 留意見，不阻擋 |
| Approve | 同意合併 |
| Request changes | 要求修改，通常會阻擋 merge |

## 24.5 Code review 看什麼

1. 正確性
2. 可讀性
3. 安全性
4. 效能
5. 測試覆蓋
6. 錯誤處理
7. 相容性
8. 維護性
9. 文件是否同步
10. 是否符合團隊風格

## 24.6 PR 大小建議

較容易 review 的 PR：

- 少於 300 行變更
- 單一目的
- 有清楚說明
- 有測試證據

大型 PR 要拆：

```text
PR 1: refactor only
PR 2: add new interface
PR 3: implement feature
PR 4: add tests and docs
```

## 24.7 Draft PR

Draft PR 適合：

- 提早讓隊友看到方向
- CI 預跑
- 討論架構
- 尚未準備正式 review

---

# 25. GitHub Flow、Fork Flow、Git Flow

## 25.1 GitHub Flow

簡潔流程：

```text
main
  ↓
create feature branch
  ↓
commit changes
  ↓
push branch
  ↓
open PR
  ↓
review + CI
  ↓
merge to main
  ↓
deploy
```

適合：

- Web app
- SaaS
- CI/CD
- 小到中型團隊
- 頻繁部署

## 25.2 Fork Flow

常見於開源專案：

```text
upstream repo
  ↓ fork
my fork
  ↓ branch
commit
  ↓ PR back to upstream
```

設定 upstream：

```bash
git remote add upstream https://github.com/ORIGINAL_OWNER/REPO.git
```

同步 fork：

```bash
git fetch upstream
git switch main
git merge upstream/main
git push origin main
```

或：

```bash
git pull upstream main --rebase
```

## 25.3 Git Flow

常見分支：

```text
main       正式版本
release/* 釋出候選
develop    整合開發
feature/*  功能
hotfix/*   緊急修正
```

適合：

- 版本週期明確
- 需要維護多個 release
- 桌面軟體、嵌入式、套裝軟體

不適合：

- 超頻繁部署的小團隊
- 想保持流程簡單的專案

## 25.4 Trunk-based development

核心：大多數變更快速合併到 trunk/main，搭配 feature flags。

適合：

- 高成熟 CI/CD
- 測試自動化完善
- 大型工程團隊

---

# 26. GitHub Branch Protection 與 Rulesets

## 26.1 Branch Protection 是什麼

Branch protection 可以保護重要 branch，例如 `main`、`release/*`，要求合併前必須滿足條件。

常見設定：

- Require pull request reviews before merging
- Require status checks before merging
- Require conversation resolution before merging
- Require signed commits
- Require linear history
- Require merge queue
- Require deployments to succeed before merging
- Lock branch
- Restrict who can push
- Block force pushes
- Block deletions

## 26.2 建議 main branch 保護規則

```text
Branch: main

- Require a pull request before merging
- Require approvals: 1 或 2
- Require review from Code Owners
- Dismiss stale approvals when new commits are pushed
- Require status checks to pass
- Require branches to be up to date before merging
- Require conversation resolution
- Require signed commits（視團隊成熟度）
- Do not allow bypassing the above settings（高安全專案）
- Restrict who can push
- Do not allow force pushes
- Do not allow deletions
```

## 26.3 Rulesets 是什麼

Rulesets 是比傳統 branch protection 更可組合、可觀察、可套用多規則的政策機制，可控制 branch、tag、push 行為。

Rulesets 可用於：

- 要求 PR review
- 要求 status check
- 要求 signed commit
- 限制 tag 刪除或重新命名
- 限制特定檔案路徑
- 限制檔案大小
- 限制副檔名
- block force push
- block deletion

## 26.4 Branch protection vs Rulesets

| 項目 | Branch Protection | Rulesets |
|---|---|---|
| 套用方式 | 單一 branch rule | 多個 ruleset 可同時作用 |
| 可見性 | 管理者設定 | Read access 可看 active rulesets |
| 政策組合 | 較有限 | 可 layer，多規則聚合 |
| 適合 | 小型 repo、簡單保護 | 組織治理、多 repo、多政策 |

## 26.5 Merge Queue

Merge queue 適合高頻 PR 專案。它會在 PR 滿足條件後排隊，並以最新 base + queue 中變更重新測試，降低 main 被多個 PR 互相破壞的機率。

## 26.6 Force push 原則

禁止在：

```text
main
develop
release/*
shared feature branches
```

可有限使用於：

```text
個人 feature branch
尚未被他人基於它開發的 branch
```

並使用：

```bash
git push --force-with-lease
```

---

# 27. CODEOWNERS 與 PR Template

## 27.1 CODEOWNERS 用途

CODEOWNERS 用來指定哪些人或 team 負責哪些檔案。當 PR 修改相關檔案時，GitHub 會自動 request code owners review。

## 27.2 CODEOWNERS 位置

GitHub 會搜尋：

```text
.github/CODEOWNERS
CODEOWNERS
docs/CODEOWNERS
```

若多個位置存在，依 GitHub 規則使用第一個找到的。

## 27.3 CODEOWNERS 範例

```text
# Default owners for everything
* @org/core-team

# Security-sensitive files
/SECURITY.md @org/security-team
/.github/workflows/ @org/devops-team @org/security-team
/deploy/ @org/platform-team

# Frontend
/frontend/ @org/frontend-team
*.css @org/frontend-team

# Backend
/backend/ @org/backend-team
*.go @org/backend-team

# Docs
/docs/ @org/docs-team
```

## 27.4 CODEOWNERS 注意事項

1. Owner 必須有 write 權限
2. Team 必須 visible
3. Draft PR 不會自動 request code owners
4. Path 大小寫要正確
5. CODEOWNERS 過大可能不載入
6. 最後匹配的 pattern 通常優先

## 27.5 PR Template

位置：

```text
.github/pull_request_template.md
```

或多模板：

```text
.github/PULL_REQUEST_TEMPLATE/bugfix.md
.github/PULL_REQUEST_TEMPLATE/feature.md
```

範例：

```markdown
## Summary

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation
- [ ] Refactor

## Checklist
- [ ] I have tested this change
- [ ] I have updated documentation
- [ ] I have reviewed my own diff
- [ ] No secrets are included

## Related Issues
Closes #
```

---

# 28. GitHub Actions CI/CD

## 28.1 GitHub Actions 是什麼

GitHub Actions 是 GitHub 內建自動化平台。你可以在 repo 中建立 workflow，當 push、PR、release、schedule、manual trigger 等事件發生時，自動執行 build、test、deploy、scan 等任務。

Workflow 檔案位置：

```text
.github/workflows/*.yml
.github/workflows/*.yaml
```

## 28.2 Actions 核心概念

| 概念 | 說明 |
|---|---|
| Workflow | 一個自動化流程 |
| Event | 觸發 workflow 的事件 |
| Job | workflow 中的一組工作 |
| Step | job 中的一個步驟 |
| Action | 可重用的步驟封裝 |
| Runner | 執行 job 的機器 |
| Matrix | 多版本、多環境組合測試 |
| Artifact | workflow 產物 |
| Cache | 快取依賴，加速 CI |
| Environment | 部署環境與保護規則 |
| Secret | 敏感資料 |
| Variable | 非敏感設定值 |

## 28.3 最小 workflow 範例

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Run tests
        run: echo "run tests here"
```

## 28.4 常見事件

```yaml
on: push
```

```yaml
on: [push, pull_request]
```

```yaml
on:
  push:
    branches:
      - main
      - 'release/**'
```

```yaml
on:
  pull_request:
    branches:
      - main
    paths:
      - 'src/**'
      - '.github/workflows/**'
```

手動觸發：

```yaml
on:
  workflow_dispatch:
```

排程：

```yaml
on:
  schedule:
    - cron: '0 0 * * *'
```

注意：cron 通常以 UTC 計算。

## 28.5 Node.js CI 範例

```yaml
name: Node CI

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [20, 22]

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: npm

      - run: npm ci
      - run: npm test
```

## 28.6 Python CI 範例

```yaml
name: Python CI

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        python-version: ['3.11', '3.12']

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - run: python -m pip install --upgrade pip
      - run: pip install -r requirements.txt
      - run: pytest
```

## 28.7 Job 依賴

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: echo test

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - run: echo deploy
```

## 28.8 條件執行

```yaml
if: github.ref == 'refs/heads/main'
```

範例：

```yaml
jobs:
  deploy:
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - run: echo deploy
```

## 28.9 Matrix

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    node: [20, 22]
```

使用：

```yaml
runs-on: ${{ matrix.os }}
```

## 28.10 Cache

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-npm-${{ hashFiles('package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-npm-
```

## 28.11 Artifact

上傳：

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: build-output
    path: dist/
```

下載：

```yaml
- uses: actions/download-artifact@v4
  with:
    name: build-output
```

## 28.12 Environment 與部署保護

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - run: echo deploy
```

Environment 可設定：

- required reviewers
- wait timer
- environment secrets
- deployment branches

## 28.13 Actions 安全原則

1. `permissions` 預設最小化
2. 不要在 log 印出 secret
3. 第三方 action 盡量 pin 到 commit SHA
4. PR from fork 的 workflow 權限要小心
5. 不要在 `pull_request_target` 中 checkout 不可信程式碼後執行
6. Secrets 只給需要的 environment
7. production deploy 需 reviewer approval
8. 定期更新 actions 版本
9. Dependabot 也可更新 GitHub Actions references

---

# 29. GitHub Actions Secrets、Variables、Permissions

## 29.1 Secrets vs Variables

| 類型 | 用途 | 是否敏感 |
|---|---|---|
| Secrets | token、password、private key | 是 |
| Variables | region、environment name、非敏感設定 | 否 |

## 29.2 Repository secret

GitHub 網頁：

```text
Repository -> Settings -> Secrets and variables -> Actions -> Secrets -> New repository secret
```

GitHub CLI：

```bash
gh secret set SECRET_NAME
```

## 29.3 在 workflow 使用 secret

```yaml
steps:
  - name: Use secret
    env:
      API_TOKEN: ${{ secrets.API_TOKEN }}
    run: |
      echo "Token length is ${#API_TOKEN}"
```

不要：

```yaml
run: echo ${{ secrets.API_TOKEN }}
```

## 29.4 GITHUB_TOKEN

GitHub Actions 每個 job 會有自動產生的 `GITHUB_TOKEN`，可用來對目前 repo 做授權操作。建議明確設定 permissions。

```yaml
permissions:
  contents: read
```

需要建立 release：

```yaml
permissions:
  contents: write
```

需要寫 PR comment：

```yaml
permissions:
  pull-requests: write
  contents: read
```

## 29.5 最小權限範例

```yaml
name: CI

on: pull_request

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo test
```

## 29.6 不要把 secret 放在

```text
.env committed to repo
README
Issue / PR comment
Actions logs
Docker image layer
Build artifact
Client-side frontend bundle
```

---

# 30. GitHub Pages

## 30.1 GitHub Pages 是什麼

GitHub Pages 可從 repo 發布靜態網站。常見用途：

- 個人首頁
- 專案文件
- Blog
- Portfolio
- Lab notes
- 靜態 demo

## 30.2 發布來源

常見方式：

1. 從特定 branch 發布
2. 使用 GitHub Actions workflow 發布

## 30.3 常見 branch 發布結構

```text
main branch /docs
```

或：

```text
gh-pages branch /
```

## 30.4 自訂網域

常見設定：

- `www.example.com`
- `blog.example.com`
- `example.com`

建議：

1. 先在 GitHub Pages 設定 custom domain
2. 再設定 DNS
3. 啟用 HTTPS
4. 驗證 domain ownership

## 30.5 Pages 常見 404 原因

1. 沒有 `index.html`
2. 發布來源選錯
3. branch 還沒 build 完
4. Jekyll build 失敗
5. SPA routing 沒有 fallback
6. custom domain DNS 未生效
7. repo private / plan 限制

---

# 31. GitHub CLI：gh

## 31.1 gh 是什麼

`gh` 是 GitHub 官方命令列工具，可在 terminal 操作 GitHub：repo、issue、PR、release、workflow、secret、auth 等。

## 31.2 安裝

Windows：

```powershell
winget install --id GitHub.cli
```

macOS：

```bash
brew install gh
```

Linux 依發行版安裝。

## 31.3 登入

```bash
gh auth login
```

查看狀態：

```bash
gh auth status
```

## 31.4 Repo 操作

建立 repo：

```bash
gh repo create my-repo --public --source=. --remote=origin --push
```

Clone：

```bash
gh repo clone OWNER/REPO
```

查看 repo：

```bash
gh repo view OWNER/REPO --web
```

## 31.5 PR 操作

建立 PR：

```bash
gh pr create --base main --head feature/login --title "feat: add login" --body "Add login page"
```

查看 PR：

```bash
gh pr list
gh pr view 123
```

Checkout PR：

```bash
gh pr checkout 123
```

合併 PR：

```bash
gh pr merge 123 --squash --delete-branch
```

## 31.6 Issue 操作

```bash
gh issue list
gh issue create --title "Bug: login fails" --body "Steps..."
gh issue view 42
gh issue close 42
```

## 31.7 Actions 操作

列出 workflow：

```bash
gh workflow list
```

手動執行 workflow：

```bash
gh workflow run ci.yml
```

查看 run：

```bash
gh run list
gh run view --log
```

重新執行：

```bash
gh run rerun <run-id>
```

## 31.8 Secret 操作

```bash
gh secret set API_TOKEN
gh secret list
gh secret delete API_TOKEN
```

## 31.9 Release 操作

```bash
gh release create v1.0.0 --title "v1.0.0" --notes "First release"
gh release list
gh release view v1.0.0
gh release download v1.0.0
```

---

# 32. GitHub Security：Dependabot、CodeQL、Secret Scanning

## 32.1 Security 功能總覽

GitHub 安全功能常見包含：

- Dependabot alerts
- Dependabot security updates
- Dependabot version updates
- Dependency graph
- Code scanning
- CodeQL
- Secret scanning
- Push protection
- Security policy
- Private vulnerability reporting

## 32.2 Dependabot

Dependabot 可自動幫你：

1. 偵測有漏洞的依賴
2. 開 PR 更新 vulnerable dependency
3. 定期更新依賴到新版
4. 更新 GitHub Actions references

## 32.3 dependabot.yml 範例

位置：

```text
.github/dependabot.yml
```

Node.js npm 範例：

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
    labels:
      - "dependencies"
      - "security"
```

GitHub Actions 更新範例：

```yaml
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
```

## 32.4 CodeQL

CodeQL 是 GitHub 的程式碼分析引擎，可把程式碼當成資料查詢，找出漏洞與錯誤，結果會顯示為 code scanning alerts。

常見支援語言包含：

- C/C++
- C#
- Go
- Java/Kotlin
- JavaScript/TypeScript
- Python
- Ruby
- Rust
- Swift
- GitHub Actions workflows

## 32.5 CodeQL workflow 範例

```yaml
name: CodeQL

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 3 * * 1'

permissions:
  security-events: write
  packages: read
  actions: read
  contents: read

jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Initialize CodeQL
        uses: github/codeql-action/init@v3
        with:
          languages: javascript-typescript

      - name: Autobuild
        uses: github/codeql-action/autobuild@v3

      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v3
```

## 32.6 Secret scanning

Secret scanning 用於偵測 repo 中的 token、key、credentials。

## 32.7 Push protection

Push protection 會在 secret 被 push 進 repo 前阻擋，降低機密進入 Git 歷史的風險。

如果真的誤 commit secret：

1. 立刻 revoke / rotate secret
2. 從目前版本移除
3. 視情況清理 Git history
4. 檢查 logs 是否被濫用
5. 加入 secret scanning / push protection

重點：刪除檔案不等於 secret 從歷史消失。

## 32.8 SECURITY.md

範例：

```markdown
# Security Policy

## Supported Versions

| Version | Supported |
|---|---|
| 1.x | Yes |
| 0.x | No |

## Reporting a Vulnerability

Please report vulnerabilities to security@example.com.
Do not open a public issue for security vulnerabilities.
```

---

# 33. GitHub 權限、Organization、Team

## 33.1 Repository roles

GitHub organization repository 常見角色：

| Role | 適合對象 |
|---|---|
| Read | 只需查看、討論的人 |
| Triage | 管理 issue / PR，但不 push code |
| Write | 一般開發者，可 push |
| Maintain | 專案維護者，可管理 repo 但不做敏感破壞操作 |
| Admin | 完整權限，包含安全與刪除 repo |

## 33.2 最小權限原則

不要人人 Admin。建議：

```text
一般開發者：Write
Tech lead：Maintain
Repo owner / DevOps：Admin
產品 / QA：Triage 或 Read
外部顧問：Read / Triage / limited Write
```

## 33.3 Organization

Organization 適合：

- 公司
- 團隊
- 開源組織
- 課程或研究群組

功能：

- Teams
- Repository permissions
- Organization secrets
- Rulesets
- Audit log
- Security settings
- SSO / SAML
- 2FA enforcement

## 33.4 Teams

Team 可用來：

- 管理 repo 權限
- CODEOWNERS 指派
- PR review request
- Mention 群組

命名建議：

```text
frontend
backend
platform
security
docs
maintainers
release-managers
```

## 33.5 Deploy keys

Deploy key 是加到 repo 的 SSH key，可讓機器讀取或寫入 repo。

注意：擁有 private key 的人即使後來被移出 organization，只要 key 還有效，就仍可能透過 deploy key 存取該 repo。

建議：

1. 只給 read-only，除非必要
2. 每個 repo / service 使用不同 key
3. 定期 rotate
4. 離職或系統退役時移除

---

# 34. SSH、HTTPS、PAT 與簽署 Commit

## 34.1 HTTPS vs SSH

| 方式 | 優點 | 缺點 |
|---|---|---|
| HTTPS + PAT / Credential Manager | 容易設定，企業代理較友善 | token 管理要小心 |
| SSH key | 開發體驗好，不必每次輸入密碼 | key 管理與 agent 設定需理解 |

## 34.2 產生 SSH key

建議 Ed25519：

```bash
ssh-keygen -t ed25519 -C "you@example.com"
```

舊系統不支援 Ed25519 時：

```bash
ssh-keygen -t rsa -b 4096 -C "you@example.com"
```

## 34.3 啟動 ssh-agent 並加入 key

macOS / Linux：

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Windows PowerShell：

```powershell
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

## 34.4 加到 GitHub

複製 public key：

```bash
cat ~/.ssh/id_ed25519.pub
```

GitHub：

```text
Settings -> SSH and GPG keys -> New SSH key
```

測試：

```bash
ssh -T git@github.com
```

## 34.5 Personal Access Token

PAT 可用於 HTTPS Git 操作或 API。GitHub 建議能用 fine-grained PAT 時優先使用，並限制 repo、權限與期限。

原則：

1. 只給必要權限
2. 設定過期時間
3. 不要硬編碼在程式碼
4. 不要貼在 Issue / PR / Actions logs
5. 泄漏後立刻 revoke

## 34.6 Commit signing

GitHub 支援顯示 verified commit。常見方式：

- GPG key
- SSH signing key
- S/MIME

啟用 SSH commit signing 範例：

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
```

建立 commit：

```bash
git commit -S -m "feat: signed commit"
```

---

# 35. 常見錯誤與解法

## 35.1 `fatal: not a git repository`

原因：目前資料夾不是 Git repo，或不在 repo 內。

解法：

```bash
pwd
ls -la
cd path/to/repo
```

或初始化：

```bash
git init
```

## 35.2 `non-fast-forward`

原因：遠端有你本機沒有的 commit。

解法：

```bash
git pull --rebase
git push
```

## 35.3 `Your local changes would be overwritten`

原因：你有本機修改，切 branch / pull 會覆蓋。

解法：

```bash
git status
git stash -u
git pull --rebase
git stash pop
```

或先 commit。

## 35.4 Merge conflict

解法：

```bash
git status
# 編輯衝突檔案
git add <file>
git merge --continue
```

或：

```bash
git rebase --continue
```

## 35.5 Detached HEAD

原因：checkout 到 commit 而非 branch。

如果只是查看：

```bash
git switch main
```

如果要保留修改：

```bash
git switch -c new-branch
```

## 35.6 忘記切 branch 就 commit 在 main

如果 commit 還沒 push：

```bash
git branch feature/my-work
git reset --hard origin/main
git switch feature/my-work
```

或：

```bash
git switch -c feature/my-work
# 回 main 後 reset
git switch main
git reset --hard origin/main
```

## 35.7 誤 commit secret

處理順序：

1. Revoke / rotate secret
2. 移除檔案或 secret
3. 加入 `.gitignore`
4. 清理 history：使用 `git filter-repo` 或 BFG Repo-Cleaner
5. 通知團隊重新 clone 或清理本機歷史
6. 啟用 secret scanning / push protection

## 35.8 大檔 push 被拒

解法：

1. 若尚未 commit：加入 `.gitignore`
2. 若需要版本控制：使用 Git LFS
3. 若已進歷史：清理 history

## 35.9 `Permission denied (publickey)`

檢查：

```bash
ssh -T git@github.com
ssh-add -l
git remote -v
```

可能原因：

- public key 沒加到 GitHub
- ssh-agent 沒有 key
- remote URL 用錯
- key 權限不正確
- 公司代理或防火牆阻擋 SSH

## 35.10 `Support for password authentication was removed`

GitHub 不再接受帳密作為 HTTPS Git 操作密碼。使用：

- Git Credential Manager
- Personal Access Token
- SSH key
- GitHub CLI login

## 35.11 PR 無法 merge，check pending

可能原因：

1. Required check 沒跑完
2. Workflow path / branch filter 導致 check 被 skipped 但仍 required
3. Job 名稱重複造成 ambiguous status check
4. Branch 沒有 up to date
5. Conversation 未 resolve
6. Required reviewer 未 approve

## 35.12 Pull 後多了 merge commit

原因：`git pull` 預設 merge。

改用：

```bash
git pull --rebase
```

或設定：

```bash
git config --global pull.rebase true
```

---

# 36. 實戰工作流範本

## 36.1 個人專案最小流程

```bash
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin git@github.com:USER/REPO.git
git push -u origin main
```

日常：

```bash
git status
git add .
git commit -m "feat: ..."
git push
```

## 36.2 團隊 feature branch 流程

```bash
git switch main
git pull --rebase
git switch -c feature/my-feature
# edit files
git add .
git commit -m "feat: add my feature"
git push -u origin feature/my-feature
```

開 PR，review 後 merge。

merge 後：

```bash
git switch main
git pull --rebase
git branch -d feature/my-feature
git fetch --prune
```

## 36.3 Hotfix 流程

```bash
git switch main
git pull --rebase
git switch -c hotfix/payment-crash
# fix
git add .
git commit -m "fix: prevent payment crash"
git push -u origin hotfix/payment-crash
```

PR -> CI -> review -> merge -> tag release。

## 36.4 開源 fork 貢獻流程

```bash
git clone git@github.com:YOUR_NAME/REPO.git
cd REPO
git remote add upstream git@github.com:ORIGINAL_OWNER/REPO.git
git fetch upstream
git switch main
git rebase upstream/main
git switch -c fix/typo
# edit
git add .
git commit -m "docs: fix typo"
git push -u origin fix/typo
```

到 GitHub 開 PR 給 upstream。

## 36.5 Release 流程

```bash
git switch main
git pull --rebase
npm test
# update changelog/version if needed
git tag -a v1.2.0 -m "release: v1.2.0"
git push origin v1.2.0
```

使用 GitHub Release 發布 notes 與 assets。

## 36.6 Monorepo 基本策略

建議：

```text
/apps/web
/apps/api
/packages/ui
/packages/config
/docs
.github/workflows
```

搭配：

- path-based CI
- CODEOWNERS
- sparse checkout
- changesets
- workspace package manager
- rulesets

---

# 37. Git 指令速查表

## 37.1 設定

```bash
git config --global user.name "Name"
git config --global user.email "email@example.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
git config --list --show-origin
```

## 37.2 建立 / 取得 repo

```bash
git init
git clone <url>
git clone --depth 1 <url>
```

## 37.3 狀態 / 差異

```bash
git status
git status -sb
git diff
git diff --staged
git diff --stat A B
git diff --name-only A B
```

## 37.4 Add / Commit

```bash
git add <file>
git add .
git add -p
git commit -m "message"
git commit --amend
git commit --amend --no-edit
```

## 37.5 Log

```bash
git log
git log --oneline
git log --oneline --graph --decorate --all
git log -p
git log --stat
git show <commit>
```

## 37.6 Branch

```bash
git branch
git branch -a
git switch <branch>
git switch -c <branch>
git branch -d <branch>
git branch -D <branch>
git branch -m old new
```

## 37.7 Merge / Rebase

```bash
git merge <branch>
git rebase <branch>
git rebase -i HEAD~3
git rebase --continue
git rebase --abort
```

## 37.8 Remote

```bash
git remote -v
git remote add origin <url>
git remote set-url origin <url>
git fetch
git fetch --prune
git pull --rebase
git push
git push -u origin <branch>
git push --force-with-lease
```

## 37.9 Undo

```bash
git restore <file>
git restore --staged <file>
git reset --soft HEAD~1
git reset --mixed HEAD~1
git reset --hard HEAD~1
git revert <commit>
git reflog
```

## 37.10 Stash

```bash
git stash
git stash -u
git stash list
git stash show -p
git stash apply
git stash pop
git stash drop
git stash clear
```

## 37.11 Tag

```bash
git tag
git tag -a v1.0.0 -m "release: v1.0.0"
git push origin v1.0.0
git push origin --tags
git tag -d v1.0.0
git push origin --delete v1.0.0
```

## 37.12 Debug / Search

```bash
git grep "keyword"
git blame file.txt
git bisect start
git fsck
git gc
```

---

# 38. 團隊規範模板

## 38.1 Branch 規範

```markdown
# Branch Naming

- feature/<short-description>
- fix/<short-description>
- hotfix/<short-description>
- chore/<short-description>
- docs/<short-description>
- release/<version>

Examples:
- feature/login-page
- fix/api-timeout
- hotfix/payment-crash
```

## 38.2 Commit 規範

```markdown
# Commit Convention

Use Conventional Commits:

- feat: new feature
- fix: bug fix
- docs: documentation
- refactor: code refactor
- test: tests
- chore: maintenance
- ci: CI/CD

Examples:

feat(auth): add login endpoint
fix(api): handle timeout
```

## 38.3 PR 規範

```markdown
# Pull Request Rules

Before opening PR:

- Rebase on latest main
- Keep PR focused
- Add or update tests
- Update docs if needed
- Do self-review
- No secrets
- No unrelated formatting changes

Merge requirements:

- At least 1 approval
- All CI checks pass
- Conversations resolved
- Code owner approval for sensitive paths
```

## 38.4 Release 規範

```markdown
# Release Rules

- Use semantic versioning
- Create annotated tags
- Publish GitHub Release
- Include changelog
- Include migration notes for breaking changes
- Include rollback plan
```

## 38.5 Security 規範

```markdown
# Security Rules

- Never commit secrets
- Use GitHub Secrets for credentials
- Enable Dependabot
- Enable secret scanning / push protection where available
- Require PR review for .github/workflows changes
- Require CODEOWNERS review for deployment and security-sensitive files
- Use least privilege for tokens and Actions permissions
```

---

# 39. 學習路線圖

## 39.1 初學者階段

目標：能自己使用 Git 管理專案。

必學：

```text
git init
git clone
git status
git add
git commit
git log
git diff
git branch
git switch
git merge
git push
git pull
```

練習：

1. 建立 repo
2. 修改 README
3. commit
4. 建 branch
5. merge branch
6. push 到 GitHub

## 39.2 協作階段

目標：能在團隊中用 PR 開發。

必學：

```text
feature branch
Pull Request
Code Review
merge conflict
git pull --rebase
git push -u
git fetch --prune
```

練習：

1. Fork 專案
2. 開 PR
3. 解 conflict
4. Review 別人的 PR
5. 用 issue 追蹤工作

## 39.3 進階階段

目標：能整理歷史與救援。

必學：

```text
rebase -i
cherry-pick
revert
reset
reflog
stash
bisect
worktree
```

練習：

1. squash commits
2. 修改 commit message
3. 找回誤刪 branch
4. 用 bisect 找 bug
5. 用 worktree 修 hotfix

## 39.4 維護者階段

目標：能管理 GitHub 專案。

必學：

```text
branch protection
rulesets
CODEOWNERS
PR templates
issue templates
GitHub Actions
Dependabot
CodeQL
secret scanning
release management
```

練習：

1. 設定 main protection
2. 設定 CODEOWNERS
3. 設定 CI
4. 設定 Dependabot
5. 建立 GitHub Release

## 39.5 DevOps / Security 階段

目標：能建立安全、可審計、自動化的 SDLC。

必學：

```text
least privilege permissions
GITHUB_TOKEN permissions
OIDC deployment
environment protection
artifact attestation
supply chain security
secret rotation
audit log
organization policies
```

---

# 40. 參考資料

以下資料作為本筆記校對來源，建議優先閱讀官方文件：

## Git 官方

- Git Reference: https://git-scm.com/docs
- Git Documentation: https://git-scm.com/docs/git
- Git Data Model: https://git-scm.com/docs/gitdatamodel
- Pro Git Book - Git Objects: https://git-scm.com/book/en/v2/Git-Internals-Git-Objects
- Pro Git Book - Rebasing: https://git-scm.com/book/en/v2/Git-Branching-Rebasing
- Pro Git Book - Branching Workflows: https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows
- git-stash: https://git-scm.com/docs/git-stash
- git-reflog: https://git-scm.com/docs/git-reflog
- git-worktree: https://git-scm.com/docs/git-worktree
- gitattributes: https://git-scm.com/docs/gitattributes

## GitHub 官方

- GitHub Docs: https://docs.github.com/
- GitHub CLI Manual: https://cli.github.com/manual/
- GitHub SSH key setup: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
- GitHub Personal Access Tokens: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
- GitHub Branch Protection: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- GitHub Rulesets: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets
- GitHub Pull Request Management: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/managing-and-standardizing-pull-requests
- GitHub CODEOWNERS: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
- GitHub Actions Workflows: https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows
- GitHub Actions Workflow Syntax: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
- GitHub Actions Secrets: https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets
- GitHub Pages: https://docs.github.com/pages
- GitHub LFS: https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage
- GitHub Dependabot: https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-version-updates
- GitHub CodeQL: https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-code-scanning
- GitHub Push Protection: https://docs.github.com/en/code-security/concepts/secret-security/push-protection
- GitHub Repository Roles: https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization

---

# 附錄 A：一頁式 Git 工作流圖

```text
Start
  |
  v
git switch main
  |
  v
git pull --rebase
  |
  v
git switch -c feature/x
  |
  v
edit files
  |
  v
git status -> git diff
  |
  v
git add -p / git add .
  |
  v
git commit -m "feat: x"
  |
  v
git push -u origin feature/x
  |
  v
Open PR
  |
  v
CI + Review + Fix
  |
  v
Merge
  |
  v
git switch main
  |
  v
git pull --rebase
  |
  v
git branch -d feature/x
  |
  v
git fetch --prune
```

---

# 附錄 B：危險指令警戒表

| 指令 | 風險 | 安全替代或注意事項 |
|---|---|---|
| `git reset --hard` | 丟掉 working tree 修改 | 先 `git status`，必要時 `git stash -u` |
| `git clean -fdx` | 刪除 untracked 與 ignored files | 先 `git clean -n` |
| `git push --force` | 覆蓋遠端歷史 | 用 `--force-with-lease` |
| `git rebase` shared branch | 改寫他人基於的歷史 | 只 rebase 自己 branch |
| 刪除 tag 後重建 | 破壞 release 可追溯性 | 正式 release tag 避免重寫 |
| 清 history | 影響所有 clone | 先溝通、備份、公告 |

---

# 附錄 C：推薦 `.gitignore` 起手式

```gitignore
# OS
.DS_Store
Thumbs.db

# Editors
.vscode/
.idea/
*.swp

# Logs
*.log
logs/

# Environment
.env
.env.*
!.env.example

# Dependency directories
node_modules/
vendor/

# Build outputs
dist/
build/
out/
coverage/

# Python
__pycache__/
*.py[cod]
.venv/
venv/

# Java
*.class
target/

# Archives
*.zip
*.tar.gz
```

---

# 附錄 D：推薦 `.gitattributes` 起手式

```gitattributes
* text=auto

*.md text eol=lf
*.json text eol=lf
*.yml text eol=lf
*.yaml text eol=lf
*.sh text eol=lf
*.py text eol=lf
*.js text eol=lf
*.ts text eol=lf
*.css text eol=lf
*.html text eol=lf

*.bat text eol=crlf
*.cmd text eol=crlf
*.ps1 text eol=crlf

*.png binary
*.jpg binary
*.jpeg binary
*.gif binary
*.webp binary
*.pdf binary
*.zip binary
*.7z binary
*.exe binary
```

---

# 附錄 E：最小安全 GitHub Repo Baseline

```text
Repository:
- README.md
- LICENSE
- SECURITY.md
- CONTRIBUTING.md
- .gitignore
- .gitattributes
- .github/pull_request_template.md
- .github/ISSUE_TEMPLATE/bug_report.md
- .github/ISSUE_TEMPLATE/feature_request.md
- .github/CODEOWNERS
- .github/dependabot.yml
- .github/workflows/ci.yml

Settings:
- Private by default for non-open-source
- main as default branch
- Delete head branches after merge
- Disable unused features
- Enable vulnerability alerts
- Enable Dependabot where applicable
- Enable secret scanning / push protection where available

Branch protection / Rulesets:
- Require PR before merge
- Require 1-2 approvals
- Require CODEOWNERS for sensitive paths
- Require status checks
- Block force push
- Block deletion
- Require conversation resolution

Actions:
- Minimal permissions
- No plaintext secrets in logs
- Use environments for production
- Review workflows touching deployment or secrets
```
