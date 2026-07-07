"""
Enunciado Exercício 26 – Primeira e última ocorrência de uma string

Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
"""

#Lendo a frase pelo teclado
frase = str(input('Diga uma frase: ')).strip().upper()

#Contagem de letras "A"
quantidade_de_letras_A = frase.count('A')

#Posição em que a letra "A" aparece pela 1° vez
aparicao_da_letra_A = frase.find('A')

#Posição em que a letra "A" aparece pela última vez
ultima_letra_A = frase.rfind('A')

contagem_de_espaços = frase.count(' ')

print(f'A quantidade de letras "A" que aparece na frase é: {quantidade_de_letras_A}')
print(f'A primeira aparição da letras "A" é: {aparicao_da_letra_A + 1}')
print(f'A ultima aparição da letra "A" é: {(ultima_letra_A + 1) - contagem_de_espaços}')
