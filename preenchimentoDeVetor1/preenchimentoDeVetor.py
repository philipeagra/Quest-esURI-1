V=[0]*10
num = int(input())

for i in range(len(V)):
    V[i] = num
    num = num * 2
    print('N[{}] = {}'.format(i,V[i]))