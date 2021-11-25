dias=int(input("Dias:"))
horas=int(input("Horas:"))
minutos=int(input("Minutos:"))
segundos=int(input("Segundos:"))
quantidade_segundos = dias * 24 * 3600 + horas *3600 + minutos * 60 +segundos
print("convertido em segundos é igual a %d em segundos." %quantidade_segundos)