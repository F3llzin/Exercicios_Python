'''Crie um programa que simule quatro jogadores lançando um dado, 
gere resultados aleatórios, armazene os resultados em um dicionário 
e mostre na tela a classificação dos jogadores em ordem decrescente, 
considerando como vencedor quem obtiver o maior valor no dado.'''

from random import randint
from time import sleep

jogadores = {
    'jogador1' : 0,
    'jogador2' : 0,
    'jogador3' : 0,
    'jogador4' : 0
}

print("Valores sorteados:")

for k in jogadores.keys():
    jogadores[k] = randint(1, 6)

for k, v in jogadores.items():
    print(f"    O {k} tirou {v}")
    sleep(1)

print("Ranking dos jogadores: ")

for k in jogadores:
    maior = 0
    for j in jogadores:
        if jogadores[j] > maior:
            maior = jogadores[j]
        

    jogadores[k] = maior