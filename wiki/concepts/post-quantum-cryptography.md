---
type: concept
title: "後量子密碼學與量子金鑰分發（PQC / QKD）"
tags: [cryptography, quantum-cryptography, post-quantum]
sources: [quantum-crypto-hybrid-xor-paper]
created: 2026-07-17
updated: 2026-07-17
---

# 後量子密碼學與量子金鑰分發（PQC / QKD）

量子計算對現行公鑰密碼構成威脅，因而發展出兩條不同的因應路線：**後量子密碼（PQC）**——在傳統電腦上執行、但被認為連量子電腦也難破的演算法；**量子金鑰分發（QKD）**——用量子物理特性交換金鑰，安全性來自物理定律而非計算難度。本頁概念取自通識，並以 [[quantum-crypto-hybrid-xor-paper]] 為來源之一（該論文的具體統計數字未獨立佐證，見下）。

## 為什麼有威脅：Shor 與 Grover
- **Shor 演算法**（1994）：量子電腦可有效率地做**大數質因數分解與離散對數**，直接破解 **RSA（基於分解）與 ECC/DH（基於離散對數）**。這是「量子威脅」的核心。
- **Grover 演算法**：對暴力搜尋只有平方根加速，使對稱金鑰的有效強度約減半（AES-128 → 約 64-bit 安全），因此建議用 **AES-256**。對稱密碼受影響遠小於公鑰密碼。
- 實務隱憂「harvest-now-decrypt-later」：現在攔截加密流量、待未來量子電腦成熟再解密——故遷移有時間壓力。

## 路線一：後量子密碼（PQC）
在傳統硬體上跑、可直接替換現有公鑰演算法。主要家族：**格密碼（lattice）**、雜湊式、碼式（如 McEliece）。**NIST 於 2024 年公布標準**（建議以 NIST 官方為準）：
- **ML-KEM（源自 Kyber）= FIPS 203**：金鑰封裝。
- **ML-DSA（源自 Dilithium）= FIPS 204**、**SLH-DSA（源自 SPHINCS+）= FIPS 205**：數位簽章。

## 路線二：量子金鑰分發（QKD）
用量子態傳遞對稱金鑰，竊聽會擾動量子態而被偵測（no-cloning、量測擾動）。
- **BB84**（Bennett & Brassard, 1984，源於 Wiesner 1970s「conjugate coding」）：以光子偏振的兩組基底編碼位元。
- **E91**（Ekert, 1991）：以量子糾纏為基礎。
- 以 **QBER（量子位元錯誤率）** 判斷是否遭竊聽。QKD 需專用硬體與量子通道，且仍依賴一條「已認證的古典通道」。

## Hybrid 遷移
過渡期常把**古典 + 後量子並用**（如 TLS 中 ECDH + Kyber 併用），在保留相容性的同時取得抗量子性。這也是 [[quantum-crypto-hybrid-xor-paper]] 想談的方向（雖然它實作出來的只是古典 XOR）。

## ⚠️ 來源論文的數字：一律標「宣稱、待查證」
[[quantum-crypto-hybrid-xor-paper]] 引用多項具體統計（18% 光子損耗/50km、$500k/km 中繼器、89% 組織無遷移路線圖、63% TLS 仍用 RSA-2048、Kyber 比 AES-256 多 2.5× 開銷…），**多數未附一手引用**，本 wiki 不採信為既定事實，需回查 NIST/ETSI/QKD 實測。

## 常見誤解
| 誤解 | 正確理解 |
|---|---|
| QKD = 後量子密碼 | 兩條不同路線：QKD 靠物理+硬體換金鑰；PQC 是可直接部署的軟體演算法 |
| 量子電腦會破所有加密 | 主要威脅公鑰（RSA/ECC）；對稱（AES-256）與雜湊只需加大參數 |
| Kyber 是量子演算法 | 它是**格密碼**（傳統電腦上跑），只是被設計成抗量子 |

## 相關頁面
- 來源：[[quantum-crypto-hybrid-xor-paper]]
- 對照古典對稱密碼：[[circular-shift-symmetric-cipher]]、[[crypto-circular-shift-cipher-paper]]

## 建議查證來源
NIST PQC（FIPS 203/204/205）、ETSI Quantum-Safe Cryptography、BB84/E91 原始論文。
