string = input()
string_limpa = string.lower().replace(" ", "") 

string_palindromo = string_limpa[::-1]

if string_limpa and string_limpa == string_palindromo :            
    print("A cadeia é palindromo")
else :
    print("A cadeia não é palindromo")