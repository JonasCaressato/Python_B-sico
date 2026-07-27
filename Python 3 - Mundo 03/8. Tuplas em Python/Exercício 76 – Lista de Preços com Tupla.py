"""
Enunciado Exercício 76 – Lista de Preços com Tupla

Crie um programa que tenha uma tupla única com nomes de produtos e os seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

mercadinho = ('Arroz', 20, 'Feijão', 12, 'Ovo', 15)

for n in range(0, len(mercadinho)):
    if n % 2 == 0:
        print(f'{mercadinho[n]} R${mercadinho[n + 1]}')
