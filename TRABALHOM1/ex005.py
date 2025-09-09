def anoB (ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def dataValida(dia, mes, ano):
    if mes < 1 or mes > 12:
        return False

    if dia < 1:
        return False

    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return dia <= 31
    elif mes in [4, 6, 9, 11]:
        return dia <= 30
    elif mes == 2:
        if anoB(ano):
            return dia <= 29
        else:
            return dia <= 28
    else:
        return False

try:
    dia = int(input("digite o dia: "))
    mes = int(input("digite o mês: "))
    ano = int(input("digite o ano: "))

    if dataValida(dia, mes, ano):
        print("data válida!")
    else:
        print("data inválida")
except ValueError:
    print("digite um valor que seja inteiro")