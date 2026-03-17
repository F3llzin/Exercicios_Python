nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

media = (nota1 + nota2) / 2

print(f"A média dele foi: \033[35m{media:.1f}\033[m")

#"\033[m" é apenas para dar cor ao número no terminal  