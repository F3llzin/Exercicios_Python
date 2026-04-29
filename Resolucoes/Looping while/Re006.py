primeiro_termo_pa = int(input("Digite o primeiro termo da PA: "))
razao_pa = int(input("Digite a razão dessa PA: "))
ultimo_termo = 10
resposta_anterior = 0
resposta = 1

while resposta != 0:
    resposta_anterior = ultimo_termo
    while ultimo_termo > 0:
        print(primeiro_termo_pa + (ultimo_termo - 1) * razao_pa, end=(" "))
        ultimo_termo -= 1
    
    resposta = int(input("Quantos termos a mais você quer mostrar? "))
    ultimo_termo = resposta_anterior + resposta