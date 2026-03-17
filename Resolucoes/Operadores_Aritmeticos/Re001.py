numero = int(input("Digite um número: "))

print(f'''O número digitado é: \033[31m{numero}\033[m
Esse é o antecessor: \033[31m{numero - 1}\033[m
E esse é o sucessor: \033[31m{numero + 1}\033[m''')

#Essa é apenas umas das formas de fazer esse programa
#"\033[m" é apenas para dar cor ao número no terminal  