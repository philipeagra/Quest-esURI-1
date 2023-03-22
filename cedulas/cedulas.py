v = int(input())
print(v)

v100 = v//100
valor_resto = v%100

v50 = valor_resto//50
valor_resto2 = valor_resto%50

v20 = valor_resto2//20
valor_resto3 = valor_resto2%20

v10 = valor_resto3//10
valor_resto4 = valor_resto3%10

v5  = valor_resto4//5
valor_resto5 = valor_resto4%5

v2 = valor_resto5//2
valor_resto6 = valor_resto5%2

v1 = valor_resto6//1
valor_resto7 = valor_resto6%1

print('{} nota(s) de R$ 100,00'.format(v100))
print('{} nota(s) de R$ 50,00'.format(v50))
print('{} nota(s) de R$ 20,00'.format(v20))
print('{} nota(s) de R$ 10,00'.format(v10))
print('{} nota(s) de R$ 5,00'.format(v5))
print('{} nota(s) de R$ 2,00'.format(v2))
print('{} nota(s) de R$ 1,00'.format(v1))