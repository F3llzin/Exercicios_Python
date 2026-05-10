frase = input("Digite uma frase: ").lower().strip().replace(" ","")
palindromo = frase[::-1]

print(palindromo)

if frase == palindromo:
    print(f"A frase: {frase} é um palíndromo")
else:
    print(f"A frase: {frase} não é um palindromo")

