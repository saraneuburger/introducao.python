print("cliente vip")

try:
    preco = float(input("digite o preço do produto: "))
    vip = input("voce é cliente VIP? (sim/nao): ").strip().lower()

    desconto = 0
    if preco >= 100:
        desconto = 20
    elif preco >= 50:
        desconto = 10
    else:
        desconto = 0
    if vip == "sim":
        desconto += 5

    precoFinal = preco * (1 - desconto / 100)

    print(f"\ndesconto adicionado: {desconto}%")
    print(f"preço final com desconto: R$ {precoFinal:.2f}")

except ValueError:
    print("erro: digite um número valido para o preço")