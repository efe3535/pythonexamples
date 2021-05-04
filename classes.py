class hayvanlar:
    def __init__(self, hayvan, hayvanismi):
        self.hayvan = hayvan
        self.hayvanismi = hayvanismi

    def hayvanbilgisi(self):
        return "Hayvan ismi:" + str(self.hayvanismi) + "\nHayvan: " + str(self.hayvan)

devam = True
hayvanlistesi = ["Köpek", "Kedi", "Kuş", "Hamster"]
hayvansayisi = 0
kayitlihayvanlar = []

while devam:
    sec = ""
    try:
        sec = int(input("""
        1-Köpek
        2-Kedi
        3-Kuş
        4-Hamster

        Hangi hayvan (sayı girin lütfen)
        """))

    except ValueError:
        print("Arkadaşım sen anlamıyor musun? Sayı gireceksin bak yazdık oraya!")
        exit()

    isim = input("    Adı ne olsun?\n    ")
    hayvankaydi = hayvanlar(hayvanlistesi[int(sec)-1], isim)
    kayitlihayvanlar.append(hayvankaydi.hayvanbilgisi() + "\n\n\n")
    
    print("="*30)
    print("HAYVAN(LAR)")
    print("="*30)
    for kayit in kayitlihayvanlar:
        print(kayit)
    devamsoru = input("Bir hayvan daha tanımlamak ister misiniz? (e/h)")
    if devamsoru == "h":
        devam = False

print("İyi günler.")