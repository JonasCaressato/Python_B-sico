"""
Enuciado Exercício 57 – Validação de Dados

Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

while True:
    sexo = str(input('Informe o seu sexo [F/M]: ')).strip().upper()

    if sexo == 'F':
        print(f'Seu sexo foi salvo como Feminino ({sexo})!')
        break
    elif sexo == 'M':
        print(f'Seu sexo foi salvo como Masculino ({sexo})!')
        break
    else:
        print('-' * 20)
        print('Opção inválida!!!')
        print('Só é aceito a definição F ou M!!!')
        print('Digite novamente: ')
        print('-' * 20)