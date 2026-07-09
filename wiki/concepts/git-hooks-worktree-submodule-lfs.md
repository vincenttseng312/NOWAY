---
type: concept
title: "Git Hooks、Worktree、Submodule／Subtree、LFS"
tags: [git]
sources: [git-github-complete-notes]
created: 2026-07-09
updated: 2026-07-09
---

# Git Hooks、Worktree、Submodule／Subtree、LFS

四個進階但常用的 Git 功能：自動化腳本、多分支並行工作、引用外部 repo、大檔管理。

## Git Hooks

在特定 Git 事件發生時自動執行的腳本，位置在 `.git/hooks/`：

| Hook | 觸發時機 | 用途 |
|---|---|---|
| pre-commit | commit 前 | lint、format、secret scan |
| commit-msg | commit message 建立後 | 檢查 commit 格式 |
| pre-push | push 前 | 跑測試 |
| post-merge | merge 後 | 安裝依賴、清 cache |

```bash
#!/bin/sh
npm test
# 存為 .git/hooks/pre-commit，並 chmod +x .git/hooks/pre-commit
```

**`.git/hooks` 預設不會被 commit**，團隊共享 hooks 通常用 pre-commit framework、Husky、Lefthook，或設定共用路徑：

```bash
git config core.hooksPath .githooks
```

## Git Worktree

讓同一個 repository 同時 checkout 多個 branch 到不同資料夾，不用一直 stash 或切換：

```bash
git worktree add ../my-project-hotfix hotfix/payment          # 建立 worktree
git worktree add -b hotfix/payment ../my-project-hotfix main  # 同時建立新分支
git worktree list
git worktree remove ../my-project-hotfix
git worktree prune                                             # 清理 metadata
```

適合情境：一邊開發 feature 一邊緊急修 hotfix、同時比較兩個 branch、大型 repo 切分工作、避免反覆 stash。

## Submodule vs Subtree

Submodule 在一個 Git repo 中引用另一個 Git repo 的特定 commit：

```bash
git submodule add https://github.com/USER/LIB.git external/lib
git submodule update --init --recursive
git clone --recurse-submodules <url>          # clone 時一併帶入
```

常見坑：主 repo 只記錄 submodule 的 commit、不會自動跟最新版；clone 後忘記 `submodule update`；submodule 裡改了東西但沒 push；CI clone 可能因權限失敗；對初學團隊不友善。

Subtree 則是把另一個 repo 的內容直接合進目前 repo 的子目錄：

```bash
git subtree add --prefix=vendor/lib https://github.com/USER/LIB.git main --squash
git subtree pull --prefix=vendor/lib https://github.com/USER/LIB.git main --squash
```

| 項目 | Submodule | Subtree |
|---|---|---|
| 儲存方式 | 指向外部 repo commit | 把內容合入 repo |
| 使用難度 | 較高 | 較低 |
| 是否需額外 clone | 需要 init/update | 不需要 |
| 適合 | 外部依賴獨立管理 | 想簡化使用者體驗 |

## Git LFS（大檔案管理）

Git 不適合頻繁變動的大型二進位檔（PSD、影片、模型權重等）。Git LFS 把大檔內容放在 LFS 儲存空間，repo 裡只留 pointer file：

```bash
git lfs install
git lfs track "*.psd"                 # 這會修改 .gitattributes，見 git-tag-release-and-repo-config
git add .gitattributes assets/design.psd
git commit -m "chore: track design assets with lfs"
git lfs ls-files
```

注意事項：不要把大型二進位檔直接 commit 到一般 Git 歷史；已 commit 的大檔即使刪掉，歷史中仍存在；GitHub LFS 有儲存與流量限制；追蹤規則要在加入檔案「之前」設定好。

## 與其他頁面的關聯

`.gitattributes` 的其他用途（換行控制）見 [[git-tag-release-and-repo-config]]；hooks 若涉及 CI，對應 GitHub 端的自動化見 [[github-actions-cicd]]；worktree 常見用於 hotfix 流程，對應分支策略見 [[github-workflow-strategies-and-branch-protection]]。
