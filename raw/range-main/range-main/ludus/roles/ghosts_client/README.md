# ghosts_client（自寫 Ansible role）

GHOSTS client（`ghosts.exe`，Windows、.NET 4.6.1）沒有現成 Ludus role，這裡自寫。
它是 baseline / 要件 3 的 Phase 0 缺口。

## 做法

照 frack113 的 Windows agent pattern 改（`ludus_caldera_agent` / `ludus_aurora_agent`），
不是從零寫。client 佈署要點：解壓 `ghosts.exe` 到 `c:\exercise\ghosts\`、改
`application.json` 指向 API server 即註冊；每個 NPC 靠 `timeline.json` 定義行為
（HandlerType：`Command` / `BrowserFirefox` / `Chrome` / Word / Excel…）。

## Phase 0 範圍：只做 headless Command handler

**關鍵複雜點**：GUI handler（瀏覽器/Office）需以一般使用者跑在**互動桌面 session** +
預裝 app/driver，不是 headless service。這在 Phase 0 是不必要的痛。

**減痛解**：Phase 0 先用 headless `Command` handler——產生網路/認證/程序類正常噪音，
已足以當 baseline。GUI 行為當增量後加。

## 待評估

- GHOSTS LITE 輕量變體是否更省事。

## 對映

- 每個 NPC 對應報告帳戶模型的一個使用者。
