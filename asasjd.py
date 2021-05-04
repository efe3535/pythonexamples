import os

sayi = int(input("Kaç klasör istersiniz?\n"))

for i in range(sayi):
    os.mkdir("merhaba")
    os.chdir("merhaba")