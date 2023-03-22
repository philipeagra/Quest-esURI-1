n = int(input())
a = 0

for i in range(1,100):
    b = int(input())
    if b > a:
        maior = b
        posicao = i + 1
        a = b

print(maior)
print(posicao)