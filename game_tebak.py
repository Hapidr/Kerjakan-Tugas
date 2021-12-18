while True:
    print("game tebak binatang dalam bahasa inggris".center(90).title())

    nama = {"Ant":'Semut', "Bee":"Lebah", "Mosquito":"Nyamuk", "Butterfly":"Kupu-kupu", "Spider":"Laba-laba", "Fly":"Lalat", 
    "Hedgehog":"Landak", "Snail":"Siput", "Cat":"Kucing", "Dog":"Anjing"}
    lst_name = list(nama)
    benar = 0
    salah = 0
    for i in lst_name:
        print(i)
        answer = input("Jawaban Anda: ")
        if answer.lower() == nama[i].lower(): 
            print("BENAR!")
            benar += 1
        else:
            print(f"SALAH\nJawaban yang benar adalah {nama[i]}")
            salah += 1
        print("-"*50)
    print(f"SKOR: {benar} benar dan {salah} salah")
    confirm = input("Ingin main lagi? : ")
    if confirm.lower() != "ya":
        print("Terima Kasih sudah bermain\nSampai Jumpa!")
        exit()