from Enuns import Estados, Tiro, Direcao
import random
from Navio import Navio
class Tabuleiro:
    def __init__(self):
        self.largura = 9
        self.altura = 9
        self.matriz = []
        self.navios =[]
        for _ in range(0,self.altura): #Estrutura do tabuleiro
            self.linha =[]
            for _ in range(0,self.largura): # Aprendi q dá pra usar _ com for
                self.linha.append (Estados.AGUA)
            self.matriz.append(self.linha)
    def imprimir_tabuleiro(self, mostrar_navio= False):
        for linha in self.matriz:
            for item in linha:
                if item == Estados.AGUA:
                        print('w', end=' ')
                elif item == Estados.NAVIO:
                    if mostrar_navio: #Se mostrar navio retornar True, mostra os navios
                        print('o' ,  end=' ')
                    else:
                        print('w', end=' ')
                elif item == Estados.TIRO_NAVIO:
                    print('x', end=' ')
                elif item == Estados.TIRO_AGUA:
                    print('-', end=' ')
            print( )
#################################### Criando Navios no tabuleiro
    def criar_navio(self):
        quant_navios = 6
        while len(self.navios) < quant_navios:
            direcao = random.choice(list(Direcao))#random.choice escolhe 'direções' aleatórias
            navio= Navio()
            if direcao == Direcao.VERTICAL:
                linha = random.randint(0, self.altura - navio.tamanho ) #randint, pega um numero aleatorio entre 0 e 7
                coluna = random.randint(0, self.largura - 1) # 0 e 8
                navio.adicionar_posicao(linha, coluna, direcao)
            else:
                linha = random.randint(0, self.altura - 1) # 0 e 8
                coluna = random.randint(0, self.largura - navio.tamanho) # 0 e 7
                navio.adicionar_posicao(linha, coluna, direcao)

            if not self.sobrepoe(navio):
                self.navios.append(navio)
                for linha,coluna in navio.posicoes:
                    self.matriz[linha][coluna] = Estados.NAVIO
    def sobrepoe(self, novo_navio):
        for navio in self.navios:
            for posicao in novo_navio.posicoes:
                if posicao in navio.posicoes:
                    return True
        return False
############################################## Tabuleiro recebendo tiro
    def receber_tiro(self,linha,coluna):
        if self.matriz[linha][coluna] == Estados.AGUA:
            self.matriz[linha][coluna] = Estados.TIRO_AGUA
            return Tiro.ERROU #Se o tiro for na agua errou
        elif self.matriz[linha][coluna]== Estados.NAVIO:
            self.matriz[linha][coluna] = Estados.TIRO_NAVIO
            for navio in self.navios:
                if navio.posicao_atingida(linha, coluna):
                    if navio.afundou():
                       return Tiro.AFUNDOU
            return Tiro.ACERTOU
        else:
            return Tiro.INVALIDO
################################################# Pra saber se todos os navios afundaram
    def todos_afundaram(self):
        for navio in self.navios:
            if not navio.afundou():
                return False
        return True
###################################################### FUNCIONA



















