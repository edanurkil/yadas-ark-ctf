# generate_signal2.py
from PIL import Image, ImageDraw

OUTPUT_PNG = "hive_telemetry.png"
FLAG = b"YADA{last_bee_vital_signs_stable_0x8f}"

# 1. 3487 stili bir telemetri arayüz görseli çiz
img = Image.new('RGB', (600, 300), color=(10, 16, 13))
draw = ImageDraw.Draw(img)

# Çerçeve ve sahte HUD telemetri çizgileri
draw.rectangle([10, 10, 590, 290], outline=(0, 255, 102), width=2)
draw.text((25, 25), "[ BIO-CHAMBER TELEMETRY // POD #001 ]", fill=(0, 255, 102))
draw.text((25, 60), "SPECIMEN: APIS MELLIFERA (LAST COLONY)", fill=(0, 255, 102))
draw.text((25, 90), "OXYGEN SATURATION: 41.2%", fill=(255, 170, 0))
draw.text((25, 120), "CORE TEMPERATURE: 12.8 C [CRITICAL]", fill=(255, 80, 80))
draw.text((25, 160), "STATUS: ARCHIVE CORRUPTED - DATA APPENDED AT EOF", fill=(0, 255, 102))

# Görseli diske kaydet
img.save(OUTPUT_PNG)

# 2. Steganografi: PNG dosyasının sonuna gizli log ve FLAG enjekte et
secret_payload = (
    b"\n\n--- [ORBITAL POD EMERGENCY LOG EXCERPT] ---\n"
    b"Timestamp: 3487-11-04 03:14:07 UTC\n"
    b"Decryption Key Matched: Hive payload locked into cryo-carrier.\n"
    b"RECOVERY_FLAG=" + FLAG + b"\n"
    b"--- [END OF LOG] ---\n"
)

with open(OUTPUT_PNG, "ab") as f:
    f.write(secret_payload)

print(f"[+] 2. Soru dosyasi hazir: {OUTPUT_PNG}")