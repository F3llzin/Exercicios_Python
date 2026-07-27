expressao = input("Digite uma expressão: ")
parentese_aberto = 0
parentese_fechado = 0

for i in expressao:
    if i == "(":
        parentese_aberto += 1
    if i == ")":
        parentese_fechado += 1

if parentese_aberto == parentese_fechado:
    print("Essa expressão é válida")
else:
    print("Expressão inválida")
