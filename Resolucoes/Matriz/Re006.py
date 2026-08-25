alunos = []
condicao = "s"

while condicao[0] == "s":
    notas = []
    
    alunos.append(input("Digite o nome do aluno: "))
    notas.append(float(input("Digite a 1° nota do aluno: ")))
    notas.append(float(input("Digite a 2° nota do aluno: ")))
    condicao = input("Deseja cadastrar outro aluno[S/N]? ").strip().lower()

    alunos.append(notas)

    while condicao[0] not in "sn":
        condicao = input("Deseja cadastrar outro aluno[S/N]? ").strip().lower()
    

media = soma = 0

print("-_" * 15)
print("No.  Nome             Média")
print("-_" * 15)

for i in range(len(alunos)):
    if i % 2 == 1:
        for j in range(len(alunos[i])):
            soma += alunos[i][j]
            
        media = soma / 2
        print(f"         {media:.1f}")
        media = soma = 0
    else:
        print(f"{i//2}    {alunos[i]}", end=(""))

while True:
    print("-_" * 15)
    resposta = int(input("Mostrar notas de qual aluno? (999 interrompe): "))

    if resposta == 999:
        break

    resposta *= 2
    print(resposta)

    if resposta >= len(alunos) or resposta < 0:
        print("Não há esse número, digite novamente.")
    else:
        print(f"Notas de {alunos[resposta]} são {alunos[resposta + 1]}")


print("Finalizando, Volte sempre")