mulheres_menores = soma = homem_idade_maior = 0
homem_maior = ""

for i in range(0, 4):
    nome = input("Digite o nome: ").strip()
    idade = int(input("Digite a sua idade: "))
    sexo = input("Digite o seu sexo: ").upper().strip()[:1]

    soma += idade

    if sexo in "F" and idade < 20:
        mulheres_menores += 1

    if sexo in "M":
        if i == 0 or idade > homem_idade_maior:
            homem_maior = nome
            homem_idade_maior = idade


    
media = soma / 4

print(f"A média das idades é: {media}, o homem mais velho é: {homem_maior} e a quantidade de mulheres que tem menos de vinte é: {mulheres_menores}")
