"""
Enunciado do exercício 11 - Pintando parede:

Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

print (f'Sua parede tem dimensão de {largura} x {altura}, sua área total é de: {largura * altura}m²')
print(f'Você precisará de {(largura * altura) * 0.15}l de tinta')
