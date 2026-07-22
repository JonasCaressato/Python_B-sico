"""
Enunciado Exercício 52 – Números primos

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
print('Descubra se um número é primo!')

numero =int(input('Digite um número inteiro: '))
contador_de_resto_zero = 0

for contador in range (1, numero + 1):
    if numero % contador == 0:
        contador_de_resto_zero += 1

if contador_de_resto_zero == 2 and numero > 1:
    print(f'O número {numero} É PRIMO!')
elif contador_de_resto_zero != 2:
    print(f'O número {numero} NÃO É PRIMO!')

