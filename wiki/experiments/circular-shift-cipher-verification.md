---
id: exp-circular-shift-cipher-verification
type: experiment
topic: "驗證論文《A New Approach of Cryptography》所述循環移位密碼"
status: completed
hypothesis: "論文的金鑰生成與 encrypt/decrypt 演算法如述可運作：範例可重現、且 decrypt(encrypt(P))==P。"
result: partial
confidence: high
verified_on_this_machine: true
code_paths: [code/2026-07-17/circular-shift-cipher/cipher.py]
sources: [crypto-circular-shift-cipher-paper]
created: 2026-07-17
updated: 2026-07-17
related: [circular-shift-symmetric-cipher, crypto-circular-shift-cipher-paper]
---

# 實驗：驗證循環移位對稱密碼（Masud et al., 2022）

本 wiki **第一個用本機 Python（3.12.10，2026-07-16 安裝）實測的實驗**。

## 1. 假設 Hypothesis

### H1（主要）
論文 [[crypto-circular-shift-cipher-paper]] 所述的密碼，照演算法實作後應：(a) 金鑰生成重現 Table I（ASCII 65,68,89,88 → `[01,04,19,18]`）；(b) encrypt→decrypt 能還原原文。

理由：Algorithm 2（加密）與 Algorithm 3（解密）在結構上互為逆（左移↔右移、反序、反轉自逆），故理應 round-trip。
信心（驗證前）：Medium——結構看似對，但論文有若干未言明的細節（「from first_digit position」的位置語意、金鑰整數表示）。

### H2（替代）
論文的金鑰表示（把 `MSB%2` 與 `LSB` 併成兩位數整數，再用 `//10`、`%10` 取回 first/last）在某些字元會失真，導致「照字面實作」與「照意圖實作」不一致。

## 2. 實作 Implementation
純標準函式庫重建：金鑰生成、位元循環移位/反轉、Algorithm 2/3。程式碼 `code/2026-07-17/circular-shift-cipher/`（`cipher.py` + `README.md` + `manifest.json`）。三個驗證點 V1（金鑰生成）、V2（round-trip）、V3（整數金鑰表示的邊界）。

## 3. 驗證 Verification

於本機實測（Python 3.12.10, 2026-07-17）：

| 編號 | 要驗證 | 方法 | 預期 | 實際 | 判定 |
|---|---|---|---|---|---|
| V1 | 金鑰生成重現 Table I | 對 ASCII 65,68,89,88 跑 key-gen | `[01,04,19,18]` | `[01,04,19,18]` | ✅ |
| V2 | Algorithm 2/3 round-trip | encrypt 後 decrypt，比對原文 | 完全還原 | `The World Is a Book` + 5 隨機字串全還原 | ✅ |
| V3 | 整數金鑰表示在 LSB≥10 是否失真 | 對 `O`(0x4F, 低 nibble=15) 檢查 `//10,%10` 取回 | 應得 (0,15) | 取回 (1,5)，**不符** | ⚠️ 缺陷確認 |

附帶發現：Table I **表頭「A D X Y」標錯**——ASCII 值 65,68,89,88 對應 A,D,**Y,X**（論文內文的 array 順序 `[A,D,Y,X]` 才是對的）。

## 4. 反思 Reflection
- 原本以為：論文若結構對就能完整運作。
- 結果顯示：**核心密碼確實可逆**（V2 全過）——它本質是「以金鑰驅動的可逆位元置換」。但**論文的呈現有兩個會絆倒實作者的缺陷**：(1) Table I 表頭字元標反；(2) 把金鑰併成兩位數整數的表示法，在低 nibble ∈ A–F（約 37.5% 的位元組值）時 `//10,%10` 取回錯誤、且不同 (first,last) 會碰撞成同一整數（資訊遺失）。正確實作必須保留 pair、不可 merge。
- 更重要的心智模型更新：**「round-trip 成功」只證明可逆，不證明安全**。論文用 chi-square 值高來論證安全性，但那不是標準安全指標；這個密碼實質是保序的位元重排，現代標準下很可能不具密碼強度。驗證「能不能還原」與驗證「安不安全」是兩回事。
- 下次遇到類似「論文提出新密碼」：先實作驗可逆性（便宜、能抓 spec bug），但對安全性宣稱另立更高門檻，別把「可運作」誤當「安全」。

## 5. 後續問題 Next Questions
1. 這個密碼對已知明文攻擊（known-plaintext）有多脆弱？金鑰空間（每字元 2×10 種、實為 (first∈{0,1}, last∈0..15)）到底多大？
2. 若把「chi-square 高」當賣點，chi-square 到底衡量了什麼、為何不足以當安全性證明？（連 [[circular-shift-symmetric-cipher]]）
3. 論文的 padding `_` 會洩漏原文長度資訊嗎？
