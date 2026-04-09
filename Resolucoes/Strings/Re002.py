numero = int(input("Digite um número: "))
resto = 0

milhar = numero // 1000
resto = numero % 1000

centena = resto // 100
resto %= 100

dezena = resto // 10
resto %= 10

unidade = resto // 1

print(f"O número tem: {milhar} milhar(es), {centena} centena(s), {dezena} dezena(s) e {unidade} unidade(s)")