def area(largura, comprimento) :
    print(f"{largura * comprimento}m².")

print("Controle de terrenos")
print("-" * 20)

largura = float(input("LARGURA(m): "))
comprimento = float(input("COMPRIMENTO(m): "))

print(f"A área de um terreno {largura:.1f}x{comprimento:.1f} é de ", end=(""))
area(largura, comprimento)