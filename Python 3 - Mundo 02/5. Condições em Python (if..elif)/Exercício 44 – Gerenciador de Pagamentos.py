"""
Enunciado Exercício 44 – Gerenciador de Pagamentos

Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
"""

valor_do_produto = float(input('Digite o valor do produto: '))

print('Escolha uma opção de pagamento:')
print('1 - à vista dinheiro/pix')
print('2 - à vista no cartão')
print('3 - em até 2x no cartão')
print('4 - 3x ou mais no cartão')

opcao_de_pagamento = int(input('Digite sua opção de pagamento: '))

if opcao_de_pagamento == 1:
    print('O produto recebeu 10% de desconto')
    print(f'O produto de R${valor_do_produto} - 10% = R${valor_do_produto - ((valor_do_produto * 10) / 100):.2f}')
elif opcao_de_pagamento == 2:
    print('O produto recebeu 5% de desconto')
    print(f'O produto de R${valor_do_produto} - 5% = R${valor_do_produto - ((valor_do_produto * 5) / 100):.2f}')
elif opcao_de_pagamento == 3:
    print(f'O valor do produto é R${valor_do_produto:.2f}')
elif opcao_de_pagamento == 4:
    print('O produto terá 20% de juros')
    print(f'O produto de R${valor_do_produto} + 20% = R${valor_do_produto + ((valor_do_produto * 20) / 100):.2f}')
