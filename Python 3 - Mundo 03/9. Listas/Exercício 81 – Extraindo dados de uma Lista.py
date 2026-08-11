"""
Enunciado Exercício 81 – Extraindo dados de uma Lista

Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

print('Digite 0 para encerrar o programa!')
numeros = []

while True:
    num = int(input('Digite um número: '))

    if num == 0:
        break
    else:
        numeros.append(num)

numeros.sort(reverse=True)

print(f'Foram digitados um total de: {len(numeros)} valores!')
print(f'Essa é lista ordenada de forma decrescente:\n {numeros}')
print('O número 5 foi digitado' if 5 in numeros else 'O número 5 não aparece na lista')