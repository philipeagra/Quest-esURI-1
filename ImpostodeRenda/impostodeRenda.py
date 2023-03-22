renda  = float(input())
tributo = 0
acumulado = 0

if (renda > 4500):
    taxa = 0.28
    resto = renda - 4500
    tributo = resto * taxa
    acumulado += resto
    
if (renda > 3000):
    taxa = 0.18
    resto = renda - 3000 - acumulado
    tributo += resto * taxa
    acumulado += resto
    
if (renda > 2000):
    taxa = 0.08
    resto = renda - 2000 - acumulado
    tributo += resto * taxa
    
    print('R$ %.2f' %(tributo))

else:
    print('Isento')