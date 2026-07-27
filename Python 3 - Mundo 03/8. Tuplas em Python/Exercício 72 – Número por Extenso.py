"""
Enunciado Exercício 72 – Número por Extenso

 Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
 O seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

#Definindo a Tupla
numero_por_extenso = ('zero', 'Um', 'Dois', 'Três', 'Quatro','Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
                      'Onze', 'Doze', 'Treze', 'Quatorze','Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
                      'Dezenove', 'Vinte')

while True:
    #Obtendo o 'Input' do usuário
    n = int(input('Digite um número entre 0 e 20: '))

    #Verificando se a entrada condiz com as especificações pedidas
    if n < 0 or n > 20:
        print('Opção inválida! \nTente Novamente!')
        continue

    print(f'Você digitou o número {numero_por_extenso[n]}')
    break
