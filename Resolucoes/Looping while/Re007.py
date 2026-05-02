numero = int(input("Digite um número N para ler os N primeiros termos da sequência de Fibonacci: "))
fibonacci = (1 / 5 ** 0.5) * ((1 + 5 ** 0.5) / 2) ** numero  - ((1 - 5 ** 0.5) / 2) ** numero 

while numero >= 2:
    numero -= 1
    print(f"F({numero + 1})= {((1 / 5 ** 0.5) * ((1 + 5 ** 0.5) / 2) ** numero  - ((1 - 5 ** 0.5) / 2) ** numero):.0f}")
    
print("F(1) = 0")