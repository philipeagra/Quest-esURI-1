def idade(qdias):

    ano = qdias // 365
    qdias = qdias - ano * 365

    meses = qdias // 30
    qdias = qdias - meses * 30

    print('{} ano(s)'.format(ano))
    print('{} mes(es)'.format(meses))
    print('{} dia(s)'.format(qdias))



dias = int(input())
idade(dias)