conversao = input("Escolha a base de conversão(binário, octal ou hexadecimal): ").lower()
numero = int(input("Digite um número para conversão: "))

if conversao == "binario" or conversao == "binário":
    print(f"A forma de conversão escolhida é binário, convertendo esse número: {bin(numero[2:])}")
elif conversao == "octal":
    print(f"A forma de conversão escolhida é octal, convertendo esse número: {oct(numero)[2:]}")
elif conversao == "hexadecimal":
    print(f"A forma de conversão escolhida é hexadecimal, convertendo esse número: {hex(numero)[2:]}")
else:
    print("Forma de conversão inválida, use uma das formas dentro do parêntese")