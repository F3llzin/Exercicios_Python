numeros_extenso = ("ZERO", "UM", "DOIS", "TRÊS", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVE", "DEZ", "ONZE", "DOZE", "TREZE", "QUATORZE", "QUINZE", "DEZESSEIS", "DEZESETE", "DEZOITO", "DEZENOVE", "VINTE")

numero = int(input("Digite um número de 0 a 20: "))

while True:

    if numero not in range(0, 21):
        numero = int(input("Digite um número de 0 a 20: "))
    else: 
        break


print(f"O número: {numero} por extenso é: {numeros_extenso[numero]}")