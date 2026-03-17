import math

cateto_oposto = int(input("Digite o valor do cateto oposto: "))
cateto_adjacente = int(input("Digite o valor do cateto adjacente: "))

hipotenusa = math.sqrt(math.pow(cateto_oposto, 2) + math.pow(cateto_adjacente, 2))

print(f"O valor da hipotenusa é {hipotenusa}")