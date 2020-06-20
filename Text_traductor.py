from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox
from tkinter import ttk
import time
import pyperclip
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
        self.finished = True
        #self.lang = 'en'
        self.copia = ""

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
        self.btnTans.place(x=516,y=225)
        self.label3 = Label(self.ventana,text='TRADUCIR A:',bg="light blue")
        self.label3.place(x=511,y=1)
        self.entryLang = ttk.Combobox(self.ventana,width=24,state='readonly')
        self.entryLang.place(x=467,y=1)#y=170)
        self.valores = list(langs.values())
        self.claves = list(langs.keys())
        self.entryLang["values"]=self.valores
        self.entryLang.set("Selecciona Idioma")
        self.btnCopy = Button(self.ventana,text="PEGAR UN TEXTO",command=self.inicia_copia)
        self.btnCopy.place(x=30,y=420)
        self.textLabel = Label(self.ventana, width=156, bg="light blue")
        self.textLabel.place(x=1,y=25)
        self.btnReset = Button(self.ventana, text="RECUPERAR TEXTO",command=self.recover_text)
        self.btnReset.place(x=30,y=450)
        
        self.ventana.mainloop()

    def detect(self):
        if "speaking1.mp3" in os.listdir():
            os.remove("speaking1.mp3")
        if len(self.display1.get('1.0',END)) > 1:
            self.lang = (self.translator.translate(self.display1.get('1.0',END)).src)
            print(self.lang)
            self.tts = gtts.gTTS(self.display1.get('1.0',END),lang=self.lang)
            self.tts.save("speaking1.mp3")
            self.textLabel.configure(text="")
            playsound("speaking1.mp3")

    def copy_text(self):
        self.display1.delete('1.0',END)
        self.ultima_copia = pyperclip.paste().strip()
        while True:
            time.sleep(0.1)
            self.copia = pyperclip.paste().strip()
            if self.copia != self.ultima_copia:
                self.display1.insert(END,self.copia)
                self.ultima_copia = self.copia 
                print("Done!")
                break

    def recover_text(self):
        self.display1.insert(END,self.copia)
        
    def traduce(self):
        try:
            if "speaking.mp3" in os.listdir():
                os.remove("speaking.mp3")
            self.display2.delete('1.0',END)
            if len(self.display1.get('1.0',END)) > 1 and self.entryLang.get() != "":
                self.texto = self.display1.get('1.0',END)
                self.lang = self.claves[(self.valores).index(self.entryLang.get())]
                self.traduc = (self.translator.translate(self.texto.lower(),dest=self.lang).text)
                self.display2.insert(END,self.traduc)
                self.textLabel.configure(text="")
                self.tts = gtts.gTTS(self.traduc,lang=self.lang)
                self.tts.save("speaking.mp3")
                self.texto = ""
                self.finished = True
        except:
            self.textLabel.configure(text="SE PRODUJO UN ERROR")
        self.textLabel.configure(text="")
            

    def inicia_traduc(self):
        self.finished = False
        self.textLabel.configure(text="TRADUCIENDO...")
        t1 = threading.Thread(target=self.traduce)
        t1.start()

    def inicia(self):
        t = threading.Thread(target=self.listen)
        t.start()

    def inicia_detect(self):
        self.textLabel.configure(text="GENERANDO AUDIO...")
        t2 = threading.Thread(target=self.detect)
        t2.start()

    def listen(self):
        if "speaking.mp3" in os.listdir() and self.finished == True:
            playsound("speaking.mp3")

    def inicia_copia(self):
        messagebox.showinfo("COPIAR TEXTO","Seleccione el texto a pegar y escoje la opción \'Copiar\'")
        t3 = threading.Thread(target=self.copy_text)
        t3.start()

    def __del__(self):
        if "speaking1.mp3" in os.listdir():
            os.remove("speaking1.mp3")
        if "speaking.mp3" in os.listdir():
            os.remove("speaking.mp3")
        
if __name__=="__main__":
    traductor()
