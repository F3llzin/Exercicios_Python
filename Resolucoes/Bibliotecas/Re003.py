import math 
angulo = int(input("Digite um ângulo: "))

cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'''O seu cosseno é: {cosseno:.2f}
O seu seno é {seno:.2f}
A sua tangente é: {tangente:.2f}''')