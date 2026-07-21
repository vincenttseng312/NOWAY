# Wiki 架構說明（Schema）

這個檔案是這份 wiki 的設定檔，記錄了慣例、頁面類型、標籤分類法，以及任何工作流程上的客製化。LLM 進入 wiki 時會最先讀這個檔案，這裡的規範會覆蓋 `llm-wiki` 技能文件中所描述的預設值。

這個檔案是**與使用者共同演進**的。當 LLM 注意到使用者的編輯或回饋中出現這裡沒記錄的規律模式時，會主動提議加進來；當某條規則不再適用時，也會提議刪除。

## Wiki 位置

- Wiki 根目錄：`wiki/`
- 原始來源：`raw/`
- 資源／圖片儲存：`raw/assets/`

## 語言慣例

- **對話語言**：自 2026-07-08 起，與使用者的對話一律使用繁體中文。
- **Wiki 內容（正文）**：所有頁面的正文（source、entity、concept、synthesis）一律以繁體中文撰寫。
- **保持原文（不翻譯）的部分**：
  - YAML frontmatter 的欄位名稱（`type`、`title`、`tags`、`sources`、`created`、`updated` 等）— 這些是結構化欄位，不是散文內容。
  - `tags` 的值 — 維持英文 slug 形式（例如 `windows`、`dll`、`dotnet`），以確保跨頁面標籤比對一致。
  - 頁面檔名／slug（例如 `dynamic-link-library.md`）— `[[wikilink]]` 依賴這些 slug 解析，不可翻譯。
  - `source` 頁面的 `title` 欄位 — 保留原始來源的英文標題，作為精確引用；但內文的 `# 標題` 大標題與敘述可用中文說明。
  - 程式碼區塊、函式名稱、API 名稱（如 `DllMain`、`LoadLibrary`、`__declspec(dllexport)`）— 維持英文原樣。
- 舊有（2026-07-08 之前）以英文寫成的 log 條目維持原樣，視為歷史紀錄，不回頭翻譯。

## 頁面類型

這個 wiki 使用以下頁面類型，各自有專屬子目錄：

- `source`（位於 `wiki/sources/`）— 每個已收錄來源對應一篇摘要頁。
- `entity`（位於 `wiki/entities/`）— 描述具體事物的頁面：人物、論文、產品、地點、組織。
- `concept`（位於 `wiki/concepts/`）— 描述想法、方法、框架、抽象概念的頁面。
- `experiment`（位於 `wiki/experiments/`）— 一個可驗證的學習單元：假設→實作→驗證→反思。自 2026-07-09 導入 H-I-V-R-K-C 流程後新增，見下方「工作流程客製化」。
- `synthesis`（位於 `wiki/synthesis/`）— 跨主題分析、比較，或查詢結果的歸檔。（跨多實驗的統整型 `reflection` 也歸這裡，tag 標 `reflection`。）

隨著 wiki 演進可在此新增其他類型。

## 標籤分類法（Tag taxonomy）

（初始為空。採用新標籤時請在此記錄，附一行說明。保持精簡且有紀律 —— 一個有 200 個標籤的 wiki 等於沒有標籤。）

範例結構：
- `methodology` — 關於研究或分析方法的頁面。
- `open-question` — 標記尚未解決問題的頁面或段落。
- `contested` — 來源之間互相矛盾的頁面。

