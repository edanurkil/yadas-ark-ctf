# generate_signal3.py
import os

FLAG = "YADA{nav_c00rd1nat3s_d3crypt3d_st4r_612}"
SECRET_KEY = "ARK3487"  # 7 baytlık periyodik anahtar

def repeating_xor(data: str, key: str) -> bytes:
    data_bytes = data.encode('utf-8')
    key_bytes = key.encode('utf-8')
    return bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data_bytes)])

# 1. Şifreli koordinat dosyasını üret (.hex olarak)
cipher_bytes = repeating_xor(FLAG, SECRET_KEY)
with open("enc_coords.hex", "w") as f:
    f.write(cipher_bytes.hex())

# 2. Oyuncuya verilecek kısmen bozuk/ipuçlu Python kaynak kodu
leaked_code = '''# [YADA'S ARK - ONBOARD CRYPTO SUB-ROUTINE v3.4]
# SYSTEM RECOVERY SCRIPT
import sys

# UYARI: Bellek sektoru bozuldu. Anahtarin sadece format bilgisi kurtarilabiliyor.
# Bilinen kural: Anahtar 7 karakterden olusur ve 'ARK' ile baslar: "ARK????"

def decrypt(hex_data, key):
    raw_data = bytes.fromhex(hex_data)
    key_bytes = key.encode('utf-8')
    return "".join([chr(b ^ key_bytes[i % len(key_bytes)]) for i, b in enumerate(raw_data)])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanim: python3 encryptor_leaked.py <enc_coords.hex>")
        sys.exit(1)
        
    with open(sys.argv[1], "r") as f:
        data = f.read().strip()
        
    # TODO: Kalan 4 haneli acil durum kodunu (yil/sektor) bulun ve anahtari tamamlayin.
    # KEY = "ARK????"
    # print(decrypt(data, KEY))
'''

with open("encryptor_leaked.py", "w") as f:
    f.write(leaked_code)

print("[+] 3. İstasyon dosyalari hazirlandi: enc_coords.hex, encryptor_leaked.py")