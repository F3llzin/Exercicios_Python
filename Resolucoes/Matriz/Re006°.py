'''Crie um programa que leia o nome e duas notas de vários alunos, 
armazenando os dados em uma lista composta e mostrando 
na tela um boletim com a média de cada aluno, permitindo que o 
usuário consulte individualmente as notas de qualquer aluno cadastrado.'''
alunos = []
condicao = "s"

while condicao[0] == "s":
    notas = []
    
    alunos.append(input("Digite o nome do aluno: "))
    notas.append(int(input("Digite a 1° nota do aluno: ")))
    notas.append(int(input("Digite a 2° nota do aluno: ")))
    condicao = input("Deseja cadastrar outro aluno[S/N]? ").strip().lower()

    while condicao[0] not in "sn":
        condicao = input("Deseja cadastrar outro aluno[S/N]? ").strip().lower()
    
    alunos.append(notas)

media = soma = 0

for i in len(alunos):
    if i % 2 == 1:
        for j in len(notas):
            soma += notas[j]
            
        media = soma / 2
        print(media)
        media = soma = 0


print(alunos)
