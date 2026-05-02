'''Crie um programa que leia vários números inteiros, calcule a média, o maior e o menor 
valor e mostre na tela os resultados e quantos números foram digitados, 
perguntando ao usuário se deseja continuar a cada novo número.'''
contador = 1
soma = 0
media = 0
maior = 0
menor = 0
valores = int(input("Digite um número "))
resposta = input("Deseja continuar [S/N]? ").upper()

while resposta != "N":
    menor = valores
    maior = valores
    soma += valores
    media = soma / contador
    contador += 1
    valores = int(input("Digite um número "))
    soma += valores
    if valores > maior:
        maior = valores
    if valores < menor:
        menor = valores
    resposta = input("Deseja continuar [S/N]? ").upper()
 
print(f"Você digitou {contador} números, {media:.2f} é a média entre esses números, o maior é {maior} e o menor é {menor}")


#corrigir esse exercício