def metade_prox_posi(X):
    vetor = [0] * 100
    for i in range(len(vetor)):
        vetor[i] = X
        print(f'N[{i}] = {vetor[i]:.4f}')
        X = X / 2

X = float(input())
metade_prox_posi(X)