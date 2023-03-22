testes = int(input())
total = 0
C = 0
S = 0
R = 0

for i in range(testes):
    numero, tipo = input().split()
    numero = int(numero)

    total = total + numero
    if tipo == "C":
        C = C + numero
    if tipo == "S":
        S = S + numero
    if tipo == "R":
        R = R + numero
perc_C = (C * 100) / total
perc_R = (R * 100) / total
perc_S = (S * 100) / total
print("Total: {} cobaias" .format(total))
print("Total de coelhos: {}" .format(C))
print("Total de ratos: {}" .format(R))
print("Total de sapos: {}" .format(S))
print("Percentual de coelhos: {:.2f} %" .format(perc_C))
print("Percentual de ratos: {:.2f} %" .format(perc_R))
print("Percentual de sapos: {:.2f} %" .format(perc_S))