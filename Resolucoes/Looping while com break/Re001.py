soma = 0
quantidade_numeros = 0

while True:
    numeros = int(input("Digite um número: "))
    if numeros == 999:
        break
    else:
        soma += numeros
        quantidade_numeros += 1

print(f"A soma dos números digitados foi: {soma} e a quantidade de números digitados foi: {quantidade_numeros}")
        