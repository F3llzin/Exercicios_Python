from random import randint

numero = int(input("Tente adivinhar o número que estou pensando entre 0 e 5: "))

sorteio = randint(0, 5)

print(f"Número em que pensei: {sorteio}")

if numero == sorteio:
    print("Parabéns, você acertou o número pensado!")
elif numero > sorteio:
    print("Chute alto, mais sorte na próxima")
elif numero < sorteio: 
    print("Chute baixo, mais sorte na próxima!")