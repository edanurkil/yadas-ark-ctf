# generate_signal1_perfect_full.py
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import scipy.signal
from scipy.io import wavfile

FLAG_TEXT = "YADA{s1gn4l_r3c0v3r3d_b34c0n_3487}"
OUTPUT_WAV = "distress_beacon.wav"

# 1. FFT ve Frekans parametreleri
n_fft = 2048
hop_length = 512
sample_rate = 44100
num_freq_bins = n_fft // 2 + 1  # 1025 basamak (0 - 22050 Hz)

# 2. Font belirleme
font_size = 46
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except:
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", font_size)
    except:
        font = ImageFont.load_default()

# 3. Metin boyutuna göre dinamik tuval genişliği hesaplama
dummy_img = Image.new('L', (1, 1))
dummy_draw = ImageDraw.Draw(dummy_img)
try:
    text_width = int(dummy_draw.textlength(FLAG_TEXT, font=font))
except AttributeError:
    # Eski PIL sürümleri için fallback
    text_width, _ = dummy_draw.textsize(FLAG_TEXT, font=font)

# Başlangıç ve bitiş için pay bırakarak tam genişliği ayarla
padding = 100
time_bins = text_width + (padding * 2)

# 4. Spektrogram matrisini çiz
img = Image.new('L', (time_bins, num_freq_bins), color=0)
draw = ImageDraw.Draw(img)

# Metni frekans cetvelinde rahat görünecek orta bantta (~4000-8000 Hz) çiz
# PIL'de y=0 üsttür, bu nedenle y koordinatı ~280 ideal görünürlük sağlar
draw.text((padding, 280), FLAG_TEXT, fill=255, font=font)

# Matrisi al ve dikey yönünü doğrula (Alçak frekans alta gelsin)
spec_magnitude = np.array(img, dtype=np.float32)
spec_magnitude = np.flipud(spec_magnitude)

# Kontrastı güçlendir
spec_magnitude = (spec_magnitude / 255.0) ** 1.5 * 100.0

# 5. ISTFT ile pürüzsüz sese çevir
np.random.seed(42)
random_phase = np.exp(1j * np.random.uniform(0, 2 * np.pi, spec_magnitude.shape))
stft_matrix = spec_magnitude * random_phase

_, signal = scipy.signal.istft(stft_matrix, fs=sample_rate, nperseg=n_fft, noverlap=n_fft - hop_length)

# Ses normalizasyonu ve WAV kaydı
signal = signal / (np.max(np.abs(signal)) + 1e-8)
wavfile.write(OUTPUT_WAV, sample_rate, (signal * 32767).astype(np.int16))

print(f"[+] Tam boyutlu bayrak WAV dosyasina aktarildi: {OUTPUT_WAV}")
print(f"[+] Toplam sure: {len(signal)/sample_rate:.2f} saniye")