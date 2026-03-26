nome = input("Digite seu nome: ")
nome_alterado = nome

nome = nome.lower()
print(nome)

nome = nome.upper()
print(nome)

nome_alterado = nome_alterado.replace(" ", "")
print(len(nome))

nome = nome.split()
print(len(nome[0]))