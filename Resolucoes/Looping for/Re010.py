peso = float(input("Digite seu peso: "))
peso_maior = peso
peso_menor = peso

for i in range(0, 4):
    peso = float(input("Digite seu peso: "))

    if peso > peso_maior:
        peso_maior = peso
    if peso_menor > peso:
        peso_menor = peso

print(f"O maior preço é: {peso_maior} e o menor é: {peso_menor}")