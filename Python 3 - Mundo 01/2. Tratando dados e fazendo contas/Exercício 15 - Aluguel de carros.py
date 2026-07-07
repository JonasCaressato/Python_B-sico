"""
Mostra qual o valor a pagar ao alugar um carro sabendo que a diaria é de $60 + $0,15 por km rodado
"""

dias_alugado = int(input('Por quantos dias o carro foi alugado?: '))
km_percorrido = float(input('Quantos km foram percorridos?: '))

print(f'O valor total a ser pago é de: ${(60 * dias_alugado) + (0.15 * km_percorrido):.2f}')