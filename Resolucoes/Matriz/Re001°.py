'''Crie um programa que leia o nome e o peso de várias pessoas, 
perguntando ao usuário se deseja continuar após cada cadastro, 
armazenando todos os dados em uma lista e mostrando na tela 
ao final quantas pessoas foram cadastradas, quais são as pessoas 
mais pesadas e quais são as pessoas mais leves, exibindo todas elas em caso de empate.'''
pessoas = []
continuar = "S"

while continuar == "S":
    pessoa = []
    
    pessoa.append(input("Digite seu nome: "))
    pessoa.append(int(input("Digite seu peso: ")))
    
    pessoas.append(pessoa)

    continuar = input("Deseja conttinuar[S/N]? ").upper().strip()

    while continuar[0] not in "SN":
        continuar = input("Deseja conttinuar[S/N]? ").upper().strip()

print(f"A quantidade de pessoas cadastradas são: {len(pessoas)}")

nome_maior_peso = []
maior_peso = pessoas[0][1]

for p in pessoas:
    if p[1] >= maior_peso:
        maior_peso = p[1]
        nome_maior_peso.append(p[0])

print(maior_peso, nome_maior_peso)

# print(f"O maior peso foi de {max((pessoas[1]))}")