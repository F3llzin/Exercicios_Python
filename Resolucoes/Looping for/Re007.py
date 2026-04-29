'''Crie um programa que leia um número inteiro 
e mostre na tela se ele é ou não primo.'''
numero = int(input("Digite um número: "))

if (numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0) and numero != 1 or numero == 2:
    print("Ele é primo")
else: 
    print("Não é primo")



# não consegui fazer, revisitar exercício