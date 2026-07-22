"""
Enunciado Exercício 54 – Grupo da Maioridade

Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

contador_de_maioridade = 0
contador_de_menoridade = 0

for pessoa in range(1, 8):
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        contador_de_maioridade += 1
    else:
        contador_de_menoridade += 1

print(f'{contador_de_maioridade} já atingiram a maioridade!')
print(f'{contador_de_menoridade} ainda são de menoridade!')