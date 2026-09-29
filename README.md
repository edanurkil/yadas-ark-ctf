# yadas-ark-ctf

# 🛸 PROJECT: YADA'S ARK // EMERGENCY RECOVERY PROTOCOL (3487)

> **[ CLASSIFIED TRANSMISSION // SECTOR-9 ]**  
> Yıl 3487. Yerküre üzerindeki biyosfer filtreleri çöktü ve türlerin ezici çoğunluğu yok oldu. Hayatta kalmayı başaran son bal arısı kolonisi derin dondurucu bir biyokapsülde kurtarılmayı bekliyor. Kalan yaşamsal potansiyeli yeni bir yıldıza taşıyacak tek araç olan **Yada's Ark**, manyetik fırtınalar sonrası derin uyku moduna geçti.  
> 
> Göreviniz: Uzaya yayılan 5 aşamalı zayıf acil durum sinyalini sırasıyla çözmek, kovanı kurtarmak ve hiper-sürücüyü ateşlemektir.

---

## 🗺️ Görev & İstasyon Haritası (Linear Progression)

Sistem çizgisel (linear quest) mantığıyla kurgulanmıştır. Her istasyonun bayrağı (`FLAG`), bir sonraki sistemin kapısını açar:

| İstasyon | Kategori | Hedef | Puan |
|---|---|---|---|
| **Sinyal 01: Bozuk Frekans** | `Forensics` | Telsiz spektrumundan ilk acil durum sinyalini yakala. | 100 |
| **Sinyal 02: Kovan Telemetrisi** | `Steganography` | Yaşam destek kapsülünün hasarlı telemetri baytlarını analiz et. | 150 |
| **Sinyal 03: Arşiv Şifrelemesi** | `Cryptography` | Seyir bilgisayarının periyodik anahtar algoritmasını çöz. | 200 |
| **Sinyal 04: Güverte Kilidi** | `Reverse Engineering` | Kriyojenik hava kilidi binary kontrol mekanizmasını baypas et. | 250 |
| **Sinyal 05: Fırlatma Yetkilendirmesi** | `Pwn / Buffer Overflow` | Motor konsolundaki bellek taşmasını sömürerek `launch_ark()` rutinini tetikle. | 300 |

* **Standart Bayrak Formatı:** `YADA{...}`

---

## 🚀 Yerel Kurulum (CTFd ile Yayına Alma)

Bu platform Docker ve Docker Compose ile saniyeler içinde çalıştırılabilir:

### Gereksinimler
* Docker & Docker Compose

### Başlatma
```bash
# Depoyu klonlayın
git clone [https://github.com/](https://github.com/)<KULLANICI_ADINIZ>/<REPO_ADINIZ>.git
cd <REPO_ADINIZ>

# Servisleri ayağa kaldırın
docker compose up -d
