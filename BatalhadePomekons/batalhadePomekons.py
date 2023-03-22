n_instancias = int(input())
golpeG = 0
golpeD = 0

for i in range(n_instancias):
    bonus = int(input())
    dabriel = input().split()
    guarte = input().split()

    v_ataq_D = int(dabriel[0])
    v_def_D = int(dabriel[1])
    level_D = int(dabriel[2])

    v_ataq_G = int(guarte[0])
    v_def_G = int(guarte[1])
    level_G = int(guarte[2])

    if level_D % 2 == 0:
        golpeD = ((v_ataq_D + v_def_D) / 2) + bonus
    else:
        golpeD = (v_ataq_D + v_def_D) / 2


    if level_G % 2 == 0:
        golpeG = ((v_ataq_G + v_def_G) / 2) + bonus
    else:
        golpeG = (v_ataq_G + v_def_G) / 2


    if golpeG > golpeD:
        print('Guarte')
    elif golpeG < golpeD:
        print('Dabriel')
    else:
        print('Empate')