tempo = int(input())
velocidade_media = int(input())
distancia = tempo * velocidade_media
quantidade_litros = distancia / 12

print('{:.3f}' .format(quantidade_litros))