entrada = input("Você quer 'entrar' ou 'sair': ")

if entrada == "entrar":
    print("Você entrou no sistema! ")
    print("so roda no if")
elif entrada == "sair":
    print("Você saiu do sistema! ")
    print("so roda no elif")
else :
    print("Você não digitou nem 'entrar' e nem 'sair' ")
    print("so roda no else")
    
print("Isso roda sempre!")

