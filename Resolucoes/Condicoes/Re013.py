numeroa = int(input("Digite um valor: "))
numerob = int(input("Digite um outro valor: "))

if numeroa > numerob:
    print("O primeiro número é maior que o segundo.")
elif numerob > numeroa:
    print("O segundo número é maior que o primeiro.")
else:
    print("Não há números maiores que o outro, eles são iguais.")