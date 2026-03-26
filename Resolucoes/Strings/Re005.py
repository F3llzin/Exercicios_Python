frase = input("Digite uma frase: ").lower()

indice_a = frase.count("a")
posicao_primeira_a = frase.find("a")
posicao_ultima_a = frase.rfind("a")

print(f'''A quantidade de letra "a": {indice_a}
A posição que aparece a primeira letra "a": {posicao_primeira_a}
A posição que aparece a última letra "a": {posicao_ultima_a}
''')
