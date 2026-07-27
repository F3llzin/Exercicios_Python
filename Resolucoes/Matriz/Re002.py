numeros = [[], []]

for i in range(7):
    numero = int(input(f"Digite o {i + 1}° número: "))

    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

print(f"Os pares digitados foram:", sorted(numeros[0]))
print(f"Os impares digitados foram:", sorted(numeros[1]))