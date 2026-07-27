'''Crie um programa que leia cinco valores 
e os armazene em uma lista em ordem crescente 
sem utilizar o sort(), mostrando na tela 
em qual posição cada valor foi inserido.'''
numeros = []
x = y = z = maior = 0

for i in range(5):
    numero = int(input("Digite um número: "))

    if numero > z:
        z = numero
        y = x
        x = y
    if x > y:
        y = x
        x = y
    if numero > x:
        pass