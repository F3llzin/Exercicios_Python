numeros = []
continuar = "s"

while continuar[0] == "s":
    numero = int(input("Digite um número: "))

    numeros.append(numero)

    continuar = input("Deseja continuar[s/n]? ").lower().strip()

    while continuar[0] not in "sn":
        continuar = input("Deseja continuar[s/n]? ").lower().strip()

print(f"A quantidade de números na lista é: {len(numeros)}")
print(f"A lista em ordem decrescente: {sorted(numeros, reverse=True)}")

if 5 in numeros:
    print("O valor 5 está presente na lista")
else:
    print("O valor 5 não está presente na lista")
