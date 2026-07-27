jogador = {
    'nome' : "",
    'gols' : [],
    'total' : 0
}

jogador['nome'] = input("Nome do jogador: ")
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for i in range(partidas) :
    jogador['gols'].append(int(input(f"Quantos gols na partida {i}? ")))

for i in range(len(jogador['gols'])) :
    jogador['total'] += jogador['gols'][i]

print("=-" * 60)
print(jogador)
print("=-" * 60)

for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}.")

print("=-" * 60)

print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")

for i in range(len(jogador['gols'])) :
    print(f"    => Na partida {i}, fez {jogador['gols'][i]} gols.")

print(f"Foi um total de {jogador['total']} gols.")