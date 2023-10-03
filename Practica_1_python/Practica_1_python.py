# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import*
import tkinter as tk

pantalla=tk.Tk()
pantalla.title("Hola")
pantalla.geometry("520x480")
boton = tk.Button(pantalla,text="Hola Mundo")
boton.place(x=50,y=50)
entrada = tk.Entry()
entrada.place(x=50,y=100,width=150)
pantalla.mainloop()

