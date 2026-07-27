numeros = []
continuar = "S"

while continuar == "S":
    numero = int(input("Digite um número: "))

    if numero not in numeros:
        numeros.append(numero)
    else:
        pass

    continuar = input("Deseja continuar[S/N]? ").upper().strip()

    while continuar[0] not in "SN":
        continuar = input("Deseja continuar[S/N]? ").upper().strip()

print(f"Você digitou os valores: {sorted(numeros)}")
