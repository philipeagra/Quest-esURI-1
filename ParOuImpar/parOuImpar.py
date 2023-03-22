N = int(input())

entrada_valor = 0
    
for c in range (N):
    valor = int(input())
    
    if (valor %2 == 0 and valor > 0):
        print('EVEN POSITIVE')
        entrada_valor += 1
        
    elif (valor %2 != 0 and valor > 0):
        print('ODD POSITIVE')
        entrada_valor += 1
              
    elif (valor %2 == 0 and valor < 0):
        print('EVEN NEGATIVE')
        entrada_valor += 1
                
    elif (valor %2 != 0 and valor < 0):
        print('ODD NEGATIVE')
        entrada_valor += 1
                
    elif (valor == 0):
        print('NULL')
        entrada_valor += 1