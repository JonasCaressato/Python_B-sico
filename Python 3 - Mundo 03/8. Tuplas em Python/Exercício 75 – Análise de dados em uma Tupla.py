"""
Enunciado Exercício 75 – Análise de dados em uma Tupla

Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
"""
#Definindo variáveis
contador_de_9 = 0

#Lendo quatro valores
minha_tupla = (
    int(input('Digite o primeiro valor: ')),
    int(input('Digite o segundo valor: ')),
    int(input('Digite o terceiro valor: ')),
    int(input('Digite o quarto valor: '))
)

#Contagem de 9's
for n in range (0,4):
    if minha_tupla[n] == 9:
        contador_de_9 += 1
print(f'Há um total de {contador_de_9} número(s) 9 que você digitou!')

#Posição do primeiro número 3
print(f'O 1° número 3 aparece na posição: {minha_tupla.index(3)} da tupla!')

#Mostrando os números pares
print('Esses são os números pares que você digitou: ')
for n in range(0, 4):
    if minha_tupla[n] % 2 == 0:
        print(minha_tupla[n])
