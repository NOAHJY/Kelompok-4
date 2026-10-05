# Function: return, tanpa parameter
def baca_nominal() -> int:
    return int(input("Nominal donasi (Rp): "))


# Function: return, berparameter
def tentukan_efek(nominal: int) -> str:
    if nominal >= 500000:
        return "DRAMOK PREMIUM"
    elif nominal >= 200000:
        return "SEMOGA KEINGINANNYA TERCAPAI, AMIN"
    elif nominal >= 100000:
        return "SEMOGA KEINGINANNYA TERCAPAI, TAMBAH 100K LAGI BARU AMIN"
    elif nominal >= 10000:
        return "ADUH APAAN SIH!!"
    elif nominal >= 5000:
        return "AMSSRBLHGSHARKM"
    else:
        return "..."


# ===== CLASS dan METHOD =====
class Saweria:
    def __init__(self):
        self.riwayat = []   # daftar donasi, bisa dilihat semua orang
        self.total = 0

    # Method: non-return, tanpa parameter
    def tampilkan_menu(self) -> None:
        print("\n=== MINI SAWERIA ===")
        print("1. Kirim Donasi")
        print("2. Lihat Riwayat Donasi")
        print("3. Keluar")

    # Method: non-return, berparameter
    def tampilkan_alert(self, nama: str, pesan: str, efek: str) -> None:
        print(f"\n>>> {efek} <<<")
        print(f'{nama} berdonasi: "{pesan}"')

    # Method: non-return, berparameter
    def simpan_donasi(self, nama: str, nominal: int) -> None:
        self.riwayat.append(f"{nama} - Rp{nominal:,}")
        self.total += nominal

    # Method: non-return, tanpa parameter
    def tampilkan_riwayat(self) -> None:
        print("\n--- Semua orang bisa lihat ---")
        for i, data in enumerate(self.riwayat, start=1):   # loop riwayat
            print(f"{i}. {data}")
        print(f"Total terkumpul: Rp{self.total:,}")


# ===== PROGRAM UTAMA =====
akun = Saweria()
pilihan = 0

while pilihan != 3:                      # loop menu
    akun.tampilkan_menu()
    pilihan = int(input("Pilih: "))

    if pilihan == 1:
        nama = input("Nama: ")
        pesan = input("Pesan: ")
        nominal = baca_nominal()

        efek = tentukan_efek(nominal)            # panggil function
        akun.tampilkan_alert(nama, pesan, efek)  # panggil method
        akun.simpan_donasi(nama, nominal)

    elif pilihan == 2:
        akun.tampilkan_riwayat()

print("Sampai jumpa!")