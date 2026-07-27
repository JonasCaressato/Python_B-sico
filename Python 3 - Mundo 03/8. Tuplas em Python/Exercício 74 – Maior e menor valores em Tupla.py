"""
Enunciado Exercício 74 – Maior e menor valores em Tupla

Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
import random
menor_valor = 0
maior_valor = 0
#Gerando cinco números aleatórios
numeros_aleatorios = tuple(random.sample(range(0,100), 5))

#Mostrando os números gerados
print('Os número aleatórios são: ')
for n in range(0, 5):
    print(numeros_aleatorios[n])


    #Menor valor na tupla
    if n == 0:
        menor_valor = numeros_aleatorios[0]
    elif numeros_aleatorios[n] < menor_valor:
        menor_valor = numeros_aleatorios[n]

    #Maior valor na Tupla
    if n == 0:
        maior_valor = numeros_aleatorios[0]
    elif numeros_aleatorios[n] > maior_valor:
        maior_valor = numeros_aleatorios[n]

print('-' * 40)
print(f'O menor valor da lista aletória é: {menor_valor}')
print('-' * 40)

print(f'O maior valor da lista aletória é: {maior_valor}')
print('-' * 40)