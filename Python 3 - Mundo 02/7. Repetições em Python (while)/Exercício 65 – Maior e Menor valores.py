"""
Enunciado Exercício 65 – Maior e Menor valores

Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

maior_numero = 0
menor_numero = 0
soma_de_todos_numeros = 0
contador_de_ciclos = 0

while True:

    numero = int(input('Digite qualquer número inteiro: '))
    contador_de_ciclos += 1
    soma_de_todos_numeros += numero

    if maior_numero <= 0 and menor_numero <= 0:
        maior_numero = numero
        menor_numero = numero
    else:
        if numero > maior_numero:
            maior_numero = numero
        if numero < menor_numero:
            menor_numero = numero

    opcao_para_continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opcao_para_continuar == 'S':
        continue
    elif opcao_para_continuar == 'N':
        print('Encerrando sistema!')
        break

print(f'O maior número da sequência que voce digitou é: {maior_numero}')
print(f'O menor número da sequência que voce digitou é: {menor_numero}')
print(f'A média de todos os números digitados é: {soma_de_todos_numeros / contador_de_ciclos}')
