'''
Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''

temperatura_c = float(input("Temperatura em Celsius:"))

temperatura_f = (temperatura_c* 9/5) + 32

print(f"Temperatura em Fahrenheit: {temperatura_f: .2f}")