nome = input("Digite seu nome: ")
nome_alterado = nome.strip()

nome = nome.lower()
print("Seu nome em minúsculas é: ", nome)

nome = nome.upper()
print("Seu nome em maiúsculas é: ", nome)

nome_alterado = nome_alterado.replace(" ", "")
print("A quantidade de letras do seu nome é: ", len(nome_alterado))

nome = nome.split()
print("A quantidade de letras do seu primeiro nome é: ", len(nome[0]))