print("PROGRAM MENGHITUNG 50 HARI KEMUDIAN\n ")
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jum'at" , "Sabtu", "Minggu"]

print("0. Senin\n1. Selasa\n2. Rabu\n3. Kamis\n4. Jum'at\n5. Sabtu\n6. Minggu")

day = int(input("Masukkan hari ini: "))

yaum = day + (50 % 7)
print("50 Hari setelah hari ", hari[day], " adalah hari", hari[yaum])