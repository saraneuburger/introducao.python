# questão 10:

senha = input("Crie uma senha (mínimo 8 caracteres, 1 letra maiúscula, 1 letra minúscula, 1 número, 1 símbolo !@#$%): ")

if (len(senha) >= 8 and
    any(c.isupper() for c in senha) and
    any(c.islower() for c in senha) and
    any(c.isdigit() for c in senha) and
    any(c in "!@#$%" for c in senha)):
    print("Senha válida!")
else:
    print("Senha inválida, tente denovo.")