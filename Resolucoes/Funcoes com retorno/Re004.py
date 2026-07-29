def leiaInt(texto = '') :
    numero = input(texto)

    while not(numero.isdigit()):
        print("\033[31mERRO! Digite um número válido.\033[m")
        numero = input(texto)

    return numero


numero = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {numero}")
