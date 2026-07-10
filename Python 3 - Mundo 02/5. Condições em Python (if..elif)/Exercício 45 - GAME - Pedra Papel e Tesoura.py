"""
Enunciado Exercício 45 – GAME: Pedra Papel e Tesoura

Crie um programa que faça o computador jogar Jokenpô com você.
"""

import random

print('JOKENPO!!!')

print('[1] - Pedra')
print('[2] - Papel')
print('[3] - Tesoura')

player = int(input('Escolha a sua jogada: '))

bot = random.randint(1, 3)
