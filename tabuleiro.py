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
        
        # Definindo botões
        # Botão 11
        self.botão_1_1 = tk.Button(self.window)
        self.botão_1_1.configure(command=self.botão_1_1clicado)
        self.botão_1_1.grid(row=1, column=1, sticky="nsew")
        # Botão 12
        self.botão_1_2 = tk.Button(self.window)
        self.botão_1_2.configure(command=self.botão_1_2clicado)
        self.botão_1_2.grid(row=1, column=2, sticky="nsew")
        # Botâo 13
        self.botão_1_3 = tk.Button(self.window)
        self.botão_1_3.configure(command=self.botão_1_3clicado)
        self.botão_1_3.grid(row=0, column=0, sticky="nsew")
        # Botão 21
        self.botão_2_1 = tk.Button(self.window)
        self.botão_2_1.configure(command=self.botão_2_1clicado)
        self.botão_2_1.grid(row=2, column=1, sticky="nsew")
        # Botão 22
        self.botão_2_2 = tk.Button(self.window)
        self.botão_2_2.configure(command=self.botão_2_20clicado)
        self.botão_2_2.grid(row=2, column=2, sticky="nsew")
        # Botão 23 
        self.botão_2_3 = tk.Button(self.window)
        self.botão_2_3.configure(command=self.botão_2_3clicado)
        self.botão_2_3.grid(row=2, column=3, sticky="nsew")
        # Botão 31
        self.botão_3_1 = tk.Button(self.window)
        self.botão_3_1.configure(command=self.botão_3_1clicado)
        self.botão_3_1.grid(row=3, column=1, sticky="nsew")
        # Botão 32
        self.botão_3_2 = tk.Button(self.window)
        self.botão_3_2.configure(command=self.botão_3_2clicado)
        self.botão_3_2.grid(row=3, column=2, sticky="nsew")
        # Botão 33
        self.botão_3_3 = tk.Button(self.window)
        self.botão_3_3.configure(command=self.botão_3_3clicado)
        self.botão_3_3.grid(row=3, column=3, sticky="nsew")
        
        # Definindo label
        self.label = tk.Label(self.window)
        self.label.grid(row = 0, column = 0, columnspan=3)
        if self.jogador == 'X':
            self.label.configure(text = "X, é a sua vez")
        if self.jogador == 'O':
            self.label.configure(text = "O, é a sua vez")
        # Definindo botôes
        #self.matriz = np.zeros((3,3))
        
        
    def iniciar(self):
        self.window.mainloop() 
        
    def joga_X(self):
        self.label.configure(text = "X, é a sua vez")
        
        
jogo = tabuleiro()
jogo.iniciar()