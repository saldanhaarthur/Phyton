nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
# A função input guarda sempre a variável como uma string, portanto se temos um número devemos converte-lo

int_idade = int(idade)

print(f"Nome: {nome} \nIdade: {int_idade}")