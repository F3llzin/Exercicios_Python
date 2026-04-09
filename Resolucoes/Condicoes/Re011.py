valor_casa = float(input("Digite o valor da casa que quer comprar: "))
salario = float(input("Digite o seu salário: "))
tempo = int(input("Digite em quantos anos pretende quitar a casa: "))

tempo = tempo * 12

calculo_prestacoes = valor_casa / tempo
condicao = salario * 0.30

if calculo_prestacoes <= condicao:
    print(f"Perfeito o seu empréstimo está aprovado, o valor das prestações é {calculo_prestacoes:.2f}")
else:
    print(f"O seu empréstimo foi recusado, pois o valor da prestação é {calculo_prestacoes:.2f} e 30% do seu salário é: {condicao:.2f}")