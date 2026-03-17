numero = int(input("Digite um número: "))
separacao = "="   #Vai servir só para o visual no terminal "==="

print(f'''
TABUADA DE MULTIPLICAÇÃO:
{separacao * 20}   
    {numero} * 1 = \033[32m{numero * 1}\033[m
    {numero} * 2 = \033[32m{numero * 2}\033[m
    {numero} * 3 = \033[32m{numero * 3}\033[m
    {numero} * 4 = \033[32m{numero * 4}\033[m
    {numero} * 5 = \033[32m{numero * 5}\033[m
    {numero} * 6 = \033[32m{numero * 6}\033[m
    {numero} * 7 = \033[32m{numero * 7}\033[m
    {numero} * 8 = \033[32m{numero * 8}\033[m
    {numero} * 9 = \033[32m{numero * 9}\033[m
    {numero} * 10 = \033[32m{numero * 10}\033[m
{separacao * 20}''')

#Essa é apenas umas das formas de fazer esse programa
#"\033[m" é apenas para dar cor ao número no terminal  