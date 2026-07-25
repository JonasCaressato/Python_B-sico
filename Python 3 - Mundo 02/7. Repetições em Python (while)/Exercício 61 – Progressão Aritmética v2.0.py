"""
Enunciado Exercício 61 - Progressão Aritmética v2.0.py

 Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
 mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

termo_da_progressao_aritmetica = int(input('Digite o primerio termo de uma Progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
contador = 1

while contador < 11:
    print(f'O {contador}° termo da PA: {termo_da_progressao_aritmetica}')
    termo_da_progressao_aritmetica += razao
    contador += 1
