from random import randint

vitorias = 0

while True:
    jogador = int(input("Digite um número para jogar par ou impar: "))
    par_impar = input("Escolha entre par ou ímpar[P/I]: ").upper()[:1]
    maquina = randint(0, 10)
    soma = jogador + maquina
    resultado = ""

    if soma % 2 == 1:
        resultado = "IÍ"
    else:
        resultado = "P"

    print(f"{"=" * 50}\nVocê escolheu {jogador} e eu escolhi {maquina}. O total é: {soma}\n{"=" * 50}")

    if par_impar in resultado:
        print("Parabéns, você venceu! Vamos jogar de novo!")
        vitorias += 1
    else: 
        print("Você perdeu! Paramos por aqui!")
        break

print(f"A quantidade de vitórias consecutivas que você obteve foi: {vitorias}")
