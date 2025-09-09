# questão 2:

lado1 = float(input("Lado 1 em cm: "))
lado2 = float(input("Lado 2 em cm: "))
lado3 = float(input("Lado 3 em cm: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:

    if lado1 == lado2 == lado3:
        tipo = "equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "isósceles"
    else:
        tipo = "escaleno"
    print(f"Forma um triângulo {tipo}.")
else:
    print("Não forma um triângulo.")