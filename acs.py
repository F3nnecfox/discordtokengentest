#!/usr/bin/env python3
"""
hCaptcha hsw リクエストボディ復号スクリプト
入力: getcaptcha への POST ボディ（生バイト列）
出力: 復号された plain テキスト（JSON）
"""

import msgpack
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# ---- 抽出済みキー（build-static） ----
# 実際の運用では、対象ビルドから抽出した hsw.decrypt_key を入れる
DECRYPT_KEY = bytes.fromhex(
    "7857bc0eb3329edcae71db2d774d75d9"
    "ab616850d871a70e054eed59dfcc88b2"   # hsw.encrypt_key
)

AAD = b""              # wire_format 定義より aad は空
EXTTYPE_HSW = 18       # ExtType のコード（実測: 0x12）
IV_LEN = 12
TAG_LEN = 16


def decrypt_hsw_body(body: bytes) -> bytes:
    # 1. MessagePack としてパース
    obj = msgpack.unpackb(body, raw=False, strict_map_key=False)
    assert isinstance(obj, list) and len(obj) == 2, f"想定外の構造: {type(obj)}"
    meta, ext = obj

    # 2. ExtType(18) を抽出
    if not isinstance(ext, msgpack.ExtType):
        raise TypeError(f"ExtType ではない: {type(ext)}")
    if ext.code != EXTTYPE_HSW:
        raise ValueError(f"ExtType code 不一致: {ext.code} != {EXTTYPE_HSW}")

    blob = ext.data  # ここが iv||ct||tag
    if len(blob) < IV_LEN + TAG_LEN:
        raise ValueError(f"blob が短すぎる: {len(blob)}")

    # 3. iv||ct||tag に分解
    iv  = blob[:IV_LEN]
    tag = blob[-TAG_LEN:]
    ct  = blob[IV_LEN:-TAG_LEN]

    # 4. AES-256-GCM で復号（cryptography は ct||tag を連結して渡す仕様）
    aesgcm = AESGCM(DECRYPT_KEY)
    plain = aesgcm.decrypt(iv, ct + tag, AAD)
    return plain


def main():
    import sys
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <body.bin>", file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1], "rb") as f:
        body = f.read()

    # 末尾に改行などが混じっている場合は剥がす（バイナリなので注意）
    plain = decrypt_hsw_body(body)
    print(plain.decode("utf-8", errors="replace"))


if __name__ == "__main__":
    main()
