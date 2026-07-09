#!/usr/bin/env bash
#
# run_experiment.sh — 驗證 git reset 三種模式對 Commit / Staging / Working Tree 的實際影響
#
# 對應實驗頁：wiki/experiments/git-reset-modes.md
# 對應概念頁：wiki/concepts/git-branching-merge-rebase.md（reset 對照表）
#
# 設計：對每個模式各建一個乾淨的臨時 repo，做出 C1、C2 兩個 commit
#       （C2 讓 file.txt 從 "line1" 變成 "line1\nline2"），
#       然後 `git reset --<mode> HEAD~1`（從 C2 退回 C1），
#       觀察 git log / git status --porcelain / file.txt 三項。
#
# 執行：bash run_experiment.sh
# 依賴：git、bash、mktemp（不需要 Python）
set -euo pipefail

BASE="$(mktemp -d)"
trap 'rm -rf "$BASE"' EXIT

run_trial() {
  local mode="$1"
  local d="$BASE/$mode"
  mkdir -p "$d"; cd "$d"
  git init -q
  git config user.email a@b.c
  git config user.name test
  git config commit.gpgsign false

  printf 'line1\n' > file.txt
  git add .
  git commit -qm C1

  printf 'line1\nline2\n' > file.txt
  git add .
  git commit -qm C2

  git reset "--$mode" -q HEAD~1

  echo "=== mode=--$mode  (reset HEAD~1: 從 C2 退回 C1) ==="
  echo "-- git log --oneline --"
  git log --oneline
  echo "-- git status --porcelain=v1  (第1欄=index/staged, 第2欄=working tree; 空=clean) --"
  git status --porcelain=v1 || true
  echo "-- cat file.txt --"
  cat file.txt
  echo
}

run_trial soft
run_trial mixed
run_trial hard

echo "git version: $(git --version)"
