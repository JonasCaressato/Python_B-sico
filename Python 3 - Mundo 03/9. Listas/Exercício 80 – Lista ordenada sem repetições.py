"""
Enunciado Exercício 80 – Lista ordenada sem repetições

Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
lista = []
for _ in range(5):
    n = int(input('digite o número: '))
    inicio, fim = 0, len(lista)
    while inicio < fim:
        meio = (inicio + fim) // 2
        if n < lista[meio]:
            fim = meio
        else:
            inicio = meio + 1
    lista.insert(inicio, n)
print(lista)
