def tabung(r = int(input("Masukkan Jari-Jari alas Tabung: ")), t = int(input("Masukkan Tinggi Tabung: "))):
    print("Volume Tabung adalah " + str(3.14 * (r**2) * t))
tabung()

def kerucut(r = int(input("Masukkan Jari-Jari alas Kerucut: ")), t = int(input("Masukkan Tinggi Kerucut: "))):
    print("Volume Kerucut adalah " + str((1/3) * 3.14 * (r**2) * t))
kerucut()

def kubus(r = int(input("Masukkan rusuk Kubus: "))):
    print("Volume Kubus adalah " + str(r*r*r))

kubus()