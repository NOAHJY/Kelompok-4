nama_streamer = "Reza dan Ladesh"


# FUNCTION: return, tanpa parameter
def baca_nominal() -> int:
    return int(input("Nominal donasi (Rp): "))


# FUNCTION: return, berparameter (if-else ada di sini)
def tentukan_respon(nama: str, nominal: int) -> str:
    if nominal >= 500000:
        return f"KAMU NGAPAIN SEMALAM SAMA {nama}! Ah, gila kamu! 😱 Kamu yang gila, ih! 🤯 Hah, kamu gila! 🤬 Apa salah aku? 😭 Bertahun-tahun loh kamu... Baru kali ini kamu KDRT sama aku. Aku udah muak sama kamu! 😡 Aku udah muak! 😤 Aku muak! 💢 Kamu cuekin gua terus! 🙈 Kamu cuekin gua terus, hah? 🗯️ Mas, dengarin dulu! 🗣️ Dipikir enggak sakit nih? 💔"
    elif nominal >= 200000:
        return f"{nama}, SEMOGA KEINGINANNYA TERCAPAI, AMIN"
    elif nominal >= 100000:
        return f"Makasih {nama}, SEMOGA KEINGINANNYA TERCAPAI, TAMBAH 100K LAGI BARU AMIN"
    elif nominal >= 10000:
        return f"ADUH APAAN SIH!!"
    elif nominal >= 5000:
        return f"AMSSRBLHGSHARKM"
    else:
        return f"..."


class Saweria:
    def __init__(self):
        self.riwayat = []   # variabel: daftar donasi

    # METHOD: non-return, tanpa parameter
    def tampilkan_menu(self) -> None:
        print("\n=== MINI SAWERIA ===")
        print("1. Kirim Donasi")
        print("2. Lihat Riwayat")
        print("3. Keluar")

    # METHOD: non-return, berparameter
    def tampilkan_respon(self, respon: str) -> None:
        print(f"\n{nama_streamer} berkata: {respon}")


# ===== PROGRAM UTAMA =====
akun = Saweria()
pilihan = 0

while pilihan != 3:                          
    akun.tampilkan_menu()
    pilihan = int(input("Pilih: "))

    if pilihan == 1:
        nama = input("Nama: ")
        nominal = baca_nominal()
        respon = tentukan_respon(nama, nominal)   
        akun.tampilkan_respon(respon)             
        akun.riwayat.append(f"{nama} - Rp{nominal:,}")

    elif pilihan == 2:
        print("\n--- Riwayat Donasi ---")
        for data in akun.riwayat:                 
            print("-", data)