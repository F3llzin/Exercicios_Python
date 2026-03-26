numero1, numero2, numero3, numero4 = input().split()

numero1 = float(numero1)
numero2 = float(numero2)
numero3 = float(numero3)
numero4 = float(numero4)

# 2.0 4.0 7.5 8.0
# 6.4
media = (numero1 * 2 + numero2 * 3 + numero3 * 4 + numero4 * 1) / 10

print(f"Media: {media:.1f}")

if media >= 7:
    print("Aluno aprovado.")
elif media >= 5 and media < 7:
    print("Aluno em exame.")
    nota_exame = float(input("Nota do exame: "))
    media_exame = (media + nota_exame) / 2
    if media_exame >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Média final: {media_exame:.1f}")
else:
    print("Aluno reprovado")