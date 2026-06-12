"""
Enuciado do exercício 08 - Conversor de Medidas:

Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""
metro = int(input('Uma distância em metros: '))

print(f'A medida de {metro}m corresponde a: ')

print(f'{metro / 1000}km')
print(f'{metro / 100}hm')
print(f'{metro / 10}dam')
print(f'{metro}m')
print(f'{metro * 10}dm')
print(f'{metro * 100}cm')
print(f'{metro * 1000}mm')
