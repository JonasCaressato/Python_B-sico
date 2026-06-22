"""
Enunciado Exercício 25 – Procurando uma string dentro de outra

Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""

nome = input('Nome completo: ').upper()

if nome.find('SILVA') != -1:
    print('Há SILVA no seu nome!!!')
else:
    print('Não há SILVA no seu nome!!!')