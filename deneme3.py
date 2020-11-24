user = input("admin/user ")
while True:
    if user == "admin":
        baslangic = input("başlanacak sayı")
        bitis = input("kaça kadar?")
        atlama = input("kaç atlamalıyız")
        
        for _ in range(int(baslangic),int(bitis)+1,int(atlama)):
            print(_)
        break
    elif user == "user":
        sayi4 = input("kaça kadar?")
        for _ in range(int(sayi4)+1):
            print(_)
        break
    else:
        print("lütfen dogru giriniz")