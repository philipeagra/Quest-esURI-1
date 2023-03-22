n_cartinhas = int(input())

carrinho = 0
bonecas = 0

for i in range(n_cartinhas):

    sexo = input().split()

    if sexo[1] == 'F':
        bonecas += 1

    else :
        carrinho += 1
print('{} carrinhos' .format(carrinho))
print('{} bonecas'.format(bonecas))