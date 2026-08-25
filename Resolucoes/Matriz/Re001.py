pessoas = []
continuar = "S"

while continuar == "S":
    pessoa = []
    
    pessoa.append(input("Digite seu nome: "))
    pessoa.append(float(input("Digite seu peso: ")))
    
    pessoas.append(pessoa)

    continuar = input("Deseja conttinuar[S/N]? ").upper().strip()

    while continuar[0] not in "SN":
        continuar = input("Deseja conttinuar[S/N]? ").upper().strip()

print(f"A quantidade de pessoas cadastradas são: {len(pessoas)}")

nome_maior_peso = []
nome_menor_peso = []
maior_peso = pessoas[0][1]
menor_peso = pessoas[0][1]

for p in range(len(pessoas)):
    if pessoas[p][1] >= maior_peso:
        maior_peso = pessoas[p][1]

    if pessoas[p][1] <= menor_peso:
        menor_peso = pessoas[p][1]

for p in range(len(pessoas)):
    if pessoas[p][1] == maior_peso:
            nome_maior_peso.append(pessoas[p][0])

    if pessoas[p][1] == menor_peso:
            nome_menor_peso.append(pessoas[p][0])
    

print(f"O maior peso foi de {maior_peso:.2f}KG. Peso de ", end=(""))

for i in nome_maior_peso:
    print(f"[{i}] ", end=(""))

print()

print(f"O menor peso foi de {menor_peso:.2f}KG. Peso de ", end=(""))

for i in nome_menor_peso:
    print(f"[{i}] ", end=(""))