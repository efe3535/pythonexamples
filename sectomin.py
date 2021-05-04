saat = input("Saat girin.\n")
sl = saat.split(":")

hourtominute = int(sl[0]) * 60 * 60 #Saati saniyeye.
minutetosec = int(sl[1]) * 60 #Dakikayı saniyeye çeviriyoruz.

print("Saniye:\t",hourtominute + minutetosec)