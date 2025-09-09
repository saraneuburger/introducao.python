idade = int(input("Digite sua idade: "))
nacionalidade = input("Digite sua nacionalidade (brasileiro/estrangeiro): ").lower()

if idade < 16:
    print("Não pode votar.")
elif 16 <= idade < 18:
    print("Voto opcional.")
else:  # idade >= 18
    if nacionalidade == "brasileiro":
        print("Voto obrigatório.")
    else:
        print("Voto opcional.")