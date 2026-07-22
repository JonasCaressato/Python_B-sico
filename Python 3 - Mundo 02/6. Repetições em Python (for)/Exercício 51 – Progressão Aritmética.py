"""
Enunciado Exercício 51 – Progressão Aritmética

Desenvolva um programa que leia o primeiro termo
e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""

termo_da_progressao_aritmetica = int(input('Digite o primerio termo de uma Progressão aritmética: '))
razao = int(input('Digite a Razão da progressão aritmética: '))

for contador in range(1,11):
    print(f'{contador}° termo da PA = {termo_da_progressao_aritmetica}')
    termo_da_progressao_aritmetica += razao
