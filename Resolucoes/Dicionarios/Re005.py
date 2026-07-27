pessoas = []

soma = 0

while True:
    pessoa = {
        'nome' : "",
        'sexo' : "",
        'idade' : 0
    }

    pessoa["nome"] = input("Nome: ")
    pessoa["sexo"] = input("Sexo[M/F]: ").upper().strip()[0]

    while pessoa["sexo"] not in "MF" :
            pessoa["sexo"] = input("Sexo[M/F]: ").upper().strip()[0]

    pessoa["idade"] = int(input("Idade: "))

    soma += pessoa["idade"]

    resposta = input("Deseja continuar[S/N]? ").upper().strip()[0]

    while resposta not in "SN" :
        resposta = input("Deseja continuar[S/N]? ").upper().strip()[0]

    pessoas.append(pessoa)

    if resposta == "N" :
        break


media = soma / (len(pessoas))

print("=-" * 50)
print(f"O grupo tem {len(pessoas)} pessoas.")
print(f"A média de idade é de {media:.2f} anos.")
print("As mulheres cadastradas foram: ", end=(""))

for i in range(len(pessoas)) :
    if pessoas[i]['sexo'] == "F":
        print(pessoas[i]['nome'], end=(" "))

print("\nA lista das pessoas que estão acima da média:")

for i in range(len(pessoas)) :
    if pessoas[i]['idade'] > media:
        print()
        for k, v in pessoas[i].items():
            print(f"{k} = {v}; ", end=(""))
        print()