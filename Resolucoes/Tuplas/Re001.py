numeros_extenso = ("ZERO", "UM", "DOIS", "TRÊS", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVE", "DEZ", "ONZE", "DOZE", "TREZE", "QUATORZE", "QUINZE", "DEZESSEIS", "DEZESETE", "DEZOITO", "DEZENOVE", "VINTE")

while True:
    numero = int(input("Digite um número de 0 a 20: "))

    while numero < 0 or numero >= 21:
        numero = int(input("Digite um número de 0 a 20: "))
    else: 
        pass

    print(f"O número: {numero} por extenso é: {numeros_extenso[numero]}")

    while True:
        continuar = input("Quer continuar? ").lower()
        

        if continuar[0] not in "sn":
            continue
        else:
            break
    
    if continuar[0] == "s":
        pass
    else:
        break

print("FIM")