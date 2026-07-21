---
type: source
title: "A New Approach of Cryptography for Data Encryption and Decryption"
authors: ["Khawja Imran Masud", "Md Rakib Hasan", "MD. Mozammel Hoque", "Upel Dev Nath", "Md. Obaidur Rahman"]
url: "https://doi.org/10.1109/ICCI54321.2022.9756078"
raw: "raw/A_New_Approach_of_Cryptography_for_Data_Encryption_and_Decryption.pdf"
ingested: 2026-07-17
tags: [cryptography, symmetric-cipher]
entities: []
concepts: [circular-shift-symmetric-cipher]
---

# A New Approach of Cryptography for Data Encryption and Decryption

會議論文（2022 5th International Conference on Computing and Informatics, ICCI；IEEE；DUET Gazipur, 孟加拉）。提出一個以「金鑰驅動的循環位元移位」為核心的對稱加密新方法，並用 chi-square 檢定與 RSA/AES 比較。

## 核心主張
- **金鑰生成**：取隨機字元 → 每字元 ASCII 8-bit → 拆高 4 位（MSB）與低 4 位（LSB）→ 取各自十進位值 → `MSB_val % 2` 與 `LSB_val` 併成一個「兩位數」金鑰對。範例：ASCII 65,68,89,88 → `[01,04,19,18]`。
- **加密（Algorithm 2）**：明文切 10-byte 區塊（不足補 `_`）；金鑰分兩半，前半做循環左移、後半做循環右移；移位數 >8 時改為位元反轉。解密（Algorithm 3）為其反序、反方向的逆運算。
- **實驗宣稱**：以 chi-square 檢定衡量明文/密文的非同質性（non-homogeneity），宣稱其值高於 RSA/AES/[3]，據此主張較安全。**論文自承速度比 AES/RSA 慢**（時間複雜度較高，僅優於文獻[3]）。

## 本 wiki 的實測與批判（見 [[circular-shift-cipher-verification]]）
以 Python 重建後：
- ✅ 金鑰生成能重現 Table I；✅ encrypt/decrypt 確實 round-trip（可逆）。
- ⚠️ **缺陷 1**：Table I 表頭「A D X Y」標錯，依 ASCII 應為 A D **Y X**。
- ⚠️ **缺陷 2**：把金鑰對併成兩位數整數、再用 `//10,%10` 取回，在低 nibble ∈ A–F（約 37.5% 位元組值）時會失真且碰撞。
- ⚠️ **方法論保留**：「chi-square 高 = 較安全」不是標準安全論證；此密碼實為可逆位元置換，現代標準下很可能不具密碼強度。**round-trip 成功只證可逆、不證安全。**

## 與其他頁面的關聯
- 技術細節與批判見 [[circular-shift-symmetric-cipher]]
- 驗證閉環見 [[circular-shift-cipher-verification]]
- 對照現代密碼威脅面見 [[post-quantum-cryptography]]

## 建議查證來源
IEEE Xplore 原文（DOI 10.1109/ICCI54321.2022.9756078）。論文引用的 AES/RSA/chi-square 背景宜另查一手教材。
