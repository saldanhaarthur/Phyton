"""
Faça um programa que peça a temperatura em graus Fahrenheit,
 transforme e mostre a temperatura em graus Celsius.
"""
temperatura_f = float(input("Temperatura em Fahrenheit: "))

temperatura_c = 5 * ((temperatura_f-32) / 9)

print(f"Temperatura em Celsius: {temperatura_c: .2f}")