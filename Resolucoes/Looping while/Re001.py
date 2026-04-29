sexo_usuario = input("Digite seu sexo(M/F): ").upper().strip()

while sexo_usuario != "M" and sexo_usuario != "F":
    print("Sexo inválido, por favor, escreva um sexo válido(M/F)")
    sexo_usuario = input("Digite seu sexo(M/F): ").upper()

print(f"Seu sexo é {sexo_usuario}")