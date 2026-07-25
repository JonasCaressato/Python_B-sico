"""
Enunciado Exercício 64 – Tratando vários valores v1.0

Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o ‘Flag’).
"""
contador_de_numeros_digitados = 0
soma_de_todos_os_numeros = 0

while True:
    print('-' * 40)
    print('Digite qualquer valor, MAS se deseja parar, então digite: 999')
    numero_digitado = int(input('Digite um número qualquer: '))

    if numero_digitado != 999 or numero_digitado < 999:
        contador_de_numeros_digitados += 1
        soma_de_todos_os_numeros += numero_digitado
    elif numero_digitado == 999:
        break

print(f'Voçê digitou um total de: {contador_de_numeros_digitados} números')
print(f'A soma de todos os números digitados é: {soma_de_todos_os_numeros}')
