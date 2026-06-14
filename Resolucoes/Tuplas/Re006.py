from time import sleep

palavras = ("aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro")
vogais = ("a", "e", "i", "o", "u")

for i in palavras:
    print(f"A palavra: {i} tem as vogais:", end=(" "))

    for j in vogais:
        if j in i:
            print(j, end=(" "))

    print()
    sleep(1)

print("Fim")
