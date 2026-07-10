"""
Enunciado Exercício 40 – Aquele clássico da Média

Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
"""

nota_1 = float(input('Qual a primeira nota do aluno? '))
nota_2 = float(input('Qual a segunda nota do aluno? '))

media = (nota_1 + nota_2) / 2

if media < 5.0:
    print('REPROVADO')
elif 5.0 <= media <= 6.9:
    print('RECUPERAÇÃO')
elif media >= 7.0:
    print('APROVADO')
