from random import randint

numero1 = randint(0, 10)
numero2 = randint(0, 10)
numero3 = randint(0, 10)
numero4 = randint(0, 10)
numero5 = randint(0, 10)

numeros = (numero1, numero2, numero3, numero4, numero5)

print("Os números sorteados foram: ", end=(""))

for i in range(0, len(numeros)):
    print(numeros[i], end=(" "))

numeros = sorted(numeros)

print(f"\nO menor número é: {numeros[0]}")
print(f"O maior número é: {numeros[-1]}")