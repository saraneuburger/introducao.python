# questão 1:

salario = float(input("Qual o salário do funcionário em reais?: R$ "))
tempo = int(input("Qual o tempo do funcionário dentro da empresa em anos?: "))

if salario < 2000:
    if tempo >= 5:
        percentual = 0.20
    else:
        percentual = 0.10
else:
    if tempo >= 5:
        percentual = 0.05
    else:
        percentual = 0.0

bonus = salario * percentual
print(f'Bônus: R$ {bonus:.2f} ({percentual * 100:.0f}%)')