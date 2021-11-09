import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyautogui
import subprocess as sub
from traductor import empezar
from time import sleep
from tkinter import *
from PIL import Image, ImageTk 
import webbrowser

main_window = Tk()
main_window.title("Alita IA")

main_window.geometry("900x500")
main_window.resizable(0,0)
main_window.configure(bg='#902BF7')

label_title = Label(main_window, text="Alita Asistente Virtual", bg="#C595F7", fg="#2F2C33", font=('Times New Roman', 30, 'bold'))
label_title.pack(pady=10)

alita_photo = ImageTk.PhotoImage(Image.open("Alita3.jpg"))
window_photo = Label(main_window, image=alita_photo)
window_photo.pack(pady=5)

listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id) 

engine.say("Hola soy Alita, tu asistente virtual")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()
 
def listen():
    try:
        with sr.Microphone() as source:
            talk("Escuchando...")
            print("Escuchando..")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if 'alita' in rec:
                rec = rec.replace('alita', '')
                print(rec)
                
    except:  
        pass   
    return rec  

def run():
      
    rec = listen()
    print(rec)
    if 'reproduce' in rec:         
        music = rec.replace('reproduce', '')        
        talk('Reproduciendo' + music)
        pywhatkit.playonyt(music)   
    elif 'traducir' in rec:
        empezar()       
    elif 'wikipedia' in rec:
        order = rec.replace('wikipedia', '')
        info = wikipedia.set_lang("es")
        info = wikipedia.summary(order, 1)
        print(info)
        talk(info)        
    elif 'busca' in rec:
        order = rec.replace('busca', '')
        talk('Resultados de'+ order) 
        info = pywhatkit.search(order)
        #talk(info)
    elif 'pantalla' in rec:
        screenshot = pyautogui.screenshot()
        screenshot.save("Screenshot.png")
        talk("Capturando la pantalla...")        
    elif 'escribir' in rec:
        sub.call('start notepad.exe', shell=True)
        tex = rec.replace('escribir', '')
        sleep(1)  
        talk("Texto listo") 
        pyautogui.write(tex)        
    elif 'peliculas' in rec:
        webbrowser.open("https://www.netflix.com/do/")             
    else:
        talk("No logro entenderte")               

button_escuchar = Button(main_window, text="Escuchar", fg="white", bg="#A322B9", font=("Times New Roman", 15, "bold"), width=20, height=3, command=run) 
button_escuchar.place(x=750, y=250, width=100, height=50)
 
main_window.mainloop()            
 
             

