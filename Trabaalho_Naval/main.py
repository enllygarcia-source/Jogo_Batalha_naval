from Tabuleiro import Tabuleiro
from Jogador_pc import Pc
from Jogador import Jogador
def jogar():
    meu_tabuleiro= Tabuleiro()
    tabuleiro_pc = Tabuleiro()
    meu_tabuleiro.criar_navio()
    tabuleiro_pc.criar_navio()
    user = Jogador(meu_tabuleiro, tabuleiro_pc)
    pc = Pc(tabuleiro_pc, meu_tabuleiro)
    while True:
        turno_pc = pc.sua_vez()
        if turno_pc :
            print('Mais sorte na prox!!')
            break
        turno_user = user.sua_vez()
        if turno_user:
            print('Tu venceu fi, congratulations!!')
            break
while True:
    jogar()
    reiniciar = input('Jogar novamente?').strip().upper()
    if reiniciar == 'NÃO' or reiniciar == 'NAO' or reiniciar== 'N':
        print("Ok, agradeço a jogatina")
        break
