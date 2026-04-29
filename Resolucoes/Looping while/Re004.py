numero = int(input("Digite um número para fazermos seu fatorial: "))
antecessor = numero
resultado = 1

while antecessor > 1:
    antecessor -= 1
    resultado *= antecessor

print(f"{numero}! = {numero * resultado}")
