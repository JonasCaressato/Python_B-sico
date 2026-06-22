"""
Enunciado Exercício 28 - Jogo da adivinhação v.1.0

Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

#importações
import random
import time

#Pensando em um número
print(f'Pensando em um número inteiro entre 0 e 5...')
time.sleep(2)
numero_aleatorio = random.randint(0, 5)

print('Pensei!!!')
numero_do_jogador = int(input('Tente adivinhar o número: '))

if numero_do_jogador == numero_aleatorio:
    print('Parabéns, voçê consegui adivinhar!')
else:
    print(f'Voce errou! voce digitou: {numero_do_jogador}, enquanto eu pensei no número {numero_aleatorio} ')
