"""
Enunciado Exercício 23 – Separando dígitos de um número

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""

n = int(input('Digite um número entre 0 a 9999: '))
numero = str(n)

print(f'UNIDADE: {numero[3]}')
print(f'DEZENA: {numero[2]}')
print(f'CENTENA: {numero[1]}')
print(f'MILHAR: {numero[0]}')
