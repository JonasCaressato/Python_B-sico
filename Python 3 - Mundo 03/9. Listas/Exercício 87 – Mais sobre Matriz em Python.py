"""
Enunciado Exercício 87 – Mais sobre Matriz em Python

Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

#Declarando as linhas de uma matriz 3x3
matriz_i1 = []
matriz_i2 = []
matriz_i3 = []

#Lendo valores pelo teclado e declarando na matriz 3x3
for cont in range (1, 11):

    if cont <= 3:
        matriz_i1.append(int(input(f'Digite o {cont}° valor: ')))
    elif 3 < cont <= 6:
        matriz_i2.append(int(input(f'Digite o {cont}° valor: ')))
    elif 6 < cont <=9:
        matriz_i3.append(int(input(f'Digite o {cont}° valor: ')))

#Mostrando a matriz 3x3
print('', matriz_i1,'\n', matriz_i2,'\n', matriz_i3)

#Soma de todos os valores pares
matriz_completa = (matriz_i1, matriz_i2, matriz_i3)
soma_par = 0
for i in matriz_completa:
    for v in i:
        if v % 2 == 0:
            soma_par += v

print(f'A soma de todos os valores pares da matriz é: {soma_par}')

#Soma dos valores da terceira coluna
soma_j3 = matriz_i1[2] + matriz_i2[2] + matriz_i3[2]
print(f'A soma de todos os valores da coluna 3 é: {soma_j3}')

#Maior valor da segunda linha
maior_i2 = max(matriz_i2)
print(f'O maior valor da segunda linha é: {maior_i2}')
