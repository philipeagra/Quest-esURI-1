import math


AlturaPulo_QuantCanos = input().split()
AlturaPulo = int(AlturaPulo_QuantCanos[0])
QuantCanos = int(AlturaPulo_QuantCanos[1])
ganhou = True
AlturaCanos = input().split()

for i in range(len(AlturaCanos) - 1):
    AlturaCano = (int(AlturaCanos[i]) - int(AlturaCanos[i+1]))
    if math.fabs(AlturaCano) > AlturaPulo:
        ganhou = False

if ganhou:
    print('YOU WIN')
else:
    print('GAME OVER')