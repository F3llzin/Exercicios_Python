from random import randint

numero = int(input("Digite um número e tente adivinhar o que estou pensando: "))

sorteio = randint(0, 5)

print(f"Número em que pensei: {sorteio}")

if numero == sorteio:
    print("Parabéns, você acertou o número pensado!")
elif numero > sorteio:
    print("Chute alto, mais sorte na próxima")
elif numero < sorteio: 
    print("Chute baixo, mais sorte na próxima!")