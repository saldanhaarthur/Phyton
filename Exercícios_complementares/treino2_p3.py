frase = input().strip()
frase_minuscula = frase.lower()
vogais_redondas = 0
vogais_n_redondas = 0
final = False
palindromo = False
so_letras = ""

for letra in frase_minuscula:
    if letra == "o" or letra == "u":
        vogais_redondas += 1
    elif letra == "a" or letra == 'e' or letra == 'i':
        vogais_n_redondas += 1

if frase_minuscula[-1] == "z" or frase_minuscula[-1] == "x":
    final = True
    sem_ultima = frase_minuscula[:-1].strip()
    for c in sem_ultima:
        if c.isalpha():
            so_letras +=c

if so_letras == so_letras[::-1]:
    palindromo = True

if vogais_redondas >= 3 and vogais_n_redondas <= 3 and final and palindromo:
    print("ACESSO LIBERADO")
else:
    print("ACESSO NEGADO")




