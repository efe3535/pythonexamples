import os,string

alfabe = string.ascii_lowercase

#TODO: Alfabedeki her harf için bir dosya oluşturan bir program yaz.

for harf in alfabe:
    f=open(harf,"w")
    f.close()