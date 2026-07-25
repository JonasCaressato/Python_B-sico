"""
Enunciado Exercício 66 – Vários números com 'Flag'

Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o Flag).
"""

print('Digite números inteiros, caso deseje encerrar o ciclo digite 999')
contador_de_ciclos = 0
total_dos_valores = 0
while True:
    numero = int(input('Digite um número inteiro: '))

    if numero == 999:
        break

    total_dos_valores += numero
    contador_de_ciclos +=1

print(f'Você digitou um total de {contador_de_ciclos}, a soma de todos os números é: {total_dos_valores}')
