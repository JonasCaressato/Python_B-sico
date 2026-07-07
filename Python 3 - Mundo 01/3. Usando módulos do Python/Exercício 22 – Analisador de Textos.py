"""
Enunciado Exercício 22 – Analisador de Textos

Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.
"""

nome = input('Digite seu nome completo: ')

print(f'Seu nome em maiuscula é: {nome.upper()}')

print(f'Seu nome em minuscula é: {nome.lower()}')

#len conta todos os caracteres e o count vai contar todos os espaços
print(f'O seu nome contém: {len(nome) - nome.count(' ')} letras')

#a função find retorna o indice ao encontrar a string desejada
print(f'Seu primeiro nome tem: {nome.find(' ')} letras')
