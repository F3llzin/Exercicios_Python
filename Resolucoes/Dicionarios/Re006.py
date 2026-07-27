jogadores = []
a = ""

while True:
    jogador = {
        'nome' : "",
        'gols' : [],
        'total' : 0
    }

    print("-" * 20)

    jogador['nome'] = input("Nome do jogador: ")
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    for i in range(partidas) :
        jogador['gols'].append(int(input(f"Quantos gols na partida {i}? ")))
        jogador['total'] += jogador['gols'][i]

    resposta = input("Deseja continuar[S/N]? ").upper().strip()[0]
    
    while resposta not in "SN" :
        resposta = input("Deseja continuar[S/N]? ").upper().strip()[0]

    jogadores.append(jogador)

    if resposta == "N":
        break


print("=-" * 50)
print(f"cód nome{a:<20}gols{a:^20}total{a:>20}")
print("-" * 70)

for i in range(len(jogadores)) :
    print(f"    {i}", end=(" "))

    for j in jogadores[i]:
        if j == 'nome' :
            print(f"{jogadores[i][j]:<20}", end=(" "))
        elif j == 'gols' :
            print(f"{jogadores[i][j]}", end=(" "))
        elif j == 'total' :
            print(f"{jogadores[i][j]:<20}", end=(" "))
    
    print()

print("-" * 70)

while True:
    codigo = int(input("Mostrar dados de qual jogador? "))

    if codigo > len(jogadores) or codigo < 0:
        if codigo == 999:
                break
        print(f"ERRO! Não existe jogador de código {codigo}! Tente novamente")
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {jogadores[codigo]['nome']}:")

        for i in range(len(jogadores[codigo]['gols'])) :
            print(f"    No jogo {i} fez {jogadores[codigo]['gols'][i]} gols.")

    print("-" * 70)
