"""
Atividade focada em receber e mostrar sua tabuada até 10
"""

numero =  int(input('Digite um numero para ver sua tabuada: '))
print('-' * 30)
for n in range (1, 11):
    print(f'{numero} x {n} = {numero * n}')

print('-' * 30)