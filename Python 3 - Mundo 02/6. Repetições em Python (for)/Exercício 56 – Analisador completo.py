"""
Enunciado Exercício 56 – Analisador completo

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""

#Atribuição de valores-base
media_de_idade = 0

homem_mais_velho = ''
idade_do_homem_mais_velho = 0

total_de_mulheres_com_menos_de_20_anos = 0

for n in range (1, 5):

    #Obtendo os dados para a analise
    print('-' * 20)
    nome = str(input(f'Digite o NOME do {n}° integrante: '))
    idade = int(input(f'Digite a IDADE do {n}° integrante: '))
    sexo = str(input(f'Digite o SEXO do {n}° integrante [M/F]: '))

    #Obtendo a média de idade do grupo
    media_de_idade = idade / n

    #Homem mais velho do grupo
    if sexo == 'M':
        if homem_mais_velho == '':
            homem_mais_velho = nome
            idade_do_homem_mais_velho = idade
        else:
            if idade > idade_do_homem_mais_velho:
                idade_do_homem_mais_velho = idade
                homem_mais_velho = nome

    #Total de mulheres com menos de 20 anos
    elif sexo == 'F':
        if idade < 20:
            total_de_mulheres_com_menos_de_20_anos += 1


print('-' * 20)
print(f'A média de idade é: {media_de_idade}!')
print(f'{homem_mais_velho} é o homem mais velho com {idade_do_homem_mais_velho} anos!')
print(f'Há um total de {total_de_mulheres_com_menos_de_20_anos} mulheres com menos de 20 anos!')
print('-' * 20)
