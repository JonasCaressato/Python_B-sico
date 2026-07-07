"""
Enucniado do exercício 06 - Dobro, Triple, Raiz:

Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""


import math

numero = int(input('Digite algo: '))

print(f'O dobro de {numero} vale: {numero *2}')
print(f'O triplo de {numero} vale: {numero *3}')
print(f'A raiz de {numero} vale: {math.sqrt(numero):.2f}')
