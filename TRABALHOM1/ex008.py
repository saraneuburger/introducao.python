
# sequência correta
correta = ['B', 'C', 'D', 'A']

# entrada do usuário
resposta = []
for i in range(4):
    carta = input(f"Digite a {i+1}ª carta (A, B, C ou D): ").upper()
    resposta.append(carta)

# cálculo da pontuação
pontuacao = 0

# 10 pontos por acerto
for i in range(4):
    if resposta[i] == correta[i]:
        pontuacao += 10

# bônus da letra A
if 'A' in resposta:
    pontuacao += 5

# bônus C seguido de D
for i in range(3):
    if resposta[i] == 'C' and resposta[i+1] == 'D':
        pontuacao += 5
        break  # só conta uma vez

# limite máximo de pontos
if pontuacao > 50:
    pontuacao = 50

print(f"Sua pontuação: {pontuacao}")