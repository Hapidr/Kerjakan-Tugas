def volume_tabung(jari_jari, tinggi):
    print(f"Jari-jari tabung {jari_jari}, tinggi {tinggi}".title())
    if jari_jari % 7 == 0:
        return (22/7) * (jari_jari**2) * tinggi
    else:
        return 3.14 * (jari_jari**2) * tinggi

def volume_kerucut(jari_jari, tinggi):
    print(f"Jari-jari kerucut {jari_jari}, tinggi {tinggi}".title())
    if jari_jari % 7 == 0:
        return (1/3) * ((22/7) * (jari_jari**2) * tinggi)
    else:
        return (1/3) * ((22/7) * (jari_jari**2) * tinggi)

def volume_kubus(rusuk):
    print(f"Rusuk kerucut {rusuk}".title())
    return rusuk**3

print(volume_tabung(8, 10))
print(volume_kerucut(7, 10))
print(volume_kubus(7))
