"""
Enunciado do exercício 12 - Calculando descontos:

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

valor = float(input('Digite o Preço do(s) produto(s): $'))
desconto = (valor * 5) / 100

print(f'O produto que custava ${valor}, na promoção de 5% vai custar R${(valor - desconto):.2f}')
