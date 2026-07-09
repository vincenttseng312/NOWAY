---
type: concept
title: "Git Tag、Release 與 Repo 設定檔（.gitignore／.gitattributes）"
tags: [git]
sources: [git-github-complete-notes]
created: 2026-07-09
updated: 2026-07-09
---

# Git Tag、Release 與 Repo 設定檔

涵蓋版本標記、Semantic Versioning、GitHub Release 流程，以及 `.gitignore`／`.gitattributes` 這類 repo 層級設定檔。

## Tag 與 Semantic Versioning

| 類型 | 指令 | 說明 |
|---|---|---|
| Lightweight tag | `git tag v1.0.0` | 像簡單指標 |
| Annotated tag | `git tag -a v1.0.0 -m "release: v1.0.0"` | 有作者、日期、訊息，正式 release 建議用這種 |

```bash
git push origin v1.0.0        # 推單一 tag
git push origin --tags        # 推全部 tag
git tag -d v1.0.0              # 本機刪除
git push origin --delete v1.0.0  # 遠端刪除
```

Semantic Versioning 格式 `MAJOR.MINOR.PATCH`：MAJOR 代表不相容變更、MINOR 代表向下相容的新功能、PATCH 代表向下相容的 bug fix。

GitHub Release 通常基於 tag 建立，包含版本標題、release notes、binary assets、source code archive、changelog：

```bash
git tag -a v1.2.0 -m "release: v1.2.0"
git push origin v1.2.0
# 再到 GitHub 建立 Release，或用 gh release create（見 github-cli-and-security）
```

## .gitignore

告訴 Git 哪些未追蹤檔案不需納入版本控制，常見忽略項：`node_modules/`、`dist/`、`.env`、`*.log`、`.DS_Store`、`__pycache__/`。

**已被追蹤的檔案，`.gitignore` 不會自動生效**——要先取消追蹤再 commit：

```bash
git rm --cached .env
git commit -m "chore: stop tracking env file"
```

全域 ignore（跨所有 repo 生效）：

```bash
git config --global core.excludesfile ~/.config/git/ignore
```

## .gitattributes

可控制換行符號、檔案類型 diff 策略、merge 策略、Git LFS tracking（見 [[git-hooks-worktree-submodule-lfs]]）、語言判斷。換行統一範例：

```gitattributes
* text=auto
*.sh text eol=lf
*.bat text eol=crlf
*.png binary
```

重新正規化既有檔案的換行：

```bash
git add --renormalize .
git commit -m "chore: normalize line endings"
```

## 與其他頁面的關聯

`core.autocrlf` 的初始設定見 [[git-setup-and-daily-workflow]]；Git LFS 的 `.gitattributes` tracking 規則見 [[git-hooks-worktree-submodule-lfs]]；GitHub Release 的 `gh` CLI 操作見 [[github-cli-and-security]]；推薦的 `.gitignore`/`.gitattributes` 起手式範本收錄在來源頁 [[git-github-complete-notes]] 的附錄摘要中。
