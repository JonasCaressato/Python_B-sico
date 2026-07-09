"""
Enunciado Exercício 36 – Aprovando Empréstimo

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

valor_da_casa = float(input("Digite o valor da casa: "))
salario_do_comprador = float(input('Digite o seu salário(R$) mensal: '))
parcelamento = int(input('Em quantas parcelas será pago: '))

#Valor das parcelas <= limite de 30% do salário
if (valor_da_casa / parcelamento) <= (salario_do_comprador / 10) * 3:
    print(f'O empréstimo bancario para a compra dp imóvel de R${valor_da_casa:.2f} foi APROVADO!')
else:
    print(f'O empréstimo bancario para a compra dp imóvel de R${valor_da_casa:.2f} foi NEGADO!')

