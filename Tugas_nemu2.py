hari = ["Senin", "Selasa", "Rabu","Kamis","Jum'at","Sabtu","Minggu"]

print('PROGRAM MENGHITUNG 50 HARI KEMUDIAN \n ')

day = int(input(" 0. Senin \n 1. Selasa \n 2. Rabu \n 3. Kamis \n 4. Jum'at \n 5. Sabtu \n 6. Minggu \n Masukkan Hari: "))

while day <= 6:
	for i in range(0, 50):
		
		day += 1
		if day > 6:
			day *= 0
		print(hari[day])
			
	print("\n50 Hari dari hari {} adalah hari {}".format(hari[day -1], hari[day]))
			
	break

else:
	print('Masukkan Angka yang sesuai')


