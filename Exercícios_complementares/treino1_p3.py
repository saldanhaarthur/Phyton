completo = []
frase = ""
pilha = []
bem_formada = True
pares = {")" : "(", "}" : "{", "]" : "["}

while True:
    simbolo = input()
    if simbolo == "!":
        break
    if simbolo == "*" and len(completo) >=2:
        del completo[-2]
    elif simbolo in "(){}[]":
        completo.append(simbolo)

for simb in completo:
    if simb in "({[":
        pilha.append(simb)
    else:
        if not pilha or pilha[-1] != pares[simb]:
            bem_formada = False
        else:
            del pilha[-1]

if len(pilha) > 0:
    bem_formada = False

if bem_formada:
    print("bem formada")
else:
    print("mal formada")








