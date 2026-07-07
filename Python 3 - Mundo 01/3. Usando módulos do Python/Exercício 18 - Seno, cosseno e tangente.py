"""
Enunciado do exercício 18 - Seno, cosseno e em python:

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

import math

angulo_graus = float(input('Digite um ângulo em graus: '))
angulo_radiano = math.radians(angulo_graus)

seno = math.sin(angulo_radiano)
cosseno = math.cos(angulo_radiano)
tangente = math.tan(angulo_radiano)

print(f'O valor de Seno é: {seno:.2f}')
print(f'O valor de cosseno é: {cosseno:.2f}')
print(f'O valor da tangente é: {tangente:.2f}')
