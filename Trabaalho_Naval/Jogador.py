from Enuns import Tiro
class Jogador:
    def __init__(self,tabuleiro_proprio, tabuleiro_inimigo):
        self.proprio = tabuleiro_proprio
        self.inimigo = tabuleiro_inimigo

    def ler_coordenadas(self):
        linha,coluna = input("Digite as coordenadas: ").split(',')
        linha = int(linha)
        coluna = int(coluna)
        return linha,coluna

    def sua_vez(self):
        while True:
            linha, coluna = self.ler_coordenadas()
            if linha == coluna == -1: # Mostra o nosso tabuleiro
                self.proprio.imprimir_tabuleiro(True)
            elif linha == coluna == -2:# Mostra o tabuleiro inimigo
                self.inimigo.imprimir_tabuleiro(True)
            else: # Atira no tabuleiro inimigo
                if 0<=linha< self.inimigo.altura and 0<= coluna <self.inimigo.largura:
                    tiro = self.inimigo.receber_tiro(linha, coluna)
                    if tiro == Tiro.INVALIDO :
                        print('Coordenada invalida!! Por favor digite outra.')
                    elif tiro == Tiro.ACERTOU or tiro == Tiro.AFUNDOU:
                        print(tiro.value)
                        self.inimigo.imprimir_tabuleiro(False)
                        if self.inimigo.todos_afundaram():
                            return True
                    elif tiro == Tiro.ERROU:
                        print(tiro.value)
                        self.inimigo.imprimir_tabuleiro(False)
                        return False
                else:
                    print('Coordenada invalida!! Por favor digite outra.')


