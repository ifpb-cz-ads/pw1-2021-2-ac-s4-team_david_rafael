dist = float(input("Digite a distância em km:"))
velocidade_média = float(input("Digite a velocidade média em km/h:"))
tempo = dist / velocidade_média
print("O tempo estimado é de %5.2f horas" % tempo)
tempo_s = int(tempo * 3600)
horas = int(tempo_s / 3600) 
tempo_s = int(tempo_s % 3600)  
minutos = int(tempo_s / 60)
print("%02d:%02d" % (horas, minutos))