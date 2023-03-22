entrada = input().split()

codigo = int(entrada[0])
quantidade = int(entrada[1])
Valor = 0

if codigo == 1:
    Valor = 4.00 * quantidade
elif codigo == 2:
    Valor = 4.50 * quantidade
elif codigo == 3:
    Valor = 5.00 * quantidade
elif codigo == 4:
    Valor = 2.00 * quantidade
elif codigo == 5:
    Valor = 1.50 * quantidade

print("Total: R$ {:0.2f}" . format(Valor))