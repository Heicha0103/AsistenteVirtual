from googletrans import Translator
import speech_recognition as sr
import pyttsx3, pywhatkit
from wikipedia.wikipedia import languages


listener = sr.Recognizer()


engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)



translator = Translator()

texto = ""
resultado = ""
contador = 0
contador2 = 0
saber = 0


def talk(text):
    engine.say(text)
    engine.runAndWait()


def talk2(text):
    engine2 = pyttsx3.init()
    voices = engine2.getProperty("voices")
    engine2.setProperty("voice", voices[0].id)

    engine2.say(text)
    engine2.runAndWait()



def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc)
            rec = rec.lower()
            #if name in rec:
                #rec = rec.replace(name, "")
    except:
        pass
    return rec

def listen2():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, languages="es-ES")
            rec = rec.lower(0)

    except:
        pass
    return rec



def empezar():
    global texto
    global resultado
    global contador
    global contador2
    global saber
    talk("¿Quieres traducir del inglés al español o del español al inglés?")
    print("¿Quieres traducir del inglés al español o del español al inglés?")
    rec = listen()
    if "del inglés al español" in rec:
        print("Qué quieres decir?")
        talk("Qué quieres decir?")
        rec = listen2()
        if "" in rec: 
            texto = rec
            resultado = str(translator.translate(texto, src = "en", dest = "es"))
            for i in resultado:
                contador +=1
                if i == ",":
                    contador2 +=1
                    if contador2 == 3:
                        saber = contador
                        contador2 = 0
                        talk(resultado[33:saber])
                        print(resultado)
                    else:
                        pass



    
    else:
        print("Qué quieres decir?")
        talk("Qué quieres decir?")
        rec = listen()
        if "" in rec: 
            texto = rec
        texto = rec
        resultado = str(translator.translate(texto, src = "es", dest = "en"))  
        for i in resultado:
            contador +=1
            if i == "=":
                contador2 +=1
                if contador2 == 4:
                    saber = contador
                    contador2 = 0
                    talk(resultado[33:saber])
                    print(resultado)
                else:
                    pass   
talk("")



