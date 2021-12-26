def volume_tabung(jari_jari = 8, tinggi = 10):
    print(f"Jari-jari tabung {jari_jari}, tinggi {tinggi}".title())
    if jari_jari % 7 == 0:
        return (22/7) * (jari_jari**2) * tinggi
    else:
        return 3.14 * (jari_jari**2) * tinggi

def volume_kerucut(jari_jari = 7, tinggi = 10):
    print(f"Jari-jari kerucut {jari_jari}, tinggi {tinggi}".title())
    if jari_jari % 7 == 0:
        return (1/3) * ((22/7) * (jari_jari**2) * tinggi)
    else:
        return (1/3) * ((22/7) * (jari_jari**2) * tinggi)

def volume_kubus(rusuk = 7):
    print(f"Rusuk kerucut {rusuk}".title())
    return rusuk**3

print(f"{volume_tabung():.2f}")
print(f"{volume_kerucut():.2f}")
print(volume_kubus())
