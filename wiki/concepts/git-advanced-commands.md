---
type: concept
title: "Git 進階指令"
tags: [git]
sources: [git-github-complete-notes]
created: 2026-07-09
updated: 2026-07-09
---

# Git 進階指令

較少日常使用、但在特定情境（除錯、大型 repo、搬移 repo）非常關鍵的一組指令。

## bisect：二分搜尋找出引入 bug 的 commit

```bash
git bisect start
git bisect bad                  # 標記目前是壞的
git bisect good v1.0.0          # 標記某個舊版本是好的
# Git 會自動切到中間 commit，測試後標記
git bisect good   # 或 git bisect bad
git bisect reset  # 結束
```

## grep 與 blame：搜尋與追溯

```bash
git grep "function login"        # 搜尋 repo 內容
git grep "TODO" HEAD~3           # 指定 commit
git blame src/app.js             # 行級歷史
git blame -w src/app.js          # 忽略空白差異
```

## archive 與 bundle：打包與離線搬移

```bash
git archive --format zip --output source.zip main    # 打包原始碼（不含 .git）

git bundle create repo.bundle --all   # 建立可離線搬移的完整 repo bundle
git clone repo.bundle repo            # 從 bundle clone
```

## 大型 repo 的效能技巧

```bash
git sparse-checkout init --cone
git sparse-checkout set src docs                       # 只 checkout 部分目錄，適合大型 monorepo

git clone --filter=blob:none <url>                      # partial clone，延遲下載 blob 內容
```

## Bare repository

沒有 working tree，常用於伺服器端存放 repo：

```bash
git init --bare myrepo.git
```

## 完整性檢查與清理

```bash
git fsck    # 檢查物件完整性
git gc      # 清理與壓縮，回收無用物件
```

## 與其他頁面的關聯

sparse checkout 與 monorepo 策略相關的 CI/CODEOWNERS 搭配見 [[github-repository-and-project-management]]；bare repository 常配合自架 Git 伺服器或 CI 環境，與 [[github-actions-cicd]] 中的 runner 環境概念相關。
