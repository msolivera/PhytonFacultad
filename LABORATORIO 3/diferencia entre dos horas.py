def hora_a_segundos (hora, minutos, segundos):
    return hora*3600+minutos*60+segundos

def diferencia_segundos (hora1, hora2, minutos1, minutos2, segundos1, segundos2):
    return abs (hora_a_segundos(hora1, minutos1, minutos1) - hora_a_segundos(hora2, minutos2, segundos2))
print (diferencia_segundos(19, 59, 20, 15, 30, 15))
