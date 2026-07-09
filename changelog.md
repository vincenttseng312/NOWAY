# Changelog

本檔記錄 wiki 結構層級的重大變更（新增頁型、導入流程、分片等）。逐次 ingest／實驗的細節在 `wiki/log.md`；本檔只留「里程碑」。

- 2026-07-09：導入 H-I-V-R-K-C 學習閉環（加法式）。新增 `templates/`（concept/experiment/reflection/code_readme）、`db/`（learning_log/experiments/concepts/code_index 的 jsonl 與 2 份 schema）、`code/`、`wiki/experiments/` 頁型、本 changelog。既有 34 頁保持不動。SCHEMA.md 記錄新約定與「無 Python → V/C 邊界」。完成第一個實驗 [[git-reset-modes]]（reset 三模式，本機實測 supported），保存程式碼於 `code/2026-07-09/git-reset-modes/`。
- 2026-07-09：改寫 `CLAUDE.md` 為正式版操作 charter（13 節，涵蓋權威順序／兩層知識模型／查詢協定／H-I-V-R-K-C／ingest／V-C 邊界／資安防禦原則／規模化紀律／維護節奏／工具限制）。確立 `LLM_Wiki\CLAUDE.md` 為正本、`tt\CLAUDE.md` 降為指標，避免雙路徑漂移。
