"""
Enunciado Exercício 30 – Par ou Ímpar?

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

#Recebendo um número inteiro
numero = int(input('Digite um número inteiro: '))

#Condição Ímpar ou Par
if numero % 2 == 0:
    print(f'O número {numero} é Par!')
else:
    print(f'O número {numero} é Impar!')
