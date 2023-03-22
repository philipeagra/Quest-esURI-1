Notas = input().split()

Nota_1 = float(Notas[0])
Nota_2 = float(Notas[1])
Nota_3 = float(Notas[2])
Nota_4 = float(Notas[3])


media = (Nota_1 * 2 + Nota_2 * 3 + Nota_3 * 4 + Nota_4 *1) / 10

print('Media: %.1f' %media)

if (media >= 7.0):
    print('Aluno aprovado.')
elif (media < 5.0):
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    nota_exame = float(input())
    print('Nota do exame: %.1f' %nota_exame)
    media_2 = (media + nota_exame)/2
    if (media_2 >= 5):
        print('Aluno aprovado.')
    else:
        print('aluno reprovado.')

    print('Media final: %.1f' %media_2)