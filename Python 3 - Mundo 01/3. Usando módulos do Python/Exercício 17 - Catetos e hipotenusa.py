"""
Enunciado do exercício 17 - Catetos e hipotenusa:

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
"""
import math

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

print(f'Com os valores dos catetos correspondendo a: {cateto_oposto}cm e {cateto_adjacente}cm ')
print(f'O valor da Hipotenusa corresponde a: {math.sqrt( (cateto_oposto**2) + (cateto_adjacente**2) ):.2f}cm')