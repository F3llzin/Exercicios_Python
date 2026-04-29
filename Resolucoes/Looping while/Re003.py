numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
condicao = 0
resultado = 0

while condicao != 5:
    print('''Escolha uma das opções:
    [1]: soma
    [2]: multiplica
    [3]: maior
    [4]: novos números
    [5]: sair do programa''')
    condicao = int(input("Escolha uma das opções acima: "))
    if condicao == 1:
        resultado = numero1 + numero2
        print(f"O resultado dessa operação é: {resultado}")
    elif condicao == 2:
        resultado = numero1 * numero2
        print(f"O resultado dessa operação é: {resultado}")
    elif condicao == 3:
        if numero1 > numero2:
            print(f"O número {numero1} é maior")
        elif numero1 < numero2:
            print(f"O número {numero2} é maior")
        else:
            print("Os números são iguais")
    elif condicao == 4:
        numero1 = int(input("Digite um número: "))
        numero2 = int(input("Digite outro número: "))
    elif condicao == 5:
        pass
    else:
        print("Opção inválida, digite uma dos menu")