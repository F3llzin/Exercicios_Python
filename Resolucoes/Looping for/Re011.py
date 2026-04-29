'''Crie um programa que leia o nome, idade e sexo de quatro pessoas, 
calcule a média de idade do grupo e mostre na tela a média, 
o nome do homem mais velho e quantas mulheres têm menos de vinte anos.'''
mulheres_menores = 0
contador = 0
homem_maior = ""
soma = 0

for i in range(0, 4):
    nome, idade, sexo = input("Digite o sexo: ").split()

    nome = nome.lower()
    sexo = sexo.lower()
    idade = int(idade)

    soma += idade
    media = soma / 4

    if sexo == "feminino" and idade < 20:
        mulheres_menores += 1

    if sexo == "masculino" and contador > idade:
        contador = idade
        homem_maior = nome
        print("F")
    

print(mulheres_menores)
print(media, homem_maior)







# não consegui fazer, revisitar exercício