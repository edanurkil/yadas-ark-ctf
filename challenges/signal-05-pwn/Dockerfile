FROM ubuntu:22.04

# Gerekli araçlar
RUN apt-get update && apt-get install -y socat libc6 && rm -rf /var/lib/apt/lists/*

# Düşük yetkili kullanıcı oluştur
RUN useradd -m -s /bin/bash pwnuser

WORKDIR /home/pwnuser

# Derlenmiş binary'yi kopyala
COPY launch_ark /home/pwnuser/launch_ark
RUN chown -R root:pwnuser /home/pwnuser && \
    chmod 750 /home/pwnuser/launch_ark

USER pwnuser
EXPOSE 9005

# Gelen her bağlantı için launch_ark binary'sini ayağa kaldır
CMD ["socat", "-T30", "TCP-LISTEN:9005,reuseaddr,fork", "EXEC:/home/pwnuser/launch_ark,stderr"]