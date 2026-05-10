numero = int(input("Digite um número: "))

if numero != 1 and (numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0) or numero == 2:
    print("Ele é primo")
else: 
    print("Não é primo")

