from datetime import datetime

def voto(nascimento) :
    anoAtual = datetime.now().year
    anos = anoAtual - nascimento

    return anos


situacao = ""

anoNascimento = int(input("Em que ano você nasceu: "))

anos = voto(anoNascimento)

if anos < 16:
    situacao = "NÃO VOTA"
elif anos <= 17 or anos >= 65:
    situacao = "VOTO OPCIONAL"
else: 
    situacao = "VOTO OBRIGATÓRIO"
    

print(f"Com {voto(anoNascimento)} anos: {situacao}.")