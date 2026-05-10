resposta = "S"
condicao = soma = media = maior = menor = numeros_digitados = 0

while resposta == "S":
    numeros = int(input("Digite um número: "))

    numeros_digitados += 1
    condicao += 1

    soma += numeros
    media = soma / numeros_digitados

    if condicao == 1:
        maior = numeros
        menor = numeros
    else: 
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros

    resposta = input("Digite uma resposta[S/N]: ").upper().strip()[:1]

    while resposta not in "NS":
        print("Valor inválido, digite outro!")
        resposta = input("Digite uma resposta válida[S/N]: ").upper().strip()[:1]

print(f"O maior número é: {maior}, o menor número é: {menor}, a média é: {media} e a quantidade é: {numeros_digitados}")
