numero1, numero2, numero3 = input().split()

numero1, numero2, numero3 = int(numero1), int(numero2), int(numero3)

if numero1 > numero2:
    menor = numero2
    numero2 = numero1
    numero1 = menor
if numero1 > numero3:
    menor = numero3
    numero3 = numero1
    numero1 = menor
if numero2 > numero3:
    menor = numero3
    numero3 = numero2
    numero2 = menor

print(f"O maior numero entre eles é: {numero3} e o menor é: {numero1}")