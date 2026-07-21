---
type: source
title: "Encryption and Decryption in Quantum Cryptography"
authors: ["A. Arulmurugan", "Manoj S K", "Panabaka Mahesh"]
url: "https://doi.org/10.1109/ICSSAS66150.2025.11081373"
raw: "raw/Encryption_and_Decryption_in_Quantum_Cryptography.pdf"
ingested: 2026-07-17
tags: [cryptography, quantum-cryptography, post-quantum]
entities: []
concepts: [post-quantum-cryptography]
---

# Encryption and Decryption in Quantum Cryptography

會議論文（2025 3rd International Conference on Self Sustainable AI Systems, ICSSAS；IEEE；SRM Institute, 印度）。**兩塊內容**：(a) 量子/後量子密碼的文獻綜述；(b) 一個「hybrid 加密框架」的實作。

## 兩塊分開看

### (a) 綜述（真正有價值、但數字要查證的部分）
涵蓋：Shor 演算法威脅 RSA/ECC、QKD（BB84、E91）、格密碼 Kyber-1024、hybrid 古典+後量子遷移。**底層概念正確且重要**——已抽成 [[post-quantum-cryptography]]。

### (b) 實作框架（名實有落差）
論文描述五層架構與「hybrid cryptographic framework」，但**實際做出來的是古典 XOR 加密 + Base64 + Streamlit UI**；BB84/Kyber 都列為「模擬/future work」。論文**自承**「achieves 70% of publication-ready potential」「current reliance on classical binary keys limits its quantum resistance」——即「量子」大多是回顧與未來工作，非實作。

## ⚠️ Claim vs Fact（本頁重要紀律）
論文含大量**具體但多數未附一手引用**的統計，一律記為「論文宣稱、未獨立佐證」，不可當既定事實：
- 「18% 光子損耗/50km 光纖」「$500k/km 量子中繼器」「210 MB/s（XOR）」「89% 組織無量子遷移路線圖」「63% TLS 1.3 仍用 RSA-2048」「E91 降低竊聽風險 40%」「Kyber-1024 比 AES-256 多 2.5× 運算開銷」等。
- 可自行核對的一項：2048-bit 金鑰空間 ≈ 2^2048 ≈ 3.2×10^616，論文寫「3.31×10^616」量級正確。

## 與其他頁面的關聯
- 概念抽取見 [[post-quantum-cryptography]]
- 其 XOR round-trip 的可逆性與 [[circular-shift-symmetric-cipher]] 同屬「可逆≠安全」的例子
- 對照論文一的古典位移密碼 [[crypto-circular-shift-cipher-paper]]

## 建議查證來源
IEEE Xplore 原文（DOI 10.1109/ICSSAS66150.2025.11081373）。文中統計數字建議回查 NIST PQC、ETSI QSC、各 QKD 實測論文等一手來源。
