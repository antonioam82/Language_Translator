from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox, filedialog
from tkinter import ttk
import pyttsx3
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
        self.btnListen1 = Button(self.ventana,text='ESCUCHAR',bg='green',fg='white',width=64)
        self.btnListen1.place(x=30,y=373)
        self.btnListen2 = Button(self.ventana,text='ESCUCHAR',bg='green',fg='white',width=64)
        self.btnListen2.place(x=610,y=373)
        self.label1 = Label(self.ventana,text="TEXTO",bg="light blue",width=64)
        self.label1.place(x=30,y=53)
        self.label2 = Label(self.ventana,text="TRADUCCIÓN",bg="light blue",width=64)
        self.label2.place(x=610,y=53)
        self.btnTans = Button(self.ventana,text='TRADUCIR',command=self.traduce)
        self.btnTans.place(x=516,y=310)
        self.label3 = Label(self.ventana,text='TRADUCIR A:',bg="light blue")
        self.label3.place(x=511,y=154)
        self.entryLang = ttk.Combobox(self.ventana,width=7)
        self.entryLang.place(x=516,y=170)
        

        self.ventana.mainloop()

    def traduce(self):
        self.display2.delete('1.0',END)
        self.texto = self.display1.get('1.0',END)
        self.traduc = (self.translator.translate(self.texto,dest='es').text)
        self.display2.insert(END,self.traduc)
        self.traduc = ""
        self.texto = ""

if __name__=="__main__":
    traductor()
