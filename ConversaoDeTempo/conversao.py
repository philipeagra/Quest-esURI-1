segundos = int(input())
hora = segundos // 60**2
segundos = segundos - hora * 60**2

minutos = segundos // 60
segundos = segundos - minutos*60



print('{}:{}:{}'.format(hora, minutos, segundos))