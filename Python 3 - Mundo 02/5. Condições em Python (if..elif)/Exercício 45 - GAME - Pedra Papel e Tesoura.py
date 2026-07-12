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

if player == 1:

    if bot == 1:
        print('VOCÊS EMPATARAM')
        print('Ambos escolheram Pedra')
    elif bot == 2:
        print('VOCÊ PERDEU!')
        print('Você escolheu Pedra e o BOT escolheu Papel')
    elif bot == 3:
        print('VOCÊ VENCEU')
        print('voce escolheu pedra e o BOT escolheu tesoura')

elif player == 2:

    if bot == 1:
        print('VOCÊ VENCEU')
        print('Você escolheu papel e o bot escolheu pedra')
    elif bot == 2:
        print('VOCÊS EMPATARAM')
        print('ambos escolheram papel')
    elif bot == 3:
        print('VOCÊ PERDEU')
        print('você escolheu papel e o bot escolheu tesoura')

elif player == 3:

    if bot == 1:
        print('VOCÊ PERDEU')
        print('você escolheu tesoura e o bot escolheu pedra')
    elif bot == 2:
        print('VOCÊ VENCEU')
        print('você escolheu tesoura e o bot escolheu papel')
    elif bot == 3:
        print('VOCÊS EMPATARAM')
        print('ambos escolheram papel')
else:
    print('JOGADA INVALIDA, REINICIE O JOGO!!!')
