matriz = []

for i in range(3):
    linhas = []
    for j in range(3):
        linhas.append(int(input(f"Digite um número para [{i}][{j}]: ")))
    matriz.append(linhas)

soma_pares = soma_coluna = 0

for linha in range(3):
    for coluna in range(3):
        print(f"[{matriz[linha][coluna]:^5}]", end=(" "))

        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]

        if linha == 2:
            soma_coluna += matriz[coluna][linha]

        if linha == 1:
            if coluna == 0:
                maior = matriz[linha][coluna]

            elif matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]

    print()

print("A soma dos valores pares:", soma_pares)
print("A soma dos valores da terceira coluna é:", soma_coluna)
print("O maior valor da segunda linha é:", maior)