user = input("admin/user")
while True:
    if user == "admin":
        sayi1 = input("başlanacak sayı")
        sayi2 = input("kaça kadar?")
        sayi3 = input("kaç atlamalıyız")
        
        for _ in range(int(sayi1),int(sayi2),int(sayi3)):
            print(_)
        break
    elif user == "user":
        sayi4 = input("kaça kadar?")
        for _ in range(int(sayi4)):
            print(_)
        break
    else:
        print("lütfen dogru giriniz")