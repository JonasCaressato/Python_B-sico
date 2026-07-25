"""
Enunciado Exercício 67 – Tabuada v3.0

Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""
print('Digite um valor e veja a sua tabuda!')
n = int(input('Digite um número inteiro: '))
contador_de_ciclo = 0

while True:
    contador_de_ciclo += 1

    print(f'{n} x {contador_de_ciclo} = {n * contador_de_ciclo}')

    if contador_de_ciclo == 10:
        print('Caso deseje encerrar, digite um número negativo!')
        n = int(input('Digite um número para ver a tabuada: '))
        contador_de_ciclo = 0
        if n < 0:
            print('Encerrando o programa!')
            break
