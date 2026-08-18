"""
Enunciado Exercício 84 – Lista composta e análise de dados

Faça um programa que leia nome e peso de várias pessoas, guardando tudo numa lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com a pessoa mais pesada.
C) Uma listagem com a pessoa mais leve.
"""

dados_completos = []
mais_pesada = 0
mais_leve = 0
while True:

    #Obtendo dados
    nome = input('Digite seu nome/(sair): ').strip().lower()

    #Confirmação de saida
    if nome == 'sair':
        break

    peso = float(input(f'Peso de {nome}: KG'))

    #sublista
    dados_individuais = [nome, peso]

    #Lista aninhada
    dados_completos.append(dados_individuais)

for i, v in enumerate(dados_completos):
    if i == 0:
        mais_pesada = i
        mais_leve = i

    else:
        if v[1] > dados_completos[mais_pesada][1] :
            mais_pesada = i
        if v[1] <dados_completos[mais_leve][1]:
            mais_leve = i

#Mostrando os dados
print(f'Há um total de {len(dados_completos)} pessoas cadastradas!')
print(f'A pessoa mais pesada é: {dados_completos[mais_pesada][0]}, com {dados_completos[mais_pesada][1]}KG')
print(f'A pessoa mais leve é: {dados_completos[mais_leve][0]}, com {dados_completos[mais_leve][1]}KG')