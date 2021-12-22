
def getPanjangLebar():
    panjang = float(input("Masukkan nilai: "))
    lebar = float(input("Masukkan nilai: "))

    print(f"======REKAP INPUTAN======\nPanjang : {panjang}cm\nLebar : {lebar}cm")

    hitungLuasPP(panjang, lebar)
    tampilLuasPP(hitungLuasPP(panjang, lebar))

def hitungLuasPP(panjang, lebar):
    return panjang * lebar

def tampilLuasPP(luas):
    print(f"Luas bangunan ini adalah {luas}cm")

getPanjangLebar()
