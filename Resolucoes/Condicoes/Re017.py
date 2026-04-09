preco_produto = float(input("Digite o valor do produto: "))
forma_pagamento = input("Digite a forma de pagamento(dinheiro, boleto ou cartão): ").lower()
preco_final = 0

if forma_pagamento == "dinheiro" or forma_pagamento == "cheque":
    preco_final = preco_produto - preco_produto * 0.1
    print(f"O valor a ser pago é: {preco_final:.2f}")
elif forma_pagamento == "cartao" or forma_pagamento == "cartão":
    forma_pagamento_cartao = input("Digite se quer pagar à vista ou parcelado: ").lower()
    if forma_pagamento_cartao == "à vista" or forma_pagamento_cartao == "a vista":
        preco_final = preco_produto - preco_produto * 0.05
        print(f"O valor a ser pago é: {preco_final:.2f}")
    elif forma_pagamento_cartao == "parcelado":
        parcelas = int(input("Escolha quantas vezes quer parcelar: "))
        if parcelas == 2:
            print(f"O valor a ser pago é: {preco_produto:.2f}, de {parcelas} parcelas de {preco_produto / parcelas}")
        elif parcelas >= 3:
            preco_final = (preco_produto + preco_produto * 0.2) / parcelas
            preco_final = preco_final * parcelas
            print(f"O valor a ser pago é: {preco_final:.2f}")
    else:
        print("O que foi digitado não está nas opções.")
else:
    print("O que foi digitado não está nas opções.")