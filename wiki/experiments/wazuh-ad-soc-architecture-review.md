---
id: exp-wazuh-ad-soc-architecture-review
type: experiment
topic: "Wazuh × AD × OPNsense × AI SOC 架構基線審查"
status: completed
hypothesis: "將資料平面、網路邊界與 AI 整合平面分開定義後，可把架構圖轉為可安全部署、可觀測且可驗證的實驗室基線。"
result: partial
confidence: medium
verified_on_this_machine: false
code_paths: []
sources: [wazuh-ad-soc-architecture-diagram, wazuh-ad-soc-architecture-research]
created: 2026-07-14
updated: 2026-07-14
related: [soc-lab-segmentation-and-telemetry, wazuh-ad-soc-architecture-diagram, wazuh-ad-soc-architecture-research]
---

# 實驗：Wazuh × AD × OPNsense × AI SOC 架構基線審查

## 1. 假設 Hypothesis

### H1（主要）

若將圖中的 Wazuh Agent 遙測、OPNsense 跨區規則、AI MCP 存取與 RDP/WinRM 管理流量拆成獨立信任邊界，便能避免「監控與管理、AI、攻擊測試共用同一個寬鬆網段」的設計缺口。

理由：Wazuh 官方架構把 Agent 資料收集與 Server 分析分開；AD DS 集中身分與權限；圖片中的 OPNsense 正好可成為跨區控制點。

信心程度：Medium。架構原則有官方文件支持，但目前尚未取得實際 VM 網路設定與服務狀態。

### H2（替代）

圖片中的 MCP 與 RDP 箭頭可能只是展示資料／測試關係，不代表任何已部署的通訊服務。

如何區分 H1/H2：檢查 OPNsense 規則、Wazuh Agent 狀態、服務 listener、AI MCP 認證設定與端點日誌。

## 2. 實作 Implementation

### 實驗目標

把使用者的架構圖編譯為可執行的驗收基線，而非直接假定圖中服務已可用。

### 最小實驗設計

- 輸入：使用者架構圖與 Wazuh、Microsoft、OPNsense 官方文件。
- 操作：轉錄主機角色與資源；劃分資料、網路與 AI 整合邊界；提出連線 allow-list 與驗收證據。
- 預期輸出：一份有來源的架構基線、待驗證清單與下一階段部署順序。
- 成功條件：所有圖中元件都有角色、信任邊界、可觀測證據與明確的不確定性標記。
- 失敗條件：把圖片線條誤寫成已開放服務，或把官方預設值當作本機事實。

### Code Preservation

本輪是設計與研究審查，未建立或執行設定檔、腳本或攻防程式碼，因此 `code_paths` 為空。原始設計與研究證據已保存在 `raw/`；後續實作 OPNsense 規則、Wazuh 設定或 MCP connector 時，必須將可執行檔與 manifest 保存到 `code/YYYY-MM-DD/<topic>/`。

## 3. 驗證 Verification

| 編號 | 要驗證的事 | 方法 | 預期 | 實際 | 判定 |
|---|---|---|---|---|---|
| V1 | 圖中元件與角色已被完整轉錄 | 人工比對圖片與原始轉錄 | 7 個主機角色、資源與箭頭語意均記錄 | 已完成 | 通過 |
| V2 | 既有 KB 可承接新設計 | 比對專題的 topology、inventory、RAG 文件 | 找出五主機佔位與新七角色基線的差異 | 已完成，已建立基線頁並更新相關頁 | 通過 |
| V3 | Wazuh Agent 遙測通道可達 | 實機確認 Agent active、TCP 1514 與測試事件 | DC/兩台 Windows 11 均有可追溯遙測 | 待執行 | 待驗證 |
| V4 | OPNsense 僅允許必要跨區流量 | 審查規則與 firewall log | RDP/WinRM/管理/AI 皆有最小 allow-list | 待執行 | 待驗證 |
| V5 | MCP 對 AI 是只讀且可稽核 | 檢查 connector、身分、授權與 audit log | 無管理權限、查詢可追溯 | 待執行 | 待驗證 |

> 環境備註：本機沒有 Python，也沒有本專題 VM/OPNsense/AI Server 的執行存取。V1、V2 是已完成的文件層驗證；V3–V5 絕不填造實際結果。

## 4. 反思 Reflection

- 原本圖已清楚呈現元件，但不足以判定服務暴露與資料權限。
- 研究結果支持「Wazuh all-in-one + 端點 Agent + OPNsense 分段」作為小型實驗室的合理起點。
- MCP 應被視為獨立的應用信任邊界，而不是 Wazuh 到 AI 的一般箭頭。
- 心智模型更新為：拓撲圖回答「誰存在、誰相連」；驗收矩陣才回答「誰可以做什麼、如何證明」。

## 5. Knowledge Ingestion

- 原始圖：[[wazuh-ad-soc-architecture-diagram]]
- 官方文件研究：[[wazuh-ad-soc-architecture-research]]
- 可複用概念：[[soc-lab-segmentation-and-telemetry]]
- 子專案基線：`projects/wazuh-ad-soc/01-architecture/architecture-baseline-and-validation.md`

## 6. 後續問題 Next Questions

1. 七個角色的實際 IP/CIDR/VLAN、主機名與 OPNsense 介面分配是什麼？
2. 哪些 Windows 主機與 DC 已註冊 Wazuh Agent，並各自採集哪些 Event Channel？
3. MCP 的 transport、認證機制、工具白名單、資料遮罩與 audit log 位置為何？
4. RDP 與 WinRM 是否只對授權測試帳號與來源暫時開放，且有關閉／還原程序？
