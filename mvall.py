import os,shutil,send2trash

fname = __file__+"_folder"
if(not os.path.isdir(fname)):
    os.system("mkdir "+fname)

try:
    for dosya in os.listdir():
            if not dosya.endswith(".py"):
                shutil.move(dosya,fname)
    send2trash.send2trash(fname)
except shutil.Error:
    print("Bu Script'i birden fazla çalıştırmışsınız gibi...")