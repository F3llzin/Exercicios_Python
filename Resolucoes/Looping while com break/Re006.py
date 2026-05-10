cedula = int(input("Digite um valor a ser sacado: R$"))
valor = 50
quantidade_cedula = 0

while True:
    if cedula >= valor:
        cedula -= valor
        quantidade_cedula += 1
    else:
        if quantidade_cedula > 0:
            print(f"Tem {quantidade_cedula} cédulas de {valor}R$.")
        if valor == 50:
            valor = 20
        elif valor == 20:
            valor = 10
        elif valor == 10:
            valor = 1
        quantidade_cedula = 0
        if cedula == 0:
            break
