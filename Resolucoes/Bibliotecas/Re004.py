import random

aluno1 = input("Digite o nome do aluno número um: ")
aluno2 = input("Digite o nome do aluno número dois: ")
aluno3 = input("Digite o nome do aluno número três: ")
aluno4 = input("Digite o nome do aluno número quatro: ")
alunos = aluno1, aluno2, aluno3, aluno4

sorteado = random.choice(alunos)

print(f"O nome do aluno sorteado é: {sorteado}")