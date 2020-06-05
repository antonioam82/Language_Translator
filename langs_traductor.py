from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox, filedialog
from tkinter import ttk
#import pyttsx3
from langs_dict import langs
import threading
from playsound import playsound
import gtts
import os
from googletrans import Translator

class traductor():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Traductor")
        self.ventana['bg'] = 'light blue'
        self.ventana.geometry('1101x490')
        self.translator = Translator()
        self.texto = ""
        self.traduc = ""
        self.lang = 'en'

        self.display1 = scrolledtext.ScrolledText(self.ventana,width=55,height=18)
        self.display1.place(x=30,y=77)
        self.display2 = scrolledtext.ScrolledText(self.ventana,width=55,height=18)
        self.display2.place(x=610,y=77)
        self.btnListen1 = Button(self.ventana,text='ESCUCHAR',bg='green',fg='white',width=64,command=self.inicia_detect)
        self.btnListen1.place(x=30,y=373)
        self.btnListen2 = Button(self.ventana,text='ESCUCHAR',bg='green',fg='white',width=64,command=self.inicia)
        self.btnListen2.place(x=610,y=373)
        self.label1 = Label(self.ventana,text="TEXTO A TRADUCIR",bg="light blue",width=64)
        self.label1.place(x=30,y=53)
        self.label2 = Label(self.ventana,text="TRADUCCIÓN",bg="light blue",width=64)
        self.label2.place(x=610,y=53)
        self.btnTans = Button(self.ventana,text='TRADUCIR',command=self.inicia_traduc)
        self.btnTans.place(x=516,y=310)
        self.label3 = Label(self.ventana,text='TRADUCIR A:',bg="light blue")
        self.label3.place(x=511,y=154)
        self.entryLang = ttk.Combobox(self.ventana,width=7)
        self.entryLang.place(x=516,y=170)
        self.entryLang["values"]=list(langs.values())
        
        self.ventana.mainloop()

    def detect(self):
        if "speaking1.mp3" in os.listdir():
            os.remove("speaking1.mp3")
        if len(self.display1.get('1.0',END)) > 1:
            self.lang = (self.translator.translate(self.display1.get('1.0',END)).src)
            self.tts = gtts.gTTS(self.display1.get('1.0',END))
            self.tts.save("speaking1.mp3")
            playsound("speaking1.mp3")

    def traduce(self):
        if "speaking.mp3" in os.listdir():
            os.remove("speaking.mp3")
        self.display2.delete('1.0',END)
        if len(self.display1.get('1.0',END)) > 1:
            self.texto = self.display1.get('1.0',END)
            self.lang = self.entryLang.get()
            if self.entryLang.get() == "":
                self.lang = 'en'
            self.traduc = (self.translator.translate(self.texto.lower(),dest=self.lang).text)
            print(self.traduc)
            self.display2.insert(END,self.traduc)
            self.tts = gtts.gTTS(self.traduc,lang=self.lang)
            self.tts.save("speaking.mp3")
            self.texto = ""

    def inicia_traduc(self):
        t1 = threading.Thread(target=self.traduce)
        t1.start()

    def inicia(self):
        t = threading.Thread(target=self.listen)
        t.start()

    def inicia_detect(self):
        t2 = threading.Thread(target=self.detect)
        t2.start()

    def listen(self):
        if "speaking.mp3" in os.listdir():
            playsound("speaking.mp3")

    def __del__(self):
        if "speaking1.mp3" in os.listdir():
            os.remove("speaking1.mp3")
        if "speaking.mp3" in os.listdir():
            os.remove("speaking.mp3")        
        
        
if __name__=="__main__":
    traductor()

