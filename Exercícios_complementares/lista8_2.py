quantidade = int(input())
pares_transformados = []
impares_originais = []

for n in range(quantidade):
    num = int(input())
    if num % 2 == 0:
        pares_transformados.append(num*2)
    else :
        impares_originais.append(num)

print(f"Pares transformados : {pares_transformados}")
print(f"Ímpares originais : {impares_originais}")
        

