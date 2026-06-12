"""
Enuciado do exercício 10 - Conversor de Moedas:

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
"""

dinheiro = float(input('Quanto dinheiro você tem na carteira?: $'))

print(f'Com ${dinheiro} você pode comprar US$ {dinheiro / 5.19:.2f}')