已採用的標籤：
- `windows` — Windows 作業系統相關主題。
- `dll` — DLL／動態連結相關主題。
- `dotnet` — .NET 平台相關主題。
- `malware-analysis` — 惡意程式分析技術與實作。
- `dfir` — 數位鑑識與資安事件應變（Digital Forensics & Incident Response）。
- `sysinternals` — 微軟 Sysinternals 工具集。
- `git` — Git 版本控制本身（與平台無關的部分）。
- `github` — GitHub 平台功能（Issues/PR/Actions/Security 等）。
- `ci-cd` — CI/CD 自動化流程，目前主要指 GitHub Actions。
- `devops` — 跨工具鏈的維運／協作流程主題。
- `sysinternals` — 微軟 Sysinternals 工具集。
- `ai-security` — AI 系統或 AI 輔助安全工作的主題。
- `llm-security` — LLM、RAG、agent 的攻擊面、測試與防護。
- `security-tools` — 具體資安工具或產品實體。
- `pentesting` — 已授權滲透測試與攻擊模擬。
- `appsec` — 應用程式安全。
- `sast` — 靜態應用程式安全測試。
- `guardrails` — AI 應用的輸入、輸出與工具使用防護。
- `mcp` — Model Context Protocol 及其工具整合安全。
- `soc` — Security Operations Center 的偵測、調查與處置流程。
- `opnsense` — OPNsense 防火牆、路由、VPN 與相關網路服務。
- `networking` — IP、路由、子網與封包路徑等網路基礎。
- `network-segmentation` — VLAN、zone、跨區路由與信任邊界分割。
- `nat` — Network Address Translation，包括 SNAT、DNAT、PAT 與 NAT reflection。
- `firewall` — 防火牆規則、stateful filtering、規則順序與流量控制。
- `cryptography` — 密碼學（加解密、金鑰、協定）主題。
- `symmetric-cipher` — 對稱密碼（含位移/XOR 類）。
- `quantum-cryptography` — 量子密碼、QKD（BB84/E91）。
- `post-quantum` — 後量子密碼（PQC，如格密碼 Kyber/NIST FIPS 203）。

## 頁面大小限制

- 軟上限：400 行／約 2,000 字（英文字計）。超過建議考慮拆分。
- 硬上限：800 行。必須拆分。

## Frontmatter 必要欄位

每個頁面至少要有：
- `type`
- `title`
- `tags`
- `created`
- `updated`

加上依類型而定的欄位：
- `source` 頁面：`authors`、`url`（若適用）、`raw`、`ingested`
- 非 `source` 頁面：`sources` 列出引用的來源摘要頁
- `experiment` 頁面：`id`、`status`（planned/running/completed/inconclusive）、`hypothesis`、`result`（supported/refuted/partial/pending）、`confidence`（low/medium/high）、`code_paths`。模板見 `templates/experiment_note.md`。

## 選用的圖譜（Graph）中繼資料

頁面可以在 frontmatter 頂層宣告 `graph:` 型別化中繼資料。這是編譯後知識圖譜（位於 `wiki/graph/`）的權威來源。Markdown 仍是唯一正本；圖譜只是可重新產生的索引。沒有 `graph:` 的頁面仍會作為節點出現（依 `type`/`kind` 推導），並會從內文的 `[[wikilinks]]` 產生 `mentions` 邊。

```yaml
graph:
  node_id: person:praney-behl       # 選填；預設 <node_type>:<slug>
  node_type: person                  # 選填；預設依 ontology 由 type/kind 對映
  canonical: true                    # 多個 slug 指向同一實體時標記為正本
  aliases: [Praney, praney@example.com]
  relationships:
    - predicate: founded
      object: company:seedblocks
      source: praney-founder-context-dump   # 來源頁 slug
      evidence: "Solo technical founder and sole director..."
      confidence: high               # high | medium | low
      status: current                # current | historical | proposed | disputed | superseded
      # 選填：
      # valid_from: 2025-01-15
      # valid_to: 2026-03-01
      # notes: "..."
      # raw_ref: "raw/founder-dump.md#L42"
      # contradicts: edge-id-or-source-slug
      # supersedes: edge-id-or-source-slug
```

每個 relationship 必填欄位：`predicate`、`object`、`source`、`evidence`、`confidence`、`status`。Predicate 及其可接受的主詞／受詞型別定義於 `wiki/graph/ontology.yaml`。型別化的語意邊必須有明確來源支持 —— 絕不可憑訓練資料推論生成。

## 索引結構

（分片後請更新這一段。）

目前是扁平結構：單一 `wiki/index.md` 列出所有頁面。

當 wiki 超過約 150 頁，或 `index.md` 超過 300 行時，請分片為 `wiki/indexes/<type>.md`，並更新這一段。

## 圖譜層

Wiki 有一個選用的編譯後圖譜層，位於 `wiki/graph/`：

- `wiki/graph/ontology.yaml` — 宣告節點型別與 predicate。**受版本控制。** 引入新 predicate 或新領域型別時編輯此檔。
- `wiki/graph/nodes.jsonl`、`wiki/graph/edges.jsonl` — 自動產生。若想在 PR 中看到圖譜差異可納入版控。
- `wiki/graph/graph.sqlite` — 自動產生。預設不納入版控（gitignore）。
- `wiki/graph/graph.graphml` — 自動產生。若想做差異比對可納入版控。

