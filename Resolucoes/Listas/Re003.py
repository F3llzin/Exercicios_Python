numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    

    if i == 0:
        print("Adicionando ao final da lista...")
        numeros.insert(4, numero)

    if i > 0:
        if numero > max(numeros):
            print("Adicionando ao final da lista...")
            numeros.insert(4, numero)
        else:
            condicao = 0

            while condicao < len(numeros):
                if numero <= numeros[condicao]:
                    numeros.insert(condicao, numero)
                    print(f"Adicionando na posição {condicao} da lista...")
                    break

                condicao += 1

print(numeros)