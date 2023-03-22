QuantFib = int(input())

for i in range(QuantFib):
    num = int(input())
    f = [0, 1]

    if num > 1:
        for c in range(2, num + 1):
            f.append(f[c - 2] + f[c - 1])
        print('Fib({}) = {}'.format(num, f[num]))

    if num <= 1:
        print('Fib({}) = {}'.format(num, f[num]))