primeiro_termo_pa = int(input("Digite o primeiro termo da PA: "))
razao_pa = int(input("Digite a razão dessa PA: "))
ultimo_termo = 10

while ultimo_termo > 0:
    print(primeiro_termo_pa + (ultimo_termo - 1) * razao_pa, end=(" "))
    ultimo_termo -= 1
