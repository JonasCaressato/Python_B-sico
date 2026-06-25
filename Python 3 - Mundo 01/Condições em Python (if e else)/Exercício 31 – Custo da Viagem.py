"""
Enunciado Exercício 31 – Custo da Viagem

Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""

#Recebendo a quilometragem
quilometragem = float(input('Quantos quilometros tem a viagem? '))

#Condição de valor(R$) da viagem
if quilometragem <= 200:
    valor_de_viagem = quilometragem * 0.50
    print(f'A viagem de {quilometragem}KM vai custar R${valor_de_viagem:.2f}')
else:
    valor_de_viagem = quilometragem * 0.45
    print(f'A viagem de {quilometragem}KM vai custar R${valor_de_viagem:.2f}')
