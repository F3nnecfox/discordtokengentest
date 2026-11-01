from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag

ENC_HEX = "09bfa52faf8aebd3e714d840ad837b35470f423810195db8fcebf19e3a087a457d2675c359"
REQUEST_KEY = bytes.fromhex(
    "f46374858f577c290f67dfb8db04901d"
    "8089136eab8fd906890fb691e5855aa3")

enc = bytes.fromhex(ENC_HEX)
iv, ct, tag = enc[:12], enc[12:-16], enc[-16:]
print("len =", len(enc), "iv/ct/tag =", len(iv), len(ct), len(tag))

try:
    pt = AESGCM(REQUEST_KEY).decrypt(iv, ct + tag, b"")
    print("[+] decrypted:", pt)      # → b'iiyokoiyo'
except InvalidTag:
    print("[-] InvalidTag: request_key が違う / ビルド不一致")
