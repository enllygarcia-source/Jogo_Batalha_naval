from Enuns import Direcao
class Navio:
    def __init__(self):
        self.tamanho = 2
        self.posicoes = [0,0]
        self.atingiu = []
    def adicionar_posicao(self, linha, coluna, direcao):
        self.posicoes = []
        if direcao == Direcao.VERTICAL: # Se a posição for vertical
            for i in range(self.tamanho):# Adiciona 2 posições, uma em cima/baixo da outra
                prox_posicao_v = linha + i
                self.posicoes.append((prox_posicao_v, coluna)) #dois parênteses, pois o append não funciona em mais de um item
                # E com um parênteses a mais, oq estiver dentro dele é considerado 1 ‘item’
        else:
            for i in range(self.tamanho): # Se a posição for horizontal
                prox_posicao_h = coluna +i # Adiciona 2 posições, uma do lado da outra
                self.posicoes.append((linha,prox_posicao_h ))

    def posicao_atingida(self, linha, coluna):# Fazer de forma q o jogador não atinja a mesma posição duas vezes
        if (linha,coluna) in self.posicoes and (linha,coluna) not in self.atingiu: # Se a posição não foi atingida
            self.atingiu.append((linha,coluna))# Atinge
            return True
        return False

    def afundou(self): #Se atingiu 2 espaços o navio afunda
        return len(self.atingiu) == self.tamanho

















