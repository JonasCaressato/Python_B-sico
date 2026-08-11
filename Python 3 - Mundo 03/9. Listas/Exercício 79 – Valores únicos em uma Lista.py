"""
Enunciado Exercício 79 – Valores únicos em uma Lista

Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

lista_numerica = []

while True:

    #Obtendo valores
    print('Caso deseje encerrar o programa digite [0]')
    numero = int(input('Digite um número qualquer: '))

    #Verificando a condição para encerrar o programa
    if numero == 0:
        print('Encerrando o programa!')
        break

    #Verificando e adicionando itens na lista_numerica
    elif numero not in lista_numerica:
        lista_numerica.append(numero)
lista_numerica.sort()
print(f'Todos os valores digitados sem repetição em ordem crescente são: {lista_numerica}')
