"""
Enunciado Exercício 58 – Jogo da Adivinhação v2.0

Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Contudo, agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""

import random
import time

print('Irei pensar em um número entre 0 e 10, tente adivinhar!')
print('Pensando...')
time.sleep(3)

numero_aleatorio = random.randint(0, 10)

while True:
    resposta =  int(input('Diga seu palpite: '))

    if resposta == numero_aleatorio:
        print(f'Parabéns, pensei exatamente no número {numero_aleatorio}!')
        break
    else:
        print(f'Errou!\nNão pensei no número: {resposta} \nTente novamente!')
