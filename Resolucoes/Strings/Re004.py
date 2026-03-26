'''Crie um programa que leia o nome completo
e mostre na tela se tem ou não 'Silva' no nome'''
nome = input("Digite o seu nome: ")


if nome.lower().find("silva") != -1:
    print("O nome da sua cidade tem 'Silva'")
else:
    print("O nome da sua cidade não tem 'Silva'")