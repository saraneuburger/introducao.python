n1 = float(input("Digite a nota da 1ª prova: "))
n2 = float(input("Digite a nota da 2ª prova: "))
n3 = float(input("Digite a nota da 3ª prova: "))

# Verificação automática de nota zero
if n1 == 0 or n2 == 0 or n3 == 0:
    print("Reprovado automaticamente (nota zero em uma prova).")
else:
    media = (n1 + n2 + n3) / 3
    print(f"Média: {media:.2f}")

    if media >= 7:
        print("Situação: Aprovado")
    elif media >= 5:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")