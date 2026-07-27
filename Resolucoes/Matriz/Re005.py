from time import sleep
from random import randint

matriz = []

jogos = int(input("Quantos jogos serão gerados? "))

for i in range(jogos):
    jogo = []
    for j in range(6):
        numero = randint(1, 60)

        if numero not in jogo:
            jogo.append(numero)
        else:
            numero = randint(1, 60)
            jogo.append(numero)


    matriz.append(sorted(jogo))

for p, c in enumerate(matriz):
    print(f"O seu {p + 1}° jogo é: {c}")
    sleep(1)

print("Fim")
