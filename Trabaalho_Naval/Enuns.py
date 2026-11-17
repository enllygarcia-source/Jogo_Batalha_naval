# Pesquisando sobre:
from enum import Enum
class Direcao(Enum):
    VERTICAL = 1
    HORIZONTAL = 2
class Estados(Enum):
    AGUA='AGUA'
    TIRO_AGUA='TIRO_AGUA'
    TIRO_NAVIO='TIRO_NAVIO'
    NAVIO='NAVIO'
class Tiro(Enum):
    ACERTOU = 'ACERTOU'
    AFUNDOU = 'AFUNDOU'
    ERROU= 'ERROU'
    INVALIDO = 'REPETIDO'

#Serve pra manter uma melhor organização (pro código ficar mais entendivel)