'''Crie um programa que leia vários números inteiros, calcule a média, o maior e o menor 
valor e mostre na tela os resultados, perguntando ao usuário se deseja continuar a cada novo número.'''
contador = 1
soma = 0
media = 0
maior = 0
menor = 0
resposta = "S"
valores = 0

while resposta != "N":
    valores = int(input("Digite um número"))
    soma += valores
    media = soma / contador
    contador += 1
    if valores > maior:
        maior = valores
    if valores < menor:
        menor = valores
    print(f"{media} a média entre esses números, o maior é {maior} e o menor é {menor}")
    resposta = input("Deseja continuar [S/N]? ").upper()