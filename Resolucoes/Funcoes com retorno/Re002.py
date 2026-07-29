def fatorial(numero, show = False) :
    """
    =>Calcula o fatorial de um número
        para número: O valor a ser calculado
        para show: Mostra ou não o calculo e é uma variável opcional
        return: Retorna o cálculo do valor n informado
    """
    fatorial = 1

    print("-" * 30)

    for i in range(numero, 0, -1) :
        if show == True:
            if i == 1:
                print(i, end=(" = "))
            else:
                print(i, end=(" * "))
        fatorial *= i

    return fatorial


print(fatorial(5, True))
