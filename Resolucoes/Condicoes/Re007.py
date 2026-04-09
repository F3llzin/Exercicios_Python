salario = float(input("Digite seu sálario: "))
aumento10 = salario + salario * 0.1
aumento15 = salario + salario * 0.15

if salario > 1250:
    print(f"O seu novo sálario é: R${aumento10:.2f}")
else:
    print(f"O seu novo sálario é: R${aumento15:.2f}")