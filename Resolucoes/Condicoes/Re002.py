velocidade = int(input("Digite a velocidade em km/h: "))

if velocidade > 80:
    print(f"Você foi multado, a sua multa é de: {(velocidade % 80) * 7}")
else:
    print("Você não foi multado.")