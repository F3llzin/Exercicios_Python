def entrada(texto) :
    tupla = (texto)
    print("\033[42m")

    for i in range(len(tupla) + 4):
        print("~", end=(""))

    print("\033[42m")
    print(f"  {texto}")

    for i in range(len(tupla) + 4):
        print("~", end=(""))

    print("\033[m", end=(""))

def controle(texto) :
    tupla = (texto)
    print("\033[45m")

    for i in range(len(tupla) + 7 + len(n)):
        print("~", end=(""))

    print("\033[45m")
    print(f"  {texto} '{n}'")

    for i in range(len(tupla) + 7 + len(n)):
        print("~", end=(""))

    print("\033[m", end=(""))

def corpo() :
    print("\033[46m")
    help(n)
    print("\033[m", end=(""))

def fim() :
    print("\033[31;41m\n~~~~~~~~~~~~~", end=(""))
    print("\n  ATÉ LOGO.")
    print("~~~~~~~~~~~~~\033[m")


#programa principal
while True: 
    entrada("SISTEMA DE AJUDA PyHELP")
    n = input("\nFunção ou Biblioteca > ")

    if n.upper() == "FIM":
        fim()
        break

    controle("Acessando o manual do comando")
    corpo()
