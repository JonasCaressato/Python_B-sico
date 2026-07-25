"""
Enunciado Exercício 63 – Sequência de Fibonacci v1.0

Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8
"""

n = int(input('Digite um número inteiro: '))

primeiro_termo = 0
segundo_termo = 1

contador = 2

print(primeiro_termo)
print(segundo_termo)

while contador < n:

    #Mostrando a sequencia de Fibonacci
    fibonacci = primeiro_termo + segundo_termo
    print(fibonacci)

    #Trocando os termos para realizar a operação de soma
    primeiro_termo = segundo_termo
    segundo_termo = fibonacci

    #Contador para o término do while
    contador += 1