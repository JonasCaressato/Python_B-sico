"""
Enunciado Exercício 50 – Soma dos pares

Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

print('Soma de números pares!')

soma_dos_numero_pares = 0

for c in range (1, 7):
    numero = int(input(f'Digite o {c}° número inteiro: '))
    if numero % 2 == 0:
        soma_dos_numero_pares += numero
print(f'A soma de todos os números pares digitados são: {soma_dos_numero_pares}')
