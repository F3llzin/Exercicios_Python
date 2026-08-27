from random import randint
from time import sleep
from operator import itemgetter

jogadores = {
    'jogador 1' : 0,
    'jogador 2' : 0,
    'jogador 3' : 0,
    'jogador 4' : 0
}

ranking = list()

print("Valores sorteados:")

for k in jogadores.keys():
    jogadores[k] = randint(1, 6)

for k, v in jogadores.items():
    print(f"    O {k} tirou {v}")
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print("Ranking dos jogadores: ")

for k, v in enumerate(ranking):
    print(f"    {k + 1}° Lugar = O {v[0]} tirou {v[1]}")
    sleep(1)

