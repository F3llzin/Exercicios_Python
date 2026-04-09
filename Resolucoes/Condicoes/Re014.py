from datetime import datetime

ano_atual = datetime.now().year
ano_nascimento = int(input("Digite o seu ano de nascimento: "))

idade_usuario = ano_atual - ano_nascimento

if idade_usuario < 18:
    print(f"Ainda não chegou a sua hora de se alistar, ainda falta {18 - idade_usuario} anos para isso.")
elif idade_usuario == 18:
    print("Ótimo! Chegou sua vez de se alistar.")
elif idade_usuario > 18:
    print(f"Oh oh! A sua hora de se alistar já passou. O tempo passado foi {idade_usuario - 18} anos.")