"""
O código procura dissecar cada parte de uma variável que possui valor agregado através de um simples imput
"""

variavel = input('Digite Algo: ')

print(f'O tipo primitivo da variavel: {type(variavel)}')
print(f'A variável possui apenas espaços? {variavel.isspace()} ')
print(f'A variável é um numero? {variavel.isnumeric()} ')
print(f'A variável é alfabética? {variavel.isalpha()} ')
print(f'A variável é alphanumérica? {variavel.isalnum()} ')
print(f'A variével está em maiuscula? {variavel.isupper()} ')
print(f'A variavel está em minusculo? {variavel.islower()} ')
print(f'A variável está capitalizada? {variavel[0].isupper()}')