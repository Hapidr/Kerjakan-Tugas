print("PROGRAM MENGHITUNG 50 HARI KEMUDIAN".center(50))
hari = {1: "Senin", 2: "Selasa", 3: "Rabu", 4: "Kamis", 5: "Jumat", 6: "Sabtu", 7: "Minggu"}
print("1. Senin\n2. Selasa\n3. Rabu\n4. Kamis\n5. Jum'at\n6. Sabtu\n7. Minggu")

day = int(input("Masukkan Angka 1-7: "))
if day > 6 and day <= 7:
    hi = day * 0
    yaum = hi + (50 % 7)
    print(f"Hari ke-{day} adalah {hari[day]}")
    print(f"50 Hari setelah hari {hari[day]} adalah hari {hari[yaum]}")

elif day > 0 and day <= 6:
    yaum = day + (50 % 7)
    print(f"Hari ke-{day} adalah {hari[day]}")
    print(f"50 Hari setelah hari {hari[day]} adalah hari {hari[yaum]}")
else:
    print("Angka yang anda masukkan tidak sesuai")
