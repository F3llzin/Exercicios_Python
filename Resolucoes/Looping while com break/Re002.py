while True:
    numeros = int(input("Digite um número para fazer a sua tabuada: "))

    if numeros < 0:
        break
    else:
        print(f"A tabuada do número {numeros} é")
        for i in range(0, 11):
            print(f"{numeros} X {i} = {numeros * i}")

print("Fim do looping")
