from datetime import datetime

anoAtual = datetime.now().year

trabalhador = {
    'nome' : "",
    'idade' : 0,
    'ctps' : 0,
    'contratação' : 0,
    'salário' : 0,
    'aposentadoria' : 0
}

trabalhador['nome'] = input("Nome: ")
trabalhador['idade'] = int(input("Ano de nascimento: "))

aux = trabalhador['idade']
trabalhador['idade'] = anoAtual - trabalhador['idade']

trabalhador['ctps'] = int(input("Carteira de trabalho(0 não tem): "))

if trabalhador['ctps'] == 0:
    for k in trabalhador:
        print(f"{k} tem o valor {trabalhador[k]}")

        if k == 'ctps':
            break
else:
    trabalhador['contratação'] = int(input("Ano de contratação: "))
    trabalhador['salário'] = float(input("Salário: R$"))

    trabalhador['aposentadoria'] = (trabalhador['contratação'] - aux) + 35

    for k in trabalhador:
            print(f"{k} tem o valor {trabalhador[k]}")

    