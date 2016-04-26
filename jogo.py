# -*- coding: utf-8 -*-
import numpy as np

class Jogo:
    def __init__(self):
        self.jogador = 'X' 
        self.tabuleiro = np.array([['', '', ''], ['', '', ''], ['', '', '']])

    def recebe_jogada(self, linha, coluna):
        if self.tabuleiro[linha,coluna] == '':
            self.tabuleiro[linha, coluna] = self.jogador
            if self.jogador == 'X':
                self.jogador = 'O'
            else:
                self.jogador = 'X'

    def verifica_ganhador(self):
        if self._checar('X'):
            return 1
        if self._checar('O'):
            return 2
        empate = True
        for i in range(3):
            for j in range(3):
                empate = empate and self.tabuleiro[i,j]
        if empate:
            return 0
        return -1


    def _checar(self, jogador):
        for i in range(3):
            w = True
            for j in range(3):
                w = w and (self.tabuleiro[i,j] == jogador)   
            if w:
                return w
        
            for j in range(3):
                w = w and (self.tabuleiro[j,i] == jogador)
            if w:
                return w
            
        w = True    
        for i in range(3):
            w = w and (self.tabuleiro[i,i] == jogador)
        if w:
            return w
        
        w = True
        for i in range(3):
            w = w and (self.tabuleiro[i, 2-i] == jogador)
        return w

    def limpa_jogadas():
        self.tabuleiro = np.array([['', '', ''], ['', '', ''], ['', '', '']])