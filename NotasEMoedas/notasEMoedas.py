valor = float(input())

n100 = valor // 100
valor = valor - n100*100

n50 = valor // 50
valor = valor - n50*50

n20 = valor // 20
valor = valor - n20*20

n10 = valor // 10
valor = valor - n10*10

n5 = valor // 5
valor = valor - n5*5

n2 = valor // 2
valor = valor - n2*2

m1 = valor // 1
valor = valor - m1*1
m1 = float('%.2f'% m1)
valor= float('%.2f'% valor)

m50 = valor // 0.5
valor = valor - m50*0.5
m50 = float('%.2f'% m50)
valor = float('%.2f'% valor)

m25 = valor // 0.25
valor = valor - m25*0.25
m25 = float('%.2f'% m25)
valor = float('%.2f'% valor)

m10 = valor // 0.10
valor = valor - m10*0.10
m10 = float('%.2f'% m10)
valor = float('%.2f'% valor)

m5 = valor // 0.05
valor = valor - m5*0.05
m5 = float('%.2f'% m5)
valor = float('%.2f'% valor)

m01 = valor * 100
m01=float('%.2f'% m01)
valor = float('%.2f'% valor)

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(n100)))
print('{} nota(s) de R$ 50.00'.format(int(n50)))
print('{} nota(s) de R$ 20.00'.format(int(n20)))
print('{} nota(s) de R$ 10.00'.format(int(n10)))
print('{} nota(s) de R$ 5.00'.format(int(n5)))
print('{} nota(s) de R$ 2.00'.format(int(n2)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(m1)))
print('{} moeda(s) de R$ 0.50'.format(int(m50)))
print('{} moeda(s) de R$ 0.25'.format(int(m25)))
print('{} moeda(s) de R$ 0.10'.format(int(m10)))
print('{} moeda(s) de R$ 0.05'.format(int(m5)))
print('{} moeda(s) de R$ 0.01'.format(int(m01)))
