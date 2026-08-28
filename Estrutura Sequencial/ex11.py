'''
Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

1. O produto do dobro do primeiro com metade do segundo .
2. A soma do triplo do primeiro com o terceiro.
3. O terceiro elevado ao cubo.
'''


numero1 = int(input("Digite um numero inteiro: "))
numero2 = int(input("Digite outro numero inteiro: "))
numero3 = float(input("Digite um numero Real: "))

parte1 = (numero1*2) * (numero2/2)
parte2 = (numero1*3) + numero3
parte3 = numero3**3

print(f"1. {parte1}")
print(f"2. {parte2:.2f}")
print(f"3. {parte3: .2f}")