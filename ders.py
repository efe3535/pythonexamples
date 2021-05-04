liste=[]
tektoplam=0
print("="*35)
girissayisitek=int(input("Kaç kere tek sayı girmek istersiniz? "))
print("="*35)
for i in range(girissayisitek):
    tekler=int(input(str(girissayisitek-i)+ " adet tek sayı giriniz."))
    tektoplam+=tekler
    if tekler%2==0:
        print("Tek sayı girmelisiniz.")
        exit()
print("="*35)
print("Tek sayıların toplamı:",tektoplam)
print("="*35)
cifttoplam=0

girissayisicift=int(input("Kaç kere çift sayı girmek istersiniz? "))
print("="*35)
for j in range(girissayisicift):
    ciftler=int(input(str(girissayisicift-j)+ " adet çift sayı giriniz."))
    cifttoplam+=ciftler
    if ciftler %2!=0 or ciftler==0:
        print("Çift sayı girmediniz ya da 0 girdiniz.")
        exit()

print("Çift sayıların toplamı",cifttoplam)
print("="*35)