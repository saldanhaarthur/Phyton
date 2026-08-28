""""
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
 Calcule e mostre o total do seu salário no referido mês.
 """

ganho_h = float(input("Ganhos por hora: "))
horas_t = float(input("Horas trabalhadas no mes: "))

total_salario = ganho_h * horas_t

print(f"Ganhou um total de {total_salario: .2f} em {horas_t} horas trabalhadas nesse mes! ")