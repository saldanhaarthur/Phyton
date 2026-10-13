"""
. Receber duas linhas de texto:
- 1° Produtos em estoque 
- 2° Produtos que o cliente deseja comprar   --> Ambos sendo recebidos separados por espaços 
 
. Gerar uma lista que o cliente pediu mas que faltam no estoque 

"""


estoque = input().split() # leio a string de estoque e separo ela pelos espaços atráves do split
cliente = input().split() # mesma coisa feita em split 
itens_faltando = [] # Crio uma lista vazia dos itens faltando

for n in cliente:
    if n not in estoque:
        itens_faltando.append(n)

if itens_faltando:
    print(f"Faltam os itens: {itens_faltando}")
    
else:
    print("Tudo em estoque!")


            
    