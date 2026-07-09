# git reset 三模式驗證腳本

## 目的
用真實 `git` 指令驗證 `git reset --soft / --mixed / --hard` 對 Commit、Staging、Working Tree 三者的實際影響，並示範在「無 Python」的環境下，凡是有現成工具（git/bash）就能做出真正的 Verification，而非驗證劇場。

## 驗證的假設
對應實驗頁：[[git-reset-modes]]。驗證的假設是：`wiki/concepts/git-branching-merge-rebase.md` 中的 reset 對照表正確——
- `--soft`：Commit 退回、Staging 保留、Working Tree 保留
- `--mixed`：Commit 退回、Staging 取消、Working Tree 保留
- `--hard`：Commit 退回、Staging 取消、Working Tree 丟掉

## 檔案結構
```
code/2026-07-09/git-reset-modes/
├── README.md
├── manifest.json
└── run_experiment.sh
```

## 執行方式
```bash
bash code/2026-07-09/git-reset-modes/run_experiment.sh
```

## 測試方式
跑上面的指令，把輸出對照下方「預期輸出」。三個模式的 `git status --porcelain`、`file.txt` 內容、`git log` 若全部相符即通過。

## 預期輸出
```
=== mode=--soft  ===   git log 只剩 C1；status: "M  file.txt"(第1欄M=staged)；file.txt: line1+line2
=== mode=--mixed ===   git log 只剩 C1；status: " M file.txt"(第2欄M=unstaged)；file.txt: line1+line2
=== mode=--hard  ===   git log 只剩 C1；status: 空(clean)；file.txt: 只剩 line1
```

## 實驗結果
2026-07-09 於本機（git 2.55.0.windows.2, Git Bash）實際執行，三模式全部符合預期，假設 **supported**，信心 High。（唯一雜訊：Windows autocrlf 的 LF→CRLF warning，屬 cosmetic，不影響結論。）

## 反思
三個月後這段還跑得起來嗎？可以——只依賴 git + bash + mktemp，無語言 runtime 依賴，是這個 wiki 目前少數「我能自己驗證」的資產類型。若日後改用 PowerShell-only 環境，需把 `mktemp`／`printf` 換成對應寫法。

## 後續可擴充方向
- 加入 `reset --hard` 後用 `git reflog` 救回 C2 的驗證（連到 [[git-undo-and-recovery]]）。
- 擴充成「reset vs revert vs restore」對照實驗。
