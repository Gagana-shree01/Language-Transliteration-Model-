import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm
import os
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
from googletrans import Translator
import trans as ret

bgcolor="#CDCDC0"
bgcolor1="#8B8B88"
fgcolor="black"

def Home():
        global window
        
        
        def clear():
                
            print("Clear1")
            txt.delete(0, 'end')
            txt3.delete(0, 'end')
            txt2.delete(0.0, 'end')
            txt4.delete(0.0, 'end')
        def sel():
            selection = str(var.get())
            label.config(text = selection)
            

        window = tk.Tk()
        var = IntVar()
        window.title("Native Language Translation To English and OCR...")
        C = tk.Canvas(window, bg="blue", height=250, width=300)
        filename = ImageTk.PhotoImage(file = "bg1.jpg")
        background_label = tk.Label(window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        C.pack()
        

 
        window.geometry('1280x720')
        window.configure(background=bgcolor)
        #window.attributes('-fullscreen', True)

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        

        message1 = tk.Label(window, text="Native Language Translation To English and OCR Image Translation"   ,fg=fgcolor  ,width=70  ,height=2,font=('times', 25, 'bold underline'))
        message1.place(x=50, y=10)

        lbl = tk.Label(window, text="Enter Your Text",width=20  ,height=2  ,fg=fgcolor   ,font=('times', 15, ' bold ') ) 
        lbl.place(x=100, y=100)
        
        txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt.place(x=400, y=115)

        
        R1 = Radiobutton(window, text="Hindi", variable=var, value=1,command=sel)
        R1.place(x=350, y=160)
        #R1.pack( anchor = W )
        R2 = Radiobutton(window, text="Kanada", variable=var, value=2,command=sel)
        R2.place(x=450, y=160)
        #R2.pack( anchor = W )
        R3 = Radiobutton(window, text="Tamil", variable=var, value=3,command=sel)
        R3.place(x=550, y=160)
        R4 = Radiobutton(window, text="Telugu", variable=var, value=4,command=sel)
        R4.place(x=650, y=160)
        #R3.pack( anchor = W)
        

        lbl2 = tk.Label(window, text="Converted Text",width=20  ,height=2  ,fg=fgcolor  ,font=('times', 15, ' bold ') ) 
        lbl2.place(x=100, y=220)

        txt2 = Text(window, width = 70, height = 5, bg="white",fg="red",font=('times', 15, ' bold '))
        txt2.place(x=400, y=225)
        lbl3 = tk.Label(window, text="Select Image",width=20  ,height=2  ,fg=fgcolor  ,font=('times', 15, ' bold ') ) 
        lbl3.place(x=100, y=420)

        txt3 = tk.Entry(window, width = 20,  bg="white",fg="red",font=('times', 15, ' bold '))
        txt3.place(x=400, y=425)

        lbl4 = tk.Label(window, text="Result",width=20  ,height=2  ,fg=fgcolor  ,font=('times', 15, ' bold ') ) 
        lbl4.place(x=100, y=520)

        txt4 = Text(window, width = 70, height = 5, bg="white",fg="red",font=('times', 15, ' bold '))
        txt4.place(x=400, y=525)

        def browseprocess():
                path=filedialog.askopenfilename()
                print(path)
                txt3.delete(0, 'end')
                txt3.insert('end',path)
                if path !="":
                        load = Image.open(path)
                        render = ImageTk.PhotoImage(load)
                        img = tk.Label(image=render, height="350", width="500")
                        img.image = render
                        img.place(x=960, y=200)
                else:
                        tm.showinfo("Input error", "Select image")
        

        
        def ocr():
                path=txt3.get()
                translator = Translator()
                reader = easyocr.Reader(['en'])
                result = reader.readtext(path,paragraph="False")
                print("Extracted text:",result)
                text = result[0][1]
                
                from_lang="en"
                to_lang="kn"
                text_to_translate = translator.translate(text, src= from_lang,dest= to_lang)
                text = text_to_translate.text
                txt4.insert('end',text)
                                


        


        def lan1toeng():
                txt2.delete(0.0, 'end')
                sym=txt.get()
                lang=label.cget("text")
                print("file path=",sym)
                print("language=",lang)
                if sym != "" and lang!="" :
                        if lang=="1":
                                txt2.delete(0.0, 'end')
                                txt4.delete(0.0, 'end')
                                lan="devanagari"
                                converted,translated=ret.process(sym,lan)
                                txt2.insert('end',converted)
                                txt4.insert('end',translated)
                                tm.showinfo("Result", "Hinglish to English Translation done successfull")
                        if lang=="2":
                                txt2.delete(0.0, 'end')
                                txt4.delete(0.0, 'end')
                                lan="kannada"
                                converted,translated=ret.process(sym,lan)
                                txt2.insert('end',converted)
                                txt4.insert('end',translated)
                                tm.showinfo("Result", "Kanglish to English Translation done successfull")
                        if lang=="3":
                                txt2.delete(0.0, 'end')
                                txt4.delete(0.0, 'end')
                                lan="tamil"
                                converted,translated=ret.process(sym,lan)
                                txt2.insert('end',converted)
                                txt4.insert('end',translated)
                                tm.showinfo("Result", "Tanglish to English Translation done successfull")
                        if lang=="4":
                                txt2.delete(0.0, 'end')
                                txt4.delete(0.0, 'end')
                                lan="telugu"
                                converted,translated=ret.process(sym,lan)
                                txt2.insert('end',converted)
                                txt4.insert('end',translated)
                                tm.showinfo("Result", "Teluglish to English Translation done successfull")
                                
                else:
                        tm.showinfo("Input error", "Enter your text or choose language")


        

        browse = tk.Button(window, text="Translate", command=lan1toeng  ,fg=fgcolor  ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse.place(x=650, y=110)
        browse1 = tk.Button(window, text="Browse", command=browseprocess  ,fg=fgcolor  ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse1.place(x=650, y=425)
        browse2 = tk.Button(window, text="OCR", command=ocr  ,fg=fgcolor  ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse2.place(x=850, y=425)


        clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
        clearButton.place(x=820, y=700)
         
        

        quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        quitWindow.place(x=990, y=700)

        window.mainloop()
Home()

