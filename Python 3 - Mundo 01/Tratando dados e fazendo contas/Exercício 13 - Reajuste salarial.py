"""
Enunciado do exercício 13 - Reajuste salarial:

Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

salario = float(input('Qual o salario do funcionario?: $'))
print(f'Um funcionario que ganhava ${salario}, passa a ganhar {salario * 1.15:.2f}.')
