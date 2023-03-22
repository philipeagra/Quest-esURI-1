lista = []
for i in range(20):    
    valor = int(input())
    lista.append(valor)

pos = 0
for j in range(len(lista)-1, -1, -1):
    print("N[%d] = %d" %(pos,lista[j]))
    pos += 1