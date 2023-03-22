quant_produto = int(input())


total = 0

for i in range(quant_produto):
    produto = input().split()

    if int(produto[0]) == 1001:
        total += int(produto[1]) * 1.50
    if int(produto[0]) == 1002:
        total += int(produto[1]) * 2.50
    if int(produto[0]) == 1003:
        total += int(produto[1]) * 3.50
    if int(produto[0]) == 1004:
        total += int(produto[1]) * 4.50
    if int(produto[0]) == 1005:
        total += int(produto[1]) * 5.50
print('{:.2f}' .format(total))
