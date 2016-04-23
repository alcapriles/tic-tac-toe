# -*- coding: utf-8 -*-
import tkinter as tk
import numpy as np
class Tabuleiro:
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
        
        # definindo botôes
        for i in range(1,4):
            for j in range(3):
                self._fazer_botao(i,j)

        # Definindo label
        self.label = tk.Label(self.window)
        self.label.grid(row = 0, column = 0, columnspan=3)
        self.label.configure(font="Courier 20 bold")
        self.label.configure(text = "Jogo da Velha")   

    def _fazer_botao(self, linha, coluna):
        botao = tk.Button(self.window)
        botao.configure(command = lambda: self.botao_clicado(linha, coluna, botao))
        botao.grid(row=linha, column=coluna, sticky="nsew")

        

    # Definindo funções da classe 
    # Função iniciar
    def iniciar(self):
        self.window.mainloop() 
    # Função label, precisa melhorar    
    def preenche_label(self, letra):
        print("Label funciona para: {0}".format(letra))
   #    self.jogador == 'X':
   #        self.label.configure(font="Courier 20 bold")
   #        self.label.configure(text = "X, é a sua vez")
   #    if self.jogador == 'O':
   #        self.label.configure(font="Courier 20 bold")
   #        self.label.configure(text = "O, é a sua vez")
   # Função dos botões
    def botao_clicado(self, i, j, botao):
        print('Botão {0}, {1} clicado'.format(i, j))
        botao.configure(font="Courier 35 bold")
        botao.configure(text = "x")
        botao.configure(state = "disabled")

jogo = Tabuleiro()
jogo.iniciar()