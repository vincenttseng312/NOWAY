---
type: concept
title: "GitHub Actions CI/CD"
tags: [github, ci-cd]
sources: [git-github-complete-notes]
created: 2026-07-09
updated: 2026-07-09
---

# GitHub Actions CI/CD

GitHub 內建的自動化平台，在 push/PR/release/schedule/manual trigger 等事件發生時自動執行 build、test、deploy、scan 等任務。Workflow 檔案位於 `.github/workflows/*.yml`。

## 核心概念

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
| Secret / Variable | 敏感 / 非敏感設定值 |

## 最小 workflow 範例

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
      - uses: actions/checkout@v4
      - name: Run tests
        run: echo "run tests here"
```

常見觸發事件：`on: push`、`on: [push, pull_request]`、`paths:` 過濾特定路徑、`workflow_dispatch`（手動觸發）、`schedule: - cron: '0 0 * * *'`（注意 cron 以 UTC 計算）。

Node.js / Python CI 範例都會用到 `actions/checkout@v4` + 對應語言的 `setup-*` action + `strategy.matrix` 測試多版本，並建議設定 `permissions: contents: read` 走最小權限。

## Job 依賴、條件執行、Matrix

```yaml
jobs:
  deploy:
    needs: test                              # job 依賴
    if: github.ref == 'refs/heads/main'      # 條件執行
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
```

## Cache 與 Artifact

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-npm-${{ hashFiles('package-lock.json') }}

- uses: actions/upload-artifact@v4
  with:
    name: build-output
    path: dist/
```

## Environment 與部署保護

```yaml
jobs:
  deploy:
    environment: production   # 可設定 required reviewers、wait timer、environment secrets、deployment branches
```

## Secrets、Variables 與 GITHUB_TOKEN

Secrets（token/password/private key）與 Variables（region、非敏感設定）分開管理；設定路徑 `Settings -> Secrets and variables -> Actions`，或 `gh secret set SECRET_NAME`。

```yaml
steps:
  - env:
      API_TOKEN: ${{ secrets.API_TOKEN }}
    run: echo "Token length is ${#API_TOKEN}"   # 不要直接 echo secret 本身
```

每個 job 有自動產生的 `GITHUB_TOKEN`，**建議明確設定最小 permissions**（例如僅 `contents: read`，需要建立 release 才加 `contents: write`，需要寫 PR comment 才加 `pull-requests: write`）。Secret 不該放在 `.env` committed to repo、README、Issue/PR comment、Actions logs、Docker image layer、前端 bundle。

## Actions 安全原則

`permissions` 預設最小化；不在 log 印出 secret；第三方 action 盡量 pin 到 commit SHA；PR from fork 的 workflow 權限需小心；不要在 `pull_request_target` 中 checkout 不可信程式碼後執行；production deploy 需 reviewer approval；定期更新 actions 版本（Dependabot 也可更新 GitHub Actions references，見 [[github-cli-and-security]]）。

## GitHub Pages

可從 repo 發布靜態網站（個人首頁、專案文件、blog、demo）。發布來源可選特定 branch（如 `main /docs` 或 `gh-pages` branch）或透過 Actions workflow。常見 404 原因：沒有 `index.html`、發布來源選錯、branch 未 build 完、Jekyll build 失敗、SPA routing 無 fallback、custom domain DNS 未生效。

## 與其他頁面的關聯

CI 的 status checks 對應 [[github-workflow-strategies-and-branch-protection]] 的合併條件；Dependabot/CodeQL 等安全掃描見 [[github-cli-and-security]]；`gh workflow run`/`gh run list` 等 CLI 操作也在 [[github-cli-and-security]]。
