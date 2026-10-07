
ganho_h = int(input("Ganho por hora: "))
horas_t = int(input("Horas trabalhadas: "))

salario_br = ganho_h * horas_t
ir = salario_br * (11/100)
inss = salario_br * (8/100)
sindicato = salario_br * (5/100)
salario_liq = salario_br - (ir + inss + sindicato)

print(f"Salario bruto: {salario_br}R$")
print(f"Imposto de renda: {ir}R$")
print(f"INSS: {inss}R$")
print(f"Sindicato: {sindicato}R$")
print(f"Salario Liquido: {salario_liq} R$")