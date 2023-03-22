N = int(input())

for i in range(N):
    num = input().split()
    a, b = num
    a = int(a)
    b = int(b)

    if b == 0:
        print('divisao impossivel')
    if b != 0:
        divisao = a / b
        print('{:.1f}' .format(divisao))