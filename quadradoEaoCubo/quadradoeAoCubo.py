n = int(input())
seq = 1
for index in range(n):
    print("{} {} {}" .format(seq, seq**2, seq**3))
    seq = seq + 1
