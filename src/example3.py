#Python simple if else and while loop example.
#Python basit if else ve while döngüsü örneği.

#You can copy that file as you want.
#Its ok for me :D

#Dosyayı istediğiniz gibi kopyalayabilirsiniz.
#Benim için sorun yok :D

user = input("admin/user ")

parola = "1234"

haksayac = 0

if user == "admin":
    while True:
        sifre = input("parolayı giriniz")
        if sifre == parola:
            while True:
                if user == "admin":
                    baslangic = input("başlanacak sayı")
                    bitis = input("kaça kadar?")
                    atlama = input("kaç atlamalıyız")

                    for _ in range(int(baslangic), int(bitis)+1, int(atlama)):
                        print(_)
                    break
                elif user == "user":
                    sayi4 = input("kaça kadar?")
                    for _ in range(int(sayi4)+1):
                        print(_)
                    break
                else:
                    print("lütfen dogru giriniz")
        else:
            if haksayac != 3:
                haksayac += 1
                print(f"Yanlış girdiniz. {4-haksayac} hakkınız kaldı")
            elif haksayac == 3:
                print("haklarınız bitti")
                break

elif user == "user":
    sayi4 = input("kaça kadar?")
    for _ in range(int(sayi4)+1):
        print(_)
