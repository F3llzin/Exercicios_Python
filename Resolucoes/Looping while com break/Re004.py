contador_maioridade = 0
contador_homens = 0
contador_mulheres_menor = 0
resposta = "S"
sexo = ""

while True:
    if resposta == "N":
        break
    else:
        idade = int(input("Digite sua idade: "))
        sexo = input("Digite seu sexo[M/F]: ").upper()[:1]

        while sexo not in "FM":
            print("Sexo inválido, digite outro que seja válido")
            sexo = input("Digite seu sexo[M/F]: ").upper()[:1]
        
        if idade > 18:
            contador_maioridade += 1
        if sexo == "M":
            contador_homens += 1
        if sexo == "F" and idade <= 20:
            contador_mulheres_menor += 1

    resposta = input("Quer cadastrar mais alguém?[S/N] ").upper()[:1]

    while resposta not in "SN":
        print("Resposta inválida, use uma entrada válida[SIM/NÃO]")
        resposta = input("Quer cadastrar mais alguém?[S/N] ").upper()[:1]

print(f'''A quantidade de pessoas maiores de 18 anos são: {contador_maioridade}
A quantidade homens cadastrados foram: {contador_homens}
A quantidade de mulheres com menos de 20 são: {contador_mulheres_menor}''')
