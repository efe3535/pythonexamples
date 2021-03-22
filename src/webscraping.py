import requests
from bs4 import BeautifulSoup

site = requests.get("https://sondepremler.net/")

src = BeautifulSoup(site.content)

deprema = []
depremb = []
deprems = []
depremc = []

depremlistemw = src.findAll("p",{"class":"excerpt"})
depremlistesehir = src.findAll("h2",{"class":"title"})

saat = src.findAll("div",{"class":"byline"})

for depremSaat in saat:
    deprems.append(str(depremSaat.contents[1].contents[0]).strip())


for depremmw in depremlistemw:
    deprema.append(str(depremmw.contents[0]).strip())

for depremsehir in depremlistesehir:
    depremb.append(str(depremsehir.contents[1].contents[0]).strip())

for c in range(0,len(deprema) - 1):
    depremc.append(deprema[c] + "\nYer: " + depremb[c] + "\n" + "Tarih: " + deprems[c] + "\n")

for deprem in depremc:
    print("="*50 + "\n" + deprem + "\n" + "="*50)
