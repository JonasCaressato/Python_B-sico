"""
Enunciado Exercício 85 – Listas com pares e ímpares

Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
from numpy.ma.core import append

numeros = []
numeros_impares = []
numeros_pares = []

for cont in range(1,8):
    valor = int(input(f'Digite o {cont}° valor: '))

    if valor % 2 == 0:
        numeros_pares.append(valor)
    else:
        numeros_impares.append(valor)

numeros_pares.sort()
numeros_impares.sort()
numeros = numeros_impares,numeros_pares

print(numeros[0], numeros[1])
print(f'números ímpares: {numeros[0]}')
print(f'números pares: {numeros[1]}')