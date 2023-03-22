xy = input().split()

x = int(xy[0])
y = int(xy[1])

linha = 0

for i in range(0, y):
    linha += 1

    if linha == x:
        prox_linha = i +1
        print(prox_linha, end="\n")
        linha = 0

    else:
        prox_num = i + 1
        print(prox_num, end=" ")