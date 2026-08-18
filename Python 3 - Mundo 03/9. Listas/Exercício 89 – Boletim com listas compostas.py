"""
Enunciado Exercício 89 – Boletim com listas compostas

Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

lista_aluno = []

#lendo nomes e notas
while True:

    nome =  (input('Nome do aluno(Sair): ')).strip().capitalize()
    #Verificação de saida e mostrando dados
    if nome == 'Sair':
        print('-' * 100)
        print('Tabela de alunos: ')
        for aluno in lista_aluno:
            print(f'{aluno[0]}......................media: {aluno[3]}')
        print('-' * 100)
        break

    nota_01 = float(input(f'Digite a 1° nota do aluno {nome}: '))
    nota_02 = float(input(f'Digite a 2° nota do aluno {nome}: '))
    media = (nota_01 + nota_02) / 2
    print('-' * 100)
    #Adição de todos os valores em um lista aninhada
    lista_aluno.append([nome, nota_01, nota_02, media])

print('Digite o nome do aluno para acessar as suas notas ou (Sair)')

while True:
    nome = (input('Nome do aluno(Sair): ')).strip().capitalize()
    for aluno in lista_aluno:
        if nome == aluno[0]:
            print(f'Primeira nota: {aluno[1]}, Segunda nota: {aluno[2]}')
