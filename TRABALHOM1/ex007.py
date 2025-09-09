print("classificando o risco financeiro")

try:
    idade = int(input("digite sua idade: "))
    renda = float(input("digite sua renda mensal: "))
    dividas = float(input("digite o total das suas dívidas: "))

    if renda > 0:
        porcentgDivida = (dividas / renda) * 100
    else:
        porcentgDivida = 100 

    print(f"percentual de dívida: {porcentgDivida:.1f}%")

    # Classificação
    if renda < 2000 and porcentgDivida > 50:
        risco = "alta"
    elif (2000 <= renda <= 5000) or (30 <= porcentgDivida <= 50):
        risco = "média"
    elif renda > 5000 and porcentgDivida < 30:
        risco = "maixa"
    else:
        risco = " entre média-baixa"

    print(f"classificação de risco: {risco}")

except ValueError:
    print("erro: digite apenas números válidos para idade, renda e dividas")