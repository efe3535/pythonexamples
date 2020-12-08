from colorama import Fore

calisanlar = ["Ahmet","Mehmet"]

#yeni çalışanlar katılıyor

calisanlar.append("Burak")
calisanlar.append("Hüseyin")

numaralar = ["1","2","3","4"]

#Değerler yazılıyor

print("Çalışanlar\t",calisanlar)

#Döngü ile çalışanların ad ve numaraları yazılıyor
x=[]

for i in range(len(calisanlar)):
    x.append(f"Adı ve id'si: {Fore.RED} ID: {i} {Fore.RESET + Fore.GREEN}Ad: {calisanlar[i]}"+Fore.RESET)
print("\n".join(x))
