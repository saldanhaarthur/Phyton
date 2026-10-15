quant_casas = int(input())
quant_media = 0
consumo_soma = 0
int_consumo = 0
lista_int_con = []

consumo = input().split()

for posicao in consumo:
    int_consumo = int(posicao)
    lista_int_con.append(int_consumo)

consumo_soma = sum(lista_int_con)

consumo_media = consumo_soma / quant_casas
for energia in lista_int_con:
    if energia <= consumo_media:
        quant_media +=1

print(quant_media)