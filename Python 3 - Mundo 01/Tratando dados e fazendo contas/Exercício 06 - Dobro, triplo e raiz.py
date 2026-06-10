"""
Recebe um valor int e nos mostra o Dobro, Triplo e Raiz Quadrada
"""


import math

numero = int(input('Digite algo: '))

print(f'O dobro de {numero} vale: {numero *2}')
print(f'O triplo de {numero} vale: {numero *3}')
print(f'A raiz de {numero} vale: {math.sqrt(numero):.2f}')
