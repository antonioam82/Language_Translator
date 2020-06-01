from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox, filedialog
import pyttsx3
from googletrans import Translator

ventana = Tk()
ventana.title("Traductor")
ventana['bg'] = 'light blue'
ventana.geometry('1090x700')
display1 = scrolledtext.ScrolledText(ventana,width=55,height=29)
display1.place(x=30,y=77)
display2 = scrolledtext.ScrolledText(ventana,width=55,height=29)
display2.place(x=600,y=77)

ventana.mainloop()
