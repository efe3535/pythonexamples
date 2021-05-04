import requests
from bs4 import BeautifulSoup

print("GittiGidiyor ürün bilgi bulucu.\nNot: Bu program GittiGidiyor.com sitesine ait değildir. Copyright Ahmet Efe AKYAZI ©2020 \n Hak talepleri için a.efe.akyazi@gmail.com")

# url = "https://www.gittigidiyor.com/huawei-y-6s_spp_770579?id=629588430"
url = input("GittiGidiyor linkini yapıştırın:\n")
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

# print(soup.prettify())
starCount = soup.find("div", class_="catalog-dull-stars")
fiyatBul = soup.find("span", id="sp-price-highPrice")
puanBul = soup.find("strong", id="sp-reviewAverage")
urunBul = soup.find("h1", id="sp-title")
saticiPuan = soup.find('span',id="sp-positiveCommentPercentage")

icerikler = starCount.contents
icerikSayac = 0
# TODO: Derecelendirme verisi çek

for content in icerikler:
    if content == "\n":
        icerikler.pop(icerikSayac)
    icerikSayac += 1

# print(puanbul)
saticiAd = soup.find("span",id="sp-member-nick")
print("=" * 30)
print("Ürün bilgileri:")
print("=" * 30)
print("Ürün adı:", urunBul.text.strip())
print("Fiyat:", fiyatBul.text.strip())
print("Derecelendirme:", puanBul.text.strip() + "/" + str(len(icerikler)))
print("Satıcı: ",saticiAd.text.strip())
print("Satıcı puanı:",saticiPuan.text.strip() + "%")