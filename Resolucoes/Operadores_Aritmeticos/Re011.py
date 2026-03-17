numero = int(input())

#A diferença de desempenho entre os dois veículos é dada pela subtração de suas velocidades constantes
v_relativa = 90 - 60
#Para encontrar a proporção em minutos, dividimos a hora (minutos) pela distância percorrida nesse intervalo
taxa = 60 / 30
#Para descobrir o tempo necessário para uma distância arbitrária, basta multiplicar a distância pela taxa encontrada
tempo = taxa * numero

print(f"{int(tempo)}minutos")
