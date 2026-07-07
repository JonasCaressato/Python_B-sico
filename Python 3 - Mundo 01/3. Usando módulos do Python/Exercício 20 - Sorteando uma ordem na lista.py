"""
Enunciado do exerceício 20 - Sorteando uma ordem na lista

O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

import random

alunos = []

for n in range(1, 5):
        alunos.append(str(input(f'Digite o nome do aluno: ')))

random.shuffle(alunos)

print(f'A ordem de apresentção é: \n{alunos}')
