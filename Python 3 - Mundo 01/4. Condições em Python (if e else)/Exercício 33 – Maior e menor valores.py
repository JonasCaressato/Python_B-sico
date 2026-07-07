"""
Enunciado Exercício 33 – Maior e menor valores

Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

#Recebendo valores
print('Saiba qual é o maior e o menor')
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
numero_3 = int(input('Digite o terceiro número: '))
print('-' * 10)

#Número_1 maior e Número_3 menor
if numero_1 > numero_2 > numero_3:
    print(f'O MAIOR número é o {numero_1}')
    print(f'O MENOR número é o {numero_3}')

#Número_1 maior e Número_2 menor
elif numero_1 > numero_3 > numero_2:
    print(f'O MAIOR número é o {numero_1}')
    print(f'O MENOR número é o {numero_2}')

#Número_2 maior
elif numero_2 > numero_3:

    #Número_2 maior e Número_3 menor
    if numero_1 < numero_3:
        print(f'O MAIOR número é o {numero_2}')
        print(f'O MENOR número é o {numero_1}')

    #Número_2 maior e Número_1 menor
    else:
        print(f'O MAIOR número é o {numero_2}')
        print(f'O MENOR número é o {numero_3}')

#Número_3 maior
else:
    print(f'O MAIOR número é o {numero_3}')

    #Número_3 maior e Número_1 menor
    if numero_1 < numero_2:
        print(f'O MENOR número é o {numero_1}')

    #Número_3 maior e Número_2 menor
    else:
        print(f'O MENOR número é o {numero_2}')

"""
Nota do desafio:

Após terminar meu código fui fazer uma comparação com o código do Professor Gustavo Guanabara.
Ele denominou uma variavel como (menor) e atribuiu o valor de numero_1(a) como menor e fez duas verificações.
Ele também denominou uma variavel como (maior), atribuiu numero_1(a) e repitiu o processo

Seu código utilizou cinco (variaveis) e quatro (if)
O meu código utilizou três (variaveis) e oito (if, elif e else)

Nota para se estudar:

Estudar sobre o que torna o código mais robusto em larga escala, mai simples da maquina processar
e mais simples de outra pessoa interpretar.
"""