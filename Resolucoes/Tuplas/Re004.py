numero1 = int(input("Digite o 1° número: "))
numero2 = int(input("Digite o 2° número: "))
numero3 = int(input("Digite o 3° número: "))
numero4 = int(input("Digite o 4° número: "))

numeros = (numero1, numero2, numero3, numero4)

print(f"A quantidade de vezes que apareceu o valor '9' foi: {numeros.count(9)}")

if 3 in numeros:
    print(f"A posição que o valor '3' foi digitado é: {numeros.index(3) + 1}°")
else:
    print("O número 3 não foi digitado")

print("Os valores digitados que são pares:", end=(" "))

for i in numeros:
    if i % 2 == 0:
        print(i, end=(" "))
