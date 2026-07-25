"""
Enunciado Exercício 71 – Simulador de Caixa Eletrônico

Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
contador_1 = 0
contador_10 = 0
contador_20 = 0
contador_50 = 0

valor_do_saque = int(input('Valor do saque: '))

while True:

    if valor_do_saque >= 50:
        valor_do_saque -= 50
        contador_50 += 1
        continue
    elif valor_do_saque >= 20:
        valor_do_saque -= 20
        contador_20 += 1
        continue
    elif valor_do_saque >= 10:
        valor_do_saque -= 10
        contador_10 += 1
        continue
    elif valor_do_saque >= 1:
        valor_do_saque -= 1
        contador_1 += 1
        continue
    elif valor_do_saque == 0:
        break

print(f'Total de notas de R$50: {contador_50}')
print(f'Total de notas de R$20: {contador_20}')
print(f'Total de notas de R$10: {contador_10}')
print(f'Total de notas de R$1: {contador_1}')