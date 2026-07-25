"""
Enunciado Exercício 68 – Jogo do Par ou Ímpar

Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
import random
import time
contagem_de_vitorias = 0
while True:

    #Opção de escolha do jogador entre par ou impar
    player_opcao_1 = str(input('Par ou Impar? [P / I]'))
    if player_opcao_1 == 'P':
        bot_opcao_1 = 'I'
    elif player_opcao_1 == 'I':
        bot_opcao_1 = 'P'

    #digitando um valor e sorteando um valor aleatório para o 'Bot'
    print('Pensando em um número...')
    bot_opcao_2 = random.randint(0,10)
    time.sleep(2)

    player_opcao_2 = int(input('Digite um número entre 0 e 10: '))

    #Verificando se é Par ou Impar
    soma_das_jogadas = player_opcao_2 + bot_opcao_2

    if player_opcao_1 == 'P':
        if soma_das_jogadas % 2 == 0:
            print('Você ganhou!!!')
            print(f'Player = {player_opcao_2} bot = {bot_opcao_2}; a soma é: {soma_das_jogadas} ')
            contagem_de_vitorias += 1
        else:
            print('Você perdeu!!!')
            print(f'Player = {player_opcao_2} bot = {bot_opcao_2}; a soma é: {soma_das_jogadas} ')
            break

    elif player_opcao_1 == 'I':
        if soma_das_jogadas % 2 == 0:
            print('Você perdeu!!!')
            print(f'Player = {player_opcao_2} bot = {bot_opcao_2}; a soma é: {soma_das_jogadas} ')
            break
        else:
            print('Você ganhou!!!')
            print(f'Player = {player_opcao_2} bot = {bot_opcao_2}; a soma é: {soma_das_jogadas} ')
            contagem_de_vitorias += 1

print(f'Você ganhou {contagem_de_vitorias} vezes')
