"""
Enunciado Exercício 53 – Detetor de Palíndromo

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:

APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""

frase = input('Digite uma frase: ').strip().lower().replace(' ', '')
frase_inversa = ''

for letra in range(len(frase)-1,-1,-1):
    frase_inversa += frase[letra]

print(f'O inverso de {frase} é {frase_inversa}')

if frase == frase_inversa:
    print("A frase digitada é um PALÍNDROMO!")
else:
    print("A frase digitada NÃO é um palíndromo.")
