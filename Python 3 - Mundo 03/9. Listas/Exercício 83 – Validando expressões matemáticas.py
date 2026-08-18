"""
Enunciado Exercício 83 – Validando expressões matemáticas

Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
O seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""


while True:
    # Obtendo a expressão:
    expressao = str(input('Digite uma expressão matemática: '))

    #Validando a posição do primeiro parênteses
    if expressao.index('(') < expressao.index(')'):
        #Validando se a quantidade de parênteses são iguais
        if expressao.count('(') == expressao.count(')'):
            print('Sua expressão está correta!')
            break
        else:
            print('Sua expressão matemática é invalida!\nTente novamente: ')
            continue
    else:
        print('Sua expressão matemática é invalida!\nTente novamente: ')
        continue

'''
A relação de parênteses funciona como uma pilha, caso o objeto abra a sequencia ele deve necessariamente ser fechado.
Ou seja, a verificação é para saber se a expressão se inicia com "(" e saber se a quantidade de "(", ")" são iguais.
'''