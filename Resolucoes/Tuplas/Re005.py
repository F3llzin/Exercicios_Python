lista = ("Lápis", 1.75, "Borracha", 2, "Caderno", 15.9, "Estojo", 25, "Tranferidor", 4.2, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.3, "Livro", 34.9)
valor = 0

print(f'''{"=" * 46}
{"TABELA DE PREÇOS":^45}
{"=" * 46}''')

for i in range(len(lista)):
    if i % 2 == 0:
        print(f"{lista[i]:.<20}", end=(""))
    else: 
        valor = f"{float(lista[i]):.2f}"
        print(f"{"R$":.>20}{valor}")
