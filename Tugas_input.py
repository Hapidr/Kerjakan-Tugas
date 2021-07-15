def masukkan():
    #nama
    name = input("Masukkan Nama" + ": ".rjust(20))

    #NIM
    nim = int(input("Masukkan NIM" + ": ".rjust(21)))

    #Jurusan
    jur = input("Masukkan Jurusan" + ": ".rjust(17))
    
    #Tempat Lahir
    tl = input("Masukkan Tempat Lahir" + ": ".rjust(12))
    
    #Tanggal Lahir
    tgl = input("Masukkan Tanggal Lahir" + ": ".rjust(11))

    #Nomor HP
    no = int(input("Masukkan No HP" + ": ".rjust(19)))

    #Alamat
    alamat = input("Masukkan Alamat" + ": ".rjust(18))
    
    #Perguruan Tinggi
    pt = input("Masukkan Perguruan Tinggi" + ": ".rjust(8))

    #Perkerjaan
    pkrjn = input("Masukkan Pekerjaan" + ": ".rjust(15))


    print("\n", "-"*100)
    print("Selamat Datang", name, "di SISTEM MAHASISWA" + "\n -".ljust(15, "-") + "BIODATA MAHASISWA" + "-".rjust(15, "-"))
    print("-"*100)


    print("Nama ".ljust(18), ": ", name)
    print("NIM".ljust(18), ": ", nim)
    print("Jurusan ".ljust(18), ": ", jur)
    print("Tempat Lahir ".ljust(18), ": ", tl)
    print("Tanggal Lahir ".ljust(18), ": ", tgl)
    print("No HP ".ljust(18), ": ", no)
    print("Alamat ".ljust(18), ": ", alamat)
    print("Perguruan Tinggi ".ljust(18), ": ", pt)
    print("Pekerjaan ".ljust(18), ": ", pkrjn)
    
    
    
    '''print(nim)
    print(jur)
    print(tl)
    print(tgl)
    print(no)
    print(alamat)
    print(pt)
    print(pkrjn)'''

masukkan()




