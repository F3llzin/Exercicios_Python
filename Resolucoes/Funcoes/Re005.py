from random import randint

def somaPar(lista) :
    soma = 0

    print(f"Somando os valores pares de {lista}, temos", end=(" "))

    for i in lista:
        if i % 2 == 0:
            soma += i

    print(soma)

def sorteia(lista) :
    for i in range(5):
        lista.append(randint(1, 10))

    print("Sorteando os 5 valores da lista: ", end=(""))

    for i in lista:
        print(i, end=(" "))

    print("PRONTO!")
        


numeros = []
sorteia(numeros)
somaPar(numeros)