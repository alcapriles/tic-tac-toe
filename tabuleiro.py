# -*- coding: utf-8 -*-
import tkinter as tk
import numpy as np

class tabuleiro:
    # Definindo a classe
    def __init__(self):
        # Definindo janela
        self.window = tk.Tk()
        self.window.title("Jogo da velha!")
        self.window.geometry("300x350+100+100")
        self.window.rowconfigure(0, minsize=50)
        self.window.rowconfigure(1, minsize=100)
        self.window.rowconfigure(2, minsize=100)
        self.window.rowconfigure(3, minsize=100)
        self.window.columnconfigure(0, minsize=100)
        self.window.columnconfigure(1, minsize=100)
        self.window.columnconfigure(2, minsize=100)
        
        # Definindo botões
        # Botão 10
        self.botão_1_0 = tk.Button(self.window)
        self.botão_1_0.configure(command=self.botão_1_0clicado)
        self.botão_1_0.grid(row=1, column=0, sticky="nsew")
        # Botão 11
        self.botão_1_1 = tk.Button(self.window)
        self.botão_1_1.configure(command=self.botão_1_1clicado)
        self.botão_1_1.grid(row=1, column=1, sticky="nsew")
        # Botâo 12
        self.botão_1_2 = tk.Button(self.window)
        self.botão_1_2.configure(command=self.botão_1_2clicado)
        self.botão_1_2.grid(row=1, column=2, sticky="nsew")
        # Botão 20
        self.botão_2_0 = tk.Button(self.window)
        self.botão_2_0.configure(command=self.botão_2_0clicado)
        self.botão_2_0.grid(row=2, column=0, sticky="nsew")
        # Botão 21
        self.botão_2_1 = tk.Button(self.window)
        self.botão_2_1.configure(command=self.botão_2_1clicado)
        self.botão_2_1.grid(row=2, column=1, sticky="nsew")
        # Botão 22 
        self.botão_2_2 = tk.Button(self.window)
        self.botão_2_2.configure(command=self.botão_2_2clicado)
        self.botão_2_2.grid(row=2, column=2, sticky="nsew")
        # Botão 30
        self.botão_3_0 = tk.Button(self.window)
        self.botão_3_0.configure(command=self.botão_3_0clicado)
        self.botão_3_0.grid(row=3, column=0, sticky="nsew")
        # Botão 31
        self.botão_3_1 = tk.Button(self.window)
        self.botão_3_1.configure(command=self.botão_3_1clicado)
        self.botão_3_1.grid(row=3, column=1, sticky="nsew")
        # Botão 32
        self.botão_3_2 = tk.Button(self.window)
        self.botão_3_2.configure(command=self.botão_3_2clicado)
        self.botão_3_2.grid(row=3, column=2, sticky="nsew")
        
        # Definindo label
        self.label = tk.Label(self.window)
        self.label.grid(row = 0, column = 0, columnspan=3)
        self.label.configure(font="Courier 20 bold")
    #    if self.jogador == 'X':
    #        self.label.configure(text = "X, é a sua vez")
    #    if self.jogador == 'O':
    #        self.label.configure(text = "O, é a sua vez")
        
    # Definindo funções da classe 
    # Função iniciar
    def iniciar(self):
        self.window.mainloop() 
    # Função label, precisa melhorar    
    def joga_X(self):
        self.label.configure(text = "X, é a sua vez")
    # Função dos botões
    def botão_clicado(self, i, j):
        print('Botão {0}, {1} clicado'.format(i, j))
    # Botão 10
    def botão_1_0clicado(self):
        self.botão_clicado(1, 0)
        self.botão_1_0.configure(font="Courier 35 bold")
        self.botão_1_0.configure(text = "x")
        self.botão_1_0.configure(state = "disabled")
    # Botão 11
    def botão_1_1clicado(self):
        self.botão_clicado(1, 1)
        self.botão_1_1.configure(font="Courier 35 bold")
        self.botão_1_1.configure(text = "x")
        self.botão_1_1.configure(state = "disabled")
    # Botão 12
    def botão_1_2clicado(self):
        self.botão_clicado(1, 2)
        self.botão_1_2.configure(font="Courier 35 bold")
        self.botão_1_2.configure(text = "x")
        self.botão_1_2.configure(state = "disabled")
    # Botão 20
    def botão_2_0clicado(self):
        self.botão_clicado(2, 0)
        self.botão_2_0.configure(font="Courier 35 bold")
        self.botão_2_0.configure(text = "x")
        self.botão_2_0.configure(state = "disabled")
    # Botão 21
    def botão_2_1clicado(self):
        self.botão_clicado(2, 1)
        self.botão_2_1.configure(font="Courier 35 bold")
        self.botão_2_1.configure(text = "x")
        self.botão_2_1.configure(state = "disabled")
    # Botão 22
    def botão_2_2clicado(self):
        self.botão_clicado(2, 2)
        self.botão_2_2.configure(font="Courier 35 bold")
        self.botão_2_2.configure(text = "x")
        self.botão_2_2.configure(state = "disabled")
    # Botão 30
    def botão_3_0clicado(self):
        self.botão_clicado(3, 0)
        self.botão_3_0.configure(font="Courier 35 bold")
        self.botão_3_0.configure(text = "x")
        self.botão_3_0.configure(state = "disabled")
    # Botão 31
    def botão_3_1clicado(self):
        self.botão_clicado(3, 1)
        self.botão_3_1.configure(font="Courier 35 bold")
        self.botão_3_1.configure(text = "x")
        self.botão_3_1.configure(state = "disabled")
    # Botão 32
    def botão_3_2clicado(self):
        self.botão_clicado(3, 2)
        self.botão_3_2.configure(font="Courier 35 bold")
        self.botão_3_2.configure(text = "x")
        self.botão_3_2.configure(state = "disabled")
        
jogo = tabuleiro()
jogo.iniciar()