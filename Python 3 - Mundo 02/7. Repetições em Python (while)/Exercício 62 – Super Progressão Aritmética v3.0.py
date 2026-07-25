"""
Enunciado Exercício 62 – Super Progressão Aritmética v3.0

Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""
#Obtendo Termo e Razão
termo_da_progressao_aritmetica = int(input('Digite o primerio termo de uma Progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))

#Valores utilizados para verificar condições
contador = 1
limite_de_termos = 11
adicao_de_termos = 1

#Somando os termos utilizando while
while True:

    print(f'O {contador}° termo da PA: {termo_da_progressao_aritmetica}')
    termo_da_progressao_aritmetica += razao
    contador += 1

    if contador >= limite_de_termos:

        print('-' * 40)
        print('Deseja ver mais termos dessa PA?')
        print('Digite 1 para mais 1 termo, 2 para mais 2 termos...')
        print('Digite 0 se não deseja ver mais nenhum termo')
        print('-' * 40)
        adicao_de_termos = int(input('Deseja ver mais quantos termos dessa PA? '))
        limite_de_termos += adicao_de_termos

        if adicao_de_termos == 0:
            break
