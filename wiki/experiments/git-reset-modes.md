---
id: exp-git-reset-modes
type: experiment
topic: "git reset --soft / --mixed / --hard 的實際語意"
status: completed
hypothesis: "git-branching-merge-rebase 頁的 reset 對照表正確（soft 保留 staged；mixed 取消 staged；hard 丟掉 working tree）"
result: supported
confidence: high
code_paths: [code/2026-07-09/git-reset-modes/run_experiment.sh]
sources: [git-github-complete-notes]
created: 2026-07-09
updated: 2026-07-09
related: [git-branching-merge-rebase, git-undo-and-recovery, git-core-concepts]
---

# 實驗：git reset 三模式對 Commit／Staging／Working Tree 的影響

本 wiki 第一個 H-I-V-R 實驗，也是「導入學習閉環」這個決定的驗證單元之一：證明在無 Python 的環境下，仍能用現成工具（git）做出真正可執行的 Verification。

## 1. 假設 Hypothesis

### H1（主要）
[[git-branching-merge-rebase]] 頁中的 reset 對照表正確：

| 模式 | Commit | Staging | Working Tree |
|---|---|---|---|
| `--soft` | 回到前一個 | 保留 | 保留 |
| `--mixed` | 回到前一個 | 取消 staged | 保留 |
| `--hard` | 回到前一個 | 取消 | 丟掉 |

理由：這是 Git 官方文件與廣泛實務共識；筆記來源 [[git-github-complete-notes]] 也如此記載。
信心（驗證前）：Medium-High（引用而未親測）。
要驗證的點：三個模式對「staged 與否」「working tree 內容是否保留」的實際差異。

### H2（替代）
`--mixed` 與 `--soft` 對 working tree 的差異可能被我記混（例如誤以為 mixed 也會動到 working tree）。若成立，`--mixed` 後 file.txt 內容會與 `--hard` 相同——這正是本實驗能區分 H1／H2 的關鍵觀察點。

## 2. 實作 Implementation

### 最小實驗設計
- 輸入：一個乾淨 repo，兩個 commit（C1: `file.txt=line1`；C2: `file.txt=line1\nline2`）。
- 操作：對三個獨立 repo 各執行一次 `git reset --<mode> HEAD~1`（從 C2 退回 C1）。
- 觀察：`git log --oneline`、`git status --porcelain=v1`、`cat file.txt`。
- 成功條件：三模式輸出各自符合上表。
- 失敗條件：任一模式的 staging 狀態或 file.txt 內容不符。

### 程式碼
`code/2026-07-09/git-reset-modes/run_experiment.sh`（見 [[git-reset-modes|README]]，已保存並於本機執行）。`git status --porcelain` 判讀：第 1 欄非空 = 已 staged（index），第 2 欄非空 = 未 staged（working tree），全空 = clean。

## 3. 驗證 Verification

於本機實際執行（git 2.55.0.windows.2, Git Bash, 2026-07-09）：

| 編號 | 要驗證的事 | 方法 | 預期 | 實際 | 判定 |
|---|---|---|---|---|---|
| V1 | `--soft` 後 staging 狀態 | `git status --porcelain` | `M ␣`（第1欄=staged） | `M  file.txt` | ✅ |
| V2 | `--soft` 後 working tree | `cat file.txt` | 保留 line1+line2 | `line1\nline2` | ✅ |
| V3 | `--mixed` 後 staging 狀態 | `git status --porcelain` | `␣M`（第2欄=unstaged） | ` M file.txt` | ✅ |
| V4 | `--mixed` 後 working tree | `cat file.txt` | 保留 line1+line2 | `line1\nline2` | ✅ |
| V5 | `--hard` 後 working tree | `cat` + `status` | 只剩 line1、clean | `line1`、status 空 | ✅ |
| V6 | 三模式的 HEAD | `git log --oneline` | 都退回只剩 C1 | 三者皆只剩 C1 | ✅ |

判斷標準：V1 與 V3 是否不同 → 區分「保留 staged / 取消 staged」；V4 與 V5 是否不同 → 區分「保留 / 丟掉 working tree」。兩對都出現差異，故 H1 成立、H2 被排除。

## 4. 反思 Reflection

- 原本我以為：reset 表格正確，但這是「引用未親測」的信心。
- 結果顯示：六個驗證點全部命中，H1 被完整支持，H2（記混 mixed/hard）被排除。
- 心智模型更新為：reset 的三個模式是「一條指標往回移 + 兩個開關」——**Commit 一定退（三者相同）**，差別只在兩個開關：`--soft` 兩開關都「保留」、`--mixed` 關掉 staging、`--hard` 兩個都關（連 working tree 一起丟）。用「一移兩開關」記，比背三行表格穩。
- 下次遇到類似問題，先檢查：
  1. 想確認某個 git 破壞性指令的行為時，開臨時 repo 實測比查文件快也更可信（工具就在手邊）。
  2. 用 `git status --porcelain` 的兩欄位置判 staged/unstaged，比看人類可讀訊息更精確。
  3. `--hard` 是唯一動 working tree 的模式——這也是 [[git-undo-and-recovery]] 危險指令表把它列第一的原因。

## 5. 後續問題 Next Questions
1. `--hard` 丟掉的 C2，能否只靠 `git reflog` 100% 救回？（下一個可實測實驗，連 [[git-undo-and-recovery]]）
2. `git restore --staged` 與 `git reset --mixed` 在「取消 staged」上是否等價？差異在哪？
3. 對「已 push 的 commit」，reset 與 revert 的可觀察差異能否也用 repo 實測呈現？
