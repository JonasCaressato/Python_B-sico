"""
Enunciado Exercício 42 – Analisando Triângulos v2.0

Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
"""

print('Descubra se três retas formam um triângulo')
print('Descunra se ele é EQUILÁTERIO, ISÓCELES  ou ESCALENO')

lado_1 = int(input('Digite a primeira reta: '))
lado_2 = int(input('Digite a segunda reta: '))
lado_3 = int(input('Digite a terceira reta: '))

if lado_1 < lado_2 + lado_3 and lado_2 < lado_1 + lado_3 and lado_3 < lado_2 + lado_1:
    print(f'FORMAM UM TRIANGULO!')
    if lado_1 == lado_2 == lado_3:
        print('É um triângulo EQUILÁTERO!')
    elif lado_1 == lado_2 != lado_3 or lado_1 == lado_3 != lado_2 or lado_2 == lado_3 != lado_1:
        print('É um triangulo ISÓCELES!')
        print(f'Possui os lados: {lado_1} e {lado_2} e {lado_3}')
    elif lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
        print('É um triangulo ESCALENO!')
else:
    print(f'NÃO FORMAM UM TRIANGULO!')
