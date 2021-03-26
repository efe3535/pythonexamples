ogr1 = ["Ali", "Uzun", 1980, "3/C", 60, 70]
ogr2 = ["Ayse", "Kısa", 1986, "6/A", 90, 75]
ogr3 = ["Hüseyin", "Türk", 1989, "5/G", 40, 50]
ogr4 = ["Mukaddes", "Koç", 1935, "2/F", 100, 90]
ogr5 = ["Ozan", "Aral", 1969, "6/B", 95, 85]
ogr6 = ["Mesut", "Saral", 1995, "6/B", 65, 25]
ogr7 = ["Arif", "Bozan", 1955, "6/B", 90, 70]
ogr8 = ["Tuğçe", "Sözen", 1965, "6/B", 80, 80]
ogr9 = ["Pınar", "Gezen", 1984, "6/B", 100, 85]

tumogr = [ogr1, ogr2, ogr3, ogr4, ogr5, ogr6, ogr7, ogr8, ogr9]

val = 0

yetmisdenaz=0
yetmisdenfazla=0

sayac=0

sayac3=0

val2=0
for ogr in tumogr:
    val += 1
    if ogr[2] < 1970:
        yetmisdenaz+=1
        print("1970'den önce doğdu. Ad soyad: ", val,ogr[0], ogr[1], "doğduğu tarih", ogr[3],"not ortalaması",(ogr[4]+ogr[5])/2)
        sayac+=ogr[4]+ogr[5]
    else:
        val2 += 1
        yetmisdenfazla+=1
        print("1970'den sonra doğdu. Ad soyad: ", val,ogr[0], ogr[1], "doğduğu tarih", ogr[3],"not ortalaması",(ogr[4]+ogr[5])/2)
        sayac3+=ogr[4]+ogr[5]
        

buyuklerortalama=sayac/(val-1)
kucuklerortalama=sayac3/(val2-1)

if buyuklerortalama > kucuklerortalama:
    print("Büyüklerin ortalaması küçüklerden daha fazla")

if buyuklerortalama < kucuklerortalama:
    print("Küçüklerin ortalaması büyüklerden daha fazla")

if buyuklerortalama == kucuklerortalama:
    print("Büyük ve küçüklerin ortalaması eşit")

#print(buyuklerortalama)