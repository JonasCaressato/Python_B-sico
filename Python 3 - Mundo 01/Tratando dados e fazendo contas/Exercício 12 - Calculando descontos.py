"""
calcula desconto de 5% no valor de uma compra
"""

valor = float(input('Digite o Preço do(s) produto(s): $'))
desconto = (valor * 5) / 100

print(f'O produto que custava ${valor}, na promoção de 5% vai custar R${(valor - desconto):.2f}')
