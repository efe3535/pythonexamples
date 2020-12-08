def calisanAta(ad,numara):
    return ad+" "+numara

calisanlar = [calisanAta("Ahmet","71"),calisanAta("Mehmet","89")]

#yeni çalışanlar katılıyor

calisanlar.append(calisanAta("Burak","95"))
calisanlar.append(calisanAta("Hüseyin","76"))

#Değerler yazılıyor

print(calisanlar)

#Döngü ile çalışanların ad ve numaraları yazılıyor

for calisan in calisanlar:
    print("Çalışan: ",calisan)