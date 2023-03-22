n=int(input())

valores = input().split()


for i in range(len(valores)):
    valores[i] = int(valores[i])

menor = valores[0]
posicao = 0
for c in range(1,len(valores)):
    if valores[c] < menor:
        menor = valores[c]
        posicao = c

print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(posicao))