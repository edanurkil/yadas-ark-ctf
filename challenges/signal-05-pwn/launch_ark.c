// launch_ark.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void launch_ark() {
    puts("\n[+] ========================================================");
    puts("[+] ACIL DURUM HIPER-SURUCUSU DEVREYE ALINDI!");
    puts("[+] ROTASYON: PROXIMA CENTAURI B // KOVAN GUVENDE.");
    puts("[+] KAZANILAN FINAL BAYRAGI:");
    puts("[+] YADA{ark_hyp3rdr1v3_1gn1t3d_hum4n1ty_s4v3d_3487}");
    puts("[+] ========================================================");
    exit(0);
}

void engine_terminal() {
    char auth_buffer[64];

    puts("==================================================");
    puts("   YADA'S ARK - HYPERDRIVE IGNITION TERMINAL      ");
    puts("   STATUS: CRITICAL // MANUAL OVERRIDE REQUIRED   ");
    puts("==================================================");
    printf("[?] ATESLEME KONTROL PROTOKOLUNU GIRIN: ");
    fflush(stdout);

    // Zafiyet Noktası: gets() guvensizdir ve bounds check yapmaz
    gets(auth_buffer);

    puts("[-] GIRILEN PROTOKOL GECERSIZ. ATESLEME IPTAL EDILDI.");
}

int main(int argc, char **argv) {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    engine_terminal();
    return 0;
}