# [YADA'S ARK - ONBOARD CRYPTO SUB-ROUTINE v3.4]
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
