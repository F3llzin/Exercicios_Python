from time import sleep

def maior(*numeros) :
    maior = 0

    print("-=" * 20)
    print("Analisando os valores passados...")

    for i in numeros:
        print(i, end=(" "), flush=True)
        sleep(0.25)

    print(f"Foram informados {len(numeros)} valores ao todo.")

    if numeros != None:
        for i in range(len(numeros)):
            if i == 0:
                maior = numeros[i]
            else:
                if maior < numeros[i]:
                    maior = numeros[i]
    else:
        pass

    print(f"O maior valor informado foi {maior}.")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()