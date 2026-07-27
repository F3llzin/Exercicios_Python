numeros = []
continuar = "s"

while continuar[0] == "s":
    numero = int(input("Digite um número: "))

    numeros.append(numero)

    continuar = input("Deseja continuar[s/n]? ").lower().strip()

    while continuar[0] not in "sn":
        continuar = input("Deseja continuar[s/n]? ").lower().strip()

numeros_pares = []
numeros_impares = []

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        numeros_pares.append(numeros[i])
    else:
        numeros_impares.append(numeros[i])

print(f"A lista completa é: {numeros}")
print(f"A lista de pares é: {numeros_pares}")
print(f"A lista de ímpares é: {numeros_impares}")