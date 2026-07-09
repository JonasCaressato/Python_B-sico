"""
Enunciado Exercício 37 – Conversor de Bases Numéricas

Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.
"""

numero = int(input('Digite um número inteiro qualquer: '))

# noinspection NonAsciiCharacters
conversão = int(input('Qual será a conversão?: 1 - binário, 2 - octal e 3 - hexadecimal.'))

if conversão == 1:
    print(f'O número {numero} convertido para binário é: {bin(numero)[2:]}.')
elif conversão == 2:
    print(f'O número {numero} convertido para octal é: {oct(numero)[2:]}.')
elif conversão == 3:
    print(f'O número {numero} convertido para hexadecimal é: {hex(numero)[2:]}.')
