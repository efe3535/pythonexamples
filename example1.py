sayi=50
a=1

denemeler = 0

while a==1:
    if denemeler <= 5:
        denemeler+=1
        tahmin=input("tuttuğum bir sayı var. bu sayıyı tahmin edermisin?")
        tahmin=int(tahmin)
        if tahmin==sayi:
            print("Tebrik ederim! Doğru sayıyı buldun.")
            a=0 
        else:
            print("yanlış cevapladın. tekrar dene...") 
            #print("çıkıyoorum") 
    else:
        print("cok fazla denediniz.")
        break