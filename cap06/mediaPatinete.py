print("Esse programa calcula a velocidade média de um patinete")
distancia = float(input("Qual foi a distância em metros percorrida pelo patinete? ")) / 1000
tempo = float(input("Quantos minutos o patinete demorou para percorrer essa distância? ")) / 60
velocidade_media = distancia / tempo
print("O patinete atingiu uma velocidade de {0:.2f} km/hr".format(velocidade_media))