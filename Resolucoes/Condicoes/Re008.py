retaa, retab, retac = input("Digite os valores para saber se forma ou não um triângulo: ").split()

retaa, retab, retac = float(retaa), float(retab), float(retac)

if retaa + retab > retac and retaa + retac > retab and retab + retac > retaa:
    print("Os valores são capazes de formar um triângulo.")
else:
    print("Esses valores não conseguem formar um triângulo.")