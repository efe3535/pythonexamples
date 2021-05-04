import playsound
from gtts import gTTS
import speech_recognition as sr
import webbrowser
import os



filename = "sesdosyasi.mp3"

r = sr.Recognizer()
mic = sr.Microphone()


def saveandplay(recognizedtext,msgtext):
    msg = gTTS(recognizedtext + msgtext , lang="tr")
    msg.save(filename)
    playsound.playsound(filename)


def listenit():
    audio = r.listen(source)
    recognized = str(r.recognize_google(audio,language="tr-TR")).lower()
    if(recognized == "youtube aç"):
        webbrowser.open("https://www.youtube.com")
        saveandplay(recognized," komutu başarıyla uygulandı.")
    if(recognized == "ayarlar"):
        os.system("start ms-settings:")
        saveandplay(recognized,"başlatıldı")

    else:
        print(recognized,"tanınmadı, başka bir şey demek istemiş olabilir misiniz?")
        print("Tekrar dinleniyor.")

with mic as source:
    try:
        listenit()
    except sr.UnknownValueError:
        print("Ses tanınmadı.")
        print("Tekrar dinleniyor.")
        listenit()

os.mkdir("fo")