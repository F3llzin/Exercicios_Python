from random import randint

maquina = randint(0, 10)
jogador = int(input())
palpite = 0

while maquina != jogador:
    print("Você falhou, tente novamente!")
    jogador = int(input())
    palpite += 1

if palpite == 0:
    palpite += 1
    
print(f"Você acertou! A quantidade de palpites foi: {palpite}")

#melhore esse programa colocando se o número está para mais ou para menos