// airlock_auth.c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *gets(char *s);

// Obfuscated flag: "YADA{41rl0ck_d00r_unl0ck3d_99a}"
// Her bayt 0x5A ile XOR'lanmistir
unsigned char enc_flag[] = {
    0x03, 0x1b, 0x1e, 0x1b, 0x21, 0x6e, 0x6b, 0x28, 
    0x66, 0x39, 0x31, 0x05, 0x6e, 0x6a, 0x6a, 0x28, 
    0x05, 0x2f, 0x34, 0x66, 0x65, 0x61, 0x69, 0x6e, 
    0x05, 0x63, 0x63, 0x3b, 0x27
};
unsigned int flag_len = 29;

void print_banner() {
    puts("==================================================");
    puts("  YADA'S ARK - MAIN CRYO-DECK AIRLOCK CONSOLE     ");
    puts("  SYSTEM INTEGRITY: 28% | PROTOCOL: LOCKDOWN      ");
    puts("==================================================");
}

int main(int argc, char *argv[]) {
    print_banner();
    
    char input_key[64];
    printf("[?] ACIL DURUM GUVENCE KODUNU GIRIN: ");
    if (fgets(input_key, sizeof(input_key), stdin) == NULL) {
        return 1;
    }
    
    // Satir sonu karakterini temizle
    input_key[strcspn(input_key, "\n")] = 0;
    
    // Acil durum erisim parolasi (Door Access Key): "CRYOPOD-3487-OPEN"
    char required_pass[] = "CRYOPOD-3487-OPEN";
    
    if (strcmp(input_key, required_pass) == 0) {
        puts("\n[+] GUVENCE KODU DOGRULANDI. HAVA KILIDI DEVRE DISI!");
        printf("[+] ERISIM PROTOKOL BAYRAGI: ");
        for (unsigned int i = 0; i < flag_len; i++) {
            putchar(enc_flag[i] ^ 0x5A);
        }
        putchar('\n');
    } else {
        puts("\n[-] HATALI KOD! GUVENLIK KILIDI AKTIF. ERISIM REDDEDILDI.");
    }
    
    return 0;
}