n = int(input("Digite um número para o cálculo do fatorial:"))

if n <= 20:
    fat = 1
    for i in range(1, n+1):
        fat *= i
    print("Fatorial = ", fat)
else:
    print("Apenas números até 20")
