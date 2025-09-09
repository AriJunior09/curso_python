"""
CONSTANTES = Variáveis que não vão mudar de valor
Muitas condições no mesmo if (ruim)
. . . <- Contagem de complexidade (ruim)
"""

velocidade = 60     # velocidade atual do carro
trecho_carro = 99   # local em que o carro está na estrada


RADAR_1 = 60        # velocidade máxima do radar 1
LOCAL_1 = 100       # local onde o radar 1 está
RADAR_RANGE = 1     # a distância onde o radar pega


if velocidade > RADAR_1 and \
    trecho_carro in range((LOCAL_1 - RADAR_RANGE), \
                          (LOCAL_1 + RADAR_RANGE + 1)):
    print(f'Você foi multado!, A velocidade máxima na via era {RADAR_1}')
else:
    print('Carro não está no range do radar!')