numero = int(input("Digite um número: "))
soma = 0
quantidade_numeros = 0

while numero != 999:
    soma += numero
    quantidade_numeros += 1
    numero = int(input("Digite um número: "))

print(f"A soma dos números foram {soma} e a quantidade de números foram {quantidade_numeros}")