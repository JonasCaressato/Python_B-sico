"""
Enunciado Exercício 49 – Tabuada v.2.0

Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
mas, agora utilizando um laço for.
"""
numero_da_tabuada = int(input('Digite um número que queira ver a tábuada: '))

for contador in range (1, 11):
    print(f'{numero_da_tabuada} x {contador} = {numero_da_tabuada * contador}')
