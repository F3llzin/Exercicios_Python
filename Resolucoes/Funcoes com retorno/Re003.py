def ficha(nome = "<desconhecido>",  gols=0):
    return f"O jogador {nome} fez {gols} gol(s) no campeonato."


print("-" * 30)
jogador = input("Nome do jogador: ")
gol = input("Número de gols: ")


if gol.isdigit():
    gol = int(gol)
    if jogador.strip() == '' :
        print(ficha(gols=gol))
    else :
        print(ficha(jogador, gol))
else:
    if jogador.strip() == '' :
        print(ficha())
    else :
        print(ficha(jogador))


