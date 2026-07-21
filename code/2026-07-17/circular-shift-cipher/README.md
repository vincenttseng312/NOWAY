# 循環移位對稱密碼——可驗證重建

## 目的
重建並驗證論文《A New Approach of Cryptography for Data Encryption and Decryption》(Masud et al., IEEE ICCI 2022) 所述的密碼，回答「這個演算法到底能不能運作、論文範例對不對」。

## 驗證的假設
對應實驗頁：[[circular-shift-cipher-verification]]。假設：金鑰生成可重現 Table I，且 encrypt→decrypt 能還原原文。

## 檔案結構
```
code/2026-07-17/circular-shift-cipher/
├── README.md
├── manifest.json
└── cipher.py        # 實作 + 內建 V1/V2/V3 驗證
```

## 執行方式
```bash
python code/2026-07-17/circular-shift-cipher/cipher.py
```

## 測試方式
同上；`__main__` 直接印出三個驗證點結果。看 `相符=True` / `全部 round-trip 通過：True` / V3 的 `False`（= 確認缺陷）。

## 預期輸出
- V1：`A(65)->01, D(68)->04, Y(89)->19, X(88)->18`，相符=True。
- V2：`The World Is a Book` + 5 隨機字串 round-trip 全 OK，全部通過=True。
- V3：`O`(0x4F) 的整數金鑰 `//10,%10` 取回 (1,5) ≠ 正確 (0,15) → False（確認缺陷）。

## 實驗結果
2026-07-17 於本機（Python 3.12.10）實際執行：V1 通過、V2 通過、V3 確認缺陷。整體 result=partial（核心可逆、範例可重現；但論文金鑰整數表示對低 nibble≥10 失真、Table I 表頭字元標反）。

> 註：`cipher.py` 的中文 print 在 Windows cp950 console 會顯示亂碼，但所有判定結果（True/False/OK/FAIL、ASCII 數字）皆為 ASCII、可正確判讀。

## 反思
只依賴 git-bash + Python 標準函式庫，無第三方套件，三個月後可重跑。這是本 wiki 少數「我能自己驗證」的資產（呼應 CLAUDE.md §8）。

## 後續可擴充方向
- 加金鑰空間/暴力破解估算。
- 嘗試逐位元重現論文 Fig.4/Fig.5 的中間 rotation 值（需解開「from first_digit position」的確切語意）。
