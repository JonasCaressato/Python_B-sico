"""
Enunciado Exercício 27 – Primeiro e último nome de uma pessoa

Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
"""

#Leitura do nome completo
nome_completo = input('Diga seu nome completo: ').strip()

#Descobrindo o primeiro nome
primeiro_nome = nome_completo.find(' ')

#Descobrindo o ultimo nome
ultimo_nome = nome_completo.rfind(' ')

print(f'Seu nome completo é: {nome_completo}')
print(f'Seu primeiro nome é: {nome_completo[:primeiro_nome]}')
print(f'Seu último nome é : {nome_completo[ultimo_nome:]}')
