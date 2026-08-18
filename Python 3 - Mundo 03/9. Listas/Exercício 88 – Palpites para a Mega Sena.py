"""
Enunciado Exercício 88 – Palpites para a Mega Sena

Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""
from random import randint

quantidade_de_jogos = int(input('Quantos jogos deseja fazer?: '))
jogos = []
jogo_temporario = []

for cont in range(quantidade_de_jogos):
    for v in range (6):
        jogo_temporario.append(randint(1, 60))
    jogos.append((jogo_temporario.copy()))
    jogo_temporario.clear()

print(jogos)

'''
Ao utilizar jogos.append((jogo_temporario.copy())), é reservado dois espaços na memória,
assim é possível interagir com uma sem afetar a outra.

utilizar: jogo = jogos_temporarios.copy() iria fazer com que as duas lista apontassem para o mesmo espaço de memória,
caso interagisse com uma (clear()) a outra também seria afetada.
'''