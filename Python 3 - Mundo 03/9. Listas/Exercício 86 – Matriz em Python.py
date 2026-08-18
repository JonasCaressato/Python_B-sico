"""
Enunciado Exercício 86 – Matriz em Python

Crie um programa que declare uma matriz de dimensão 3 × 3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""

#Lendo valores pelo teclado e declarando na matriz 3x3
matriz = []

for cont in range (1,10):
    matriz.append((int(input(f'Declare o {cont}° valor da matriz: '))))

#Mostrando os valores em forma de matriz
for i in range(3):

    for j in range(3):
        print(matriz[0], end=' ')
        matriz.pop(0)
    print('\n')
