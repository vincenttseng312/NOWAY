---
type: concept
title: "循環移位對稱密碼（Circular-Shift Symmetric Cipher）"
tags: [cryptography, symmetric-cipher]
sources: [crypto-circular-shift-cipher-paper]
created: 2026-07-17
updated: 2026-07-17
---

# 循環移位對稱密碼（Circular-Shift Symmetric Cipher）

一類以「金鑰驅動的可逆位元移位/反轉」構成的對稱密碼。以 [[crypto-circular-shift-cipher-paper]]（Masud et al., 2022）為代表：加解密雙方共享同一把金鑰，加密時把明文切塊、對位元做循環左右移與反轉，解密時反序、反方向還原。本頁的定位是「一個被提出的方法 + 對它的實測與批判」，而非推薦用法。

## 心智模型
把它想成**一個由金鑰決定的可逆位元置換**：明文的位元被搬動位置（rotate）或翻轉（invert），沒有增刪、沒有壓縮，因此只要金鑰相同就能完全還原。它與 XOR 串流密碼（見 [[quantum-crypto-hybrid-xor-paper]] 的 hybrid 框架）同屬「結構上保證可逆」的一類——**可逆是這類設計最容易達成、也最容易被誤當成安全的性質**。

## 演算法要點（論文版）
- **金鑰**：每個隨機字元 → ASCII 8 bit → 高 4 位（MSB）與低 4 位（LSB）→ 金鑰對 `(MSB%2, LSB)`。
- **加密**：明文切 10-byte 區塊（補 `_`）；金鑰前半循環左移、後半循環右移；移位數 >8 改為位元反轉。
- **解密**：反序、反方向套用（左↔右、反轉自逆）。

## 實測結論（見 [[circular-shift-cipher-verification]]，本機 Python 實跑）
| 主張 | 結果 |
|---|---|
| 金鑰生成重現論文 Table I | ✅ 重現（`[01,04,19,18]`） |
| encrypt/decrypt round-trip | ✅ 可逆，多字串全還原 |
| 論文 Table I 表頭字元 | ⚠️ 標錯（應 A D **Y X**） |
| 金鑰併成兩位數整數的表示 | ⚠️ 低 nibble≥10 會失真、碰撞 |

## 常見誤解
| 誤解 | 為什麼錯 | 正確理解 |
|---|---|---|
| round-trip 成功代表安全 | 可逆只證明「能還原」 | 安全需另證抗攻擊；位元置換保留統計結構，易受已知明文/頻率分析 |
| chi-square 值高 = 較安全 | chi-square 衡量明文/密文差異度，非攻擊難度 | 它不是標準安全指標；高 chi-square 不排除可破解 |
| 金鑰對可安全併成整數 | `//10,%10` 在 LSB≥10 失真 | 應保留 `(first,last)` pair，不可 merge |

## 相關頁面
- 來源與批判：[[crypto-circular-shift-cipher-paper]]
- 驗證閉環與程式碼：[[circular-shift-cipher-verification]]
- 「可逆≠安全」的另一例與現代威脅面：[[post-quantum-cryptography]]
