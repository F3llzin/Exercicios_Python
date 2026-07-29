from time import sleep

def contador(inicio, fim, passo) :
    if passo == 0:
        passo = 1

    if passo < 0:
        passo = -passo

    print("=-" * 20)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")

    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=(" "), flush=True)
            sleep(0.25)
    elif inicio > fim:
        while inicio >= fim:
            print(inicio, end=(" "), flush=True)

            inicio -= passo
            sleep(0.25)

    print("FIM!")


contador(1, 10, 0)
contador(10, 0, 2)

print("=-" * 20)
print("Agora é sua vez de personalizar a contagem!")

inicio = int(input(f"Início: {"":>10}"))
fim = int(input(f"Fim: {"":>13}"))
passo = int(input(f"Passo: {"":>11}"))

contador(inicio, fim, passo)
