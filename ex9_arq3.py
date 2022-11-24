#ex 9 - arquivo 03 - slides das aulas de python

fracao, numerador, total = 0, 1000, 0
sinal = +1

for i in range(1, 51):
    fracao = sinal*(numerador/i)
    total += fracao
    numerador -= 3
    sinal *= -1 # sinal = sinal * (-1)

print("Total: %.2f" %total)
