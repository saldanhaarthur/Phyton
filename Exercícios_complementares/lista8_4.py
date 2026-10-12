quantidade = int(input())

for i in range(quantidade) :
    frase = input()
    if "batatinha" in frase.lower(): # Verificando se batatinha está escrito na frase em minuscula para facilitar a verificação
        print("Bingo!")
        break # Printando e encerrando o código já que encontrou a palavra secreta
    else :
        for letra in "aeiouAEIOU": # Percorre todas as vogais trocando elas por 1 nas palavras 
            frase = frase.replace(letra, "1")

        frase = frase.replace(" ", "-") # Trocando os espaços pelo hífen
        print(frase)


