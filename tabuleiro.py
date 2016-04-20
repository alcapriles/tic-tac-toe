# -*- coding: utf-8 -*-
import tkinter as tk
import numpy as np

class tabuleiro:
    # Definindo a classe
    def __init__(self):
        # Definindo janela
        self.window = tk.Tk()
        self.window.geometry("300x350+100+100")
        self.window.rowconfigure(0, minsize=100)
        self.window.rowconfigure(1, minsize=100)
        self.window.rowconfigure(2, minsize=100)
        self.window.rowconfigure(3, minsize=50)
        self.window.columnconfigure(0, minsize=100)
        self.window.columnconfigure(1, minsize=100)
        self.window.columnconfigure(2, minsize=100)
        # Definindo label
        self.label = tk.Label(self.window)
        self.label.grid(row = 0, column = 0, columnspan=3)
        self.label.configure(text = "X, é a sua vez")
            
        # Definindo botôes
        #self.matriz = np.zeros((3,3))
        
        
    def iniciar(self):
        self.window.mainloop() 
        
    def joga_X(self):
        self.label.configure(text = "X, é a sua vez")
        
jogo = tabuleiro()
jogo.iniciar()