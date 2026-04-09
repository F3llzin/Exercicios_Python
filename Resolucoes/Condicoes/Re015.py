from datetime import datetime

ano_atual = datetime.now().year
ano_nascimento = int(input("Digite o ano do seu nascimento: "))

idade = ano_atual - ano_nascimento

if idade >= 7 and idade <= 9:
    print("Sua categoria é Mirim.")
elif idade >= 10 and idade <= 14:
    print("Sua categoria é Infantil.")
elif idade >= 15 and idade <= 19:
    print("Sua categoria é Junior.")
elif idade == 20:
    print("Sua categoria é Sênior.")
elif idade > 20:
    print("Sua categoria é Master.")
else:
    print("Essa idade não é válida para participar")