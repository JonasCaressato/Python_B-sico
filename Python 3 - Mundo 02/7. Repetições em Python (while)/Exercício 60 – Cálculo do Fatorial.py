"""
Enunciado Exercício 60 – Cálculo do Fatorial

Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120
"""

# Lê o número digitado pelo usuário
n = int(input("Digite um número: "))

# Variáveis iniciais
c = n
fatorial = 1

print(f"{n}! = ", end="")

# Laço while para calcular o fatorial e mostrar os termos
while c > 0:
    print(c, end="")
    print(" x " if c > 1 else " = ", end="")
    fatorial *= c
    c -= 1

print(fatorial)
