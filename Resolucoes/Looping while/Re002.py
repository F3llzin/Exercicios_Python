from random import randint

maquina = randint(0, 10)
jogador = int(input())
palpite = 0

while maquina != jogador:
    jogador = int(input())
    palpite += 1

    if jogador < maquina:
        print("Hm... O número é maior")
    elif jogador > maquina:
        print("Hm... O número é menor") 

    print("Você falhou, tente novamente!")

if palpite == 0:
    palpite += 1
    
print(f"Você acertou! A quantidade de palpites foi: {palpite}")

