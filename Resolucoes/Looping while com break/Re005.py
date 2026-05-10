resposta = "S"
nome_menor_valor = ""
total = 0
contagem = 0
menor_valor = 0
maior_que_mil = 0

while True:
    if resposta == "N":
        break
    else:
        nome_produto = input("Digite o nome do produto: ")
        preco_produto = float(input("Digite o preço do produto: R$"))

        total += preco_produto

        contagem += 1
        
        if contagem == 1:
            menor_valor = preco_produto
            nome_menor_valor = nome_produto
        else:
            if preco_produto < menor_valor:
                menor_valor = preco_produto
                nome_menor_valor = nome_produto

        if preco_produto > 1000:
            maior_que_mil += 1

        resposta = input("Deseja continuar? [S/N] ").upper()[:1]

        while resposta not in "SN":
            print("Resposta inválida, digite uma válida[S/N]: ")
            resposta = input("Deseja continuar? [S/N] ").upper()[:1]

print(f'''Total da compra foi: {total}
A quantidade de ítens com mais de mil reais: {maior_que_mil}
O nome do ítem com menor preço: {nome_menor_valor}''')