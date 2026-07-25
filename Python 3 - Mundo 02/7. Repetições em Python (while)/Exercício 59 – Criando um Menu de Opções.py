"""
Enunciado Exercício 59 – Criando um Menu de Opções

Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

O Seu programa deverá realizar a operação solicitada em cada caso.
"""
import time

valor_01 = int(input('Digite um valor: '))
valor_02 = int(input('Digite outro valor: '))
print('-' * 20)

while True:
    time.sleep(1)
    (print
    ('''    MENU DE OPÇÕES
        
    [ 1 ] somar

    [ 2 ] multiplicar

    [ 3 ] maior

    [ 4 ] novos números

    [ 5 ] sair do programa'''))

    menu = int(input('Digite sua opção: '))

    if menu == 1:
        print('-' * 40)
        time.sleep(1)
        print(f'A soma dos dois valores é igual a: {valor_01 + valor_02}')
    elif menu == 2:
        print('-' * 40)
        time.sleep(1)
        print(f'O produto dos dois números é igual a: {valor_01 * valor_02}')
    elif menu == 3:
        if valor_01 > valor_02:
            print('-' * 40)
            time.sleep(1)
            print(f'O maior valor entre os dois é: {valor_01}')
        elif valor_02 > valor_01:
            print('-' * 40)
            time.sleep(1)
            print(f'O maior valor entre os dois é: {valor_02}')
        else:
            print('-' * 40)
            time.sleep(1)
            print('Os valores são iguais!')
    elif menu == 4:
        print('-' * 40)
        time.sleep(1)
        valor_01 = int(input('Digite um valor: '))
        valor_02 = int(input('Digite outro valor: '))
    elif menu == 5:
        print('-' * 40)
        time.sleep(1)
        print('ENCERRANDO PROGRAMA!')
        time.sleep(1)
        break
