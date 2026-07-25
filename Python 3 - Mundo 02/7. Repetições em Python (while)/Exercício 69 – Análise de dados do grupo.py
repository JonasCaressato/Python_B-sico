"""
Enunciado Exercício 69 – Análise de dados do grupo

Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
"""
#Definição de variáveis
contabilizador_de_maioridade = 0
contabilizador_de_homens = 0
contabilizador_de_mulheres_20 = 0

while True:
    #lendo idade e sexo de cada pessoa
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite seu sexo: [M / F] ')).strip().upper()

    #Condição de maioridade
    if idade >= 18:
        contabilizador_de_maioridade += 1
    #Condição para contabilizar homens
    if sexo == 'M':
        contabilizador_de_homens += 1
    #Condição para contabilizar mulheres com menos de 20 anos
    if sexo == 'F' and idade <20:
        contabilizador_de_mulheres_20 +=1
    #Condição de continuidade
    continuidade = str(input('Deseja continuar? [S / N]')).strip().upper()
    if continuidade == 'S':
        continue
    else:
        break

#Mostrando os dados coletados
print(f'O grupo possui um total de: {contabilizador_de_maioridade} membros com mais de 18 anos!')
print(f'O grupo possui um total de: {contabilizador_de_homens} homens!')
print(f'O grupo possui um total de: {contabilizador_de_mulheres_20} mulheres com menos de 20 anos!')
