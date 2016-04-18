import numpy as np

class Jogo:
	def __init__(self):b
		self.jogador = 'X' 
		self.tabuleiro = np.zeros((3,3))

	def recebe_jogada(linha,coluna):
		self.tabuleiro[linha, coluna] = self.jogador
		if self.jogador == 'X':
			self.jogador = 'O'
		else:
			self.jogador = 'X'

    def verifica_ganhador():
	#retorna 0 em caso de empate
	#retorna 1 se X for o vencedor
	#retorna 2 se O for o vencedor
	#retorna -2 se nenhuma das anteriores for verdadeira

	def limpa_jogadas():
	#reinicia o jogo mantendo a vez do jogador