"""
Enunciado do exercício 19 - Sorteando um item na lista:

Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""
import random

alunos = []

for n in range(1, 5):
    nome = input('Digite o nome do aluno: ')
    alunos.append(nome)

sorteado = random.choice(alunos)

print(f'O aluno sorteado para apagar a louza foi: {sorteado}')
