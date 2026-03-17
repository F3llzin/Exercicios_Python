numeroa, numerob, numeroc = input().split()
numeroa = float(numeroa)
numerob = float(numerob)
numeroc = float(numeroc)

triangulo_area = (numeroa * numeroc) / 2
circulo_area = 3.14159 * numeroc ** 2
trapezio_area = ((numeroa + numerob) * numeroc) / 2
quadrado_area = numerob ** 2
retangulo_area = numeroa * numerob

print(f"TRIANGULO: {triangulo_area:.3f}")
print(f"CIRCULO: {circulo_area:.3f}")
print(f"TRAPEZIO: {trapezio_area:.3f}")
print(f"QUADRADO: {quadrado_area:.3f}")
print(f"RETANGULO: {retangulo_area:.3f}")
