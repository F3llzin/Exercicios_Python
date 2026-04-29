primeiro_termo = int(input("Digite um número para ser o termo da PA: "))
razao = int(input("Digite um número para ser a razão da PA: "))

for i in range(10, 0, -1):
    print(primeiro_termo + (i - 1) * razao, end=(" "))