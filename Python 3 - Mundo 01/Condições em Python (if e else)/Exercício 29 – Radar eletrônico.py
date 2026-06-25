"""
Enunciado Exercício 29 – Radar eletrônico

Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

#Recebendo a velocidade
velocidade = int(input('Qual a velocidade do carro? '))

#Condição de multa
if velocidade > 80:
    print('VOCÊ FOI MULTADO!')
    velocidade_de_cobrança = velocidade - 80
    print(f'O valor da multa é de {velocidade_de_cobrança * 7}R$')
else:
    print(f'VOCÊ NÃO FOI MULTADO!')
