"""
Enunciado Exercício 38 – Comparando números

Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
"""

print('Descubra qual valor é maior ou se são iguais')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

if n1 > n2:
    print(f'O primeiro valor ({n1}) é maior')
elif n2 > n1:
    print(f'O segundo valor ({n2}) é maior')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais')
