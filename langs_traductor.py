from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox, filedialog
import pyttsx3
from googletrans import Translator

ventana = Tk()
ventana.title("Traductor")
ventana['bg'] = 'light blue'
ventana.geometry('1101x700')
display1 = scrolledtext.ScrolledText(ventana,width=55,height=29)
display1.place(x=30,y=77)
display2 = scrolledtext.ScrolledText(ventana,width=55,height=29)
display2.place(x=610,y=77)
btnListen1 = Button(ventana,text='ESCUCHAR',bg='green',fg='white',width=64)
btnListen1.place(x=30,y=548)
btnListen2 = Button(ventana,text='ESCUCHAR',bg='green',fg='white',width=64)
btnListen2.place(x=610,y=548)
label1 = Label(ventana,text="TEXTO",bg="light blue",width=64)
label1.place(x=30,y=53)
label2 = Label(ventana,text="TRADUCCIÓN",bg="light blue",width=64)
label2.place(x=610,y=53)

ventana.mainloop()
