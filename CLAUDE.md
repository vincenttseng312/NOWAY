# CLAUDE.md — LLM Wiki 專案操作規範（正式版）

> 本檔是本專案的操作 charter，每個 session 開場載入。**正本**位於 `C:\Users\vincenttseng\LLM_Wiki\CLAUDE.md`。
> 版本：2026-07-09（導入 H-I-V-R-K-C 學習閉環後改寫）。

---

## 0. 本檔定位與權威順序

- **開場三步**（回答任何需要本專案累積知識的問題前）：① 讀本檔 → ② 讀 `wiki/SCHEMA.md` → ③ 讀 `wiki/index.md`（若已分片，讀 `wiki/indexes/` 下對應分片）。
- **權威順序**：wiki 頁面機制的細節（頁型、frontmatter、標籤、分片）以 `wiki/SCHEMA.md` 為準；**工作風格與流程**以本檔為準。兩者若衝突：結構性規則聽 SCHEMA，行為模式聽本檔。
- 本檔與 SCHEMA 有意重疊處，以「本檔給協定、SCHEMA 給機制」分工。

## 1. 專案是什麼

- 一個結合 **Karpathy「LLM Wiki」模式** 與 **H-I-V-R-K-C 假設驅動學習閉環** 的個人知識庫（https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f）。
- **主路徑**：`C:\Users\vincenttseng\LLM_Wiki`（同時是一個 Obsidian vault，有 `.obsidian/`）。`C:\Users\vincenttseng\tt` 是 2026-07-08 前的舊鏡像，**已停用**，其 CLAUDE.md 只是指回本檔的指標。
- **目標**：不是堆積資料，而是養成「假設驅動、可驗證、可重跑、會複利」的知識。最高原則是引導使用者問「**我如何知道它是真的**」，把他從資料收集者訓練成假設驅動的實作者。

## 2. 語言慣例

- **對話與 wiki 正文**：一律繁體中文（自 2026-07-08 起）。
- **維持英文**：YAML frontmatter 欄位名、`tags` 值、頁面 slug／檔名、程式碼識別字（如 `DllMain`、`git reset --hard`）。
- **保留原文**：`source` 頁的 `title` 欄位保留原始來源語言以利精確引用。
- 2026-07-08 前的舊 log 條目維持英文原樣，不回頭翻譯。完整規則見 `wiki/SCHEMA.md`「語言慣例」。

## 3. 目錄結構

```
LLM_Wiki/
├── CLAUDE.md          ← 本檔（操作 charter 正本）
├── changelog.md       ← 結構級里程碑（新頁型、導入流程、分片…）
├── raw/               ← 使用者的原始來源（ingest 前先落地於此，用 slug 檔名）
├── wiki/
│   ├── SCHEMA.md      ← 頁面機制的權威設定檔（最先讀）
│   ├── index.md       ← 所有頁面的一行摘要目錄（查詢先讀這裡）
│   ├── log.md         ← 逐次 ingest／experiment／lint 的時間序紀錄
│   ├── sources/       ← 每個來源一篇摘要頁
│   ├── entities/      ← 具體事物（人／產品／工具／論文）
│   ├── concepts/      ← 想法／方法／框架
│   ├── experiments/   ← H-I-V-R 學習單元（假設→實作→驗證→反思）
│   └── synthesis/     ← 跨主題分析、查詢歸檔、統整型 reflection
├── templates/         ← concept_note / experiment_note / reflection / code_readme
├── db/                ← learning_log / experiments / concepts / code_index 的 .jsonl + .schema.json
└── code/              ← YYYY-MM-DD/<topic>/ 可複用、可重跑的程式碼資產
```

## 4. 兩層知識模型（加法式，不互相取代）

- **底層 = 知識回灌（K）的落點**：Karpathy wiki，即 `sources / entities / concepts / synthesis` + `index.md` + `log.md`。穩定、原子化、互相 `[[wikilink]]`。
- **上層 = H-I-V-R 前端**：`experiments/` + `code/` + `db/` + `templates/` + `changelog.md`。負責「假設→實作→驗證→反思」的過程與可重跑資產。
- 上層疊在底層之上。實驗若驗證了某 concept 頁的主張，就手術式回灌該頁（連結實驗頁、調整信心敘述）。

## 5. 回答問題的協定（Query）

1. 先讀 `wiki/index.md`（或分片），用一行摘要選出候選頁。
2. 讀候選頁 + 其相關 backlinks，再作答。
3. 用 `[[wikilink]]` 引用所有引述的頁面。
4. 值得複用的答案，歸檔到 `wiki/synthesis/`。
5. 索引找不到好候選 → 有 Python 時用 `llm-wiki` 技能的 `wiki_search.py` 做 BM25；**目前無 Python，改用手動 Grep/Glob**。
6. wiki 未涵蓋就**明講**，標為候選 ingest 主題，**絕不編造**（避免 silent corruption）。

## 6. H-I-V-R-K-C 學習閉環（核心工作流）

**適用範圍**：用於「學習單元」——要精通的概念、要驗證的技術、要 build 的東西。

七步（產物落點見第 3 節）：

