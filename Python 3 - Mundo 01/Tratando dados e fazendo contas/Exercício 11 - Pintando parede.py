"""
Calculadora que informa quantos litros de tinta é necessário para se o metro quadrado de uma parede
"""

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

print (f'Sua parede tem dimensão de {largura} x {altura}, sua área total é de: {largura * altura}m²')
print(f'Você precisará de {(largura * altura) * 0.15}l de tinta')
