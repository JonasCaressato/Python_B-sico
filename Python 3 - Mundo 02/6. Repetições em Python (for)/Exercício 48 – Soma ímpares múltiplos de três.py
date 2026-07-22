"""
Enunciado Exercício 48 – Soma ímpares múltiplos de três

Faça um programa que calcule a soma entre todos os números que são múltiplos de três
e que se encontram no intervalo de 1 até 500.
"""

total = 0

for numero in range (1, 501):
    if numero % 3 == 0:
        total += numero

print(f'O valor total da soma de todos os Múltiplos de 3 em um intervalo de 500 é: {total} ')
