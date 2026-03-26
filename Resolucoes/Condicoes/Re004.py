distancia = int(input("Digite a distância da viagem em km: "))

if distancia <= 200:
    print(f"O preço da sua passagem é de: {distancia * 0.5}R$")
else: 
    print(f"O preço da sua passagem é de: {distancia * 0.45}")