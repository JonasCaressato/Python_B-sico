"""
Enunciado do exercício 14 - Conversor de temperatura:

Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
"""

temperatura = float(input("Digite sua temperatura em °C: "))

print(f'A temperatura de {temperatura} °C corresponde a {((temperatura * 9) / 5) + 32}°F')
