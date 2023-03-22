n = int(input())
num = 0

for c in range(1 , n + 1):
    x = input().split()
    a, b, = x
    soma = 0
    a = int(a)
    b = int(b)

    if a > b:
        for num in range(int(b)+1, int(a)):
            if num % 2 != 0:
                soma = soma + num
    if a < b:
        for num in range(int(a)+1, int(b)):
            if num % 2 != 0:
                soma = soma + num
    if a == b:
        soma = 0
    print(soma)