ano = int(input("Digite um ano do calendário Gregoriano: "))
multiplo = False

mil = ano % 1000    #Reduz o ano para verificação dos três últimos números

if ano % 100 == 0:    #Verifica se é multiplo de 100
    multiplo = True

if ano < 1582:
    print("Esse ano não está no calendário Gregoriano.")
elif mil != 0 and multiplo == False:
    bissexto = mil % 4
    if bissexto == 0:
        print("Esse ano é bissexto")
    else:
        print("Esse ano não é bissexto")
else:
    if multiplo == True:
        bissexto = ano % 400
        if bissexto == 0:
            print("Esse ano é bissexto.")
        else:
            print("Esse ano não é bissexto.")