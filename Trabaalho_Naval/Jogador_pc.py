from Enuns import Tiro
import random
class Pc:
    def __init__(self,tabuleiro_proprio, tabuleiro_inimigo):
        self.proprio = tabuleiro_proprio
        self.inimigo = tabuleiro_inimigo
        self.tiros_dados = []
    def coordenadas(self):
        linha = random.randint(0, self.inimigo.altura - 1)
        coluna = random.randint(0, self.inimigo.largura - 1)
        while (linha, coluna) in self.tiros_dados: #Pra num repetir a coordenada
            linha = random.randint(0, self.inimigo.altura - 1)
            coluna = random.randint(0, self.inimigo.largura - 1)
        self.tiros_dados.append((linha,coluna))
        return linha, coluna

    def sua_vez(self):
        while True:
            linha, coluna = self.coordenadas()
            tiro = self.inimigo.receber_tiro(linha, coluna)
            print(f'Tiro em {linha, coluna} = {tiro.value}')
            if tiro == Tiro.ACERTOU or tiro == Tiro.AFUNDOU:
                print(tiro.value)
                if self.inimigo.todos_afundaram():
                    return True
            elif tiro == Tiro.ERROU:
                return False



