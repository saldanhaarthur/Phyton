nome = input("Digite o seu nome: ").strip()
idade = input("Digite sua idade: ").strip()

if nome and idade :
    nome_se = nome.replace(' ', '')
    print(f"Seu nome é: {nome}")
    print(f"Seu nome invertido é: {nome[ : :-1]}")
    if " " in nome :
        print("Seu nome contém espaço")
    else :
        print("Seu nome não contém espaço")

    print(f"Seu nome contém {len(nome_se)} letras")
    print(f"A primeira letra do seu nome é '{nome[0]}'")
    print(f"A última letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios")