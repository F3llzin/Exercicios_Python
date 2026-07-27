numeros = []
posicao = 0

for i in range(5):
    numero = int(input("Digite um número: "))

    numeros.append(numero)

print(f"Você digitou os valores: {numeros}")
print(f"O maior número da lista é: {max(numeros)} e a sua posição é: ", end=(""))

maior = numeros[0]

for a in range(len(numeros)):
    if a != 0:
        if maior <= numeros[a]:
            maior = numeros[a]
            posicao = a
            print(posicao, end=(" "))
    elif numeros.index(max(numeros)) == 0:
        posicao = a
        print(posicao, end=(" "))

print(f"\nO menor número da lista é: {min(numeros)} e a sua posição é: ", end=(""))

posicao = 0
menor = numeros[0]

for s in range(len(numeros)):
    if s != 0:
        if menor >= numeros[s]:
            menor = numeros[s]
            posicao = s
            print(posicao, end=(" "))
    elif numeros.index(min(numeros)) == 0:
        posicao = s
        print(posicao, end=(" "))