由 markdown 透過 `scripts/wiki_graph_extract.py` 可重現產生。圖譜可隨時刪除並重建，不會遺失知識 —— markdown 才是正本。

## 工作流程客製化

### H-I-V-R-K-C 學習閉環（自 2026-07-09 導入，加法式）

除了預設的 ingest/query/lint，本 wiki 對「要主動學習／驗證」的主題採用一個閉環：**Hypothesis → Implementation → Verification → Reflection → Knowledge Ingestion → Code Preservation → Next Questions**。這是加在既有 Karpathy 結構「之上」的前端，不取代 `sources/entities/concepts/synthesis`——後者仍是知識回灌（K）的落點。

- **適用範圍**：用於「學習單元」（要精通的概念、要驗證的技術、要 build 的東西）。**單純的事實查詢／指令查詢走輕量模式**，不套完整七段，以免瑣事變論文。
- **產物落點**：假設與驗證過程 → `wiki/experiments/<slug>.md`（用 `templates/experiment_note.md`）；可複用程式碼 → `code/YYYY-MM-DD/<topic>/`（至少 README + manifest.json + 主檔 + 驗證腳本，模板 `templates/code_readme.md`）；結構化備份 → `db/*.jsonl`。
- **回灌既有頁**：實驗若驗證了某個 concept 頁的主張，就手術式更新該頁——連結實驗頁並調整信心敘述（例：[[git-branching-merge-rebase]] 的 reset 表已被 [[git-reset-modes]] 實測支持）。
- **里程碑記錄**：結構級變更寫 `changelog.md`；逐次 ingest／實驗仍寫 `wiki/log.md`。

### 附加資料夾（在 wiki root，即 `LLM_Wiki/`）

```
templates/   concept_note / experiment_note / reflection / code_readme 模板
db/          learning_log / experiments / concepts / code_index 的 .jsonl + 2 份 .schema.json
code/        YYYY-MM-DD/<topic>/  可複用、可重跑的程式碼資產
changelog.md 結構級里程碑
```

### Verification／Code Preservation 的環境邊界（重要）

因本機無 Python（見「工具限制備註」），H-I-V-R-K-C 中的 V 與 C 有明確邊界，且已納入紀律：
- 能用現成工具（**git、bash、PowerShell**）驗證的，就實測並在實驗頁「實際」欄填**真 actual**（例：[[git-reset-modes]] 用真 git 跑）。
- 不能在本機執行的（需 Python、需特定 runtime、需真實惡意樣本環境等），「實際」欄標 `⏳待執行`，**絕不編造執行結果**；程式碼仍完整保存並標 `verified_on_this_machine: false`。
- `db/*.jsonl` 目前是「可攜出的結構化備份」，在裝 Python 前無法被查詢腳本索引；人看的快取仍是 `index.md` / `log.md`。

## 使用者偏好

- **標題層級**：H1 只用於頁名；H2 用於 Lab／主要主題；H3 用於子主題或步驟群組。標題不加裝飾性 emoji，避免索引與不同 Markdown renderer 呈現不一致。
- **語意顏色**：不寫死 HTML 色碼，統一使用 Obsidian callout：`[!NOTE]` 表示概念或補充、`[!TIP]` 表示操作建議、`[!WARNING]` 表示安全或誤判風險。正文仍須寫出語意，不可只靠顏色傳達。
- **增量整理**：新筆記優先手術式補入既有 source／concept／entity 頁；只有現有頁面無合理落點且主題可持續累積時才新增頁面。

## Lint 頻率

- 結構性 lint：每 5 次 ingest 後執行一次。
- 語意性 lint：每週或每 20 次 ingest 後執行一次。
- 缺口盤點（gap-finding）：每月一次。
- 圖譜 lint + extract：每次 ingest 新增型別化 `graph.relationships` 後執行。

依 wiki 成長速度自行調整。

## 工具限制備註

此環境沒有可用的 Python 直譯器（只有 Windows Store 的 app-execution-alias 佔位程式）。內建腳本（`wiki_search.py`、`wiki_lint.py`、`wiki_stats.py`、`wiki_graph_*.py`）在安裝真正的 Python 前無法執行。結構性檢查（孤兒頁面、失效連結、超大頁面、frontmatter 驗證）在此之前需透過 Grep/Glob 手動進行。圖譜層因此尚未啟用 —— 除非之後安裝了 Python 且使用者要求，否則暫不建立 `wiki/graph/`。
