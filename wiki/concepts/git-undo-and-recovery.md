---
type: concept
title: "Git Undo／Recovery 救援大全與 Stash"
tags: [git]
sources: [git-github-complete-notes]
created: 2026-07-09
updated: 2026-07-09
---

# Git Undo／Recovery 救援大全與 Stash

Git 筆記中最實用、查閱頻率最高的一章：涵蓋各種「改壞了怎麼辦」的情境，核心工具是 [[git-core-concepts]] 提到的 reflog。也收錄 stash（暫存未完成工作）與危險指令警戒表。

## 依「想回到哪裡」分流

```bash
git restore file.txt                # 丟掉單一檔案未 staged 的修改
git restore .                       # 丟掉全部未 staged 修改
git restore --staged file.txt       # 取消 staged（不影響工作目錄內容）
git commit --amend                  # 修改最後一次 commit

git reset --soft HEAD~1             # 回到上一 commit，保留修改且仍 staged
git reset --mixed HEAD~1            # 回到上一 commit，保留檔案但取消 staged
git reset --hard HEAD~1             # 完全丟掉最後一次 commit 與修改（危險）
```

**已 push 到共享 branch 的 commit，不要用 reset，改用 `git revert <commit>`**（建立一個新 commit 反向取消變更，不改寫歷史）。

## Reflog 救援三連發

```bash
git reflog                                    # 找出誤操作前的 commit hash
git switch -c recovered-branch <commit-hash>  # 誤刪 branch
git reset --hard <old-commit>                 # 誤 reset --hard
git reset --hard <before-rebase-commit>       # 誤 rebase
```

Reflog 記錄本機 reference 的移動歷史，是 reset/rebase/amend/誤刪 branch 之後幾乎都能救回的關鍵工具——但僅限本機、且有時效性（未被 GC 回收前）。

## 清除 untracked files

```bash
git clean -n      # 預覽（務必先執行這個）
git clean -f      # 刪除 untracked files
git clean -fd     # 刪除 untracked files 與 directories
git clean -fdx    # 連 ignored files 也刪除
```

`git clean` 沒有 reflog 可救，**務必先用 `-n` 預覽**。

## Stash：暫存未完成工作

臨時要切 branch 或 pull 最新變更，又不想 commit 半成品時使用：

```bash
git stash                              # 快速暫存
git stash push -m "wip: login form"    # 帶訊息
git stash -u                           # 包含 untracked files
git stash list                         # 查看清單
git stash show -p stash@{0}            # 查看內容
git stash apply stash@{0}              # 套用但保留 stash
git stash pop                          # 套用並刪除
git stash drop stash@{0}               # 刪除特定 stash
git stash branch feature/from-stash stash@{0}   # 從 stash 直接建立新分支
```

## 危險指令警戒表

| 指令 | 風險 | 安全替代或注意事項 |
|---|---|---|
| `git reset --hard` | 丟掉 working tree 修改 | 先 `git status`，必要時 `git stash -u` |
| `git clean -fdx` | 刪除 untracked 與 ignored files | 先 `git clean -n` |
| `git push --force` | 覆蓋遠端歷史 | 用 `--force-with-lease`，見 [[git-remote-collaboration]] |
| 對共享 branch `rebase` | 改寫他人基於的歷史 | 只 rebase 自己的 branch，見 [[git-branching-merge-rebase]] |
| 刪除 tag 後重建 | 破壞 release 可追溯性 | 正式 release tag 避免重寫 |
| 清 Git history（如誤 commit secret 後） | 影響所有 clone | 先溝通、備份、公告，並立即 revoke/rotate 洩漏的憑證 |

## 與其他頁面的關聯

Reflog 的資料模型基礎見 [[git-core-concepts]]；reset/rebase/revert 的正常用法見 [[git-branching-merge-rebase]]；force push 相關風險見 [[git-remote-collaboration]]；誤 commit secret 後的完整處理流程（含 GitHub Push Protection）見 [[github-cli-and-security]]。
