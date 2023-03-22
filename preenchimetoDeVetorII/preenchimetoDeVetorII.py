def preenchimento_vetor(num):
    vetor = [0] * 1000

    for i in range(len(vetor)):
        vetor[i] = i%num
        print('N[{}] = {}' .format(i, vetor[i]))


num = int(input())
preenchimento_vetor(num)