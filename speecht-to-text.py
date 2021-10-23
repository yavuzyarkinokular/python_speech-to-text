# Requires PyAudio and PySpeech.

import speech_recognition as sr
import time

while True:
    print(
        "*****************\x1B[3m coded by YAVUZ YARKIN OKULAR\x1B[0m*****************"
    )
    secim = input("Metin yazdırmak icin 1 'i \n Cıkmak icin 2 'i tuşlayınız:")
    if secim == "1":
        # Record Audio
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Sesi mikrofondan alacaktır dikkatli ol ! ")
            audio = r.listen(source)

        metin_yazdirici = r.recognize_google(audio, language="tr_TR")
        print(metin_yazdirici)
        print("\n")

    elif secim == "2":
        break
