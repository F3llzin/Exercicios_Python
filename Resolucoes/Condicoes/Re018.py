from random import choice

jogador = input("Escolha entre pedra, papel e tesoura: ").lower()
maquina = ["pedra", "papel", "tesoura"]

escolha_maquina = choice(maquina)

if jogador == escolha_maquina:
    print(f"Ops, deu empate! Sua escolha foi: {jogador} e a minha foi: {escolha_maquina}")
elif jogador == "pedra" and escolha_maquina == "tesoura":
    print(f"Você me venceu! Sua escolha foi: {jogador} e a minha foi: {escolha_maquina}")
elif jogador == "pedra" and escolha_maquina == "papel":
    print(f"Eu te venci! Sua escolha foi: {jogador} e a minha foi: {escolha_maquina}")
elif jogador == "papel" and escolha_maquina == "pedra":
    print(f"Você me venceu! Sua escolha foi: {jogador} e a minha foi: {escolha_maquina}")
elif jogador == "papel" and escolha_maquina == "tesoura":
    print(f"Eu te venci! Sua escolha foi: {jogador} e a minha foi: {escolha_maquina}")
elif jogador == "tesoura" and escolha_maquina == "papel":
    print(f"Você me venceu! Sua escolha foi: {jogador} e a minha foi: {escolha_maquina}")
elif jogador == "tesoura" and escolha_maquina == "pedra":
    print(f"Eu te venci! Sua escolha foi: {jogador} e a minha foi: {escolha_maquina}")
else:
    print("Opção inválida.")