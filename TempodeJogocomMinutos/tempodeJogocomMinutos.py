entradas = input().split()

hi = int(entradas[0])
mi = int(entradas[1])
hf = int(entradas[2])
mf = int(entradas[3])

mi += hi * 60
mf += hf * 60

tempo = mf - mi

if tempo <= 0:
    tempo += (24*60)
    
h = tempo//60
m = tempo%60
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)' .format(h,m))