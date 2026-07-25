"""
Enunciado Exercício 70 – Estatísticas em produtos

Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
"""
#Definição de variáveis
total_das_compras = 0
produtos_1000 = 0
valor_do_produto_mais_barato = 0
nome_do_produto_mais_barato = ''

while True:
    #lendo nome e preço dos produtos
    nome_do_produto = str(input('Informe o nome do produto: '))
    valor_do_produto = float(input('Informe o valor do produto: R$'))

    #Soma do valor de todos os produtos
    total_das_compras += valor_do_produto

    #Verficando quantos produtos custam mais que R$1000
    if valor_do_produto >= 1000:
        produtos_1000 +=1

    #Verificando o produto mais barato
    if valor_do_produto_mais_barato == 0:
        valor_do_produto_mais_barato = valor_do_produto
    if valor_do_produto < valor_do_produto_mais_barato:
        valor_do_produto_mais_barato = valor_do_produto
        nome_do_produto_mais_barato = nome_do_produto

    #Condição de continuidade
    continuidade = str(input('Deseja continuar? [S / N]')).strip().upper()
    if continuidade == 'S':
        continue
    elif continuidade == 'N':
        break
#Mostrando todos os dados
print(f'O total da sua compra é de R${total_das_compras:.2f}')
print(f'Há um total de {produtos_1000} produtos que custam mais de R$1000!')
print(f'O produto mais barato é: {nome_do_produto_mais_barato} custando R${valor_do_produto_mais_barato}')
