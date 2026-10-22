'''
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
   <- Contagem de complexidade (ruim)
'''

velocidade = 61 
local_carro = 99 # local que o carro está na estrada

# Constantes (escritas em letras maiuscúlas)
RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega 

if velocidade > RADAR_1 and local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE):
    print(f"O carro passou da velocidade maxima de {RADAR_1}Km/h do radar 1")