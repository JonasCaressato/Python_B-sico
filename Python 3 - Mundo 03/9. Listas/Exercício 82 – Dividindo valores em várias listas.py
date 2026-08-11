"""
Enunciado Exercício 82 – Dividindo valores em várias listas

Crie um programa que vai ler vários números e colocar numa lista. Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""
print('Digite 0 caso deseje encerrar o programa!')
lista_completa = []
lista_impar = []
lista_par = []

while True:
    num = int(input('Digite um valor: '))

    if num == 0:
        lista_completa.sort()
        lista_impar.sort()
        lista_par.sort()
        break

    if num % 2 == 0:
        if num in lista_par:
            continue
        lista_par.append(num)
    else:
        if num in lista_impar:
            continue
        lista_impar.append(num)

print(f'lista completa: {lista_completa}\nlista par: {lista_par}\nlista impar{lista_impar}')
