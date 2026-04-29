from datetime import datetime

ano_atual = datetime.now().year

menor = 0
maior = 0


for i in range(0, 7):
    ano_nascimento = int(input("Digite o ano do seu nascimento: "))
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f"A quantidade de maiores de idade são: {maior}, menores são: {menor}")