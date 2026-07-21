#!/usr/bin/env python3
"""
cipher.py — 論文《A New Approach of Cryptography for Data Encryption and
Decryption》(Masud et al., IEEE ICCI 2022) 所述密碼的可驗證重建。

對應實驗頁：wiki/experiments/circular-shift-cipher-verification.md
對應來源頁：wiki/sources/crypto-circular-shift-cipher-paper.md

目的：驗證三件事——
  V1 金鑰生成能否重現論文 Table I（ASCII 65,68,89,88 -> 01,04,19,18）
  V2 論文 Algorithm 2/3（加密/解密）是否真的 round-trip（decrypt(encrypt(P))==P）
  V3 論文「把 MSB%2 與 LSB 併成兩位數整數」的金鑰表示，在 LSB nibble>=10 的字元是否會壞掉

依賴：純標準函式庫（Python 3.12 實測）。
"""

# ---------- 金鑰生成（論文 Algorithm 1）----------
def char_key_pair(ch):
    """回傳 (first, last)：first = 高 nibble % 2，last = 低 nibble。"""
    a = ord(ch)
    hi = (a >> 4) & 0xF   # MSB nibble
    lo = a & 0xF          # LSB nibble
    return (hi % 2, lo)

def key_as_paper_int(ch):
    """論文寫法：Merge(MSB_val, LSB_val) 成兩位數整數，再用 //10, %10 取回。"""
    first, last = char_key_pair(ch)
    return first * 10 + last   # 論文的 "01","04","19","18" 即此

def generate_keys_pairs(key_string):
    return [char_key_pair(c) for c in key_string]

# ---------- 位元工具 ----------
def bytes_to_bits(bs):
    return [(b >> i) & 1 for b in bs for i in range(7, -1, -1)]

def bits_to_bytes(bits):
    out = bytearray()
    for i in range(0, len(bits), 8):
        v = 0
        for b in bits[i:i+8]:
            v = (v << 1) | b
        out.append(v)
    return bytes(out)

def rotate(bits, start, n, direction):
    """對 bits[start:] 這段做循環位移 n 位（其餘不動）。"""
    head, seg = bits[:start], bits[start:]
    L = len(seg)
    if L == 0:
        return bits
    n %= L
    if n == 0:
        return bits
    if direction == 'L':
        seg = seg[n:] + seg[:n]
    else:  # 'R'
        seg = seg[-n:] + seg[:-n]
    return head + seg

def invert_from(bits, start):
    return bits[:start] + [1 - b for b in bits[start:]]

def apply_op(bits, key_pair, direction):
    """套一把金鑰到一個 block 的 bit 串。key_pair=(first,last)。"""
    first, last = key_pair
    start = first * 8            # first 為 byte 位置（0 或 1）
    if last > 8:                 # 論文：位移數 >8 改為反轉
        return invert_from(bits, start)
    return rotate(bits, start, last, direction)

# ---------- 加密（Algorithm 2）/ 解密（Algorithm 3）----------
def split_keys(keys):
    m = round(len(keys) / 2)
    return keys[:m], keys[m:]

def encrypt_block(bits, keys):
    K1, K2 = split_keys(keys)
    for k in K1:                 # 前半：循環左移
        bits = apply_op(bits, k, 'L')
    for k in K2:                 # 後半：循環右移
        bits = apply_op(bits, k, 'R')
    return bits

def decrypt_block(bits, keys):
    K1, K2 = split_keys(keys)
    for k in reversed(K2):       # 反序、反方向（右->左）
        bits = apply_op(bits, k, 'L')
    for k in reversed(K1):       # 反序、反方向（左->右）
        bits = apply_op(bits, k, 'R')
    return bits

def blocks_of(data, size=10, pad=b'_'):
    data = bytearray(data)
    if len(data) % size:
        data += pad * (size - (len(data) % size))
    return [bytes(data[i:i+size]) for i in range(0, len(data), size)]

def encrypt(plaintext_bytes, keys):
    out = bytearray()
    for blk in blocks_of(plaintext_bytes):
        out += bits_to_bytes(encrypt_block(bytes_to_bits(blk), keys))
    return bytes(out)

def decrypt(cipher_bytes, keys):
    out = bytearray()
    for i in range(0, len(cipher_bytes), 10):
        blk = cipher_bytes[i:i+10]
        out += bits_to_bytes(decrypt_block(bytes_to_bits(blk), keys))
    return bytes(out)

# ---------- 驗證主程式 ----------
if __name__ == "__main__":
    import random, string

    print("== V1: 重現論文 Table I 金鑰生成 ==")
    # 論文 array 順序為 [A,D,Y,X]（ASCII 65,68,89,88）；表頭誤標為 A D X Y
    demo = [(65, 'A'), (68, 'D'), (89, 'Y'), (88, 'X')]
    got = []
    for a, name in demo:
        first, last = char_key_pair(chr(a))
        got.append(f"{first}{last}")
        print(f"  {name}(ASCII {a}): MSB%2={first}, LSB={last} -> '{first}{last}'")
    expected = ["01", "04", "19", "18"]
    print(f"  期望={expected}  實得={got}  相符={got == expected}")

    print("\n== V3: LSB nibble>=10 的字元會讓論文的整數金鑰表示壞掉 ==")
    # 例如 'O' = 79 = 0x4F -> 低 nibble = 0xF = 15
    ch = 'O'
    first, last = char_key_pair(ch)
    paper_int = key_as_paper_int(ch)
    print(f"  '{ch}'(ASCII {ord(ch)}): 正確 pair=(first={first}, last={last})")
    print(f"  論文整數表示 = {paper_int}；用 //10,%10 取回 -> first={paper_int//10}, last={paper_int%10}")
    print(f"  => 取回的 first/last 與正確值相符嗎？ {(paper_int//10, paper_int%10) == (first, last)}")

    print("\n== V2: round-trip（Algorithm 2 加密後用 Algorithm 3 解密是否還原）==")
    keys = generate_keys_pairs("ADYX")   # 論文範例金鑰
    cases = ["The World Is a Book"]
    # 加上隨機字串壓力測試（只用 low-nibble<=8 的可列印字元，避免論文整數表示的已知缺陷干擾）
    safe = [c for c in string.printable if (ord(c) & 0xF) <= 8 and c.isprintable() and c != ' ' or c == ' ']
    for _ in range(5):
        cases.append(''.join(random.choice(string.ascii_letters + string.digits + " ") for _ in range(random.randint(1, 40))))
    allok = True
    for pt in cases:
        pb = pt.encode('latin-1')
        ct = encrypt(pb, keys)
        rt = decrypt(ct, keys).rstrip(b'_')   # 去掉尾端 padding
        ok = rt == pb
        allok &= ok
        shown = pt if len(pt) <= 24 else pt[:24] + "…"
        print(f"  round-trip {'OK ' if ok else 'FAIL'} | 明文='{shown}' (len={len(pt)})")
    print(f"  全部 round-trip 通過：{allok}")

    print("\n== 環境 ==")
    import sys
    print(f"  Python {sys.version.split()[0]}")
