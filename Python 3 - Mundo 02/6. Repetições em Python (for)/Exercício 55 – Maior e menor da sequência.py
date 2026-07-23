"""
Enunciado Exercício 55 – Maior e menor da sequência

Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
#Definição dos pesos base
maior_peso = 0
menor_peso = 0

for pessoa in range(1,6):
    peso = float(input('Qual o seu peso? '))

    #Definindo o primeiro peso lido como menor e maior peso
    if maior_peso <= 0 and menor_peso <= 0:
        maior_peso = peso
        menor_peso = peso

    #Comparando valores e definindo qual o maior e o menor peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print(f'O MAIOR peso digitado é: {maior_peso:.2f}')
print(f'O MENOR peso digitado é: {menor_peso:.2f}')
