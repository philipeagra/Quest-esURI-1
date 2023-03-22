par = []
impar = []
for i in range(15):
    valor = int(input())
    if (valor % 2 == 0):
        par.append(valor)
    else:
        impar.append(valor)

    if (len(par) == 5):
        cont = 0
        for v in par:
            print("par[%d] = %d" % (cont, v))
            cont += 1
        par = []
    if (len(impar) == 5):
        cont = 0
        for v in impar:
            print("impar[%d] = %d" % (cont, v))
            cont += 1
        impar = []
if (len(impar) > 0):
    cont = 0
    for v in impar:
        print("impar[%d] = %d" % (cont, v))
        cont += 1

if (len(par) > 0):
    cont = 0
    for v in par:
        print("par[%d] = %d" % (cont, v))
        cont += 1