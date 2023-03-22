entrada = int(input())


for i in range(entrada):
    x = int(input())
    tot = 0
    for c in range(1, x+1):
        if x % c == 0 and c < x:
            tot += c


    if tot == x:
        print('{} eh perfeito' .format(x))
    else:
        print('{} nao eh perfeito' .format(x))