1. **H 假設**：至少一個主要假設 + 有不確定性時給替代假設；標信心（Low/Med/High）；明寫「要驗證什麼」。不可把猜測寫成事實。
2. **I 實作**：設計最小可行實驗（輸入／操作／預期輸出／成功條件／失敗條件）。需程式碼時**給完整檔案、不給片段**，每個區塊標檔案路徑，附執行方式／測試方式／預期輸出。
3. **V 驗證**：`expected vs actual` 表 + 判斷標準。見第 8 節環境邊界。
4. **R 反思**：原本怎麼想 → 結果如何改變想法 → 下次判斷流程如何升級。（不是總結。）
5. **K 回灌**：列出要更新的頁、要新增的卡片／實驗記錄、要 append 的 `db/*.jsonl`，並直接產出可貼入的內容。
6. **C 程式碼保存**：存到 `code/YYYY-MM-DD/<topic>/`，至少含 `README.md` + `manifest.json` + 主檔 + 驗證腳本。不產生無路徑、無測試的孤兒程式碼。
7. **Next Questions**：產生下一輪更好的問題。

**輕量模式（重要）**：純事實／指令查詢**不套七段**（例如「這是什麼」「指令怎麼打」）。至多附一行「這可以怎麼驗證」的鉤子。判斷法：問「學／搞懂／驗證／build」→ 全閉環；問「是什麼／怎麼打／在哪」→ 輕量。動手前若範圍不明，先確認走全套或輕量。

## 7. Ingest 流程（新增來源）

1. 來源先落地 `raw/`，用 slug 檔名（小寫、連字號、保留副檔名）。
2. 大型來源分段讀（單次別吃掉 >25% context）。
3. 動筆前先跟使用者聊 takeaway，並**確認拆分粒度**（粗／細）。
4. 寫 `wiki/sources/<slug>.md` 摘要頁（完整 frontmatter + 回指 raw）。
5. 找出受影響的既有頁，用 `str_replace` **手術式更新**，不整頁重寫。
6. 新概念／實體開新頁，且**每頁至少一條 inbound `[[wikilink]]`**（否則是 ingest 的 bug，不只是 lint 問題）。
7. 更新 `wiki/index.md`；在 `wiki/log.md` 追加一行。
8. 更新既有主張前，**回讀 raw source**，別拿 wiki 自己的轉述複利。

## 8. Verification／Code Preservation 的環境邊界（硬規則）

- 本機**無 Python**。凡是能用**現成工具（git、bash/Git Bash、PowerShell）**驗證的，就實測並在 V 表「實際」欄填**真 actual**。
- 不能在本機執行的（需 Python／特定 runtime／真實惡意樣本環境）：「實際」欄標 `⏳待執行`，程式碼仍完整保存並標 `verified_on_this_machine: false`，**絕不編造執行結果**（不做驗證劇場）。
- `db/*.jsonl` 目前是「可攜出的結構化備份」，裝 Python 前無法被查詢腳本索引；人看的快取仍是 `index.md` / `log.md`。

## 9. 資安／惡意程式主題原則（防禦優先）

本知識庫的資安內容**只為防禦、鑑識、偵測、報告**服務。

- **允許**：分析概念、防禦觀察點、benign/toy 模擬、log 分析、偵測邏輯、YARA/Sigma 防禦規則、隔離環境中的觀察流程、報告模板、高階原理說明。
- **不允許**：可直接濫用的惡意 payload、真實攻擊部署、持久化惡意植入教學、繞過偵測的操作步驟、竊取憑證／外洩資料／未授權存取、把防禦分析轉成攻擊實作。
- 遇高風險主題，閉環退化為：**概念 → 防禦觀察點 → benign 模擬 → log evidence → detection rule → report template**。

## 10. 規模化紀律

- **原子頁**：軟上限 400 行 / 硬上限 800 行，超過就拆（抽子概念成新頁、父頁連過去）。
- **分片**：`index.md` 超 ~300 行或 wiki 超 ~150 頁 → 分片為 `wiki/indexes/<type>.md`。
- 每頁必備 frontmatter（`type`/`title`/`tags`/`created`/`updated` + 類型專屬欄位）。
- 每個跨頁引用用 `[[wikilink]]`；更新用 `str_replace` 手術式編輯。
- 每條 wiki 主張都要能追到 `sources`（避免 silent corruption 與 wiki 讀自己輸出的漂移）。

## 11. 維護節奏

- 結構性 lint：每 5 次 ingest。語意性 lint：每週或每 20 次 ingest。缺口盤點：每月。
- 結構級里程碑寫 `changelog.md`；逐次 ingest／experiment／lint 寫 `wiki/log.md`。
- 目前無 Python，`wiki_lint.py` 跑不動，lint 需手動 Grep/Glob（查孤兒頁、失效 `[[連結]]`、超大頁、frontmatter 缺欄位）。

## 12. 工具限制

- **無 Python**（只有 Windows Store 佔位程式）：`wiki_search.py` / `wiki_lint.py` / `wiki_stats.py` / graph 工具全部無法執行；`wiki/graph/` 圖譜層**未啟用**，除非日後裝了 Python 且使用者要求。
- **可用**：`git`、`bash`（Git Bash）、`PowerShell`。這界定了第 8 節 V/C 的可驗證範圍。
- 裝上 Python 會一次解鎖：JSONL 可查詢、V/C 全面驗證、lint 自動化——值得列為里程碑。

---

_修改本檔請同步在 `changelog.md` 記一行。`tt\CLAUDE.md` 是指回本檔的精簡指標，勿在該處放實質規則以免漂移。_
