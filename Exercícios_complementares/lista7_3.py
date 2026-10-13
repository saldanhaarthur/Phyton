saida = 0
while saida != 3:
    saida = int(input())
    if saida == 1:
        binario = ''
        numero = input()
        int_numero = int(numero)
        while int_numero > 0:
            resto_div = str(int_numero % 2)
            div_inteira = int_numero // 2
            int_numero = div_inteira
            binario = resto_div + binario
        print(binario)
    elif saida == 2:
        numero = input()
        decimal = 0
        expoente = 0

        for num in numero[::-1]:
            int_numero = int(num)
            decimal = int_numero * 2**expoente + decimal    
            expoente += 1
        print(decimal)
            
        

