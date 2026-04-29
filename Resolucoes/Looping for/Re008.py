'''Crie um programa que leia uma frase, desconsidere espaços e acentos 
e mostre na tela se ela é ou não um palíndromo.'''
frase = input("Digite uma frase: ").lower()

for i in frase[::-1]:
    if i == frase: 
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")







# não consegui fazer, revisitar exercício