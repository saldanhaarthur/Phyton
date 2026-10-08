a = "AAAAAA"
b = "BBBBBB"
c = 1.1

string = "a={} b={} c={}"
formato = string.format(a, b, c)

print(formato)

modelo = "Olá, {}! Você tem {} de idade. "

print(modelo.format("arthur", 19))
print(modelo.format("Ana", 22))