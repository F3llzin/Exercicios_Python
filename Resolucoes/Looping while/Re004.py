numero = int(input("Digite um número para fazermos seu fatorial: "))
antecessor = numero
resultado = 1


print(f"{numero}! = ", end=(""))

while antecessor > 1:
    print(f"{antecessor}", end=(" X "))
    antecessor -= 1
    resultado *= antecessor

print(f"1 = {numero * resultado}")