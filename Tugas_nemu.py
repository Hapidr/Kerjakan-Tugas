

def validasi(angka):
    if angka == 1:
        print("Sampai jumpa di kelas Offline")

    elif angka == 2:
        print("Silahkan ikuti kelas Online")

    elif angka == 3:
        print("Sampai jumpa tahun depan")

    else:
        print("Masukkan Angka yang benar!")

print("""
1. Bisa hadir Offline 
2. Jaringan Bagus 
3. Tidak bisa hadir Offline dan Jaringan tidak bagus """)
angka = input("Masukkan Angka: ")
try:
    validasi(int(angka))
except:
    print("Masukkan Angka yang benar!")
