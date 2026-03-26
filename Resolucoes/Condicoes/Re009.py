valora, valorb, valorc = input().split()

valora = float(valora)
valorb = float(valorb)
valorc = float(valorc)

delta = valorb ** 2 - 4 * valora * valorc

if valora == 0 or valorb == 0 or valorc == 0 or delta < 0:
    print("Impossivel calcular")
else: 
    resultado1 = (-valorb + delta ** 0.5) / (2 * valora)
    print(f"R1 = {resultado1:.5f}")
    resultado2 = (-valorb - delta ** 0.5) / (2 * valora)
    print(f"R2 = {resultado2:.5f}")