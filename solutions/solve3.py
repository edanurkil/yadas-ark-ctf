# solve.py
def decrypt(hex_data, key):
    raw_data = bytes.fromhex(hex_data)
    key_bytes = key.encode('utf-8')
    return "".join([chr(b ^ key_bytes[i % len(key_bytes)]) for i, b in enumerate(raw_data)])

with open("enc_coords.hex", "r") as f:
    cipher_hex = f.read().strip()

# Yöntem: Doğrudan bilinen anahtarla açma
flag = decrypt(cipher_hex, "ARK3487")
print(f"[+] Cozulen Bayrak: {flag}")

