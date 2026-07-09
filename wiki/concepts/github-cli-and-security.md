---
type: concept
title: "GitHub CLI（gh）與安全治理（Dependabot／CodeQL／權限／SSH）"
tags: [github]
sources: [git-github-complete-notes]
created: 2026-07-09
updated: 2026-07-09
---

# GitHub CLI（gh）與安全治理

涵蓋 GitHub 官方命令列工具 `gh`，以及 GitHub 的安全功能（Dependabot、CodeQL、Secret Scanning）、權限模型（Organization/Team/Repository roles）、以及 SSH/HTTPS/PAT/Commit signing 等驗證機制。

## GitHub CLI：gh

```bash
gh auth login                                                    # 登入
gh repo create my-repo --public --source=. --remote=origin --push
gh repo clone OWNER/REPO
gh pr create --base main --head feature/login --title "feat: add login"
gh pr view 123 / gh pr checkout 123 / gh pr merge 123 --squash --delete-branch
gh issue create --title "Bug: login fails"
gh workflow run ci.yml / gh run list / gh run view --log / gh run rerun <run-id>
gh secret set API_TOKEN / gh secret list
gh release create v1.0.0 --title "v1.0.0" --notes "First release"
```

## GitHub Security 功能總覽

| 功能 | 用途 |
|---|---|
| Dependabot alerts / updates | 偵測有漏洞的依賴、自動開 PR 更新 |
| Dependency graph | 依賴關係視覺化 |
| Code scanning / CodeQL | 把程式碼當資料查詢，找出漏洞與錯誤 |
| Secret scanning | 偵測 repo 中的 token/key/credentials |
| Push protection | 在 secret 被 push 進 repo **前**就阻擋 |
| Security policy（`SECURITY.md`） | 說明支援版本與漏洞回報方式 |
| Private vulnerability reporting | 私下回報漏洞的管道 |

`dependabot.yml`（位於 `.github/dependabot.yml`）範例：

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    labels: ["dependencies", "security"]
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
```

CodeQL 支援 C/C++、C#、Go、Java/Kotlin、JavaScript/TypeScript、Python、Ruby、Rust、Swift、GitHub Actions workflows，結果顯示為 code scanning alerts。

**誤 commit secret 的處理順序**：立刻 revoke/rotate secret → 從目前版本移除 → 視情況清理 Git history（`git filter-repo` 或 BFG Repo-Cleaner）→ 通知團隊重新 clone → 啟用 secret scanning/push protection。**刪除檔案不等於 secret 從歷史消失**——歷史清理與救援的其餘指令見 [[git-undo-and-recovery]]。

## 權限、Organization、Team

Repository roles：Read（查看討論）< Triage（管理 issue/PR）< Write（一般開發者）< Maintain（管理 repo，非破壞操作）< Admin（完整權限含刪除 repo）。最小權限原則建議：一般開發者 Write、Tech lead Maintain、Repo owner/DevOps Admin、產品/QA Triage 或 Read。

Organization 提供 Teams、Repository permissions、Organization secrets、Rulesets、Audit log、SSO/SAML、2FA enforcement。Team 可用於管理 repo 權限、CODEOWNERS 指派、PR review request。

Deploy key 是加到 repo 的 SSH key，可讓機器讀寫 repo；**擁有 private key 者即使被移出 organization，只要 key 仍有效仍可能存取該 repo**，建議只給 read-only、每個 repo/service 用不同 key、定期 rotate。

## SSH、HTTPS、PAT 與 Commit Signing

| 方式 | 優點 | 缺點 |
|---|---|---|
| HTTPS + PAT / Credential Manager | 容易設定，企業代理較友善 | token 管理要小心 |
| SSH key | 開發體驗好，不必每次輸密碼 | key 管理與 agent 設定需理解 |

```bash
ssh-keygen -t ed25519 -C "you@example.com"     # 建議演算法
eval "$(ssh-agent -s)"; ssh-add ~/.ssh/id_ed25519
ssh -T git@github.com                          # 測試連線
```

Personal Access Token 原則：只給必要權限、設定過期時間、不硬編碼在程式碼、不貼在 Issue/PR/Actions logs、洩漏後立刻 revoke。GitHub 已不再接受帳密作為 HTTPS Git 操作密碼，改用 Credential Manager / PAT / SSH key / `gh auth login`。

Commit signing（顯示 verified commit）可用 GPG key、SSH signing key 或 S/MIME：

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
git commit -S -m "feat: signed commit"
```

## 最小安全 GitHub Repo Baseline

建議每個 repo 至少具備：`README.md`、`LICENSE`、`SECURITY.md`、`.gitignore`、`.gitattributes`、`.github/pull_request_template.md`、`.github/ISSUE_TEMPLATE/`、`.github/CODEOWNERS`、`.github/dependabot.yml`、`.github/workflows/ci.yml`；設定上 private by default（非開源）、`main` 為預設分支、merge 後自動刪除分支、啟用 vulnerability alerts 與 secret scanning/push protection。

## 與其他頁面的關聯

CODEOWNERS 的檔案格式見 [[github-repository-and-project-management]]；Actions 中使用 secrets 的方式見 [[github-actions-cicd]]；誤操作後的 Git 層級救援見 [[git-undo-and-recovery]]；分支保護中的 signed commits 要求見 [[github-workflow-strategies-and-branch-protection]]。
