import psutil

pid = None
process_name = input("Hangi işlemin PID özelliğini bulmak istiyorsunuz?\t")
for proc in psutil.process_iter():
    if(proc.name() == process_name + ".exe"):
        pid = proc.pid
        proc.kill()
        print("İstenilen işlem(ler) kapatıldı.")