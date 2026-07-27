"""
Enunciado Exercício 77 – Contando vogais em Tupla

Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
palavras = (
    'agua',
    'arvore',
    'coracao',
    'lampada',
    'cafe',
    'musica',
    'passaro',
    'tambem',
    'relampago',
    'sabado',
    'facil',
    'conexao',
    'aviao',
    'historia',
    'sofa',
    'magico',
    'xicara',
    'numero',
    'caminhao',
    'orgao',
)

for palavra in palavras:
    print(palavra)
    print(f'A palavra {palavra}: tem as seguintes vogais: ')
    for letra in palavra:
        if letra == 'a':
            print(letra)
        elif letra == 'e':
            print(letra)
        elif letra == 'i':
            print(letra)
        elif letra == 'o':
            print(letra)
        elif letra == 'u':
            print(letra)
