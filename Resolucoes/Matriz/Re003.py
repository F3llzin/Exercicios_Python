matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Digite um valor para [{i}][{j}]: ")))
    matriz.append(linha)

print("A sua matriz é assim: ")

for linha in range(3):
    for coluna in range(3):
        print(f"[{matriz[linha][coluna]:^5}]", end=(" "))
    print()