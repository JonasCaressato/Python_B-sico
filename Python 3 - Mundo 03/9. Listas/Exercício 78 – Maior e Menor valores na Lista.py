"""
Enunciado Exercício 78 – Maior e Menor valores na Lista

Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
lista_numerica = []
maior_numero = 0
menor_numero = 0

for n in range (1,6):
    numero = int(input(f'Digite o {n}° número: '))
    lista_numerica.append(numero)
    if n <= 1:
        maior_numero = numero
        menor_numero = numero
    elif numero > maior_numero:
        maior_numero = numero
    elif numero < menor_numero:
        menor_numero = numero

print(f'O maior número é {maior_numero} e sua sua posição na lista é: {lista_numerica.index(maior_numero) + 1}')
print(f'O menor número é {menor_numero} e sua sua posição na lista é: {lista_numerica.index(menor_numero) + 1}')
